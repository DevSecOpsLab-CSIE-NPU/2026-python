"""Timing decorator for Stage 1."""

from functools import wraps
from time import perf_counter


def timeit(func=None, *, repeat=3):
    if repeat < 1:
        raise ValueError("repeat must be at least 1")

    def decorator(wrapped_func):
        @wraps(wrapped_func)
        def wrapper(*args, **kwargs):
            elapsed_times = []
            result = None

            for _ in range(repeat):
                start = perf_counter()
                result = wrapped_func(*args, **kwargs)
                elapsed_times.append(perf_counter() - start)

            wrapper.records.extend(elapsed_times)
            wrapper.last_elapsed = sum(elapsed_times) / repeat
            return result

        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper

    if func is None:
        return decorator

    return decorator(func)