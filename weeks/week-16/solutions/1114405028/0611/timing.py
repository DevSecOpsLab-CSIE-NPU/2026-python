import functools
import time


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        wrapper.last_elapsed = elapsed
        if not hasattr(wrapper, 'records'):
            wrapper.records = []
        wrapper.records.append(elapsed)
        return result

    wrapper.records = []
    wrapper.last_elapsed = 0.0
    return wrapper
