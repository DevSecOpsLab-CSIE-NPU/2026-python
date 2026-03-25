from __future__ import annotations


def analyze_medians_easy(values: list[int]) -> tuple[int, int, int]:
    arr = sorted(values)
    n = len(arr)
    low = arr[(n - 1) // 2]
    high = arr[n // 2]
    count_in_range = 0
    for v in arr:
        if low <= v <= high:
            count_in_range += 1
    possible_count = high - low + 1
    return low, count_in_range, possible_count


def solve_io(data: str) -> str:
    nums = data.split()
    idx = 0
    lines: list[str] = []
    while idx < len(nums):
        n = int(nums[idx])
        idx += 1
        values = []
        for _ in range(n):
            values.append(int(nums[idx]))
            idx += 1
        a, cnt, possible = analyze_medians_easy(values)
        lines.append(f"{a} {cnt} {possible}")
    return "\n".join(lines)


def main() -> None:
    import sys

    out = solve_io(sys.stdin.read())
    if out:
        print(out)


if __name__ == "__main__":
    main()
