import sys


ROWS = [
    "`1234567890-=",
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./",
]


def build_mapping() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for row in ROWS:
        for i in range(1, len(row)):
            key = row[i]
            prev = row[i - 1]
            mapping[key] = prev
            if key.isalpha():
                mapping[key.upper()] = prev.upper()
    return mapping


MAP = build_mapping()


def decode_line(line: str) -> str:
    return "".join(MAP.get(ch, ch) for ch in line)


def solve(data: str) -> str:
    return "\n".join(decode_line(line) for line in data.splitlines())


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
