from __future__ import annotations

import functools
import time
from typing import Callable, TypeVar

F = TypeVar("F", bound=Callable)


def timed(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.last_time = time.perf_counter() - start

    wrapper.last_time = 0.0
    return wrapper
