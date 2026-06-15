# 118_ai_easy.py
# UVA 118：機器人移動 - 簡單版，附詳細繁體中文註解
# 功能：模擬機器人在矩形網格中移動，處理指令並輸出最終位置

# 方向映射：N, E, S, W
directions = ['N', 'E', 'S', 'W']
# 移動向量：北、東、南、西
moves = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

def simulate_robot(grid_width, grid_height, start_x, start_y, start_dir, instructions, scents):
    """
    模擬單個機器人的移動。
    
    參數：
    grid_width, grid_height: 網格大小
    start_x, start_y, start_dir: 初始位置和方向
    instructions: 指令字串
    scents: 所有機器人共享的香跡集合
    
    返回：
    (final_x, final_y, final_dir, lost)
    """
    x, y = start_x, start_y
    dir_index = directions.index(start_dir)
    lost = False
    
    for cmd in instructions:
        if cmd == 'L':
            # 左轉：方向索引減1
            dir_index = (dir_index - 1) % 4
        elif cmd == 'R':
            # 右轉：方向索引加1
            dir_index = (dir_index + 1) % 4
        elif cmd == 'F':
            # 前進
            dx, dy = moves[directions[dir_index]]
            new_x = x + dx
            new_y = y + dy
            
            # 檢查是否超出邊界
            if new_x < 0 or new_x > grid_width or new_y < 0 or new_y > grid_height:
                # 如果當前位置有 scent，忽略
                if (x, y) in scents:
                    continue
                else:
                    # 掉落，標記 scent
                    scents.add((x, y))
                    lost = True
                    break
            else:
                # 移動
                x, y = new_x, new_y
    
    final_dir = directions[dir_index]
    return x, y, final_dir, lost

# 主程式：讀取輸入
if __name__ == "__main__":
    import sys
    lines = sys.stdin.read().strip().split('\n')
    
    # 第一行：網格大小
    grid_line = lines[0].split()
    grid_width = int(grid_line[0])
    grid_height = int(grid_line[1])
    
    # 所有機器人共享的香跡集合
    scents = set()
    
    # 處理每個機器人
    i = 1
    while i < len(lines):
        # 機器人初始位置
        robot_line = lines[i].split()
        start_x = int(robot_line[0])
        start_y = int(robot_line[1])
        start_dir = robot_line[2]
        
        # 指令
        instructions = lines[i+1]
        
        # 模擬（共享 scents）
        final_x, final_y, final_dir, lost = simulate_robot(
            grid_width, grid_height, start_x, start_y, start_dir, instructions, scents
        )
        
        # 輸出
        output = f"{final_x} {final_y} {final_dir}"
        if lost:
            output += " LOST"
        print(output)
        
        i += 2