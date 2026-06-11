import functools
import time


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        wrapper.records.append(elapsed)
        wrapper.last_elapsed = elapsed
        return result

    wrapper.last_elapsed = None
    wrapper.records = []
    return wrapper
