def _import_component_language():
    from .McCompLexer import McCompLexer
    from .McCompParser import McCompParser
    from .McCompVisitor import McCompVisitor
    return McCompLexer, McCompParser, McCompListener, McCompVisitor


def _import_instrument_language():
    from .McInstrLexer import McInstrLexer
    from .McInstrParser import McInstrParser
    from .McInstrVisitor import McInstrVisitor
    return McInstrLexer, McInstrParser, McInstrListener, McInstrVisitor


def _import_c_language():
    from .CLexer import CLexer
    from .CParser import CParser
    from .CListener import CListener
    from .CVisitor import CVisitor
    return CLexer, CParser, CListener, CVisitor


# Import the classes defined in the language files
McCompLexer, McCompParser, McCompListener, McCompVisitor = _import_component_language()
McInstrLexer, McInstrParser, McInstrListener, McInstrVisitor = _import_instrument_language()
CLexer, CParser, CListener, CVisitor = _import_c_language()

# And set only their names to be exported:
__all__ = [
    'McCompLexer',
    'McCompParser',
    'McCompListener',
    'McCompVisitor',
    'McInstrLexer',
    'McInstrParser',
    'McInstrListener',
    'McInstrVisitor',
    'CLexer',
    'CParser',
    'CListener',
    'CVisitor',
]
