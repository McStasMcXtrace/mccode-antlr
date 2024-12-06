from mccode_antlr.translators.c_listener import (
    extract_c_declared_variables_and_defined_types as extract,
    CDeclarator, CFuncPointer
)
from textwrap import dedent

def test_alias_types():
    block = dedent("""\
    typedef unsigned int age_t;
    """)
    variables, types = extract(block)
    assert len(variables) == 0
    assert len(types) == 1
    assert types[0] == 'age_t'


def test_stackoverflow_struct_type():
    block = dedent("""\
    typedef struct nodeT {
        void *content;
        struct nodeT *next;
    } Node;
    """)
    variables, types = extract(block)
    assert len(variables) == 0
    assert len(types) == 1
    assert 'Node' == types[0]

def test_stackoverflow_enum_type():
    block = dedent("""\
    typedef enum season_t { SPRING, SUMMER, FALL, WINTER } Season;
    """)
    variables, types = extract(block)
    assert len(variables) == 0
    assert len(types) == 1
    assert 'Season' == types[0]

def test_repeated_struct_name():
    block = dedent("""\
    typedef struct PolyhedronIndexValuePair {
        int index;
        double value;
    } PolyhedronIndexValuePair;
    """)
    variables, types = extract(block)

    assert len(variables) == 0
    assert len(types) == 1
    assert types[0] == 'PolyhedronIndexValuePair'


def test_mccode_style_typedef():
    block = dedent("""\
    struct _struct_Progress_bar {
      char     _name[256]; /* e.g. instance of Progress_bar name */
      char     _type[13]; /* Progress_bar */
      long     _index; /* index in TRACE list */
      Coords   _position_absolute;
      Coords   _position_relative; /* wrt PREVIOUS */
      Rotation _rotation_absolute;
      Rotation _rotation_relative; /* wrt PREVIOUS */
      int      _rotation_is_identity;
      int      _position_relative_is_zero;
      _class_Progress_bar_parameters _parameters;
    };
    typedef struct _struct_Progress_bar _class_Progress_bar;
    """)
    variables, types = extract(block)
    assert len(variables) == 0
    assert len(types) == 1
    assert types[0] == "_class_Progress_bar"


def test_assignments():
    block = dedent("""\
    int blah=1;
    double yarg;
    // yarg = 2.0; // this parser only handles _declarations_ no out-of-declaration assignments allowed.
    char mmmm[11] = "0123456789";
    """)
    variables, types = extract(block)
    assert len(variables) == 3
    assert len(types) == 0
    expected = [
        CDeclarator(dtype='int', declare='blah', init='1'),
        CDeclarator(dtype='double', declare='yarg'),
        CDeclarator(dtype='char', declare='mmmm', init='"0123456789"', elements=(11,)),
    ]
    for x in expected:
        assert x in variables


def test_struct_declaration():
    block = dedent("""\
    struct my_struct_type the_struct;
    struct another_struct a_struct_with_values={0, 1.0, "two"};
    struct the_third_s * ptr_to_third_struct;
    """)
    variables, types = extract(block)
    assert len(variables) == 3
    assert len(types) == 0
    expected = [
        CDeclarator(dtype='struct my_struct_type', declare='the_struct'),
        CDeclarator(dtype='struct another_struct', declare='a_struct_with_values', init='{0, 1.0, "two"}'),
        CDeclarator(dtype='struct the_third_s', declare='ptr_to_third_struct', pointer='*')
    ]
    assert all(x in variables for x in expected)


def test_typedef_declaration():
    block = dedent("""\
    typedef double blah;
    blah really_a_double=1.0f;
    blah * double_ptr=NULL;
    blah double_array[10];
    """)
    variables, types = extract(block)
    assert len(variables) == 3
    assert len(types) == 1
    assert types[0] == "blah"
    expected = [
        CDeclarator(dtype='blah', declare='really_a_double', init='1.0f'),
        CDeclarator(dtype='blah', declare='double_ptr', pointer='*', init='NULL'),
        CDeclarator(dtype='blah', declare='double_array', elements=(10,))
    ]
    assert all(x in variables for x in expected)


