def count_ones(number):
    binary_text = bin(number)
    return binary_text.count("1")


def solve(data):
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    total_cases = int(lines[0])
    answers = []

    for number_text in lines[1 : 1 + total_cases]:
        # 第一個答案：把原本的十進位數字直接轉成二進位後計算 1 的個數。
        decimal_value = int(number_text)
        first_count = count_ones(decimal_value)

        # 第二個答案：把這串數字當成十六進位數字解讀，再轉成二進位計算 1 的個數。
        hex_value = int(number_text, 16)
        second_count = count_ones(hex_value)

        answers.append(f"{first_count} {second_count}")

    return "\n".join(answers)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()), end="")