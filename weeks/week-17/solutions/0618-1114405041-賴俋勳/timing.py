import functools
import time


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, repeat=3, **kwargs):
        if repeat < 1:
            raise ValueError("repeat must be >= 1")
        wrapper.records = []
        for _ in range(repeat):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            wrapper.records.append(elapsed)
        wrapper.last_elapsed = sum(wrapper.records) / len(wrapper.records)
        return result
    wrapper.records = []
    wrapper.last_elapsed = 0.0
    return wrapper
