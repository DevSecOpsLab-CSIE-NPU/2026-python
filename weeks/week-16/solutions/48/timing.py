def timeit(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.last_elapsed = None
    wrapper.records = []
    return wrapper
