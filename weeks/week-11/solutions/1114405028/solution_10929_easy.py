"""UVA 10929 簡單版本"""


def multiple_of_11_simple(num_str):
    """最簡單的解法"""
    odd_sum = 0
    even_sum = 0

    for i, digit in enumerate(reversed(num_str)):
        if i % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)

    if (odd_sum - even_sum) % 11 == 0:
        return f"{num_str} is a multiple of 11."
    else:
        return f"{num_str} is not a multiple of 11."


if __name__ == "__main__":
    print(multiple_of_11_simple("11"))
    print(multiple_of_11_simple("121"))
    print(multiple_of_11_simple("123"))
