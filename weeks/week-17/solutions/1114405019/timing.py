"""0617 任務一 — timeit 計時裝飾器。"""

import functools
import time


def timeit(repeat=3):
    """回傳一個裝飾器:把被裝飾函式實際執行 repeat 次,記錄每次耗時。

    - repeat 必須是 int 且 >= 1,否則 raise ValueError(不用 assert,
      因為 assert 在 Python 最佳化模式 -O 下會被整段拿掉,等同於沒驗證)。
    - 計時紀錄掛在 wrapper(也就是裝飾後回傳的函式物件)上,而不是
      閉包變數,這樣外部才能用 f.records / f.last_elapsed 取用。
    - 被裝飾函式拋出例外時原樣往外傳,該次不計入 records。
    """
    if not isinstance(repeat, int) or isinstance(repeat, bool) or repeat < 1:
        raise ValueError(f"repeat must be an int >= 1, got {repeat!r}")

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            times = []
            for _ in range(repeat):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                elapsed = time.perf_counter() - start
                times.append(elapsed)
                wrapper.records.append(elapsed)
            wrapper.last_elapsed = sum(times) / len(times)
            return result

        wrapper.records = []
        wrapper.last_elapsed = None
        return wrapper

    return decorator
