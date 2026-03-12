"""
UVA 272 - easy 版本（更好背）

口訣：
- 看到雙引號就「開、關、開、關」輪流換
- 開 -> ``
- 關 -> ''
- 其他字元原封不動
"""

from __future__ import annotations


def tex_quote_easy(text: str) -> str:
    """把一般雙引號轉成 TeX 引號（簡潔版）。"""
    out = []
    open_now = True

    for c in text:
        if c == '"':
            out.append("``" if open_now else "''")
            open_now = not open_now
        else:
            out.append(c)

    return "".join(out)


def solve_all(text: str) -> str:
    """與正式版同功能，命名更直覺。"""
    return tex_quote_easy(text)


if __name__ == "__main__":
    import sys

    raw = sys.stdin.read()
    if raw:
        print(solve_all(raw), end="")
