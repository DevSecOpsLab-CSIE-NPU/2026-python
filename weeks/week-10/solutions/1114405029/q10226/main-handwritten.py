import sys


def parse_cases(lines):
    t = int(lines[0].strip())
    index = 1

    if index < len(lines) and lines[index] == "":
        index += 1

    cases = []

    for _ in range(t):
        trees = []

        while index < len(lines) and lines[index] != "":
            trees.append(lines[index])
            index += 1

        cases.append(trees)

        if index < len(lines) and lines[index] == "":
            index += 1

    return cases


def solve_case(trees):
    counter = {}
    total = 0

    for name in trees:
        counter[name] = counter.get(name, 0) + 1
        total += 1

    result = []

    for name in sorted(counter):
        percentage = counter[name] * 100.0 / total
        result.append(f"{name} {percentage:.4f}")

    return result


def main():
    lines = sys.stdin.read().splitlines()

    if not lines:
        return

    cases = parse_cases(lines)
    outputs = []

    for i, trees in enumerate(cases):
        if i > 0:
            outputs.append("")

        outputs.extend(solve_case(trees))

    print("\n".join(outputs))


if __name__ == "__main__":
    main()