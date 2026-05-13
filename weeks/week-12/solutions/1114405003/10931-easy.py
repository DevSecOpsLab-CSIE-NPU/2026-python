import sys


def solve():
    # 題目要的是二進位中有幾個 1，所以先轉成二進位字串，再數 1 的數量。
    output = []

    for token in sys.stdin.read().split():
        number = int(token)

        # 0 代表結束，不用輸出。
        if number == 0:
            break

        binary = bin(number)[2:]
        ones = binary.count("1")
        output.append(f"The parity of {binary} is {ones} (mod 2).")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()