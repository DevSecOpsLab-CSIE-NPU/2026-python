"""
UVA 490 - easy 版本（更簡單、好記）

口訣：
- 找最長長度 W
- 新輸出做 W 行
- 每一行都從「原本的最後一行」往上抓同一欄
- 抓不到就補空白
"""

from __future__ import annotations


def rot_easy(lines: list[str]) -> list[str]:
    """順時針旋轉 90 度（簡潔版）。"""
    if not lines:
        return []

    w = max(len(s) for s in lines)
    ans = []

    for c in range(w):
        tmp = []
        for s in lines[::-1]:
            tmp.append(s[c] if c < len(s) else " ")
        ans.append("".join(tmp).rstrip())

    return ans


def solve_all(text: str) -> str:
    """處理整份輸入。"""
    return "\n".join(rot_easy(text.splitlines()))


if __name__ == "__main__":
    import sys

    raw = sys.stdin.read()
    if raw:
        print(solve_all(raw), end="")
