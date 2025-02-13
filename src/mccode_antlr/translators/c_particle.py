def restore_name(is_mcstas):
    return "RESTORE_NEUTRON" if is_mcstas else "RESTORE_XRAY"


def xyz_Axyz_Bxyz(is_mcstas, type_str):
    """Return lists of particle struct members

    Either:
        (x, y, z), (vx, vy, vz), (sx, sy, sz)
    or
        (x, y, z), (kx, ky, kz, phi), (Ex, Ey, Ez)
    """
    xyz = ('x', 'y', 'z')
    ps = ('', 'v', 's') if is_mcstas else ('', 'k', 'E')
    z, a, b = (tuple((f'{p}{x}', type_str) for x in xyz) for p in ps)
    if not is_mcstas:
        a = a + (('phi', type_str),)
    return z, a, b



def struct_members(is_mcstas: bool):
    """Get the name and type of the members of the _class_particle struct

    The members of the struct are not equivalent between McStas and McXtrace
    """
    z, a, b = xyz_Axyz_Bxyz(is_mcstas, 'double')
    if is_mcstas:
        a = a +  (
            ('mcgravitation', 'int'),
            ('mcMagnet', 'void *'),
            ('allow_backprop', 'int')
        )

    members = (z + a + b) + (
        ('_mctmp_a', 'double'),
        ('_mctmp_b', 'double'),
        ('_mctmp_c', 'double'),
        ('randstate', 'unsigned long []'),
        ('t', 'double'),
        ('p', 'double'),
        ('_uid', 'long long'),
        ('_index', 'long'),
        ('_absorbed', 'long'),
        ('_scattered', 'long'),
        ('_restore', 'long'),
        ('flag_nocoordschange', 'long'),
        ('_logic', 'struct particle_logic_struct'),
        # uservars
    )
    return {k: v for k, v in members}

def accessible_struct_members(is_mcstas: bool):
    """Get the name and type of the accessible members of the _class_particle struct

    The members of the struct are not equivalent between McStas and McXtrace

    Note
    ----
    Used in the generated C code by, e.g.,
        double particle_getvar(...)
        void particle_getvar_void(...)
        int particle_setvar_void(...)
        void particle_restore(...)
    written-out here within c_header.py
    """
    z, a, b = xyz_Axyz_Bxyz(is_mcstas, 'double')
    members = (z + a + b) + (
        ('t', 'double'),
        ('p', 'double'),
        ('_mctmp_a', 'double'),
        ('_mctmp_b', 'double'),
        ('_mctmp_c', 'double'),
        # uservars
    )
    return {k: v for k, v in members}

def restorable_struct_members(is_mcstas: bool):
    """Get the name and type of the restorable members of the _class_particle struct

    The members of the struct are not equivalent between McStas and McXtrace

    Note
    ----
    Used in the generated C code by, e.g.,
        void particle_restore(...)
    written-out here within c_header.py
    """
    z, a, b = xyz_Axyz_Bxyz(is_mcstas, 'double')
    members = z + a + b + (('t', 'double'), ('p', 'double'),)
    return {k: v for k, v in members}


def setstate_signature_members(is_mcstas: bool):
    z, a, b = xyz_Axyz_Bxyz(is_mcstas, 'double')
    members = (
        z + a + (('t', 'double'),) + b
        + (
            ('p', 'double'),
            ('mcgravitation', 'int'),
            ('mcMagnet', 'void *'),
            ('allow_backprop', 'int')
        )
    )
    return {k: v for k, v in members}


def getstate_signature_members(is_mcstas):
    z, a, b = xyz_Axyz_Bxyz(is_mcstas, 'double *')
    members = (
            (('mcparticle', '_class_particle'),)
            + z + a + (('t', 'double *'),) + b + (('p', 'double *'),)
    )
    return {k: v for k, v in members}



def setstate_signature_call(is_mcstas: bool):
    values = {
        'vz' if is_mcstas else 'kz': '1',
        'p': '1',
        'mcgravitation': 'mcgravitation',
        'mcMagnet': 'NULL',
        'allow_backprop': 'mcallowbackprop',
    }
    members = setstate_signature_members(is_mcstas)
    return [values.get(key, '0') for key in members]
