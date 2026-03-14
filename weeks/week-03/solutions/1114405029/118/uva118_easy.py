import sys

# 方向依序排列，方便左轉右轉
dirs = ["N", "E", "S", "W"]

# 不同方向前進時，座標的變化量
move = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0)
}

# 讀取世界右上角座標
max_x, max_y = map(int, sys.stdin.readline().split())

# 記錄會讓機器人掉出去的危險位置與方向
scent = set()

# 一組一組讀取機器人資料
for line in sys.stdin:

    # 如果遇到空行就跳過
    if not line.strip():
        continue

    # 讀取機器人的起始位置與方向
    x, y, d = line.split()
    x = int(x)
    y = int(y)

    # 讀取這台機器人的指令
    commands = sys.stdin.readline().strip()

    # 記錄這台機器人是否掉出世界
    lost = False

    # 依序執行每個指令
    for c in commands:

        # 左轉
        if c == "L":
            d = dirs[(dirs.index(d) - 1) % 4]

        # 右轉
        elif c == "R":
            d = dirs[(dirs.index(d) + 1) % 4]

        # 前進
        else:
            dx, dy = move[d]
            nx = x + dx
            ny = y + dy

            # 如果前進後會掉出邊界
            if nx < 0 or ny < 0 or nx > max_x or ny > max_y:

                # 如果這個位置與方向以前已經有人掉出去過
                # 就忽略這次前進指令
                if (x, y, d) in scent:
                    continue

                # 否則留下氣味，並標記 LOST
                scent.add((x, y, d))
                lost = True
                break

            # 沒掉出去就正常前進
            x, y = nx, ny

    # 輸出結果
    if lost:
        print(x, y, d, "LOST")
    else:
        print(x, y, d)