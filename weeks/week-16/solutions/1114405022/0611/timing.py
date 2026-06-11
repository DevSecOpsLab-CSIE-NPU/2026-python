import functools
import time


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start
            wrapper.last_elapsed = elapsed
            wrapper.records.append(elapsed)

    wrapper.last_elapsed = None
    wrapper.records = []
    return wrapper
