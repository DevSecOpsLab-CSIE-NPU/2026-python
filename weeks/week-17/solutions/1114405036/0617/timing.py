
import functools
import time
 
 
def timeit(func=None, *, repeat=3):

    if repeat < 1:
        raise ValueError(f"repeat 必須 >= 1,收到 {repeat}")
 
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(repeat):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                elapsed = time.perf_counter() - start
                wrapper.records.append(elapsed)
            wrapper.last_elapsed = sum(wrapper.records[-repeat:]) / repeat
            return result
 
        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper
 
    # @timeit(repeat=n) → func 為 None,回傳 decorator 等待套用
    if func is None:
        return decorator
    # @timeit → func 為被裝飾函式,直接套用
    return decorator(func)