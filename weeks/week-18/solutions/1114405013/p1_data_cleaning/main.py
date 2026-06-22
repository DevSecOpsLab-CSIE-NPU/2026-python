import sys


D = 5


def main():
    lines = sys.stdin.read().splitlines()
    outputs = []
    index = 0

    while index < len(lines):
        n = int(lines[index])
        index += 1

        if n == 0:
            break

        numbers = list(map(int, lines[index].split()))
        index += 1

        seen = set()
        cleaned = []
        for number in numbers:
            if number not in seen:
                seen.add(number)
                if number % D == 0:
                    cleaned.append(number)

        if cleaned:
            outputs.append(" ".join(map(str, sorted(cleaned))))
        else:
            outputs.append("NONE")

    sys.stdout.write("\n".join(outputs))
    if outputs:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
