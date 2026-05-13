import sys


def main():

    # 讀取測試資料組數
    n = int(sys.stdin.readline())

    # 逐組處理資料
    for _ in range(n):

        # 讀取總和與差
        #
        # s：兩隊分數總和
        # d：兩隊分數差
        s, d = map(int, sys.stdin.readline().split())

        # 如果差比分數總和還大
        # 代表較小分數一定會變成負數
        #
        # 例如：
        # s = 20
        # d = 40
        #
        # low = (20 - 40) / 2 = -10
        #
        # 分數不可能是負數
        if d > s:
            print("impossible")
            continue

        # 根據公式：
        #
        # high = (s + d) / 2
        # low  = (s - d) / 2
        #
        # 分數必須是整數
        #
        # 如果 s + d 為奇數
        # 就無法得到整數答案
        if (s + d) % 2 != 0:
            print("impossible")
            continue

        # 計算較大的分數
        high = (s + d) // 2

        # 計算較小的分數
        low = (s - d) // 2

        # 輸出答案
        # 題目要求較大的分數先輸出
        print(high, low)


# Python 主程式入口
if __name__ == "__main__":
    main()