"""
#   Name

k3fmt

It provides with several string operation functions.

#   Status

This library is considered production ready.

"""

# from .proc import CalledProcessError
# from .proc import ProcError

from importlib.metadata import version

__version__ = version("k3fmt")

from .strutil import (
    break_line,
    filter_invisible_chars,
    format_line,
    format_table,
    line_pad,
    page,
    parse_colon_kvs,
    struct_repr,
    tokenize,
    utf8str,
)

__all__ = [
    "break_line",
    "filter_invisible_chars",
    "format_line",
    "format_table",
    "line_pad",
    "page",
    "parse_colon_kvs",
    "struct_repr",
    "tokenize",
    "utf8str",
]
