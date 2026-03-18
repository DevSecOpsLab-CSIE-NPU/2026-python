def can_be_fake(coin, is_heavy, weighings):
    for left, right, result in weighings:
        in_left = coin in left
        in_right = coin in right

        # 如果這次秤重平衡，表示左右兩邊的硬幣都是真的。
        # 所以只要候選硬幣有出現在這次秤重中，這個假設就一定錯。
        if result == "=":
            if in_left or in_right:
                return False
            continue

        # 如果天平不平衡，假幣一定有被放上天平。
        # 若這顆候選硬幣沒有出現在左右任何一邊，就不可能造成這次結果。
        if not in_left and not in_right:
            return False

        # result == "<" 代表左邊比較輕。
        # 若假幣比較重，它必須在右邊；若假幣比較輕，它必須在左邊。
        if result == "<":
            if is_heavy and not in_right:
                return False
            if not is_heavy and not in_left:
                return False
        else:
            # result == ">" 代表左邊比較重。
            # 若假幣比較重，它必須在左邊；若假幣比較輕，它必須在右邊。
            if is_heavy and not in_left:
                return False
            if not is_heavy and not in_right:
                return False

    return True


def solve(data):
    lines = [line.strip() for line in data.splitlines()]
    index = 0

    # 題目範例中測資之間可能夾空白行，所以先跳過開頭空白。
    while index < len(lines) and lines[index] == "":
        index += 1

    total_cases = int(lines[index])
    index += 1
    results = []

    for _ in range(total_cases):
        while index < len(lines) and lines[index] == "":
            index += 1

        n, k = map(int, lines[index].split())
        index += 1
        weighings = []

        for _ in range(k):
            # 一列數字描述左右兩邊各有哪些硬幣，下一列是秤重結果。
            numbers = list(map(int, lines[index].split()))
            index += 1
            p = numbers[0]
            left = numbers[1 : 1 + p]
            right = numbers[1 + p : 1 + 2 * p]
            result = lines[index]
            index += 1
            weighings.append((left, right, result))

        candidates = []

        # 直接枚舉每顆硬幣，分別假設它比較重或比較輕。
        # 只要其中一種假設能通過所有秤重檢查，就先列入候選。
        for coin in range(1, n + 1):
            if can_be_fake(coin, True, weighings) or can_be_fake(coin, False, weighings):
                candidates.append(coin)

        # 題目要求只有在唯一可判定時輸出編號，否則輸出 0。
        if len(candidates) == 1:
            results.append(str(candidates[0]))
        else:
            results.append("0")

    return "\n\n".join(results)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()), end="")