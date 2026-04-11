"""
UVA 118 - Martian Robots (ZeroJudge c082)

解法：
  - 方向陣列 ['N','E','S','W']，左轉索引 -1、右轉 +1（mod 4）
  - 用集合 scents 記錄曾有機器人掉落的格子座標
  - 機器人在有標記的格子上，若 F 會越界則忽略該指令
  - 掉落時輸出最後位置 + "LOST"，並將該格加入 scents
"""

import sys


def solve():
    data = sys.stdin.read().split('\n')
    idx = 0

    max_x, max_y = map(int, data[idx].strip().split())
    idx += 1

    directions = ['N', 'E', 'S', 'W']
    dx = {'N': 0, 'E': 1, 'S':  0, 'W': -1}
    dy = {'N': 1, 'E': 0, 'S': -1, 'W':  0}

    scents = set()
    results = []

    while idx < len(data):
        line = data[idx].strip()
        idx += 1
        if not line:
            continue

        parts = line.split()
        if len(parts) != 3:
            continue

        x, y, facing = int(parts[0]), int(parts[1]), parts[2]

        if idx >= len(data):
            break
        commands = data[idx].strip()
        idx += 1

        lost = False

        for cmd in commands:
            if cmd == 'L':
                facing = directions[(directions.index(facing) - 1) % 4]
            elif cmd == 'R':
                facing = directions[(directions.index(facing) + 1) % 4]
            elif cmd == 'F':
                new_x = x + dx[facing]
                new_y = y + dy[facing]

                if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                    if (x, y) not in scents:
                        scents.add((x, y))
                        lost = True
                        break
                else:
                    x, y = new_x, new_y

        if lost:
            results.append(f"{x} {y} {facing} LOST")
        else:
            results.append(f"{x} {y} {facing}")

    print('\n'.join(results))


solve()