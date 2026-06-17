import time
import functools


def timeit(func=None, repeat=3):
    if repeat < 1:
        raise ValueError("repeat 必須 >= 1")

    if func is None:
        return lambda f: timeit(f, repeat=repeat)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        records = []
        for _ in range(repeat):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            records.append(end - start)
        wrapper.records = records
        wrapper.last_elapsed = sum(records) / len(records)
        return result

    return wrapper
