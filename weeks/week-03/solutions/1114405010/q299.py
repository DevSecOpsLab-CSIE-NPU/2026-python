"""UVA 299 - Train Swapping"""

import sys


def inversion_count(values):
    """計算陣列中的反序對數量，即最少相鄰交換次數。"""
    arr = values[:]
    total_swaps = 0

    for end in range(len(arr) - 1, 0, -1):
        for i in range(end):
            if arr[i] <= arr[i + 1]:
                continue
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            total_swaps += 1

    return total_swaps


def solve(text: str) -> str:
    parts = text.split()
    if not parts:
        return ""

    case_count = int(parts[0])
    p = 1
    outputs = []

    for _ in range(case_count):
        train_len = int(parts[p])
        p += 1
        trains = list(map(int, parts[p : p + train_len]))
        p += train_len
        swaps = inversion_count(trains)
        outputs.append(f"Optimal train swapping takes {swaps} swaps.")

    return "\n".join(outputs)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
