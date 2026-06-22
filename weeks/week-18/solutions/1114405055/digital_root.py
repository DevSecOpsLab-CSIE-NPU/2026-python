# 第三題：任意進位的數字根
# 學號 1114405055 末兩碼 55，個位 u=5，查表得 base=7

BASE = 7


def digit_sum_in_base(x: int, base: int) -> int:
    """把 x 換算成 base 進位，將各位數字相加，回傳十進位整數。"""
    total = 0
    while x > 0:
        total += x % base
        x //= base
    return total


def digital_root(x: int, base: int) -> int:
    """重複對 base 進位下的各位數字相加，直到結果是一位數（< base）。"""
    if x == 0:
        return 0
    while x >= base:
        x = digit_sum_in_base(x, base)
    return x


def main() -> None:
    import sys

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        print(digital_root(x, BASE))


if __name__ == "__main__":
    main()
