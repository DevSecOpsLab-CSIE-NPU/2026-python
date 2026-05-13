import sys


def digit_sum(text):
    # 字串中的每個字元都代表一個數字，所以把它們逐一轉成整數再相加。
    return sum(ord(ch) - 48 for ch in text)


def degree_of_nine(text):
    # 第一次先把整個數字的位數加總。
    total = digit_sum(text)
    degree = 1

    # 如果加總後還是兩位數以上，就繼續把它拆成各位數相加。
    while total >= 10:
        total = digit_sum(str(total))
        degree += 1

    return degree


def solve():
    output = []

    for line in sys.stdin:
        number = line.strip()

        # 題目用 0 當作結束標記，不需要處理。
        if number == "0":
            break

        # 先用「各位數字和」判斷是否為 9 的倍數。
        if digit_sum(number) % 9 != 0:
            output.append(f"{number} is not a multiple of 9.")
        else:
            # 若是 9 的倍數，再算出 9-degree。
            output.append(f"9-degree of {number} is {degree_of_nine(number)}.")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()