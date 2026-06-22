def clean_data(nums, d=2):
    seen = set()
    deduped = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            deduped.append(x)
    filtered = [x for x in deduped if x % d == 0]
    return sorted(filtered)


def solve_input(data, d=2):
    lines = data.strip().splitlines()
    results = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        n = int(line)
        if n == 0:
            break
        i += 1
        nums = list(map(int, lines[i].strip().split())) if i < len(lines) else []
        i += 1
        out = clean_data(nums, d)
        results.append(' '.join(map(str, out)) if out else 'NONE')
    return '\n'.join(results)


def main():
    import sys
    sys.stdout.write(solve_input(sys.stdin.read()))


if __name__ == '__main__':
    main()
