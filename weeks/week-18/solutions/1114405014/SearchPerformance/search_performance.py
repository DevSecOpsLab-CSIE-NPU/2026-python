import sys
import timeit

from plot import make_radar_chart


TARGET = 114


def linear_search(arr: list[int], target: int) -> tuple[bool, int, int]:
    """
    Search target from left to right.

    Return:
        found: whether target exists
        index: index of target, or -1 if not found
        cmp_count: number of comparisons
    """
    cmp_count = 0

    for index, value in enumerate(arr):
        cmp_count += 1

        if value == target:
            return True, index, cmp_count

    return False, -1, cmp_count


def binary_search(arr: list[int], target: int) -> tuple[bool, int, int]:
    """
    Search target in a sorted array by binary search.

    Return:
        found: whether target exists
        index: index of target, or -1 if not found
        cmp_count: number of loop comparisons

    Comparison rule:
        Each loop compares target with arr[mid], so cmp_count increases once
        per loop.
    """
    left = 0
    right = len(arr) - 1
    cmp_count = 0

    while left <= right:
        mid = (left + right) // 2
        cmp_count += 1

        if arr[mid] == target:
            return True, mid, cmp_count

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False, -1, cmp_count


def benchmark_search(
    arr: list[int],
    target: int,
    repeat: int = 1000,
) -> dict[str, float]:
    """
    Benchmark linear search and binary search.

    The input array is copied and sorted inside this function to ensure
    binary search receives a sorted array.
    """
    if repeat < 1:
        raise ValueError("repeat must be greater than or equal to 1")

    sorted_arr = sorted(arr)

    linear_time = timeit.timeit(
        lambda: linear_search(sorted_arr, target),
        number=repeat,
    )

    binary_time = timeit.timeit(
        lambda: binary_search(sorted_arr, target),
        number=repeat,
    )

    return {
        "linear_time": linear_time,
        "binary_time": binary_time,
    }


def solve(input_text: str, target: int = TARGET) -> str:
    """
    Parse input, sort array, compare linear search and binary search.

    Input format:
        n
        a1 a2 ... an

    Newlines are not required. The parser reads n first, then reads n numbers.
    """
    tokens = input_text.split()

    if not tokens:
        return ""

    n = int(tokens[0])
    numbers = [int(token) for token in tokens[1:1 + n]]

    sorted_arr = sorted(numbers)

    linear_found, linear_index, linear_cmp = linear_search(sorted_arr, target)
    binary_found, binary_index, binary_cmp = binary_search(sorted_arr, target)

    found = linear_found or binary_found
    index = binary_index if binary_found else linear_index

    benchmark = benchmark_search(sorted_arr, target, repeat=1000)

    metrics = {
        "linear_time": benchmark["linear_time"],
        "binary_time": benchmark["binary_time"],
        "linear_cmp": linear_cmp,
        "binary_cmp": binary_cmp,
    }

    make_radar_chart(metrics, "assets/radar.png")

    status = "FOUND" if found else "NOT FOUND"
    faster = (
        "linear"
        if benchmark["linear_time"] < benchmark["binary_time"]
        else "binary"
    )

    return "\n".join([
        f"{status} index={index}",
        f"linear_cmp={linear_cmp}",
        f"binary_cmp={binary_cmp}",
        f"linear_time={benchmark['linear_time']:.8f}",
        f"binary_time={benchmark['binary_time']:.8f}",
        f"faster={faster}",
        "chart=assets/radar.png",
    ])


def main() -> None:
    input_text = sys.stdin.read()
    output = solve(input_text, TARGET)

    if output:
        print(output)


if __name__ == "__main__":
    main()
