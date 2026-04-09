#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
UVA 118 - 機器人模擬器（簡化版）

簡化思路：
1. 用方向字串直接計算轉向和移動
2. 用一個列表處理方向循環
3. 核心邏輯極簡化
"""

DIRECTIONS = ["N", "E", "S", "W"]


def turn_left(d):
    """左轉：列表索引 -1"""
    return DIRECTIONS[(DIRECTIONS.index(d) - 1) % 4]


def turn_right(d):
    """右轉：列表索引 +1"""
    return DIRECTIONS[(DIRECTIONS.index(d) + 1) % 4]


def forward(x, y, d):
    """前進一格"""
    moves = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
    dx, dy = moves[d]
    return x + dx, y + dy


def is_out(x, y, max_x, max_y):
    """檢查是否超出邊界"""
    return x < 0 or y < 0 or x > max_x or y > max_y


def solve():
    """主程式"""
    import sys

    lines = [l.strip() for l in sys.stdin if l.strip()]
    if not lines:
        return

    max_x, max_y = map(int, lines[0].split())
    scents = set()

    for i in range(1, len(lines), 2):
        parts = lines[i].split()
        x, y = int(parts[0]), int(parts[1])
        d = parts[2]
        cmds = lines[i + 1].strip()
        lost = False

        for cmd in cmds:
            if cmd == "L":
                d = turn_left(d)
            elif cmd == "R":
                d = turn_right(d)
            elif cmd == "F":
                nx, ny = forward(x, y, d)
                if is_out(nx, ny, max_x, max_y):
                    if (x, y) in scents:
                        continue
                    else:
                        scents.add((x, y))
                        lost = True
                        break
                else:
                    x, y = nx, ny

        print(f"{x} {y} {d}" + (" LOST" if lost else ""))


if __name__ == "__main__":
    solve()