def test_flatellipse_finite_mirror():
    # A component defines a function handle (then doesn't use it).
    block = dedent("""\
        //Scene where all geometry is added to
    Scene s;
    //point structure
    Point p1;
    //Function to handle Conic-Neutron collisions with reflectivity from McStas Tables
    void traceNeutronConicWithTables(_class_particle* p, ConicSurf c);
    double *rfront_inner;//all r-distances at lStart for all mirror surfaces
    int silicon; // +1: neutron in silicon, -1: neutron in air, 0: mirrorwidth is 0; neutron cannot be in silicon and also does not track mirror transitions
    t_Table rsTable;
    """)
    variables, types = extract(block)
    assert len(types) == 0
    assert len(variables) == 6
    expected = [
        CDeclarator(dtype='Scene', declare='s'),
        CDeclarator(dtype='Point', declare='p1'),
        # the function pre-declaration _IS NOT_ a function pointer (and should be in DECLARE)
        CDeclarator(
            dtype='void',
            declare='traceNeutronConicWithTables(_class_particle* p, ConicSurf c)',
        ),
        CDeclarator(dtype='double', pointer='*', declare='rfront_inner'),
        CDeclarator(dtype='int', declare='silicon'),
        CDeclarator(dtype='t_Table', declare='rsTable')
    ]
    for x, y in zip(expected, variables):
        assert x == y


def test_function_pointer_declaration():
    block = dedent(r"""
    int (*fun_ptr)(int, int);
    int (*fun_ptr_ar3[3])(int, int);
    int (*fun_ptr_arr[])(int, int) = {add, sub, mul};
    """)
    variables, types = extract(block)
    assert len(types) == 0
    assert len(variables) == 3
    expected = [
        CDeclarator(
            dtype='int',
            declare=CFuncPointer(
                declare=CDeclarator(pointer='*', declare='fun_ptr'),
                args='int, int',
            ),
        ),
        CDeclarator(
            dtype='int',
            declare=CFuncPointer(
                declare=CDeclarator(pointer='*', declare='fun_ptr_ar3', elements=(3,)),
                args='int, int',
            ),
        ),
        CDeclarator(
            dtype='int',
            declare=CFuncPointer(
                declare=CDeclarator(pointer='*', declare='fun_ptr_arr', elements=(0,)),
                args='int, int',
            ),
            init='{add, sub, mul}',
        ),
    ]
    for x, y in zip(expected, variables):
        assert x == y
    members = [
        'int (* fun_ptr)(int, int)',
        'int (* fun_ptr_ar3[3])(int, int)',
        'int (* fun_ptr_arr[3])(int, int)',
    ]
    for x, y in zip(members, variables):
        assert x == y.as_struct_member()

def test_multi_level_static_array_types():
    big_table=dedent("""{
    { 2.087063,  0.23391E+00 ,7.485,  2.094,  0.55,	11.81,  63.54,  315,  12.00,  0.30000E+00},
    { 1.80745 , 0.17544E+00  ,7.485,  2.094,  0.55,	11.81,  63.54,  315,  12.00,  0.30000E+00},
    { 1.27806 , 0.87718E-01  ,7.485,  2.094,  0.55,	11.81,  63.54,  315,  12.00,  0.30000E+00},
    { 1.089933,  0.63795E-01 ,7.485,  2.094,  0.55,	11.81,  63.54,  315,  12.00,  0.30000E+00},
    { 0.903725,  0.43859E-01 ,7.485,  2.094,  0.55,	11.81,  63.54,  315,  12.00,  0.30000E+00},
    { 0.829315,  0.36934E-01 ,7.485,  2.094,  0.55,	11.81,  63.54,  315,  12.00,  0.30000E+00},
    { 0.808316,  0.35087E-01 ,7.485,  2.094,  0.55,	11.81,  63.54,  315,  12.00,  0.30000E+00}
	}""") # .replace('\n','')
    block = dedent(f"""\
    double mmsa[2][3] = {{{{0, 1, 2}}, {{3, 4, 5}}}};
    int mmi[][][] = {{{{{{0}}, {{1}}}}, {{{{2}}, {{3}}}}, {{{{4}}, {{5}}}}, {{{{6}}, {{7}}}}}};
    double big_table[7][10] = {big_table};
    """)
    variables, types = extract(block)
    expected = [
        CDeclarator(dtype='double', declare='mmsa', elements=(2, 3),
                    init='{{0, 1, 2}, {3, 4, 5}}',),
        CDeclarator(dtype='int', declare='mmi', elements=(0, 0, 0),
                    init='{{{0}, {1}}, {{2}, {3}}, {{4}, {5}}, {{6}, {7}}}'),
        CDeclarator(dtype='double', declare='big_table', elements=(7, 10),
                    init=big_table)
    ]
    for x, y in zip(expected, variables):
        assert x == y
    members = ['double mmsa[2][3]', 'int mmi[4][2][1]', 'double big_table[7][10]']
    for x, y in zip(members, variables):
        assert x == y.as_struct_member()