from collections import Counter
import sys


def solve(data: str) -> str:
    outputs = []

    for line in data.splitlines():
        counts = Counter(line)
        pairs = sorted(counts.items(), key=lambda item: (item[1], -ord(item[0])))
        outputs.append("\n".join(f"{ord(char)} {count}" for char, count in pairs))

    return "\n\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()