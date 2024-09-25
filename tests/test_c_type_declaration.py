from mccode_antlr.translators.c_listener import (
    extract_c_declared_variables_and_defined_types as extract
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
    assert 'blah' in variables
    assert variables['blah'] == ('int', '1')
    assert 'yarg' in variables
    assert variables['yarg'] == ('double', None)
    assert 'mmmm[11]' in variables
    assert variables['mmmm[11]'] == ('char', '"0123456789"')

def test_struct_declaration():
    block = dedent("""\
    struct my_struct_type the_struct;
    struct another_struct a_struct_with_values={0, 1.0, "two"};
    struct the_third_s * ptr_to_third_struct;
    """)
    variables, types = extract(block)
    assert len(variables) == 3
    assert len(types) == 0
    expected = {
        'the_struct': ('struct my_struct_type', None),
        'a_struct_with_values': ('struct another_struct', '{0, 1.0, "two"}'),
        '* ptr_to_third_struct': ('struct the_third_s', None),
    }
    assert all(x in variables for x in expected)
    for name, (dtype, value) in expected.items():
        assert(variables[name] == (dtype, value))


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
    expected = {
        'really_a_double': ('blah', '1.0f'),
        '* double_ptr': ('blah', 'NULL'),
        'double_array[10]': ('blah', None),
    }
    assert all(x in variables for x in expected)
    for name, (dtype, value) in expected.items():
        assert(variables[name] == (dtype, value))