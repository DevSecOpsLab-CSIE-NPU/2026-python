"""QUESTION-10035 easy 版。

這題最直觀的寫法，就是從個位數一路往左加：
1. 取出兩個數的個位數。
2. 加上上一位傳來的進位。
3. 如果總和大於等於 10，進位次數加一。
4. 再把兩個數都整除 10，繼續處理下一位。

因為題目資料量很小，這樣寫最容易背，也最不容易出錯。
"""

from __future__ import annotations

import sys


def solve(text: str) -> str:
    results = []

    for line in text.splitlines():
        if not line.strip():
            continue

        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break

        carry = 0
        carry_count = 0

        while a > 0 or b > 0:
            total = a % 10 + b % 10 + carry

            if total >= 10:
                carry = 1
                carry_count += 1
            else:
                carry = 0

            a //= 10
            b //= 10

        if carry_count == 0:
            results.append("No carry operation.")
        elif carry_count == 1:
            results.append("1 carry operation.")
        else:
            results.append(f"{carry_count} carry operations.")

    return "\n".join(results)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
