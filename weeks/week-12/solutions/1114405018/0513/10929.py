"""
UVA 10929 — Counting 11s

題目重點：
判斷一個最多 1000 位的超大正整數是否為 11 的倍數。

11 的倍數判定技巧：
一個整數的「奇數位數字之和」與「偶數位數字之和」的差，若是 11 的倍數，
則原整數也是 11 的倍數。

位置計數方式（從右往左，從 1 開始計）：
- 個位（最右邊）是第 1 位（奇數位）
- 十位是第 2 位（偶數位）
- 百位是第 3 位（奇數位）
- 依此類推

例子：
- N = 121
  個位 1（奇數位）+ 百位 1（奇數位）= 2（奇數位數字和）
  十位 2（偶數位）= 2（偶數位數字和）
  差 = 2 - 2 = 0，0 是 11 的倍數，所以 121 是 11 的倍數。✓

- N = 1234
  個位 4 + 百位 2 = 6（奇數位數字和）
  十位 3 + 千位 1 = 4（偶數位數字和）
  差 = 6 - 4 = 2，2 不是 11 的倍數，所以 1234 不是 11 的倍數。✓
"""


def is_multiple_of_11(number_text):
    """
    判斷字串形式的整數是否為 11 的倍數。

    參數：
        number_text: 由數字字元組成的字串

    回傳：
        True 若是 11 的倍數，False 否則

    演算法：
    1. 從字串的最後一位開始（個位）遍歷到第一位
    2. 紀錄位置（從 1 開始），奇數位累加到 odd_sum，偶數位累加到 even_sum
    3. 計算差 = odd_sum - even_sum
    4. 判斷差是否能被 11 整除
    """
    odd_sum = 0    # 奇數位數字之和
    even_sum = 0   # 偶數位數字之和
    position = 1   # 位置計數器，從 1 開始

    # 從字串最後往前遍歷（從個位開始）
    for i in range(len(number_text) - 1, -1, -1):
        digit = int(number_text[i])

        if position % 2 == 1:  # 奇數位
            odd_sum += digit
        else:  # 偶數位
            even_sum += digit

        position += 1

    # 計算差並判斷是否為 11 的倍數
    difference = odd_sum - even_sum
    return difference % 11 == 0


def main():
    """主程式：逐行讀入數字，遇到 0 結束。"""
    while True:
        number_text = input().strip()

        # 題目規定輸入 0 表示結束
        if number_text == "0":
            break

        if is_multiple_of_11(number_text):
            print(f"{number_text} is a multiple of 11.")
        else:
            print(f"{number_text} is not a multiple of 11.")


if __name__ == "__main__":
    main()
