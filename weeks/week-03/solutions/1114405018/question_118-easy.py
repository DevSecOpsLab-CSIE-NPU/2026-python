"""UVA 118（Mutant Flatworld Explorers）- easy 版

題目重點：
1. 世界是矩形座標，範圍從 (0, 0) 到 (X, Y)。
2. 機器人指令只有三種：
   - L：左轉 90 度
   - R：右轉 90 度
   - F：往目前朝向前進一格
3. 若 F 會讓機器人走出邊界，該機器人會 LOST，
   並在「掉落前的座標」留下 scent（氣味標記）。
4. 後續機器人在同一座標，若再次遇到會掉落的 F，需忽略該指令。
"""

import sys

# 方向轉向表：用查表方式取代 if-else 連鎖，方便記憶
L = {"N": "W", "W": "S", "S": "E", "E": "N"}
R = {"N": "E", "E": "S", "S": "W", "W": "N"}

# 前進位移表：依方向得到 (dx, dy)
M = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}


def main() -> None:
    # 讀入所有非空白行，避免空行影響後續 split
    a = [s.strip() for s in sys.stdin if s.strip()]
    if not a:
        return

    # 第一行是世界右上角座標 (X, Y)
    X, Y = map(int, a[0].split())

    # scent: 記錄「曾經掉落前」的座標點
    # out: 收集每台機器人的最終輸出
    # i: 從第 2 行開始，每兩行一組（起始狀態 + 指令字串）
    scent, out, i = set(), [], 1

    while i + 1 < len(a):
        # 機器人初始狀態：x y direction
        x, y, d = a[i].split()
        x, y = int(x), int(y)
        # 一旦掉落（LOST）就停止處理該機器人剩餘指令
        lost = False

        # 逐字處理指令
        for c in a[i + 1]:
            if c == "L":
                d = L[d]
            elif c == "R":
                d = R[d]
            else:
                # c == 'F'：嘗試往前走一格
                dx, dy = M[d]
                nx, ny = x + dx, y + dy

                # 新位置仍在地圖內：正常移動
                if 0 <= nx <= X and 0 <= ny <= Y:
                    x, y = nx, ny

                # 新位置超出邊界：檢查目前位置是否有 scent
                # - 沒有 scent：本次真的會掉落，留下 scent 並標記 LOST
                # - 已有 scent：忽略這次 F（不移動、不掉落）
                elif (x, y) not in scent:
                    scent.add((x, y))
                    lost = True
                    break

        # 按題目格式輸出；若掉落要在最後加上 LOST
        out.append(f"{x} {y} {d}" + (" LOST" if lost else ""))
        i += 2

    # 所有機器人結果逐行輸出
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
