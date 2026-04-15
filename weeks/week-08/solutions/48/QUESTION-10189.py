import sys


def main():
    # 先把所有輸入一次讀完，避免一組一組慢慢處理
    data = sys.stdin.read().split()
    index = 0
    field_number = 1
    outputs = []

    # 8 個方向：上、下、左、右、四個斜角
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    while index < len(data):
        # 讀入目前這張地圖的大小
        n = int(data[index])
        m = int(data[index + 1])
        index += 2

        if n == 0 and m == 0:
            break

        grid = data[index:index + n]
        index += n

        # 題目要求每組資料前面都要先印 Field #X:
        outputs.append(f'Field #{field_number}:')

        for row in range(n):
            answer_row = []
            for col in range(m):
                # 地雷直接保留
                if grid[row][col] == '*':
                    answer_row.append('*')
                    continue

                # 空白格子就數周圍地雷
                mine_count = 0
                for dr, dc in directions:
                    # 檢查周圍八個方向是否在地圖內，且剛好是地雷
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*':
                        mine_count += 1

                answer_row.append(str(mine_count))

            outputs.append(''.join(answer_row))

        field_number += 1

        # 不是最後一組資料時，補一個空行
        if index < len(data):
            outputs.append('')

    sys.stdout.write('\n'.join(outputs))


if __name__ == '__main__':
    main()
