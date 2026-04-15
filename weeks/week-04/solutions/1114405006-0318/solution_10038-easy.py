"""UVA 10038（簡單好記 + 繁體中文詳細註解版）。

Jolly Jumper 定義：
- 序列長度為 n。
- 把每一對相鄰數字做絕對差，必須剛好出現 1 到 n-1 這些值。
- 每個值要出現一次（用集合判斷最簡單）。
"""

from __future__ import annotations

import sys


# 好記口訣：
# 1) 算相鄰差的絕對值
# 2) 放進集合
# 3) 比對集合是否等於 {1..n-1}


def is_jolly(seq: list[int]) -> bool:
    """
    判斷單一序列是否為 Jolly Jumper。

    參數：
    seq: 一組整數序列。

    回傳：
    True  表示是 Jolly Jumper。
    False 表示不是。
    """
    n = len(seq)

    # 長度 0 或 1 時，不需要任何差值，視為 Jolly。
    if n <= 1:
        return True

    # diffs 用來收集相鄰差的絕對值。
    diffs = set()

    # 依序計算 |seq[i] - seq[i-1]|
    for i in range(1, n):
        diffs.add(abs(seq[i] - seq[i - 1]))

    # Jolly 的必要且充分條件：
    # 相鄰差集合剛好等於 {1, 2, ..., n-1}
    return diffs == set(range(1, n))


def solve(data: str) -> str:
    """
    解析所有輸入行並輸出結果。

    輸入格式（每行）：
    n a1 a2 ... an

    輸出格式（每行）：
    Jolly
    或
    Not jolly
    """
    outputs: list[str] = []

    # UVA 常見是 EOF 輸入，逐行處理即可。
    for raw in data.splitlines():
        line = raw.strip()

        # 略過空白行，避免 split 後資料不足。
        if not line:
            continue

        nums = list(map(int, line.split()))

        # 第一個數是 n，後面 n 個數是序列。
        n = nums[0]
        seq = nums[1 : 1 + n]

        # 依判斷結果輸出對應字串。
        outputs.append("Jolly" if is_jolly(seq) else "Not jolly")

    if not outputs:
        return ""

    # 每組結果一行，最後補換行。
    return "\n".join(outputs) + "\n"


def main() -> None:
    """標準輸入輸出入口。"""
    print(solve(sys.stdin.read()), end="")


if __name__ == "__main__":
    main()
