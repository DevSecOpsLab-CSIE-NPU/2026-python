import sys


def to_bangla(number: int) -> str:
    """
    簡單版雖然也是遞迴，但記法很固定：
    先切 kuti，剩下再依序切 lakh、hajar、shata、個位。
    """
    if number == 0:
        return "0"

    words = []

    def build(value: int) -> None:
        if value >= 10_000_000:
            build(value // 10_000_000)
            words.append("kuti")
            value %= 10_000_000

        for unit_value, unit_name in ((100_000, "lakh"), (1_000, "hajar"), (100, "shata")):
            if value >= unit_value:
                words.append(str(value // unit_value))
                words.append(unit_name)
                value %= unit_value

        if value:
            words.append(str(value))

    build(number)
    return " ".join(words)


def solve(data: str) -> str:
    answers = []

    for index, line in enumerate(data.splitlines(), start=1):
        text = line.strip()
        if not text:
            continue
        answers.append(f"{index:>4}. {to_bangla(int(text))}")

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()