"""
#   Name

k3fmt

It provides with several string operation functions.

#   Status

This library is considered production ready.

"""

# from .proc import CalledProcessError
# from .proc import ProcError

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


def __getattr__(name: str) -> str:
    # importlib.metadata takes about 20 ms to import, so it is loaded only
    # when __version__ is read
    if name != "__version__":
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    from importlib.metadata import version

    return version("k3fmt")
