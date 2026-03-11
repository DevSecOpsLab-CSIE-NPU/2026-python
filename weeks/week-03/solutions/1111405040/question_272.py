"""
UVA 272 - TeX 引號轉換。
"""

from __future__ import annotations

import sys


def convert_quotes(text: str) -> str:
    """
    將每個雙引號 `"` 交替替換為開引號 `` 與閉引號 ''。
    """
    opening = True
    output: list[str] = []

    for ch in text:
        if ch == '"':
            if opening:
                output.append("``")
            else:
                output.append("''")
            opening = not opening
        else:
            output.append(ch)

    return "".join(output)


def solve(text: str) -> str:
    """處理完整輸入文字並回傳轉換結果。"""
    return convert_quotes(text)


def main() -> None:
    """主程式進入點。"""
    data = sys.stdin.read()
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
