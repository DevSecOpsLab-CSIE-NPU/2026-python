"""
UVA 10922 — 2 the 9s 簡易版

題目的核心：
一個數若「反覆把各位數字加起來，最後能變成 9」，就是 9 的倍數。
而加總的次數，就叫 9-degree（9 的深度）。

這一版的記法很簡單易背：
1. 輸入數字先當字串，避免超大整數造成溢位。
2. 建立 digit_sum 函式：把字串中每一位數字加總。
3. 建立 degree_of_nine 函式：反覆呼叫 digit_sum，直到只剩一位數。
4. 若最後是 9，則回傳加總次數（就是 9-degree）。
5. 若最後不是 9，就代表不是 9 的倍數。

範例：
- 18 -> 1+8=9（加了 1 次，所以 9-degree=1）
- 999999 -> 54 -> 9（加了 2 次，所以 9-degree=2）
"""


def digit_sum(number_text):
    """
    計算字串中所有數字的總和。

    邏輯很單純：
    - 從左到右，每次取一個字元（一位數字）
    - 把它轉成整數，加到 total 裡
    - 最後回傳總和

    例子：
    - digit_sum("123") 回傳 6（因為 1+2+3=6）
    - digit_sum("999") 回傳 27（因為 9+9+9=27）
    """
    total = 0
    for digit in number_text:
        total += int(digit)
    return total


def degree_of_nine(number_text):
    """
    計算一個數字字串的 9-degree（9 的深度）。

    回傳值：
    - 0：不是 9 的倍數
    - 正整數：表示這個數的 9-degree

    演算法思路：
    1. 如果輸入本身就是一位數，則直接判斷是否為 9
    2. 否則，反覆對字串做 digit_sum
    3. 每做一次 digit_sum，就把深度 +1，並把結果轉回字串
    4. 當結果只剩一位數時停止
    5. 若最後是 9，回傳深度；否則回傳 0
    """
    current = number_text
    degree = 0

    # 邊界情況：輸入本身已經是一位數
    # 只有 9 是 9 的倍數，而且 9-degree 定義為 1
    # 其他數字（1-8）都不是 9 的倍數
    if len(current) == 1:
        return 1 if current == "9" else 0

    # 主迴圈：反覆做 digit sum，直到只剩一位數
    # 每次迴圈都代表做了一次「各位數字加總」的動作
    while len(current) > 1:
        # 把目前的字串進行 digit_sum，得到一個整數
        # 然後轉回字串，供下一次迴圈使用
        current = str(digit_sum(current))
        # 紀錄做過了多少次 digit_sum
        degree += 1

    # 迴圈結束時，current 已經是一位數字
    # 若為 9，則原數是 9 的倍數，回傳做過幾次加總（degree）
    # 若不是 9，則回傳 0 表示不是 9 的倍數
    if current == "9":
        return degree

    return 0


def main():
    """
    主程式：讀取輸入、計算 9-degree，然後依題目格式輸出。

    輸入格式：
    - 每行一個正整數（可能非常長）
    - 以 0 結束（不需處理 0）

    輸出格式：
    - 如果是 9 的倍數：9-degree of <數字> is <深度>.
    - 如果不是：<數字> is not a multiple of 9.
    """
    while True:
        # 讀入一行輸入，strip() 去掉可能的多餘空白與換行符
        number_text = input().strip()

        # 若輸入為 0，代表結束，直接跳出迴圈
        if number_text == "0":
            break

        # 計算這個數字的 9-degree
        # 回傳值：0 表示不是 9 的倍數，否則是具體的深度
        degree = degree_of_nine(number_text)

        # 根據 degree 的值輸出對應的結果
        if degree == 0:
            # 不是 9 的倍數
            print(f"{number_text} is not a multiple of 9.")
        else:
            # 是 9 的倍數，輸出它的 9-degree
            print(f"9-degree of {number_text} is {degree}.")


if __name__ == "__main__":
    main()