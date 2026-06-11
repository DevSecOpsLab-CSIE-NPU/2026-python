"""
UVA 10929 — 11's multiple 解決方案
判斷超大整數是否為 11 的倍數。
"""


def is_multiple_of_11(num_str):
    """回傳判斷字串數字是否為 11 的倍數的結果字串。"""
    odd_sum = 0
    even_sum = 0
    for idx, digit_char in enumerate(reversed(num_str)):
        digit = int(digit_char)
        if idx % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    if (odd_sum - even_sum) % 11 == 0:
        return f"{num_str} is a multiple of 11."
    return f"{num_str} is not a multiple of 11."


def main():
    while True:
        num_str = input().strip()
        if num_str == "0":
            break
        print(is_multiple_of_11(num_str))


if __name__ == "__main__":
    main()
