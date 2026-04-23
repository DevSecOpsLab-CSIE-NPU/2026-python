# 檔名: q118.py
# 這是 solution_118.py 的手打版本，此處為其加上更詳細的繁體中文註解。

def solve_robots(world_size, robots_data):
    # 解包 (Unpack) 世界邊界的最大 X 和 Y 座標
    max_x, max_y = world_size
    # 建立一個 set 來儲存所有「失聯 (LOST)」機器人墜落前的位置與方向標記 (scent)。
    # 使用 set 可以快速查詢 (O(1) 時間複雜度)。
    # scent 的格式為 (x, y, direction)，確保只有同位置同方向的墜落會被保護。
    scents = set()
    # 建立一個 list 來收集所有機器人的最終狀態報告。
    results = []

    # --- 導航輔助資料結構 ---
    # 依序定義方向 N, E, S, W，方便用索引進行左/右轉運算。
    # N=0, E=1, S=2, W=3
    directions = ['N', 'E', 'S', 'W']
    # 建立一個字典，將方向字母映射到其對應的索引，方便快速查找。
    dir_to_idx = {d: i for i, d in enumerate(directions)}
    # 定義每個方向前進一步時，X 和 Y 座標的變化量。
    moves = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    # 依序處理收到的每一台機器人資料
    for robot in robots_data:
        # 解包機器人的初始狀態：(X座標, Y座標, 當前方向, 指令字串)
        x, y, current_dir_char, instructions = robot
        # 初始化該機器人的失聯狀態為 False
        is_lost = False

        # 執行該機器人的每一條指令
        for instruction in instructions:
            # 如果機器人已經失聯 (is_lost 為 True)，就立刻跳出迴圈，不再執行後續指令。
            if is_lost:
                break

            # 根據指令字元判斷要執行的動作
            if instruction == 'L':
                # 'L' (左轉): 將當前方向索引減 1。
                # 加上 4 再取 4 的餘數，是為了處理 0-1=-1 的情況，使其能正確循環到 3 (W)。
                current_idx = dir_to_idx[current_dir_char]
                new_idx = (current_idx - 1 + 4) % 4
                current_dir_char = directions[new_idx]
            elif instruction == 'R':
                # 'R' (右轉): 將當前方向索引加 1。
                # 取 4 的餘數，確保 3+1=4 能正確循環到 0 (N)。
                current_idx = dir_to_idx[current_dir_char]
                new_idx = (current_idx + 1) % 4
                current_dir_char = directions[new_idx]
            elif instruction == 'F':
                # 'F' (前進): 根據當前方向，取得 X, Y 的變化量
                dx, dy = moves[current_dir_char]
                # 計算下一步的座標
                next_x, next_y = x + dx, y + dy

                # 檢查下一步是否會掉出世界邊界
                if not (0 <= next_x <= max_x and 0 <= next_y <= max_y):
                    # 如果會掉出邊界，檢查目前位置是否有其他機器人留下的 scent
                    if (x, y, current_dir_char) in scents:
                        # 如果有 scent 保護，則忽略這次的 'F' 指令，繼續執行下一條指令。
                        continue
                    else:
                        # 如果沒有 scent 保護，則留下自己的 scent，並將狀態設為失聯。
                        scents.add((x, y, current_dir_char))
                        is_lost = True
                else:
                    # 如果下一步仍在邊界內，則安全移動，更新機器人座標。
                    x, y = next_x, next_y

        # 組合最終狀態報告字串
        # f-string 中的三元運算式：如果 is_lost 為 True，則在結尾加上 " LOST"，否則加空字串。
        status = f"{x} {y} {current_dir_char}{' LOST' if is_lost else ''}"
        # 將該機器人的狀態報告加入結果列表中
        results.append(status)

    return results