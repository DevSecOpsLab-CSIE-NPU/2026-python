import sys

ROWS = [
    "`1234567890-=",
    "qwertyuiop[]\\",
    "asdfghjkl;'",
    "zxcvbnm,./",
]

TRANSLATION = {}
for row in ROWS + [row.upper() for row in ROWS]:
    for index in range(1, len(row)):
        TRANSLATION[row[index]] = row[index - 1]


def solve(data: str) -> str:
    outputs = []
    for line in data.splitlines():
        outputs.append("".join(TRANSLATION.get(char, char) for char in line))
    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
