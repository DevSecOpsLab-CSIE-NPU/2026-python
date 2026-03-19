def check_coin(coin: int, is_heavy: bool, weighings: list[tuple[list[int], list[int], str]]) -> bool:
    for left, right, result in weighings:
        if coin in left:
            predicted = ">" if is_heavy else "<"
        elif coin in right:
            predicted = "<" if is_heavy else ">"
        else:
            predicted = "="

        if predicted != result:
            return False

    return True


def find_fake_coin(n: int, weighings: list[tuple[list[int], list[int], str]]) -> int:
    possible_coins = []

    for coin in range(1, n + 1):
        heavy_ok = check_coin(coin, True, weighings)
        light_ok = check_coin(coin, False, weighings)

        if heavy_ok or light_ok:
            possible_coins.append(coin)

    if len(possible_coins) == 1:
        return possible_coins[0]
    return 0


def solve(data: str) -> str:
    lines = data.splitlines()
    index = 0

    while index < len(lines) and lines[index].strip() == "":
        index += 1

    m = int(lines[index].strip())
    index += 1

    answers = []

    for _ in range(m):
        while index < len(lines) and lines[index].strip() == "":
            index += 1

        n, k = map(int, lines[index].split())
        index += 1

        weighings = []

        for _ in range(k):
            parts = lines[index].split()
            index += 1

            p = int(parts[0])
            left = list(map(int, parts[1:1 + p]))
            right = list(map(int, parts[1 + p:1 + 2 * p]))

            while index < len(lines) and lines[index].strip() == "":
                index += 1

            result = lines[index].strip()
            index += 1

            weighings.append((left, right, result))

        answers.append(str(find_fake_coin(n, weighings)))

    return "\n\n".join(answers)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))