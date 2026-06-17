"""0617 任務一 — timeit 裝飾器實作

功能:
- 支援 @timeit(repeat=3)
- repeat 預設為 3
- repeat 必須是 int 且 >= 1
- 每次呼叫實際執行 repeat 次
- 每次耗時記錄到 wrapper.records
- wrapper.last_elapsed 記錄本次 repeat 的平均耗時
- 使用 functools.wraps 保留原函式 metadata
- 裝飾器內不 print
"""

from functools import wraps
from time import perf_counter


def timeit(repeat=3):
    """建立計時裝飾器。

    Args:
        repeat: 每次呼叫被裝飾函式時，要重複執行的次數，必須是 int 且 >= 1。

    Returns:
        decorator: 可套用在函式上的裝飾器。

    Raises:
        ValueError: 當 repeat 不是 int，或 repeat < 1 時拋出。
    """
    if not isinstance(repeat, int) or repeat < 1:
        raise ValueError("repeat must be an integer greater than or equal to 1")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed_times = []
            result = None

            for _ in range(repeat):
                start = perf_counter()
                result = func(*args, **kwargs)
                end = perf_counter()

                elapsed = end - start
                elapsed_times.append(elapsed)
                wrapper.records.append(elapsed)

            wrapper.last_elapsed = sum(elapsed_times) / repeat
            return result

        wrapper.records = []
        wrapper.last_elapsed = 0.0

        return wrapper

    return decorator