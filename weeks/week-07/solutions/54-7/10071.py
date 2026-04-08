import sys


def count_six_tuples(numbers: list[int]) -> int:
    pair_counts: dict[int, int] = {}
    for a in numbers:
        for b in numbers:
            pair_sum = a + b
            pair_counts[pair_sum] = pair_counts.get(pair_sum, 0) + 1

    triple_counts: dict[int, int] = {}
    for a in numbers:
        for b in numbers:
            for c in numbers:
                triple_sum = a + b + c
                triple_counts[triple_sum] = triple_counts.get(triple_sum, 0) + 1

    result = 0
    for f in numbers:
        for pair_sum, pair_count in pair_counts.items():
            result += triple_counts.get(f - pair_sum, 0) * pair_count
    return result


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    numbers = list(map(int, data[1 : 1 + n]))
    print(count_six_tuples(numbers))


if __name__ == "__main__":
    main()
