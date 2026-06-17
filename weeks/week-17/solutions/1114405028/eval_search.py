from timing import timeit
from search import linear_search, binary_search
import random
import statistics

def make_runner(func, *args, repeat=5):
    """回傳一個被 @timeit 裝飾的 runner，呼叫 runner() 即執行 func(*args)。"""
    @timeit(repeat=repeat)
    def run():
        return func(*args)
    return run

def measure_one(n, repeat=5):
    # 資料準備：已排序與打亂版本
    sorted_data = list(range(n))
    shuffled = sorted_data[:] 
    random.shuffle(shuffled)

    target_found = n - 1          # 常見 worst-case（linear 最慢）
    target_missing = -1           # 找不到的情況（linear 仍要掃完整個 list）

    # 線性搜尋（在已排序或未排序皆一樣）
    linear_runner = make_runner(linear_search, shuffled, target_found, repeat=repeat)
    linear_runner()
    linear_time = linear_runner.last_elapsed

    # 測量排序成本（對 shuffled 做排序）
    def sort_copy(data):
        return sorted(data)
    sort_runner = make_runner(sort_copy, shuffled, repeat=repeat)
    sorted_copy = sort_runner()  # 回傳值是 sorted list（unused 之外測時用）
    sort_time = sort_runner.last_elapsed

    # 二分搜尋（必須使用已排序資料）
    # 使用上面 sort_runner 產生的 sorted_copy 為輸入
    binary_runner = make_runner(binary_search, sorted_copy, target_found, repeat=repeat)
    binary_runner()
    binary_time = binary_runner.last_elapsed

    return {
        "n": n,
        "linear_ms": linear_time * 1000,
        "binary_ms": binary_time * 1000,
        "sort_ms": sort_time * 1000,
        "sort_plus_binary_ms": (sort_time + binary_time) * 1000,
    }

def main():
    sizes = [1000, 5000, 20000, 100000]
    print("n, linear(ms), binary(ms), sort(ms), sort+binary(ms)")
    for n in sizes:
        res = measure_one(n, repeat=5)
        print(f"{res['n']}, {res['linear_ms']:.3f}, {res['binary_ms']:.3f}, {res['sort_ms']:.3f}, {res['sort_plus_binary_ms']:.3f}")

if __name__ == "__main__":
    main()