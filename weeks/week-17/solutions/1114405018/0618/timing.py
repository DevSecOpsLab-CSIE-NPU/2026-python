import time
import functools


def timeit(func=None, *, repeat=3):
    if repeat < 1:
        raise ValueError("repeat must be >= 1")
    if func is None:
        return lambda f: timeit(f, repeat=repeat)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        elapsed = []
        for _ in range(repeat):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            elapsed.append(end - start)
        wrapper.records.extend(elapsed)
        wrapper.last_elapsed = sum(elapsed) / repeat
        return result

    wrapper.records = []
    wrapper.last_elapsed = None
    return wrapper
