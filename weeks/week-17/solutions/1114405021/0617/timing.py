import time
import functools


def timeit(func=None, *, repeat=3):
    if repeat < 1:
        raise ValueError("repeat must be >= 1")

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            records = []
            for _ in range(int(repeat)):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                elapsed = time.perf_counter() - start
                records.append(elapsed)
            wrapper.records.extend(records)
            wrapper.last_elapsed = sum(records) / len(records)
            return result

        wrapper.records = []
        wrapper.last_elapsed = None
        return wrapper

    if func is None:
        return decorator
    return decorator(func)
