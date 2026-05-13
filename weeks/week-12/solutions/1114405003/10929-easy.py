import sys


def solve():
    # 11 的倍數判斷：從最右邊開始，奇數位加總與偶數位加總相減。
    # 如果差值是 11 的倍數，原數就是 11 的倍數。
    output = []

    for line in sys.stdin:
        number = line.strip()

        # 0 是結束訊號，不需要列入輸出。
        if number == "0":
            break

        difference = 0
        add_next = True

        # 反向掃描字串，等於從最右邊那一位開始處理。
        for ch in reversed(number):
            digit = ord(ch) - 48
            if add_next:
                difference += digit
            else:
                difference -= digit
            add_next = not add_next

        if difference % 11 == 0:
            output.append(f"{number} is a multiple of 11.")
        else:
            output.append(f"{number} is not a multiple of 11.")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()