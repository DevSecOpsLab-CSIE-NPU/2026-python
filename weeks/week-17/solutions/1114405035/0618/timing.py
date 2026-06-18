import functools
import time


def timeit(repeat=3):
    if not isinstance(repeat, int) or repeat < 1:
        raise ValueError("repeat must be an integer greater than or equal to 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_run_times = []
            res = None
            for _ in range(repeat):
                start = time.perf_counter()
                res = func(*args, **kwargs)
                end = time.perf_counter()
                elapsed = end - start
                current_run_times.append(elapsed)
                wrapper.records.append(elapsed)

            wrapper.last_elapsed = sum(current_run_times) / repeat
            return res

        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper

    return decorator
