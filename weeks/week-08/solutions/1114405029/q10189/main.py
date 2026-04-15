import sys


def solve_field(n, m, grid):
    # 八個方向：左上、上、右上、左、右、左下、下、右下
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    # 先建立答案地圖，預設全部放 0
    result = [['0'] * m for _ in range(n)]

    # 逐格處理整張地圖
    for i in range(n):
        for j in range(m):
            # 如果目前格子是地雷，答案直接放 *
            if grid[i][j] == '*':
                result[i][j] = '*'
            else:
                # 否則統計周圍八格有幾顆地雷
                count = 0

                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy

                    # 先確認鄰居座標沒有超出邊界
                    if 0 <= ni < n and 0 <= nj < m:
                        # 如果鄰居是地雷，就加一
                        if grid[ni][nj] == '*':
                            count += 1

                # 把數字轉成字元存進答案地圖
                result[i][j] = str(count)

    # 把二維字元陣列轉成字串列表，方便輸出
    return [''.join(row) for row in result]


def main():
    lines = sys.stdin.read().splitlines()

    idx = 0
    field_number = 1
    outputs = []

    while idx < len(lines):
        n, m = map(int, lines[idx].split())
        idx += 1

        # 0 0 代表輸入結束
        if n == 0 and m == 0:
            break

        # 讀入本組地圖
        grid = lines[idx:idx + n]
        idx += n

        # 計算本組答案
        answer = solve_field(n, m, grid)

        # 不同測資之間要空一行，所以從第二組開始先加空字串
        if field_number > 1:
            outputs.append("")

        outputs.append(f"Field #{field_number}:")
        outputs.extend(answer)

        field_number += 1

    print('\n'.join(outputs))


if __name__ == "__main__":
    main()