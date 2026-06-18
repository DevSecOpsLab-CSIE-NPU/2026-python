import cProfile, math, pstats, time, timeit
from functools import wraps
def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        res = func(*args, **kwargs)
        print(f'[timed] {func.__name__}: {(time.perf_counter()-t0)*1000:.2f} ms')
        return res
    return wrapper
@timed
def squares(n): return sum(i*i for i in range(n))
def bench():
    n = 10000
    t = timeit.timeit('sum(i*i for i in range(n))', globals={'n': n}, number=1000)
    print(f'[timeit] {t:.3f}s')
if __name__ == '__main__':
    squares(100000)
    bench()
