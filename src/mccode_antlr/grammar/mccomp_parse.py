from __future__ import annotations

from antlr4 import InputStream
from antlr4.tree.Tree import ParseTree
from antlr4.error.ErrorListener import ErrorListener


def parse(
        stream: InputStream,
        entry_rule_name: str,
        error_listener: ErrorListener | None = None
) -> ParseTree:
    from .McCompParser import McCompParser
    from .McCompLexer import McCompLexer
    from .mccode_parse import parse as p
    return p(McCompLexer, McCompParser, stream, entry_rule_name, error_listener)
