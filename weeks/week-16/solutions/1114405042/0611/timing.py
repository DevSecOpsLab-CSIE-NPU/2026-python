"""@timeit 裝飾器 — 量測函式執行時間"""

import time
import functools


def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        wrapper.last_elapsed = elapsed
        wrapper.records.append(elapsed)
        return result

    wrapper.last_elapsed = 0.0
    wrapper.records = []
    return wrapper
