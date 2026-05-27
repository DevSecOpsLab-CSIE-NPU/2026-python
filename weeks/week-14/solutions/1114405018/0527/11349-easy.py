"""UVA 11349 - Symmetric Matrix (easy version).

這個版本刻意把寫法縮到最容易記憶的形式：
先把所有數字一次讀進來，再依照每筆測資的矩陣大小切出資料，
最後同時檢查「是否有負數」與「是否中心對稱」兩個條件。

題目中的 `N = 3` 這種格式看起來不像純數字輸入，
但其實只要把文字忽略、把所有整數抓出來，就能直接還原題意。
"""

from __future__ import annotations

import re
import sys


def solve() -> None:
    # 題目輸入中除了數字以外還有 `N =` 這類字樣，
    # 所以最簡單的做法就是把所有整數抓出來。
    # 這樣可以避免手動拆字串格式，也比較不容易出錯。
    data = list(map(int, re.findall(r"-?\d+", sys.stdin.read())))
    if not data:
        return

    # 第一個數字是測資筆數 T，後面的數字才是每一筆矩陣內容。
    t = data[0]
    idx = 1
    answers: list[str] = []

    for case_no in range(1, t + 1):
        # 每筆測資先讀出矩陣維度 n。
        n = data[idx]
        idx += 1

        # ok 用來累積這筆測資是否通過檢查。
        # 一開始先假設是對稱矩陣，若之後發現任一條件不符就改成 False。
        ok = True
        matrix: list[list[int]] = []
        for _ in range(n):
            # 依照 n 讀出一整列資料。
            row = data[idx:idx + n]
            idx += n
            matrix.append(row)

            # 條件 1：任何元素只要是負數，就直接判定為非對稱矩陣。
            if any(value < 0 for value in row):
                ok = False

        # 條件 2：逐格比對中心對稱位置的值是否一致。
        # 中心對稱的意思是：左上角要對應右下角，第二列第一欄要對應倒數第二列倒數第二欄，依此類推。
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                    ok = False

        # 依照題目格式輸出結果。
        answers.append(f"Test #{case_no}: {'Symmetric.' if ok else 'Non-symmetric.'}")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()