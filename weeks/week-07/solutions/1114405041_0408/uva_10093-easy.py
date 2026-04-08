import sys


def value_of(char: str) -> int:
    if char.isdigit():
        return ord(char) - ord("0")
    if "A" <= char <= "Z":
        return ord(char) - ord("A") + 10
    return ord(char) - ord("a") + 36


def solve(data: str) -> str:
    """
    簡單版記法：
    1. 先找出每個字元代表的數值。
    2. 最小進位制一定要比最大數位值大 1，而且至少是 2。
    3. 只要檢查「數位總和」能不能被 (base - 1) 整除。
    """
    results = []

    for line in data.splitlines():
        token = line.strip()
        if not token:
            continue

        digits = [value_of(char) for char in token]
        start_base = max(2, max(digits) + 1)
        digit_sum = sum(digits)
        answer = "such number is impossible!"

        for base in range(start_base, 63):
            if digit_sum % (base - 1) == 0:
                answer = str(base)
                break

        results.append(answer)

    return "\n".join(results)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()