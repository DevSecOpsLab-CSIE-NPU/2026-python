"""
UVA 272 - TEX Quotes（easy 版）

超好記口訣：
  看到雙引號就「開、關、開、關」交替換。

實作重點：
  - 用一個旗標 `open_q` 記目前要放開引號還是關引號
  - 遇到 "：
      open_q=True  -> 放 ``
      open_q=False -> 放 ''
    然後把 open_q 反轉
"""

from __future__ import annotations

import sys


def conv(text: str, open_q: bool = True) -> tuple[str, bool]:
    """easy 版單行轉換函式。"""
    out: list[str] = []

    for ch in text:
        if ch == '"':
            out.append("``" if open_q else "''")
            open_q = not open_q
        else:
            out.append(ch)

    return "".join(out), open_q


def conv_all(lines: list[str]) -> list[str]:
    """easy 版多行轉換（狀態跨行）。"""
    open_q = True
    ans: list[str] = []

    for line in lines:
        s, open_q = conv(line, open_q)
        ans.append(s)

    return ans


def main() -> None:
    open_q = True

    for raw in sys.stdin:
        line = raw.rstrip("\n")
        s, open_q = conv(line, open_q)
        print(s)


if __name__ == "__main__":
    main()
