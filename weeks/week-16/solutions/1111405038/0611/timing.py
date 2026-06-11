"""Stage 1 — @timeit 裝飾器實作"""

import functools
import time


def timeit(func):
    """計時裝飾器:記錄每次呼叫的耗時到 last_elapsed 與 records,不輸出任何內容。"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        wrapper.last_elapsed = elapsed
        wrapper.records.append(elapsed)
        return result

    wrapper.last_elapsed = None
    wrapper.records = []
    return wrapper
