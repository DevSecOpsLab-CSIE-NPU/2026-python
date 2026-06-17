import functools
import time

def timeit(func_or_repeat=None, *, repeat=3):
    """計時裝飾器，可支援帶參數或不帶參數的形式。
    
    規格：
    1. 被裝飾函式的回傳值不變。
    2. 用 functools.wraps 保留 __name__ 與 __doc__。
    3. 每次呼叫實際跑 repeat 次，每次耗時 append 到 wrapper.records，最後一次的平均耗時記在 wrapper.last_elapsed。
    4. 裝飾器內不准 print。
    5. repeat < 1 應 raise ValueError。
    """
    actual_repeat = repeat
    func = None

    if func_or_repeat is not None:
        if callable(func_or_repeat):
            func = func_or_repeat
        else:
            actual_repeat = func_or_repeat

    # 驗證 repeat 必須為 >= 1 的整數
    if not isinstance(actual_repeat, int) or isinstance(actual_repeat, bool) or actual_repeat < 1:
        raise ValueError("repeat must be an integer >= 1")

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            times = []
            res = None
            for _ in range(actual_repeat):
                start = time.perf_counter()
                res = f(*args, **kwargs)
                end = time.perf_counter()
                times.append(end - start)
            
            wrapper.records.extend(times)
            wrapper.last_elapsed = sum(times) / actual_repeat
            return res

        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper

    if func is not None:
        return decorator(func)
    return decorator
