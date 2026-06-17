"""Timing utilities for week-17 0617 practice."""

from functools import wraps
from time import perf_counter


def timeit(_func=None, *, repeat=3):
    """Measure function runtime and store per-run timing records.

    Args:
        _func: Decorated function when using @timeit directly.
        repeat: Number of runs for each call. Must be >= 1.

    Returns:
        A wrapped function with two attributes:
        - records: list[float], all historical run times in seconds.
        - last_elapsed: float, average elapsed time of the latest call.
    """
    if repeat < 1:
        raise ValueError("repeat must be >= 1")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            total_elapsed = 0.0
            result = None

            for _ in range(repeat):
                start = perf_counter()
                result = func(*args, **kwargs)
                elapsed = perf_counter() - start
                wrapper.records.append(elapsed)
                total_elapsed += elapsed

            wrapper.last_elapsed = total_elapsed / repeat
            return result

        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper

    if _func is None:
        return decorator
    return decorator(_func)
