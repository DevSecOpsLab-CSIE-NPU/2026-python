"""Timing helper for the 0617 search evaluation assignment."""

from functools import wraps
from time import perf_counter


def timeit(func, repeat: int = 3):
    """Return a wrapper that records average elapsed time for each call.

    Args:
        func: Callable to measure.
        repeat: Number of times to execute the callable per wrapper call.

    Raises:
        ValueError: If repeat is less than 1.
    """
    if repeat < 1:
        raise ValueError("repeat must be at least 1")

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        start = perf_counter()
        for _ in range(repeat):
            result = func(*args, **kwargs)
        elapsed = (perf_counter() - start) / repeat
        wrapper.records.append(elapsed)
        wrapper.last_elapsed = elapsed
        return result

    wrapper.records = []
    wrapper.last_elapsed = None
    return wrapper
