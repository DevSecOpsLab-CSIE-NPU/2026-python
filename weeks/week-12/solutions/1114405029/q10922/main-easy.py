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

        # current 用來記錄目前正在處理的數字
        current = s

        # degree 用來記錄做了幾次加總
        degree = 0

        # 不斷重複做各位數加總
        while True:

            # 計算各位數總和
            total = 0

            for ch in current:
                total += int(ch)

            # 做完一次加總
            degree += 1

            # 如果得到 9
            # 代表原數是 9 的倍數
            if total == 9:

                print(
                    f"{s} is a multiple of 9 and has 9-degree {degree}."
                )

                break

            # 如果結果已經小於 9
            # 代表不可能再變成 9
            if total < 9:

                print(
                    f"{s} is not a multiple of 9."
                )

                break

            # 將總和轉成字串
            # 繼續下一輪各位數加總
            current = str(total)


if __name__ == "__main__":
    main()