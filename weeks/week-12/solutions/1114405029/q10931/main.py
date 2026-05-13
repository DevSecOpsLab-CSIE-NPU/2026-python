import sys


# 將十進位整數轉成二進位字串
# 並計算其中 1 的個數
#
# 回傳：
# binary_string：
#     二進位表示
#
# parity_count：
#     二進位中 1 的個數
def convert_to_binary_and_count_parity(number):

    # 用來儲存二進位數字
    binary_digits = []

    # parity_count：
    #     記錄二進位中 1 的數量
    parity_count = 0

    # 不斷除以 2
    while number > 0:

        # 取得最低位元
        bit = number % 2

        # 加入二進位串列
        binary_digits.append(str(bit))

        # 如果目前位元是 1
        # parity 加 1
        if bit == 1:
            parity_count += 1

        # 去掉目前最低位元
        number //= 2

    # 因為剛剛是從低位到高位加入
    # 所以需要反轉
    binary_digits.reverse()

    # 將串列接成字串
    binary_string = "".join(binary_digits)

    return binary_string, parity_count


def main():

    # 儲存所有輸出結果
    answers = []

    # 逐行讀取輸入
    for line in sys.stdin:

        # 轉成整數
        number = int(line.strip())

        # 如果輸入是 0
        # 代表結束
        if number == 0:
            break

        # 取得二進位表示與 parity
        binary_string, parity_count = convert_to_binary_and_count_parity(number)

        # 按照題目格式輸出
        answers.append(
            f"The parity of {binary_string} is {parity_count} (mod 2)."
        )

    # 一次輸出所有答案
    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()