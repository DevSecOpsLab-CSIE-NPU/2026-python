"""
UVA 490 手打版（簡單好記）

步驟：
1. 找最長行寬 W
2. 輸出做 W 行
3. 每行從原始最後一行往上抓同欄字元，不足補空白
4. 右側補白去掉
"""


def rot_hand(lines: list[str]) -> list[str]:
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
    return "\n".join(rot_hand(text.splitlines()))


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data:
        print(solve_all(data), end="")
