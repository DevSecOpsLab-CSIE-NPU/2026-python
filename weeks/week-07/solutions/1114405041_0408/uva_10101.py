import sys


def format_bangla_number(number: int) -> str:
    """
    把十進位整數轉成 Bangla Number 表示法。

    單位規則如下：
    - 1 kuti = 10,000,000
    - 1 lakh = 100,000
    - 1 hajar = 1,000
    - 1 shata = 100

    kuti 會重複出現，因此用遞迴最乾淨。
    """
    if number == 0:
        return "0"

    parts: list[str] = []

    def append_parts(value: int) -> None:
        if value >= 10_000_000:
            append_parts(value // 10_000_000)
            parts.append("kuti")
            value %= 10_000_000

        if value >= 100_000:
            parts.append(str(value // 100_000))
            parts.append("lakh")
            value %= 100_000

        if value >= 1_000:
            parts.append(str(value // 1_000))
            parts.append("hajar")
            value %= 1_000

        if value >= 100:
            parts.append(str(value // 100))
            parts.append("shata")
            value %= 100

        if value:
            parts.append(str(value))

    append_parts(number)
    return " ".join(parts)


def solve(data: str) -> str:
    outputs = []

    for case_index, line in enumerate(data.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue

        number = int(stripped)
        outputs.append(f"{case_index:>4}. {format_bangla_number(number)}")

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()