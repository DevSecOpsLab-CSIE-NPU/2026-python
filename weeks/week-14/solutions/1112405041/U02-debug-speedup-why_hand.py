import time
def fast(): return sum(range(1000000))
if __name__ == '__main__':
    t0 = time.perf_counter()
    fast()
    print(f'Speedup audit: {(time.perf_counter()-t0)*1000:.2f}ms')
