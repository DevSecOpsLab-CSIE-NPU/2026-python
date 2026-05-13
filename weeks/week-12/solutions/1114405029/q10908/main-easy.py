import sys


def main():

    # 讀取測試資料組數
    t = int(sys.stdin.readline())

    # 逐組處理測試資料
    for _ in range(t):

        # 讀取 M、N、Q
        #
        # m：網格有幾行
        # n：網格有幾列
        # q：查詢次數
        m, n, q = map(int, sys.stdin.readline().split())

        # 讀取整個字元網格
        grid = []

        for _ in range(m):
            grid.append(sys.stdin.readline().strip())

        # 題目要求每組測試資料要先輸出 M N Q
        print(m, n, q)

        # 處理每一筆查詢
        for _ in range(q):

            # 讀取查詢中心點
            r, c = map(int, sys.stdin.readline().split())

            # 中心點的字元
            # 正方形內所有字元都必須和它一樣
            target = grid[r][c]

            # 最小答案一定是 1
            # 因為中心點自己一定可以形成 1x1 正方形
            answer = 1

            # 半徑從 1 開始
            # radius = 1 表示邊長 3
            # radius = 2 表示邊長 5
            radius = 1

            # 不斷嘗試往外擴張
            while True:

                # 計算擴張後的上下左右邊界
                top = r - radius
                bottom = r + radius
                left = c - radius
                right = c + radius

                # 如果超出邊界，就不能再擴張
                if top < 0 or bottom >= m or left < 0 or right >= n:
                    break

                # 假設目前這個正方形合法
                ok = True

                # 檢查目前正方形範圍內的所有格子
                # 這是最直觀的寫法，比較容易理解與手寫
                for i in range(top, bottom + 1):
                    for j in range(left, right + 1):

                        # 只要有一個字元和中心字元不同
                        # 目前正方形就不合法
                        if grid[i][j] != target:
                            ok = False
                            break

                    # 如果已經發現不合法，就不用繼續檢查
                    if not ok:
                        break

                # 如果目前正方形合法
                # 更新最大邊長，然後繼續往外擴張
                if ok:
                    answer = radius * 2 + 1
                    radius += 1

                # 如果目前正方形不合法
                # 更大的正方形一定也不合法
                else:
                    break

            # 輸出此查詢的答案
            print(answer)


if __name__ == "__main__":
    main()