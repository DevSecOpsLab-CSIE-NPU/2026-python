import sys

# 進階實作版：使用方向列表與模數運算 (Modulo) 處理轉向
# 核心邏輯：利用集合 (Set) 儲存掉落標記，確保 O(1) 的查詢效率
def solve():
    # 讀取地圖大小
    line = sys.stdin.readline()
    if not line: return
    max_x, max_y = map(int, line.split())
    
    # 儲存掉落標記的座標
    scents = set()
    # 定義方向順序：順時針旋轉
    directions = ['N', 'E', 'S', 'W']
    # 對應方向的位移量
    move_map = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    while True:
        # 讀取機器人初始位置
        pos_line = sys.stdin.readline()
        if not pos_line: break
        x, y, d = pos_line.split()
        x, y = int(x), int(y)
        
        # 讀取指令集
        commands = sys.stdin.readline().strip()
        
        is_lost = False
        curr_dir_idx = directions.index(d)
        
        for cmd in commands:
            if cmd == 'R':
                curr_dir_idx = (curr_dir_idx + 1) % 4
            elif cmd == 'L':
                curr_dir_idx = (curr_dir_idx - 1) % 4
            elif cmd == 'F':
                dx, dy = move_map[directions[curr_dir_idx]]
                nx, ny = x + dx, y + dy
                
                # 檢查是否超出邊界
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    # 如果當前位置沒有被標記過，才會掉下去
                    if (x, y) not in scents:
                        scents.add((x, y))
                        is_lost = True
                        break
                    else:
                        # 有標記，無視這個會掉下去的指令
                        continue
                else:
                    x, y = nx, ny
        
        # 輸出結果
        result = f"{x} {y} {directions[curr_dir_idx]}"
        if is_lost:
            result += " LOST"
        print(result)

if __name__ == "__main__":
    solve()