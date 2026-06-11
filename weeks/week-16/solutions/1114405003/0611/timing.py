import functools


def timeit(func):
    """@timeit decorator that times function execution.

    Args:
        func: The function to decorate

    Returns:
        The decorated function with timing capabilities
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        elapsed = end_time - start_time
        wrapper.last_elapsed = elapsed
        if not hasattr(wrapper, 'records'):
            wrapper.records = []
        wrapper.records.append(elapsed)
        
        return result
    
    wrapper.last_elapsed = 0.0
    wrapper.records = []
    return wrapper