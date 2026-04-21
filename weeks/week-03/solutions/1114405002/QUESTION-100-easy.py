import sys


# 快取每個數字的 cycle length，1 的長度一定是 1。
cycle_cache = {1: 1}


def get_cycle_length(start_number: int) -> int:
    # 先把走過的路徑記下來，等找到已知答案後，再倒回去補快取。
    path = []
    current_number = start_number

    while current_number not in cycle_cache:
        path.append(current_number)
        if current_number % 2 == 1:
            current_number = current_number * 3 + 1
        else:
            current_number //= 2

    # current_number 已經在快取中，所以可以直接拿到目前長度。
    current_length = cycle_cache[current_number]

    # 依照走過的順序反向補回每一個數字的 cycle length。
    for number in reversed(path):
        current_length += 1
        cycle_cache[number] = current_length

    return cycle_cache[start_number]


def main() -> None:
    # 題目可能有多組 i, j，全部一次讀進來處理最方便。
    raw_data = sys.stdin.buffer.read().split()
    answers = []

    # 每兩個數字是一組測資。
    for index in range(0, len(raw_data), 2):
        first_value = int(raw_data[index])
        second_value = int(raw_data[index + 1])

        # 題目要看區間內最大值，所以先把左右界整理好。
        left_bound = min(first_value, second_value)
        right_bound = max(first_value, second_value)

        maximum_cycle = 0

        # 逐一計算區間內每個數字的 cycle length。
        for number in range(left_bound, right_bound + 1):
            length = get_cycle_length(number)
            if length > maximum_cycle:
                maximum_cycle = length

        answers.append(f"{first_value} {second_value} {maximum_cycle}")

    sys.stdout.write("\n".join(answers) + ("\n" if answers else ""))


if __name__ == "__main__":
    main()