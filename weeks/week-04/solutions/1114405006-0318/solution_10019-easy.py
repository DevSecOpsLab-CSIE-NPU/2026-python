"""UVA 10019（簡單好記 + 詳細中文註解版）。

依你目前題目檔的描述：
- 每一行有兩個整數。
- 輸出這兩個整數的差值（正數，也就是絕對值）。
- 輸入是 EOF 模式，讀到檔案結尾為止。
"""

from __future__ import annotations

import sys


# 好記口訣：
# 1) 一行一行讀
# 2) 切成兩個數
# 3) 算 abs(a-b)
# 4) 每行輸出一個答案


def solve(data: str) -> str:
    """
    把整份輸入字串轉成題目要求的輸出字串。

    參數：
    data: 來自標準輸入的完整文字。

    回傳：
    每組資料的答案，以換行分隔；最後補一個換行。
    如果沒有有效資料，回傳空字串。
    """
    answers: list[str] = []

    # splitlines() 會把輸入切成一行一行，適合 EOF 題型。
    for raw in data.splitlines():
        line = raw.strip()

        # 遇到空白行就跳過，避免 split() 出錯。
        if not line:
            continue

        # 每行預期是兩個整數，例如："10 12"
        a_str, b_str = line.split()
        a = int(a_str)
        b = int(b_str)

        # 題目要求輸出正差值，因此使用絕對值。
        diff = abs(a - b)
        answers.append(str(diff))

    # 若整份輸入都沒有有效資料，不輸出任何內容。
    if not answers:
        return ""

    # 多組答案以換行連接，最後補 \n 符合線上評測習慣。
    return "\n".join(answers) + "\n"


def main() -> None:
    """標準輸入輸出入口：讀 stdin，寫 stdout。"""
    print(solve(sys.stdin.read()), end="")


if __name__ == "__main__":
    main()
