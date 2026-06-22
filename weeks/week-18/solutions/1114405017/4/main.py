import sys
import timeit

STUDENT_ID = "1114405017"


def get_target(student_id: str) -> int:
    """根據學號末兩碼計算搜尋目標 K。"""
    last_two = int(student_id[-2:])
    return 100 + last_two


def linear_search(array: list[int], target: int) -> tuple[int, int]:
    """線性搜尋，回傳索引與比較次數。"""
    comparisons = 0
    for index, value in enumerate(array):
        comparisons += 1
        if value == target:
            return index, comparisons
    return -1, comparisons


def binary_search(array: list[int], target: int) -> tuple[int, int]:
    """二分搜尋，回傳索引與比較次數。"""
    left = 0
    right = len(array) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if array[mid] == target:
            return mid, comparisons
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons


def parse_input() -> list[int]:
    """讀取輸入：若第一個數字等於剩餘元素數量，則視為長度標頭。"""
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return []

    numbers = [int(token) for token in tokens]
    if len(numbers) >= 2 and numbers[0] == len(numbers) - 1:
        return numbers[1:]
    return numbers


def measure_search(func, array: list[int], target: int) -> float:
    """使用 timeit 測量搜尋函式執行時間。"""
    loops = 1000 if len(array) <= 100 else 100 if len(array) <= 10000 else 10
    timer = timeit.Timer(lambda: func(array, target))
    return timer.timeit(number=loops) / loops


def main() -> None:
    array = parse_input()
    target = get_target(STUDENT_ID)

    found_idx, found_cmp = linear_search(array, target)
    if found_idx >= 0:
        print(f"FOUND {found_idx} cmp={found_cmp}")
    else:
        print(f"NOT FOUND cmp={found_cmp}")

    linear_time = measure_search(linear_search, array, target)
    binary_time = measure_search(binary_search, array, target)
    print(f"linear : {linear_time:.6f} s")
    print(f"binary : {binary_time:.6f} s")

    if binary_time < linear_time:
        print("=> binary faster")
    elif linear_time < binary_time:
        print("=> linear faster")
    else:
        print("=> same speed")


if __name__ == "__main__":
    main()
