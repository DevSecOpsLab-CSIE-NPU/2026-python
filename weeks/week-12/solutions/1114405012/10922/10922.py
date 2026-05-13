import sys


def digit_sum(value: int) -> int:
    # 把整數拆成字元後加總，每一位數都轉成 int 再相加。
    return sum(int(ch) for ch in str(value))


def nine_degree(number_text: str) -> int:
    # 先算第一次各位數字和。
    current = digit_sum(int(number_text))
    degree = 1

    # 只要還不是一位數，就繼續做數字和。
    while current > 9:
        current = digit_sum(current)
        degree += 1

    return degree


def solve() -> None:
    # 每行一個整數，遇到 0 結束。
    for line in sys.stdin:
        text = line.strip()
        if text == "0":
            break
        if not text:
            continue

        # 能否被 9 整除，只要看各位數字和是否也是 9 的倍數。
        if digit_sum(int(text)) % 9 != 0:
            print(f"{text} is not a multiple of 9.")
        else:
            print(f"9-degree of {text} is {nine_degree(text)}.")


if __name__ == "__main__":
    solve()