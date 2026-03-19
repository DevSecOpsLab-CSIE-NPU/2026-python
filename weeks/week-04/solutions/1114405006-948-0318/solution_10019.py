"""UVA 10019（依題目檔描述）解答。"""

from __future__ import annotations

import sys


def solve(data: str) -> str:
    """
    逐行讀取兩個整數，輸出它們的絕對差。

    題目為 EOF 輸入模式：
    讀到輸入結束為止，每一行各自輸出一個答案。
    """
    outputs: list[str] = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        a_str, b_str = line.split()
        a = int(a_str)
        b = int(b_str)
        outputs.append(str(abs(a - b)))

    if not outputs:
        return ""

    return "\n".join(outputs) + "\n"


def main() -> None:
    """標準輸入輸出入口。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
