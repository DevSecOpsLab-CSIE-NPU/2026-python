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

    # 第一行：矩形右上角座標（左下角固定為 (0,0)）
    max_x, max_y = map(int, data[idx].strip().split())
    idx += 1

    # 方向陣列（順時針：N→E→S→W）
    directions = ['N', 'E', 'S', 'W']

    # 各方向的 x, y 位移量
    dx = {'N': 0, 'E': 1, 'S':  0, 'W': -1}
    dy = {'N': 1, 'E': 0, 'S': -1, 'W':  0}

    # 記錄曾有機器人掉落的座標（留下「標記」）
    scents = set()

    results = []

    while idx < len(data):
        line = data[idx].strip()
        idx += 1
        if not line:
            continue

        # 解析機器人初始位置與面向方向
        parts = line.split()
        if len(parts) != 3:
            continue

        x, y, facing = int(parts[0]), int(parts[1]), parts[2]

        # 讀取指令字串
        if idx >= len(data):
            break
        commands = data[idx].strip()
        idx += 1

        lost = False  # 是否已掉落

        for cmd in commands:
            if cmd == 'L':
                # 左轉：索引 -1（mod 4）
                facing = directions[(directions.index(facing) - 1) % 4]
            elif cmd == 'R':
                # 右轉：索引 +1（mod 4）
                facing = directions[(directions.index(facing) + 1) % 4]
            elif cmd == 'F':
                new_x = x + dx[facing]
                new_y = y + dy[facing]

                if new_x < 0 or new_x > max_x or new_y < 0 or new_y > max_y:
                    # 即將越界
                    if (x, y) not in scents:
                        # 無標記：機器人掉落，留下標記，停止執行後續指令
                        scents.add((x, y))
                        lost = True
                        break
                    # 有標記：忽略此 F 指令，機器人原地不動
                else:
                    # 正常前進
                    x, y = new_x, new_y

        if lost:
            results.append(f"{x} {y} {facing} LOST")
        else:
            results.append(f"{x} {y} {facing}")

    print('\n'.join(results))


solve()
