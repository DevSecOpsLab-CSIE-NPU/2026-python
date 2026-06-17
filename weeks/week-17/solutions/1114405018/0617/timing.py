import functools
import time


def timeit(repeat=3):
    if repeat < 1:
        raise ValueError("repeat must be >= 1")

    def decorator(func):
        func.records = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            elapsed_list = []
            for _ in range(repeat):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                elapsed = time.perf_counter() - start
                elapsed_list.append(elapsed)
            wrapper.records.extend(elapsed_list)
            wrapper.last_elapsed = sum(elapsed_list) / repeat
            return result

        return wrapper

    return decorator
