import sys


def solve_field(n, m, grid):
    # 這裡先準備 8 個方向
    # 每一組 (dx, dy) 代表從目前位置要往哪裡移動
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # 用來存最後答案的陣列
    result = []

    # 一列一列處理
    for i in range(n):
        # 先準備這一列的答案
        row = []

        # 一欄一欄處理
        for j in range(m):
            # 如果這格本身就是地雷
            # 那答案就直接放 *
            if grid[i][j] == '*':
                row.append('*')
            else:
                # 如果這格不是地雷
                # 就開始數周圍 8 格有幾顆地雷
                count = 0

                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy

                    # 先確認新位置沒有超出邊界
                    if 0 <= ni < n and 0 <= nj < m:
                        # 如果鄰居是地雷，就加 1
                        if grid[ni][nj] == '*':
                            count += 1

                # 把數字轉成字串後放進這一列答案
                row.append(str(count))

        # 這一列組好後，合成字串加入答案
        result.append(''.join(row))

    return result


def main():
    # 把整個輸入一次讀進來，再逐行處理
    lines = sys.stdin.read().splitlines()

    idx = 0
    field_number = 1
    all_outputs = []

    # 只要還有輸入資料，就繼續處理
    while idx < len(lines):
        n, m = map(int, lines[idx].split())
        idx += 1

        # 遇到 0 0 表示結束
        if n == 0 and m == 0:
            break

        # 讀入這一組地圖
        grid = []
        for _ in range(n):
            grid.append(lines[idx])
            idx += 1

        # 計算答案
        answer = solve_field(n, m, grid)

        # 先輸出 Field 編號
        all_outputs.append(f"Field #{field_number}:")
        # 再把地圖答案逐行加入
        for line in answer:
            all_outputs.append(line)

        field_number += 1

    # 題目要求每組測資之間空一行
    # 所以這裡在不同 Field 之間插入空行
    current = []
    blocks = []

    for line in all_outputs:
        if line.startswith("Field #") and current:
            blocks.append('\n'.join(current))
            current = [line]
        else:
            current.append(line)

    if current:
        blocks.append('\n'.join(current))

    print('\n\n'.join(blocks))


if __name__ == "__main__":
    main()