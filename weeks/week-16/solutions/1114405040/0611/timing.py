"""Small timing decorator used by the sorting benchmark."""

from functools import wraps
from time import perf_counter
from typing import Any, Callable, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])


def timeit(func: F) -> F:
    """Measure a function call without printing during normal use."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            wrapper.last_elapsed = elapsed
            wrapper.records.append(elapsed)

    wrapper.last_elapsed = 0.0
    wrapper.records = []
    return cast(F, wrapper)
