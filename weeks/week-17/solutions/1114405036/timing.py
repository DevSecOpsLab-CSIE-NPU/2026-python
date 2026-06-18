
"""Stage 1 — timeit 計時裝飾器。
 
設計重點：
  - records / last_elapsed 掛在 wrapper 上（不用全域變數），這樣每個被裝飾
    的函式各自擁有獨立的計時紀錄，彼此不互相污染，也不需管理全域狀態。
  - 參數驗證用 raise ValueError 而非 assert：assert 在 `python -O` 最佳化
    模式會被移除，安全/輸入檢查不能依賴它。
  - 裝飾器內保持安靜（不 print），格式化輸出交給 benchmark.py，計時器才能
    被重複使用。
"""
 
import functools
import time
 
 
def timeit(func=None, *, repeat=3):
    """計時裝飾器，可用 @timeit 或 @timeit(repeat=n) 兩種寫法。
 
    參數：
        func: 被裝飾函式（裸 @timeit 時自動帶入）。
        repeat: 每次呼叫實際執行的次數，預設 3，必須 >= 1。
 
    回傳：
        包裝後的函式；回傳值與原函式相同。裝飾後額外掛上：
            - records: list[float]，累積每次執行的耗時（秒）。
            - last_elapsed: float，最近一次呼叫的 repeat 次平均耗時。
    """
    if repeat < 1:
        raise ValueError(f"repeat 必須 >= 1，收到 {repeat}")
 
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            result = None
            elapsed_times = []
            for _ in range(repeat):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                elapsed_times.append(time.perf_counter() - start)
            wrapper.records.extend(elapsed_times)
            wrapper.last_elapsed = sum(elapsed_times) / repeat
            return result
 
        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper
 
    if func is None:
        return decorator
    return decorator(func)