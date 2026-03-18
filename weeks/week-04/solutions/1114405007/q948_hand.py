def can_be_fake(coin, is_heavy, weighings):
    for left, right, result in weighings:
        in_left = coin in left
        in_right = coin in right

        if result == "=":
            if in_left or in_right:
                return False
            continue

        if not in_left and not in_right:
            return False

        if result == "<":
            if is_heavy and not in_right:
                return False
            if not is_heavy and not in_left:
                return False
        else:
            if is_heavy and not in_left:
                return False
            if not is_heavy and not in_right:
                return False

    return True


def solve(data):
    lines = [line.strip() for line in data.splitlines()]
    index = 0

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
            numbers = list(map(int, lines[index].split()))
            index += 1
            p = numbers[0]
            left = numbers[1 : 1 + p]
            right = numbers[1 + p : 1 + 2 * p]
            result = lines[index]
            index += 1
            weighings.append((left, right, result))

        fake_coin = None
        for coin in range(1, n + 1):
            if can_be_fake(coin, True, weighings) or can_be_fake(coin, False, weighings):
                if fake_coin is not None:
                    fake_coin = None
                    break
                fake_coin = coin

        results.append(str(fake_coin) if fake_coin is not None else "0")

    return "\n\n".join(results)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()), end="")