from functools import wraps
import time
from typing import Callable, Any


def timeit(func: Callable) -> Callable:
    """裝飾器：保留 metadata，呼叫後記錄 elapsed 並累積在 records。"""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        # 屬性掛在 wrapper 上，符合規格：last_elapsed, records
        wrapper.last_elapsed = elapsed
        wrapper.records.append(elapsed)
        return result

    # 初始化屬性
    wrapper.last_elapsed = None  # type: ignore
    wrapper.records = []         # type: ignore
    return wrapper
