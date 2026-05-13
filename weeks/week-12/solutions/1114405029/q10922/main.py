import sys


# 計算一個字串數字的各位數總和
#
# 例如：
# "123" -> 1 + 2 + 3 = 6
def digit_sum(number_string):

    total = 0

    # 逐一處理每個字元
    for ch in number_string:

        # 將字元轉成數字後累加
        total += int(ch)

    return total


# 計算 9-degree
#
# 如果不是 9 的倍數：
# 回傳 0
#
# 如果是 9 的倍數：
# 回傳對應的 9-degree
def calculate_nine_degree(number_string):

    # current 用來記錄目前正在處理的數字
    current = number_string

    # degree 記錄目前做了幾次各位數加總
    degree = 0

    # 不斷重複各位數加總
    while True:

        # 計算目前數字的各位數總和
        total = digit_sum(current)

        # 每做一次加總
        # 9-degree 就加 1
        degree += 1

        # 如果加總結果是 9
        # 代表找到答案
        if total == 9:
            return degree

        # 如果加總結果小於 9
        # 代表不可能再變成 9
        #
        # 例如：
        # 1、2、3、4...
        #
        # 都不可能變成 9
        if total < 9:
            return 0

        # 繼續下一輪處理
        current = str(total)


def main():

    # 儲存所有輸出結果
    answers = []

    # 逐行讀取輸入
    for line in sys.stdin:

        # 去除換行
        number_string = line.strip()

        # 遇到 0 代表輸入結束
        if number_string == "0":
            break

        # 計算 9-degree
        degree = calculate_nine_degree(number_string)

        # 如果 degree 為 0
        # 代表不是 9 的倍數
        if degree == 0:

            answers.append(
                f"{number_string} is not a multiple of 9."
            )

        # 否則代表是 9 的倍數
        else:

            answers.append(
                f"{number_string} is a multiple of 9 and has 9-degree {degree}."
            )

    # 一次輸出所有答案
    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()