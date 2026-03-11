"""
UVA 118 — 乖乖的機器人（Mutant Flatworld Explorers）
AI 教學版本：附繁體中文註解
"""
import sys

# 四個方向：北、東、南、西（順時針排列）
dirs = ['N', 'E', 'S', 'W']
# 各方向對應的 x 位移量
dx = [0, 1, 0, -1]
# 各方向對應的 y 位移量
dy = [1, 0, -1, 0]

# 一次讀取所有輸入，按行分割
lines = sys.stdin.read().split('\n')
idx = 0

# 第一行：世界右上角座標 (mx, my)，左下角固定為 (0, 0)
mx, my = map(int, lines[idx].split())
idx += 1

# scent 集合：記錄掉落過的（位置, 方向），防止後續機器人從同處掉落
scents = set()

# 逐一處理每個機器人
while idx < len(lines):
    line = lines[idx].strip()
    idx += 1
    # 跳過空行
    if not line:
        continue

    # 讀取機器人初始位置 (x, y) 和方向 d
    parts = line.split()
    x, y, d = int(parts[0]), int(parts[1]), parts[2]
    # 將方向字元轉為索引（0=N, 1=E, 2=S, 3=W）
    di = dirs.index(d)

    # 讀取指令集
    if idx >= len(lines):
        break
    cmds = lines[idx].strip()
    idx += 1

    lost = False
    # 逐一執行指令
    for c in cmds:
        if c == 'L':
            # 左轉 90 度：索引逆時針移動（+3 等同 -1 mod 4）
            di = (di + 3) % 4
        elif c == 'R':
            # 右轉 90 度：索引順時針移動
            di = (di + 1) % 4
        elif c == 'F':
            # 計算前進後的新座標
            nx = x + dx[di]
            ny = y + dy[di]
            # 檢查是否超出世界邊界
            if nx < 0 or nx > mx or ny < 0 or ny > my:
                # 若此位置+方向已有 scent 標記，忽略此指令
                if (x, y, di) in scents:
                    continue
                # 否則留下 scent 標記，機器人掉落
                scents.add((x, y, di))
                lost = True
                break
            # 更新座標
            x, y = nx, ny

    # 輸出結果
    if lost:
        print(x, y, dirs[di], "LOST")
    else:
        print(x, y, dirs[di])
