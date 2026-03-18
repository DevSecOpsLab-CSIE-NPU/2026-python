import sys


def fits(coin_id: int, is_heavy: bool, weighings):
    # 檢查某顆硬幣在「偏重/偏輕」假設下是否符合所有秤重結果
    for left, right, sign in weighings:
        on_left = coin_id in left
        on_right = coin_id in right

        if sign == "=":
            # 平衡代表假幣不在秤盤上
            if on_left or on_right:
                return False
            continue

        # 不平衡時，假幣一定要在秤盤其中一側
        if not on_left and not on_right:
            return False

        if on_left:
            expected = ">" if is_heavy else "<"
        else:
            expected = "<" if is_heavy else ">"

        if expected != sign:
            return False

    return True


def solve_case(n: int, weighings):
    candidates = []

    # 每顆硬幣都試「偏重、偏輕」兩種可能
    for coin in range(1, n + 1):
        if fits(coin, True, weighings) or fits(coin, False, weighings):
            candidates.append(coin)

    # 只有唯一候選才可確定答案
    return candidates[0] if len(candidates) == 1 else 0


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    p = 0
    t = int(data[p])
    p += 1

    outputs = []

    for _ in range(t):
        n = int(data[p])
        k = int(data[p + 1])
        p += 2

        weighings = []
        for _ in range(k):
            cnt = int(data[p])
            p += 1

            left = set(map(int, data[p:p + cnt]))
            p += cnt

            right = set(map(int, data[p:p + cnt]))
            p += cnt

            sign = data[p]
            p += 1

            weighings.append((left, right, sign))

        outputs.append(str(solve_case(n, weighings)))

    # 題目要求測資之間空一行
    print("\n\n".join(outputs))


if __name__ == "__main__":
    main()
