import functools
import time


def timeit(func=None, *, repeat=3):
    if func is None:
        return lambda f: timeit(f, repeat=repeat)

    if not isinstance(repeat, int):
        raise TypeError(f"repeat must be an int, got {type(repeat).__name__}")
    if repeat < 1:
        raise ValueError(f"repeat must be >= 1, got {repeat}")

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
