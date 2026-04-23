# 檔名: q118-easy.py
# 這是 UVA 118 的簡易好記版 (Easy Version)

def solve_robots(world_size, robots_data):
    max_x, max_y = world_size
    scents = set()
    results = []

    # --- 簡單版轉向與移動字典 ---
    # 直接寫死左轉和右轉的結果，不用背數學的 +4 或 %4 餘數運算！
    turn_left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
    turn_right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    moves = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}

    for robot in robots_data:
        x, y, face, instructions = robot
        is_lost = False

        for cmd in instructions:
            if is_lost:
                break

            # 直接使用字典查詢，直觀且不容易出錯
            if cmd == 'L':
                face = turn_left[face]
            elif cmd == 'R':
                face = turn_right[face]
            elif cmd == 'F':
                dx, dy = moves[face]
                next_x = x + dx
                next_y = y + dy

                # 簡單暴力的出界判斷：小於 0 或大於最大值就是掉出去了
                if next_x < 0 or next_x > max_x or next_y < 0 or next_y > max_y:
                    # 檢查腳下有沒有前人留下的標記 (scent)
                    if (x, y, face) in scents:
                        continue  # 有標記，不執行這一步，繼續讀下一個指令
                    else:
                        scents.add((x, y, face)) # 沒標記，掉下去並留下自己的標記
                        is_lost = True
                else:
                    # 沒出界，正常移動到新座標
                    x, y = next_x, next_y

        # 組合結果字串：不用複雜的三元運算式，直接用基礎的 if-else 搞定
        if is_lost:
            results.append(f"{x} {y} {face} LOST")
        else:
            results.append(f"{x} {y} {face}")

    return results