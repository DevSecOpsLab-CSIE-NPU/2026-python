import functools
import time


def timeit(repeat: int = 3):
    if repeat < 1:
        raise ValueError("repeat must be a positive integer greater than or equal to 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            records = []
            exc = None
            result = None
            for _ in range(repeat):
                start = time.perf_counter()
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    exc = e
                finally:
                    records.append(time.perf_counter() - start)
            wrapper.records.extend(records)
            wrapper.last_elapsed = sum(records) / repeat
            if exc is not None:
                raise exc
            return result
        wrapper.last_elapsed = 0.0
        wrapper.records = []
        return wrapper
    return decorator
