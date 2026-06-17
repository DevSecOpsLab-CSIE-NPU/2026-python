import time
from functools import wraps


def timeit(repeat=1):
    """
    Decorator factory for measuring function execution time.

    Args:
        repeat (int): Number of times to execute the wrapped function.
                      Must be greater than or equal to 1.

    Returns:
        function: Decorated function.

    Raises:
        ValueError: If repeat is less than 1.
    """
    if repeat < 1:
        raise ValueError("repeat must be greater than or equal to 1")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            records = []
            result = None

            for _ in range(repeat):
                start = time.perf_counter()
                result = func(*args, **kwargs)
                end = time.perf_counter()
                records.append(end - start)

            wrapper.records = records
            wrapper.last_elapsed = sum(records) / len(records)
            return result

        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper

    return decorator
