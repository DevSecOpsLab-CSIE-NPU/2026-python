"""timing.py - timeit 裝飾器實作"""
import functools
import time


def timeit(repeat=3):
    """計時裝飾器
    
    Args:
        repeat: 重複執行次數，預設 3
        
    Returns:
        裝飾器函式
    """
    if repeat < 1:
        raise ValueError("repeat must be >= 1")
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            wrapper.records = []
            total_time = 0.0
            
            for _ in range(repeat):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                elapsed = end - start
                wrapper.records.append(elapsed)
                total_time += elapsed
            
            wrapper.last_elapsed = total_time / repeat
            return result
        
        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper
    
    return decorator