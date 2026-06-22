import sys

D = 3


def dedupe_preserve_order(nums):
    seen = set()
    result = []
    for x in nums:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result


def process_sequence(nums):
    unique = dedupe_preserve_order(nums)
    filtered = [x for x in unique if x % D == 0]
    filtered.sort()
    return filtered


def main():
    lines = sys.stdin.read().splitlines()
    output = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        if line == "":
            i += 1
            continue
        n = int(line)
        i += 1
        if n == 0:
            break
        if i >= len(lines):
            break

        nums = list(map(int, lines[i].strip().split()))
        i += 1

        result = process_sequence(nums)
        if result:
            output.append(" ".join(map(str, result)))
        else:
            output.append("NONE")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
