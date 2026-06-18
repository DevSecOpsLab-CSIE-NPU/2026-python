"""timing.py — timeit 裝飾器

用法：
    @timeit          # repeat 預設 3
    def foo(): ...

    @timeit(repeat=5)
    def bar(): ...

呼叫後：
    foo()
    foo.last_elapsed  # float，本次 repeat 的平均耗時（秒）
    foo.records       # list[float]，所有歷次呼叫的每次耗時都累積在此
"""

import time
import functools


def timeit(func=None, *, repeat: int = 3):
    """裝飾器工廠：可不帶參數 @timeit 或帶參數 @timeit(repeat=5)。

    規格：
    - 被裝飾函式的回傳值不變。
    - functools.wraps 保留 __name__ / __doc__。
    - 每次呼叫實際跑 repeat 次，每次耗時（秒，float）append 到 wrapper.records。
    - wrapper.last_elapsed = 本次 repeat 的平均耗時。
    - 裝飾器內不 print 任何東西。
    - repeat < 1 → raise ValueError（不用 assert）。
    """
    if repeat < 1:
        raise ValueError(f"repeat 必須 >= 1，收到 {repeat!r}")

    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            times = []
            result = None
            for _ in range(wrapper.repeat):
                t0 = time.perf_counter()
                result = fn(*args, **kwargs)
                t1 = time.perf_counter()
                times.append(t1 - t0)
            wrapper.records.extend(times)
            wrapper.last_elapsed = sum(times) / len(times)
            return result

        wrapper.records = []
        wrapper.last_elapsed = 0.0
        wrapper.repeat = repeat
        return wrapper

    # 支援兩種用法：
    #   @timeit          ← func 是被裝飾函式
    #   @timeit(repeat=5) ← func 是 None，回傳 decorator
    if func is not None:
        return decorator(func)
    return decorator
