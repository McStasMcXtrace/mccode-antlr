from __future__ import annotations

import types
from antlr4 import InputStream, CommonTokenStream
from antlr4.tree.Tree import ParseTree
from antlr4.error.ErrorListener import ErrorListener


def parse(
        lexer_class,
        parser_class,
        stream:InputStream,
        entry_rule_name:str,
        error_listener: ErrorListener | None = None
) -> ParseTree:
    lexer = lexer_class(stream)
    if error_listener is not None:
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)
    token_stream = CommonTokenStream(lexer)

    parser = parser_class(token_stream)
    if error_listener is not None:
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

    entry_rule_func = getattr(parser, entry_rule_name, None)
    if not isinstance(entry_rule_func, types.MethodType):
        raise ValueError("Invalid entry_rule_name '%s'" % entry_rule_name)
    return entry_rule_func()