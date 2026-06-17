"""0617 任務一 — timeit 裝飾器

規格:
  1. 不改變被裝飾函式的回傳值
  2. 用 functools.wraps 保留 __name__ / __doc__
  3. 每次呼叫實際跑 repeat 次(預設 3),把每次耗時 append 到 f.records,
     f.last_elapsed = 本次 repeat 的平均耗時(float 秒)
  4. 裝飾器內不准 print
  5. repeat < 1 → raise ValueError(用 raise,不准 assert)
"""

import functools
import time


def timeit(func, *, repeat=3):
    if repeat < 1:
        raise ValueError("repeat must be >= 1")

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        records = []
        for _ in range(repeat):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            records.append(end - start)
        wrapper.records = records
        wrapper.last_elapsed = sum(records) / len(records)
        return result

    wrapper.records = []
    wrapper.last_elapsed = 0.0
    return wrapper
