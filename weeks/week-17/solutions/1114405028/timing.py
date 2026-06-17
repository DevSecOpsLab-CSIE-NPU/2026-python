from functools import wraps
import time

def timeit(func=None, *, repeat: int = 3):
    """裝飾器 / 裝飾器工廠。

    用法：
      @timeit
      @timeit()
      @timeit(repeat=5)

    規格：
      - repeat < 1 會在建立時 raise ValueError
      - 每次呼叫實際執行 repeat 次，將每次耗時 append 到 wrapper.records (累積)
      - wrapper.last_elapsed = 本次呼叫的平均耗時 (秒，float)
      - 保留原函式 metadata (functools.wraps)
      - 不 print
    """
    if repeat < 1:
        raise ValueError("repeat must be >= 1")

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            times = []
            result = None
            for _ in range(repeat):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                elapsed = time.perf_counter() - start
                times.append(elapsed)
            # 將本次的 times append 到累積 records，並更新 last_elapsed 為本次平均
            wrapper.records.extend(times)
            wrapper.last_elapsed = sum(times) / len(times) if times else 0.0
            return result

        # 初始化屬性
        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper

    # 支援 @timeit (func 傳入) 與 @timeit(...) / timeit()(f) 的情形
    if callable(func):
        return decorator(func)
    return decorator