def test_mccode_pooch_tags():
    from mccode_antlr.reader.registry import MCSTAS_REGISTRY, MCXTRACE_REGISTRY, LIBC_REGISTRY
    for reg in (MCSTAS_REGISTRY, MCXTRACE_REGISTRY, LIBC_REGISTRY):
        assert reg.version != "main"
