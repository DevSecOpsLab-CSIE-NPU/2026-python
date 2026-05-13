"""
UVA 10922 — 2 the 9s

題目重點：
輸入一個正整數 X，反覆做「各位數字加總」的動作。
如果最後能得到 9，表示 X 是 9 的倍數。

9-degree（9 的深度）的定義：
從原數字開始，每做一次數字加總就算一層。
例如：
  18 -> 1 + 8 = 9
  所以 18 的 9-degree 是 1。

又例如：
  999999 -> 54 -> 9
  所以 999999 的 9-degree 是 2。

這題最重要的是：輸入可能非常大，所以不能直接轉成一般整數後再做很多花式運算。
不過只要把字串每一位拿來加總，就可以安全處理。
"""


def digit_sum(number_text):
    """
    計算字串形式整數的各位數字總和。

    參數：
        number_text: 由數字字元組成的字串

    回傳：
        各位數字總和（整數）
    """
    total = 0
    for digit in number_text:
        total += int(digit)
    return total


def degree_of_nine(number_text):
    """
    計算一個數字字串的 9-degree。

    回傳規則：
        - 如果不是 9 的倍數，回傳 0
        - 如果是 9 的倍數，回傳它的 9-degree

    計算方式：
        1. 先做一次 digit sum，這算第 1 次加總
        2. 若結果不是 9，就持續對結果做 digit sum
        3. 每做一次都把深度 +1
        4. 當結果變成 9，停止並回傳深度
    """
    current = number_text
    depth = 0

    # 如果本身就是單一數字，直接判斷。
    # 題目定義中，9 自己也是 9 的倍數，而且 9-degree 為 1。
    if len(current) == 1:
        return 1 if current == "9" else 0

    # 反覆做數字加總，直到只剩一位數。
    # 每做一次加總，就代表深度多 1。
    while len(current) > 1:
        current = str(digit_sum(current))
        depth += 1

    # 若最後不是 9，就代表不是 9 的倍數。
    if current != "9":
        return 0

    return depth


def main():
    """主程式：逐行讀入，遇到 0 結束。"""
    while True:
        number_text = input().strip()

        # 題目規定輸入 0 表示結束，不需要處理。
        if number_text == "0":
            break

        depth = degree_of_nine(number_text)

        if depth == 0:
            print(f"{number_text} is not a multiple of 9.")
        else:
            print(f"9-degree of {number_text} is {depth}.")


if __name__ == "__main__":
    main()