from __future__ import annotations

import functools
from typing import Callable, TextIO
import sys


def tracer(func: Callable | None = None, *, file: TextIO | None = None):
    
    def decorator(f: Callable) -> Callable:
        depth = 0
        out = file if file is not None else sys.stdout

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            nonlocal depth
            indent = "  " * depth
            args_repr = ", ".join(
                [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
            )
            print(f"{indent}-> {f.__name__}({args_repr})", file=out)

            depth += 1
            try:
                result = f(*args, **kwargs)
            finally:
                depth -= 1

            indent = "  " * depth
            print(f"{indent}<- {f.__name__} = {result!r}", file=out)
            return result

        return wrapper

    if func is not None:
        return decorator(func)
    return decorator
