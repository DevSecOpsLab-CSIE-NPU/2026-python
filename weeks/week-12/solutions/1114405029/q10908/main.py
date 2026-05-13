import sys


# 計算某一個查詢中心點可以形成的最大正方形邊長
#
# grid：
#     字元網格
#
# row_count：
#     網格總列數，也就是 M
#
# col_count：
#     網格總欄數，也就是 N
#
# center_r：
#     查詢中心點的列座標
#
# center_c：
#     查詢中心點的欄座標
def largest_square(grid, row_count, col_count, center_r, center_c):

    # 取得中心點的字元
    # 正方形內所有字元都必須和這個字元相同
    center_char = grid[center_r][center_c]

    # 計算最多可以往外擴張幾圈
    #
    # center_r：
    #     中心點到上邊界的距離
    #
    # center_c：
    #     中心點到左邊界的距離
    #
    # row_count - 1 - center_r：
    #     中心點到下邊界的距離
    #
    # col_count - 1 - center_c：
    #     中心點到右邊界的距離
    #
    # 取最小值，代表不能超出任何一個邊界
    max_radius = min(
        center_r,
        center_c,
        row_count - 1 - center_r,
        col_count - 1 - center_c
    )

    # 最小的正方形就是中心點自己
    # 邊長為 1
    answer = 1

    # 從半徑 1 開始往外擴張
    # radius = 1 時，邊長是 3
    # radius = 2 時，邊長是 5
    for radius in range(1, max_radius + 1):

        # 計算目前正方形的上下左右邊界
        top = center_r - radius
        bottom = center_r + radius
        left = center_c - radius
        right = center_c + radius

        # 假設目前這一圈是合法的
        valid = True

        # 檢查上邊界與下邊界
        for col in range(left, right + 1):

            # 如果上邊界或下邊界有任一字元不同
            # 代表目前正方形不合法
            if grid[top][col] != center_char or grid[bottom][col] != center_char:
                valid = False
                break

        # 如果上下邊界都合法，才需要繼續檢查左右邊界
        if valid:

            # 左右邊界的角落其實已經在上下邊界檢查過
            # 所以 row 從 top + 1 到 bottom - 1 即可
            for row in range(top + 1, bottom):

                # 如果左邊界或右邊界有任一字元不同
                # 代表目前正方形不合法
                if grid[row][left] != center_char or grid[row][right] != center_char:
                    valid = False
                    break

        # 如果目前這一圈合法
        # 更新答案為目前正方形邊長
        if valid:
            answer = radius * 2 + 1

        # 如果目前這一圈不合法
        # 更大的正方形一定也不可能合法
        # 因此可以直接停止
        else:
            break

    # 回傳最大合法正方形邊長
    return answer


def main():

    # 一次讀取所有輸入
    data = sys.stdin.read().splitlines()

    # 如果沒有輸入資料，直接結束
    if not data:
        return

    # 第一行是測試資料組數
    test_case_count = int(data[0])

    # index 用來記錄目前讀到第幾行
    index = 1

    # 儲存所有輸出結果
    output = []

    # 逐組處理測試資料
    for _ in range(test_case_count):

        # 讀取 M、N、Q
        row_count, col_count, query_count = map(int, data[index].split())
        index += 1

        # 讀取字元網格
        grid = data[index:index + row_count]
        index += row_count

        # 題目要求每組測試資料要先輸出 M N Q
        output.append(f"{row_count} {col_count} {query_count}")

        # 處理每一個查詢
        for _ in range(query_count):

            # 讀取中心點座標
            center_r, center_c = map(int, data[index].split())
            index += 1

            # 計算最大正方形邊長
            result = largest_square(
                grid,
                row_count,
                col_count,
                center_r,
                center_c
            )

            # 加入輸出結果
            output.append(str(result))

    # 一次輸出全部結果
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()