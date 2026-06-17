def timeit(func=None, repeat=3):
    if func is None:
        return lambda f: timeit(f, repeat=repeat)

    def wrapper(*args, **kwargs):
        return None

    return wrapper
