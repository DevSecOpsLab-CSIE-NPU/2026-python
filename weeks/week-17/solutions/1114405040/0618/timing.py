"""Small timing decorator used by the search benchmark."""

from functools import wraps
from time import perf_counter


def timeit(func=None, *, repeat=3):
    """Measure a function call one or more times and store elapsed seconds.

    Can be used as ``@timeit`` or ``@timeit(repeat=5)``. The wrapper keeps a
    ``records`` list for the most recent call and ``last_elapsed`` as its mean.
    """
    if repeat < 1:
        raise ValueError("repeat must be at least 1")

    def decorate(target):
        @wraps(target)
        def wrapper(*args, **kwargs):
            records = []
            result = None
            for _ in range(repeat):
                start = perf_counter()
                result = target(*args, **kwargs)
                records.append(perf_counter() - start)
            wrapper.records = records
            wrapper.last_elapsed = sum(records) / len(records)
            return result

        wrapper.records = []
        wrapper.last_elapsed = 0.0
        return wrapper

    if func is None:
        return decorate
    return decorate(func)
