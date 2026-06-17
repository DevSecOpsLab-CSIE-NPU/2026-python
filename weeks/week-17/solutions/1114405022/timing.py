import functools
import time


def timeit(_func=None, *, repeat=3):
    if repeat < 1:
        raise ValueError(f"repeat must be >= 1, got {repeat}")

    if _func is None:
        return functools.partial(timeit, repeat=repeat)

    @functools.wraps(_func)
    def wrapper(*args, **kwargs):
        elapsed_list = []
        for _ in range(repeat):
            start = time.perf_counter()
            result = _func(*args, **kwargs)
            end = time.perf_counter()
            elapsed_list.append(end - start)

        if not hasattr(wrapper, "records"):
            wrapper.records = []
        wrapper.records.extend(elapsed_list)
        wrapper.last_elapsed = sum(elapsed_list) / repeat

        return result

    return wrapper
