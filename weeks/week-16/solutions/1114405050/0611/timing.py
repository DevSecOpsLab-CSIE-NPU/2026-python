import time
import functools

def timeit(func):
    """
    計時裝飾器。
    記錄函式每次執行的耗時，並保存在 func.last_elapsed 與 func.records 中。
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        
        try:
            result = func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            elapsed = end_time - start_time
            
            # 初始化屬性
            if not hasattr(wrapper, "records"):
                wrapper.records = []
                
            wrapper.last_elapsed = elapsed
            wrapper.records.append(elapsed)
            
        return result
        
    return wrapper
