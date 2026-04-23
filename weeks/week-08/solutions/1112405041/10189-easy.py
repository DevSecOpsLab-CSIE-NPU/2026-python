import sys

# 踩地雷 (Minesweeper) - 大一新鮮人輕鬆版
# 我們要幫地圖上每個空白格子算算看，它周圍 8 格到底有多少顆地雷

def main():
    # 讀取所有輸入內容，並切割成一個一個的字串
    input_text = sys.stdin.read().split()
    if not input_text:
        return

    idx = 0
    field_count = 1

    # 只要還沒讀到結束標記 (0 0)，就一直跑下去
    while idx < len(input_text):
        # 讀取列數 (n) 和行數 (m)
        rows = int(input_text[idx])
        cols = int(input_text[idx + 1])
        idx += 2

        # 如果列數和行數都是 0，就代表輸入結束了
        if rows == 0 and cols == 0:
            break

        # 讀取接下來的 rows 行地圖資料
        grid = []
        for i in range(rows):
            # 把每一行轉成字元清單，方便我們存取特定位置
            grid.append(list(input_text[idx]))
            idx += 1

        # 建立一個新的二維清單，用來存放計算後的結果
        result = []
        for r in range(rows):
            row_result = []
            for c in range(cols):
                # 如果原本就是地雷 (*)，那就維持原樣
                if grid[r][c] == '*':
                    row_result.append('*')
                else:
                    # 如果是空白 (.)，就要計算周圍 8 格的地雷數量
                    mines_found = 0

                    # 檢查周圍 8 個方向 (上方、下方、左方、右方，以及四個斜角)
                    # 我們用迴圈跑 -1, 0, 1 的偏移量
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            # 偏移量都是 0 的話，就是自己這格，跳過不看
                            if dr == 0 and dc == 0:
                                continue

                            # 計算鄰居的座標
                            nr = r + dr
                            nc = c + dc

                            # 檢查鄰居座標是否還在地圖範圍內
                            if 0 <= nr < rows and 0 <= nc < cols:
                                # 如果鄰居是地雷，計數器就加 1
                                if grid[nr][nc] == '*':
                                    mines_found += 1

                    # 把計算出來的數字轉成字串存進去
                    row_result.append(str(mines_found))
            result.append(row_result)

        # 依照題目要求輸出結果
        # 如果不是第一組資料，要先輸出一個空行跟上一組隔開
        if field_count > 1:
            print()

        print("Field #" + str(field_count) + ":")
        for r in range(rows):
            # 把清單中的字元合併成字串印出來
            line = ""
            for char in result[r]:
                line += char
            print(line)

        # 組號增加
        field_count += 1

if __name__ == "__main__":
    main()
