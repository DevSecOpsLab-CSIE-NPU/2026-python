"""
UVA 118 - Mutant Flatworld Explorers（easy 版）

好記口訣：
  轉向不動、前進看邊界、掉落留記號。

步驟：
  1. 讀一個指令字元。
  2. L/R 就改方向。
  3. F 就試著前進：
     - 會出界：看這格這方向有沒有 scent
       有 scent -> 忽略這次 F
       無 scent -> 留 scent 並 LOST
     - 不出界：更新座標
"""

from __future__ import annotations

import sys

D = ["N", "E", "S", "W"]
STEP = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def lft(d: str) -> str:
    """左轉。"""
    return D[(D.index(d) - 1) % 4]


def rgt(d: str) -> str:
    """右轉。"""
    return D[(D.index(d) + 1) % 4]


def sim(
    mx: int,
    my: int,
    x: int,
    y: int,
    d: str,
    cmds: str,
    scents: set[tuple[int, int, str]],
) -> tuple[int, int, str, bool]:
    """easy 版單機器人模擬。"""
    lost = False

    for c in cmds:
        if c == "L":
            d = lft(d)
        elif c == "R":
            d = rgt(d)
        else:
            dx, dy = STEP[d]
            nx, ny = x + dx, y + dy

            if nx < 0 or nx > mx or ny < 0 or ny > my:
                if (x, y, d) in scents:
                    continue
                scents.add((x, y, d))
                lost = True
                break

            x, y = nx, ny

    return x, y, d, lost


def fmt(x: int, y: int, d: str, lost: bool) -> str:
    """輸出格式字串。"""
    return f"{x} {y} {d} LOST" if lost else f"{x} {y} {d}"


def main() -> None:
    head = sys.stdin.readline().strip()
    if not head:
        return

    mx, my = map(int, head.split())
    scents: set[tuple[int, int, str]] = set()

    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            continue

        x, y, d = line.split()
        cmds = sys.stdin.readline().strip()

        rx, ry, rd, lost = sim(mx, my, int(x), int(y), d, cmds, scents)
        print(fmt(rx, ry, rd, lost))


if __name__ == "__main__":
    main()
