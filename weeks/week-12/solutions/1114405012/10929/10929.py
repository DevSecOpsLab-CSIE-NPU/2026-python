import sys


def is_multiple_of_11(number_text: str) -> bool:
    # 從最右邊開始做交錯加減。
    # 11 的倍數判斷規則：奇偶位數字和的差若能被 11 整除，原數就是 11 的倍數。
    total = 0
    sign = 1
    for ch in reversed(number_text):
        total += sign * int(ch)
        sign *= -1
    return total % 11 == 0


def solve() -> None:
    for line in sys.stdin:
        text = line.strip()
        if text == "0":
            break
        if not text:
            continue

        if is_multiple_of_11(text):
            print(f"{text} is a multiple of 11.")
        else:
            print(f"{text} is not a multiple of 11.")


if __name__ == "__main__":
    solve()