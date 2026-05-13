import sys


def main():

    # 逐行讀取輸入
    for line in sys.stdin:

        # 移除前後空白與換行
        s = line.strip()

        # 如果輸入是 0
        # 代表輸入結束
        if s == "0":
            break

        # odd_sum：
        #     奇數位置數字總和
        #
        # even_sum：
        #     偶數位置數字總和
        odd_sum = 0
        even_sum = 0

        # 逐位處理數字
        for i in range(len(s)):

            # 將字元轉成整數
            digit = int(s[i])

            # Python 索引從 0 開始
            #
            # i = 0 -> 第 1 位（奇數位）
            # i = 1 -> 第 2 位（偶數位）
            #
            # 所以：
            # i % 2 == 0
            # 代表奇數位
            if i % 2 == 0:
                odd_sum += digit

            # 否則是偶數位
            else:
                even_sum += digit

        # 計算差值
        difference = abs(odd_sum - even_sum)

        # 如果差值可以被 11 整除
        # 則原數字是 11 的倍數
        if difference % 11 == 0:

            print(
                f"{s} is a multiple of 11."
            )

        else:

            print(
                f"{s} is not a multiple of 11."
            )


if __name__ == "__main__":
    main()