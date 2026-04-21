import sys


# 反轉數的概念：若前面的車箱編號比後面的大，就代表需要交換一次。
def count_swaps(train):
    swap_count = 0
    total = len(train)

    for left_index in range(total):
        for right_index in range(left_index + 1, total):
            if train[left_index] > train[right_index]:
                swap_count += 1

    return swap_count


def main() -> None:
    raw = list(map(int, sys.stdin.buffer.read().split()))
    if not raw:
        return

    # 第一個數字是測資數量。
    test_cases = raw[0]
    cursor = 1
    answers = []

    for _ in range(test_cases):
        # 每筆測資先讀火車長度，再讀一整列車箱編號。
        length = raw[cursor]
        cursor += 1
        train = raw[cursor:cursor + length]
        cursor += length

        answers.append(f"Optimal train swapping takes {count_swaps(train)} swaps.")

    sys.stdout.write("\n".join(answers) + ("\n" if answers else ""))


if __name__ == "__main__":
    main()