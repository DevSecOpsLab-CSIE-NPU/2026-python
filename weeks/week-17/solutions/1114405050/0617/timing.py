import functools
import time


def timeit(repeat=3):
    if callable(repeat):
        func = repeat
        return _make_wrapper(func, 3)

    if repeat < 1:
        raise ValueError('repeat must be >= 1')

    def decorator(func):
        return _make_wrapper(func, repeat)

    return decorator


def _make_wrapper(func, repeat):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not hasattr(wrapper, 'records'):
            wrapper.records = []

        elapsed_list = []
        for _ in range(repeat):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            elapsed_list.append(end - start)

        wrapper.records.extend(elapsed_list)
        wrapper.last_elapsed = sum(elapsed_list) / repeat
        return result

    return wrapper
