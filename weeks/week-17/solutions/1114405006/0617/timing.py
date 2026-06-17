import functools
import time


def timeit(func=None, *, repeat=3):
    if repeat < 1:
        raise ValueError(f"repeat 必须 >= 1，收到: {repeat}")

    if func is None:
        return lambda f: timeit(f, repeat=repeat)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        records = []
        for _ in range(repeat):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            records.append(elapsed)

        wrapper.f = type('F', (), {'records': records, 'last_elapsed': sum(records) / len(records)})()
        return result

    return wrapper