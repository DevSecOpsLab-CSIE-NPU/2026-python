def get_D(student_id):
    u = student_id % 10
    return (u % 4) + 2


def process_sequence(numbers, D=5):
    seen = set()
    deduped = []
    for x in numbers:
        if x not in seen:
            deduped.append(x)
            seen.add(x)
    filtered = [x for x in deduped if x % D == 0]
    filtered.sort()
    return filtered


def solve(input_text, D=5):
    lines = input_text.strip().splitlines()
    i = 0
    output_parts = []
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        n = int(line)
        if n == 0:
            break
        i += 1
        if i >= len(lines):
            break
        nums = list(map(int, lines[i].split()))
        i += 1
        result = process_sequence(nums, D)
        if result:
            output_parts.append(" ".join(map(str, result)))
        else:
            output_parts.append("NONE")
    return "\n".join(output_parts) + ("\n" if output_parts else "")


def main():
    import sys
    STUDENT_ID = 1114405007
    D = get_D(STUDENT_ID)
    input_text = sys.stdin.read()
    output = solve(input_text, D)
    sys.stdout.write(output)


if __name__ == "__main__":
    main()
