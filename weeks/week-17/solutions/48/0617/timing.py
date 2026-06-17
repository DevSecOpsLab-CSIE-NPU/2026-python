import functools
import time


def timeit(func=None, repeat=3):
    if func is None:
        return lambda f: timeit(f, repeat=repeat)

    if repeat < 1:
        raise ValueError("repeat must be >= 1")

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        times = []
        for _ in range(repeat):
            t0 = time.perf_counter()
            try:
                result = func(*args, **kwargs)
            finally:
                t1 = time.perf_counter()
                times.append(t1 - t0)

        wrapper.last_elapsed = sum(times) / repeat
        wrapper.records = times
        return result

    wrapper.records = []
    wrapper.last_elapsed = 0.0
    return wrapper
