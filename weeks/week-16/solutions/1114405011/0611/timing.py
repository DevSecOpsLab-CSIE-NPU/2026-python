import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        elapsed = end - start
        wrapper.last_elapsed = float(elapsed)
        wrapper.records.append(float(elapsed))
        return result

    wrapper.last_elapsed = 0.0
    wrapper.records = []
    return wrapper
