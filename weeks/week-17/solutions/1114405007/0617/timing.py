import functools
import time


def timeit(repeat=3):
    if not isinstance(repeat, int):
        raise TypeError("repeat must be an integer")
    if repeat < 1:
        raise ValueError("repeat must be at least 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            records = []
            for _ in range(repeat):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                elapsed = time.perf_counter() - start
                records.append(elapsed)
            wrapper.records = records
            wrapper.last_elapsed = sum(records) / len(records)
            return result
        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper
    return decorator
