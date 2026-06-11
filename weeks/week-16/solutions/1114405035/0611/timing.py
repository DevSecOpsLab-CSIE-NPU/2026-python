import functools
import time


def timeit(func):
    """計時裝飾器，記錄函式呼叫的耗時。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            elapsed = time.perf_counter() - start_time
            wrapper.last_elapsed = elapsed
            if not hasattr(wrapper, "records"):
                wrapper.records = []
            wrapper.records.append(elapsed)
            
    return wrapper
