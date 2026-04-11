import sys

# 詳細繁體中文註解說明：
# 1. 我們先建立一個方向清單 'N', 'E', 'S', 'W'，
#    右轉就是往後數一個，左轉就是往前數一個。
# 2. 準備一個 scents 列表，記住哪些地方有人掉下去過。
# 3. 機器人走路時，如果下一步會出界，先看腳下有沒有別人的「警告標記」。

def solve():
    # 讀取地圖右上角的座標
    first_line = sys.stdin.readline().split()
    if not first_line: return
    max_x, max_y = int(first_line[0]), int(first_line[1])
    
    # 用來記住哪些坐標有「掉落標記」
    scents = []
    
    # 不斷讀取機器人資料直到結束
    while True:
        pos_data = sys.stdin.readline().split()
        if not pos_data: break
        
        curr_x = int(pos_data[0])
        curr_y = int(pos_data[1])
        facing = pos_data[2]
        
        # 指令集字串
        actions = sys.stdin.readline().strip()
        
        # 方向順序與索引位置
        dir_list = ['N', 'E', 'S', 'W']
        lost = False
        
        for act in actions:
            if act == 'R':
                # 右轉：N->E, E->S, S->W, W->N
                idx = dir_list.index(facing)
                facing = dir_list[(idx + 1) % 4]
            elif act == 'L':
                # 左轉：N->W, W->S, S->E, E->N
                idx = dir_list.index(facing)
                facing = dir_list[(idx - 1) % 4]
            elif act == 'F':
                # 計算前進後的座標
                next_x, next_y = curr_x, curr_y
                if facing == 'N': next_y += 1
                elif facing == 'E': next_x += 1
                elif facing == 'S': next_y -= 1
                elif facing == 'W': next_x -= 1
                
                # 判斷是否會掉出地圖 (邊界是 0 ~ max_x, 0 ~ max_y)
                if next_x < 0 or next_x > max_x or next_y < 0 or next_y > max_y:
                    # 檢查現在位置有沒有標記
                    if (curr_x, curr_y) in scents:
                        # 有標記，機器人很聰明，會無視掉下去的動作
                        continue
                    else:
                        # 沒標記，掉下去了！
                        scents.append((curr_x, curr_y))
                        lost = True
                        break
                else:
                    # 沒出界，正常移動
                    curr_x, curr_y = next_x, next_y
        
        # 印出最後狀態，如果有掉下去要加 LOST
        output = f"{curr_x} {curr_y} {facing}"
        if lost:
            output += " LOST"
        print(output)

if __name__ == "__main__":
    solve()