from collections import defaultdict


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    n = int(lines[0])
    values = [int(line) for line in lines[1 : 1 + n]]

    pair_counts = defaultdict(int)
    for a in values:
        for b in values:
            pair_counts[a + b] += 1

    triple_counts = defaultdict(int)
    for a in values:
        for b in values:
            for c in values:
                triple_counts[a + b + c] += 1

    total = 0
    for f in values:
        for triple_sum, count in triple_counts.items():
            total += count * pair_counts[f - triple_sum]

    return str(total)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
from typing import List


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    results: List[str] = []
    idx = 0
    t = int(lines[idx])
    idx += 1

    for _ in range(t):
        total_days = int(lines[idx])
        idx += 1
        party_count = int(lines[idx])
        idx += 1
        parties = [int(lines[idx + i]) for i in range(party_count)]
        idx += party_count

        strike_days = [False] * (total_days + 1)
        for h in parties:
            for day in range(h, total_days + 1, h):
                weekday = day % 7
                if weekday == 6 or weekday == 0:
                    continue
                strike_days[day] = True

        results.append(str(sum(strike_days)))

    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
