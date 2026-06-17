def timeit(repeat=3):
    from functools import wraps
    import time

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if repeat < 1:
                raise ValueError("repeat must be at least 1")
            
            records = []
            for _ in range(repeat):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                elapsed_time = end_time - start_time
                records.append(elapsed_time)

            wrapper.records = records
            wrapper.last_elapsed = sum(records) / len(records)
            return result

        return wrapper

    return decorator