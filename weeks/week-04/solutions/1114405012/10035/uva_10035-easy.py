from __future__ import annotations

import sys


def count_carry_times(a: int, b: int) -> int:
    """
    計算 a + b 在直式加法中總共產生幾次進位。

    做法：
    - 從個位數開始相加。
    - 只要該位總和 >= 10，就算一次進位。
    - 把進位帶到下一位，持續到所有位數處理完。
    """
    carry = 0
    times = 0

    # 只要兩個數字還有任一位未處理，就持續做直式加法
    while a > 0 or b > 0:
        # 取出個位數，再把前一位的 carry 加進來
        now_sum = (a % 10) + (b % 10) + carry

        if now_sum >= 10:
            # 本位發生進位，次數 +1，下一位要帶 1
            times += 1
            carry = 1
        else:
            # 沒進位，下一位不帶值
            carry = 0

        # 去掉已經處理完的個位數
        a //= 10
        b //= 10

    return times


def solve(data: str) -> str:
    """
    UVA 10035 easy 版

    輸入每行兩個整數，直到遇到 0 0 結束。
    依照進位次數輸出三種格式：
    - 0 次：No carry operation.
    - 1 次：1 carry operation.
    - >=2 次：x carry operations.
    """
    tokens = data.split()
    out: list[str] = []

    # 兩兩讀取 (x, y)
    idx = 0
    while idx + 1 < len(tokens):
        x = int(tokens[idx])
        y = int(tokens[idx + 1])
        idx += 2

        # 0 0 是結束標記，不輸出結果
        if x == 0 and y == 0:
            break

        c = count_carry_times(x, y)

        if c == 0:
            out.append("No carry operation.")
        elif c == 1:
            out.append("1 carry operation.")
        else:
            out.append(f"{c} carry operations.")

    return "\n".join(out)


def main() -> None:
    raw = sys.stdin.read()
    sys.stdout.write(solve(raw))


if __name__ == "__main__":
    main()
