import sys


def solve(data: bytes) -> str:
    # 一次讀完輸入，轉成整數陣列。
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    t = nums[0]
    idx = 1
    answers = []

    for _ in range(t):
        n = nums[idx]
        idx += 1
        p = nums[idx]
        idx += 1

        # 用集合記錄「有罷工的工作日」，可自動去除重複日期。
        strike_days = set()

        for _ in range(p):
            h = nums[idx]
            idx += 1

            # 每個政黨會在 h, 2h, 3h... 罷工。
            for day in range(h, n + 1, h):
                # day%7 == 6 代表星期五，day%7 == 0 代表星期六。
                # 題目說週五、週六是假日，不算工作日損失。
                if day % 7 in (6, 0):
                    continue
                strike_days.add(day)

        answers.append(str(len(strike_days)))

    return "\n".join(answers)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
