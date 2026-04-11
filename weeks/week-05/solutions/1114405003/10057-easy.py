import sys


def solve():
    # 這題最重要的觀念就是「中位數」。
    # 所有數字加總後，讓絕對值總和最小的位置一定在中間。
    #
    # 若資料筆數是奇數，中位數只有一個。
    # 若資料筆數是偶數，最小中位數到最大中位數之間都可以。
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    answers = []

    while index < len(data):
        n = data[index]
        index += 1

        numbers = data[index:index + n]
        index += n

        numbers.sort()

        # 左中位數與右中位數。
        left_mid = numbers[(n - 1) // 2]
        right_mid = numbers[n // 2]

        # 左中位數出現幾次。
        # 題目要的是「能產生最小值的 A 有幾個」，
        # 也就是從左中位數到右中位數之間的整數個數。
        count_left = 0
        for value in numbers:
            if value == left_mid:
                count_left += 1

        possible_count = right_mid - left_mid + 1

        answers.append(f"{left_mid} {count_left} {possible_count}")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()