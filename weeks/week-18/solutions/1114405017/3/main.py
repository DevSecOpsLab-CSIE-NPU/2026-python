import sys

STUDENT_ID = "1114405017"
BASE_MAP = {0: 2, 1: 8, 2: 16, 3: 3, 4: 5, 5: 7, 6: 9, 7: 11, 8: 13, 9: 6}


def get_base(student_id: str) -> int:
    """根據學號末位選擇進位基底。"""
    u = int(student_id[-1])
    return BASE_MAP[u]


def sum_digits_in_base(number: int, base: int) -> int:
    """將數字轉成指定進位後，各位數字相加。"""
    if number == 0:
        return 0

    total = 0
    while number > 0:
        total += number % base
        number //= base
    return total


def digit_root(number: int, base: int) -> int:
    """重複求進位數字和，直到結果成為單一位數。"""
    result = sum_digits_in_base(number, base)
    while result >= base:
        result = sum_digits_in_base(result, base)
    return result


def main() -> None:
    base = get_base(STUDENT_ID)
    for line in sys.stdin:
        text = line.strip()
        if not text:
            continue
        value = int(text)
        print(digit_root(value, base))


if __name__ == "__main__":
    main()
