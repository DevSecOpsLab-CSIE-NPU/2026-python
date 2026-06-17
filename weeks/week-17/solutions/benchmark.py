
from search import binary_search, linear_search
from timing import timeit
 
 
def main():
    n = 2_000_000
    data = list(range(n))
    target = n - 1  # 最壞情況:目標在最尾端(linear 要走完整串)
 
    timed_linear = timeit(linear_search)
    timed_binary = timeit(binary_search)
 
    idx_l = timed_linear(data, target)
    idx_b = timed_binary(data, target)
 
    assert idx_l == idx_b == target
 
    print(f"n = {n:,},target = 最後一個元素")
    print(f"linear records : {timed_linear.records}")
    print(f"linear avg     : {timed_linear.last_elapsed:.6f} s")
    print(f"binary records : {timed_binary.records}")
    print(f"binary avg     : {timed_binary.last_elapsed:.8f} s")
    speedup = timed_linear.last_elapsed / timed_binary.last_elapsed
    print(f"speedup (linear/binary): {speedup:,.0f}x")
 
 
if __name__ == "__main__":
    main()