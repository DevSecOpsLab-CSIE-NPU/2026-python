import timeit
from typing import List, Tuple


def binary_search(arr: List[int], target: int) -> Tuple[bool, int]:
    lo, hi = 0, len(arr) - 1
    cmp = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        cmp += 1
        if arr[mid] == target:
            return True, cmp
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False, cmp


def linear_search(arr: List[int], target: int) -> Tuple[bool, int]:
    cmp = 0
    for x in arr:
        cmp += 1
        if x == target:
            return True, cmp
    return False, cmp


def timeit_compare(arr: List[int], target: int, number: int = 100) -> dict:
    linear_time = timeit.timeit(lambda: linear_search(arr, target), number=number)
    binary_time = timeit.timeit(lambda: binary_search(arr, target), number=number)
    faster = 'binary' if binary_time < linear_time else 'linear'
    return {
        'linear': linear_time,
        'binary': binary_time,
        'faster': faster
    }


def main():
    import sys

    # 讀取輸入
    data = sys.stdin.read().strip().split()
    if not data:
        return

    m = int(data[0])
    arr = list(map(int, data[1:1 + m])) if m > 0 else []

    K = 118  # 100 + 學號末兩碼 18

    # 二分搜尋
    found, cmp = binary_search(arr, K)
    if found:
        idx = arr.index(K)
        print(f"FOUND idx={idx} cmp={cmp}")
    else:
        print(f"NOT FOUND cmp={cmp}")

    # timeit 比較
    result = timeit_compare(arr, K, number=100)
    print(f"linear : {result['linear']:.4f} s")
    print(f"binary : {result['binary']:.4f} s")
    print(f"=> {result['faster']} faster")


if __name__ == '__main__':
    main()
