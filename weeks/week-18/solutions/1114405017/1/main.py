import sys

STUDENT_ID = "1114405017"


def get_divisor(student_id: str) -> int:
    """根據學號末位計算整除數 D。"""
    u = int(student_id[-1])
    return u % 4 + 2


def process_numbers(numbers: list[int], divisor: int) -> list[int]:
    """依序去重、保留可整除的數，再由小到大排序。"""
    seen = set()
    filtered = []

    for value in numbers:
        if value in seen:
            continue
        seen.add(value)
        if divisor != 0 and value % divisor == 0:
            filtered.append(value)

    return sorted(filtered)


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    values = [int(token) for token in data]
    divisor = get_divisor(STUDENT_ID)
    index = 0

    while index < len(values):
        n = values[index]
        index += 1
        if n == 0:
            break

        group = values[index : index + n]
        index += n
        result = process_numbers(group, divisor)

        if result:
            print(" ".join(str(x) for x in result))
        else:
            print("NONE")


if __name__ == "__main__":
    main()
