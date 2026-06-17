"""Timing decorator for the 0617 assignment."""

from functools import wraps
from time import perf_counter


def timeit(func=None, *, repeat=3):
    """Run a function repeat times and record elapsed seconds on the wrapper."""
    if repeat < 1:
        raise ValueError("repeat must be at least 1")

    def decorate(inner_func):
        @wraps(inner_func)
        def wrapper(*args, **kwargs):
            wrapper.records = []
            result = None

            for _ in range(repeat):
                start = perf_counter()
                result = inner_func(*args, **kwargs)
                wrapper.records.append(perf_counter() - start)

            wrapper.last_elapsed = sum(wrapper.records) / repeat
            return result

        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper

    if func is None:
        return decorate

    return decorate(func)
