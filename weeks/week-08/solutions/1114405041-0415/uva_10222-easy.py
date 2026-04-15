from __future__ import annotations

import sys


# 用標準鍵盤每一排建立對照表。
ROWS = [
    "`1234567890-=",
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./",
]

# 這題的精神就是：把每個字元往左找一格，還原原本想打的字。
TRANSLATION = {}
for row in ROWS + [row.upper() for row in ROWS]:
    for index in range(1, len(row)):
        TRANSLATION[row[index]] = row[index - 1]


def solve(data: str) -> str:
    """
    逐字解碼：
    - 如果字元在鍵盤表裡，就換成左邊那一個鍵。
    - 如果是空白或其他不用轉的符號，就原樣保留。
    """
    outputs: list[str] = []

    for line in data.splitlines():
        decoded = "".join(TRANSLATION.get(char, char) for char in line)
        outputs.append(decoded)

    return "\n".join(outputs)


def main() -> None:
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()
