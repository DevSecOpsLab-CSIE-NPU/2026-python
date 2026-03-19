"""UVA 10035（簡單好記 + 繁體中文詳細註解版）。

題目要做的事：
- 每行讀入兩個整數。
- 模擬直式加法，計算發生幾次進位（carry）。
- 讀到 0 0 代表輸入結束，不再處理後續資料。
"""

from __future__ import annotations

import sys


# 好記口訣：
# 1) 由個位數開始加
# 2) 若總和 >= 10 就有進位
# 3) carry 會帶到下一位
# 4) 全部位數跑完，回傳進位次數


def count_carry(a: str, b: str) -> int:
    """
    計算兩個非負整數字串相加時，總共發生幾次進位。

    參數：
    a, b：只包含數字字元的字串。

    回傳：
    進位次數（整數）。
    """
    # i、j 從最後一個字元開始，代表從個位數往前算。
    i = len(a) - 1
    j = len(b) - 1

    # carry 代表前一位加法是否有進位（0 或 1）。
    carry = 0

    # count 用來累積進位次數。
    count = 0

    # 只要任一數字還有位數沒處理，就持續計算。
    while i >= 0 or j >= 0:
        # 若已超出左邊界，該數字位數視為 0。
        da = ord(a[i]) - ord("0") if i >= 0 else 0
        db = ord(b[j]) - ord("0") if j >= 0 else 0

        # 本位總和 = 左位 + 右位 + 前一位進位。
        s = da + db + carry

        # 若本位總和 >= 10，代表發生一次進位。
        if s >= 10:
            carry = 1
            count += 1
        else:
            carry = 0

        # 往更高位移動。
        i -= 1
        j -= 1

    return count


def format_answer(c: int) -> str:
    """依題目格式回傳對應敘述字串。"""
    if c == 0:
        return "No carry operation."
    if c == 1:
        return "1 carry operation."
    return f"{c} carry operations."


def solve(data: str) -> str:
    """
    解析整份輸入資料並輸出所有答案。

    輸入規則：
    - 每行兩個整數。
    - 遇到 0 0 停止。

    輸出規則：
    - 每組資料輸出一行 carry 描述。
    """
    outputs: list[str] = []

    # EOF 題型：逐行讀取直到結束。
    for raw in data.splitlines():
        line = raw.strip()

        # 空白行直接略過，避免 split() 失敗。
        if not line:
            continue

        a, b = line.split()

        # 終止條件：0 0
        if a == "0" and b == "0":
            break

        c = count_carry(a, b)
        outputs.append(format_answer(c))

    # 若沒有任何有效測資，回傳空字串。
    if not outputs:
        return ""

    # 多行答案用換行串接，最後補一個換行。
    return "\n".join(outputs) + "\n"


def main() -> None:
    """標準輸入輸出入口。"""
    print(solve(sys.stdin.read()), end="")


if __name__ == "__main__":
    main()
