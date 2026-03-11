import sys

# 常見的 UVA 299 範例輸入。
SAMPLE_INPUT = """3
3
1 3 2
4
4 3 2 1
2
2 1
"""

# 範例輸入對應的預期輸出。
SAMPLE_OUTPUT = """Optimal train swapping takes 1 swaps.
Optimal train swapping takes 6 swaps.
Optimal train swapping takes 1 swaps."""


def count_swaps(cars: list[int]) -> int:
    # 最少相鄰交換次數等於反序對數量。
    swaps = 0

    for i in range(len(cars)):
        for j in range(i + 1, len(cars)):
            if cars[i] > cars[j]:
                swaps += 1

    return swaps


def solve(text: str) -> str:
    # 使用 split() 直接處理所有整數，能自然忽略空白與換行。
    tokens = text.split()
    if not tokens:
        return ""

    index = 0
    case_count = int(tokens[index])
    index += 1
    output = []

    for _ in range(case_count):
        length = int(tokens[index])
        index += 1
        cars = [int(value) for value in tokens[index:index + length]]
        index += length

        swaps = count_swaps(cars)
        output.append(f"Optimal train swapping takes {swaps} swaps.")

    return "\n".join(output)


def run_sample_test() -> None:
    # 直接使用範例測資檢查演算法。
    result = solve(SAMPLE_INPUT)
    print(result)
    assert result == SAMPLE_OUTPUT, "範例測試未通過"


if __name__ == "__main__":
    # 在終端直接執行時，沒有輸入就跑範例測試。
    if sys.stdin.isatty():
        run_sample_test()
    else:
        data = sys.stdin.read()
        if not data.strip():
            sys.exit(0)
        print(solve(data))
