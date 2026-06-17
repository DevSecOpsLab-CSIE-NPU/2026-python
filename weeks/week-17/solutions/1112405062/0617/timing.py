import functools
import time


def timeit(_func=None, *, repeat=3):
    if repeat < 1:
        raise ValueError("repeat must be >= 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            records = []
            try:
                for _ in range(repeat):
                    start = time.perf_counter()
                    result = func(*args, **kwargs)
                    elapsed = time.perf_counter() - start
                    records.append(elapsed)
            except Exception:
                raise
            else:
                wrapper.records = records
                wrapper.last_elapsed = sum(records) / len(records)
                return result

        wrapper.records = []
        wrapper.last_elapsed = None
        return wrapper

    if _func is None:
        return decorator
    return decorator(_func)
