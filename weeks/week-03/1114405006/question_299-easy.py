"""UVA 299 的簡易版本。

這個版本故意選用最容易背的做法：
- 直接模擬 bubble sort 的相鄰交換
- 每交換一次就累加一次
- 因為題目要的就是最少相鄰交換次數

為什麼這樣好記：
1. 只能交換相鄰車廂
2. 不對就換一下
3. 換了幾次就是答案
"""

from __future__ import annotations

import sys


def count_swaps(train: list[int]) -> int:
    """用最直觀的 bubble sort 方式計算交換次數。

    這裡不是把火車真的排序成另一個版本再去比對，
    而是直接在每次發現相鄰順序不對時就交換，並累加次數。

    對學習者來說，這比逆序數更容易從紙上手算。
    """
    numbers = train[:]  # 保留原始資料，避免直接改掉外部傳入的 list
    swaps = 0
    length = len(numbers)

    # bubble sort 的核心：左到右掃描，相鄰不對就交換。
    # 每一輪都會把目前最大的元素往右推一格。
    for end in range(length - 1, 0, -1):
        for index in range(end):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                swaps += 1

    return swaps


def solve_text(text: str) -> str:
    """解析輸入並輸出答案。

    用 split() 直接吃 token，最不怕多餘空白或空行。
    """
    tokens = text.split()
    if not tokens:
        return ""

    case_count = int(tokens[0])
    position = 1
    outputs = []

    for _ in range(case_count):
        length = int(tokens[position])
        position += 1

        train = []
        for _ in range(length):
            train.append(int(tokens[position]))
            position += 1

        swaps = count_swaps(train)
        outputs.append(f"Optimal train swapping takes {swaps} swaps.")

    return "\n".join(outputs) + "\n"


def main() -> None:
    """主函式：讀入整份資料並輸出結果。"""
    input_text = sys.stdin.read()
    if input_text.strip():
        sys.stdout.write(solve_text(input_text))


if __name__ == "__main__":
    main()
