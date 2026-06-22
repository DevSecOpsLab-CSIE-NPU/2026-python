import functools
import time


def timeit(_func=None, *, repeat=3):
    """計時裝飾器

    每次呼叫實際執行被裝飾函式 `repeat` 次（預設 3），並將每次執行耗時（秒，float）
    記錄在屬性 `records` 中，且計算本次平均耗時存入 `last_elapsed` 屬性。
    當 repeat < 1 時，拋出 ValueError。
    內部不可有任何 print 輸出。
    """
    # 支援無括號的 @timeit 寫法
    if _func is not None and callable(_func):
        func = _func
        return timeit(repeat=3)(func)

    # 驗證輸入參數：必須為整數且大於等於 1
    if not isinstance(repeat, int) or repeat < 1:
        raise ValueError("repeat must be an integer >= 1")

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            local_records = []
            result = None
            for _ in range(repeat):
                start_time = time.perf_counter()
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                local_records.append(end_time - start_time)

            wrapper.records.extend(local_records)
            wrapper.last_elapsed = sum(local_records) / len(local_records)
            return result

        # 初始化紀錄屬性
        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper

    return decorator
