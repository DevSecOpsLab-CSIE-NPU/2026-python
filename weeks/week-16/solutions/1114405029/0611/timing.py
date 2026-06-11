"""Timing decorator for the 6/11 sorting lab."""

from functools import wraps
from time import perf_counter


def timeit(func):
    """Decorate a function and record elapsed time for each call."""
    records = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start
        wrapper.last_elapsed = elapsed
        records.append(elapsed)
        return result

    wrapper.records = records
    return wrapper
