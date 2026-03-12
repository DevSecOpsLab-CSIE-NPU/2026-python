"""
UVA 118 - easy 版本（更好記）

設計目標：
- 變數與函式命名短、直覺
- 核心流程只有三步：
  1) 轉向
  2) 嘗試前進
  3) 套用 scent 規則
- 保留繁體中文詳細註解，方便背誦
"""

from __future__ import annotations

# 順時針方向表，方便做索引運算
dirs = ["N", "E", "S", "W"]

# 各方向對應前進位移
step = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def rot(d: str, c: str) -> str:
    """
    旋轉方向。
    - c = L：左轉 90 度
    - c = R：右轉 90 度
    """
    i = dirs.index(d)
    if c == "L":
        return dirs[(i - 1) % 4]
    return dirs[(i + 1) % 4]


def oob(x: int, y: int, mx: int, my: int) -> bool:
    """是否超出邊界（out of bounds）。"""
    return x < 0 or x > mx or y < 0 or y > my


def run_one(x: int, y: int, d: str, cmds: str, mx: int, my: int, scent: set) -> tuple:
    """
    執行一台機器人，回傳 (x, y, d, lost)。

    scent 規則（好記版）：
    - F 會掉出去 + 這格有 scent -> 忽略 F
    - F 會掉出去 + 這格沒 scent -> 變 LOST，並留下 scent
    """
    for c in cmds:
        if c in ("L", "R"):
            d = rot(d, c)
            continue

        # c == 'F'：嘗試前進
        dx, dy = step[d]
        nx, ny = x + dx, y + dy

        if oob(nx, ny, mx, my):
            if (x, y) in scent:
                # 有標記就忽略這個危險動作
                continue
            scent.add((x, y))
            return x, y, d, True

        x, y = nx, ny

    return x, y, d, False


def solve_all(text: str) -> str:
    """處理整份輸入，回傳整份輸出。"""
    ls = [s.strip() for s in text.splitlines() if s.strip()]
    if not ls:
        return ""

    mx, my = map(int, ls[0].split())
    scent = set()
    ans = []

    i = 1
    while i + 1 < len(ls):
        x, y, d = ls[i].split()
        cmds = ls[i + 1]

        fx, fy, fd, lost = run_one(int(x), int(y), d, cmds, mx, my, scent)

        if lost:
            ans.append(f"{fx} {fy} {fd} LOST")
        else:
            ans.append(f"{fx} {fy} {fd}")

        i += 2

    return "\n".join(ans)


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data.strip():
        print(solve_all(data))
