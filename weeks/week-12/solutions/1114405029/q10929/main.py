import sys


# 判斷一個大數字字串是否為 11 的倍數
#
# 回傳：
# True  -> 是 11 的倍數
# False -> 不是 11 的倍數
def is_multiple_of_11(number_string):

    # odd_sum：
    #     奇數位置數字總和
    #
    # even_sum：
    #     偶數位置數字總和
    odd_sum = 0
    even_sum = 0

    # enumerate 可以同時取得：
    #
    # index：
    #     目前位置
    #
    # ch：
    #     目前字元
    for index, ch in enumerate(number_string):

        # 將字元轉成整數
        digit = int(ch)

        # Python 索引從 0 開始
        #
        # index = 0 -> 第 1 位（奇數位）
        # index = 1 -> 第 2 位（偶數位）
        #
        # 因此：
        # index % 2 == 0
        # 代表奇數位
        if index % 2 == 0:
            odd_sum += digit

        # 否則代表偶數位
        else:
            even_sum += digit

    # 計算奇偶位總和差
    difference = abs(odd_sum - even_sum)

    # 如果差值可以被 11 整除
    # 則原數字是 11 的倍數
    return difference % 11 == 0


def main():

    # 儲存所有輸出結果
    answers = []

    # 逐行讀取輸入
    for line in sys.stdin:

        # 去除換行與空白
        number_string = line.strip()

        # 遇到 0 代表輸入結束
        if number_string == "0":
            break

        # 判斷是否為 11 的倍數
        if is_multiple_of_11(number_string):

            answers.append(
                f"{number_string} is a multiple of 11."
            )

        else:

            answers.append(
                f"{number_string} is not a multiple of 11."
            )

    # 一次輸出所有答案
    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()