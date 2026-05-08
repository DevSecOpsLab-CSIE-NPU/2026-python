#!/usr/bin/env python3


def process_input(input_text: str) -> str:
    n = int(input_text.strip())
    if n == 0:
        return '0'
    results = []
    num_str = str(n)
    frequency = {}
    for char in num_str:
        frequency[char] = frequency.get(char, 0) + 1
    char_pair_list = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    for char, count in char_pair_list:
        results.append(f'{char} {count}')
    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
from typing import List, Tuple


def parse_test_case(lines: List[str], start: int) -> Tuple[int, int, int]:
    header = lines[start].split()
    n, k = int(header[0]), int(header[1])
    return n, k, start + 1


def update_possibilities(n: int, left: List[int], right: List[int], result: str, possible_light: List[bool], possible_heavy: List[bool]) -> None:
    left_set = set(left)
    right_set = set(right)
    all_coins = set(range(1, n + 1))

    if result == '=':
        for coin in left_set | right_set:
            possible_light[coin] = False
            possible_heavy[coin] = False
        return

    if result == '<':
        for coin in range(1, n + 1):
            if coin in left_set:
                possible_heavy[coin] = False
            elif coin in right_set:
                possible_light[coin] = False
            else:
                possible_light[coin] = False
                possible_heavy[coin] = False
    elif result == '>':
        for coin in range(1, n + 1):
            if coin in left_set:
                possible_light[coin] = False
            elif coin in right_set:
                possible_heavy[coin] = False
            else:
                possible_light[coin] = False
                possible_heavy[coin] = False


def find_fake_coin(n: int, weighings: List[Tuple[List[int], List[int], str]]) -> int:
    possible_light = [True] * (n + 1)
    possible_heavy = [True] * (n + 1)

    for left, right, result in weighings:
        update_possibilities(n, left, right, result, possible_light, possible_heavy)

    candidates = [coin for coin in range(1, n + 1) if possible_light[coin] or possible_heavy[coin]]
    if len(candidates) == 1:
        return candidates[0]
    return 0


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    m = int(lines[0])
    i = 1
    outputs = []
    for _ in range(m):
        n, k = map(int, lines[i].split())
        i += 1
        weighings = []
        for _ in range(k):
            parts = lines[i].split()
            pi = int(parts[0])
            left = [int(x) for x in parts[1 : 1 + pi]]
            right = [int(x) for x in parts[1 + pi : 1 + 2 * pi]]
            i += 1
            result = lines[i]
            i += 1
            weighings.append((left, right, result))
        outputs.append(str(find_fake_coin(n, weighings)))
    return '\n\n'.join(outputs)


def main() -> None:
    import sys
    input_text = sys.stdin.read()
    print(process_input(input_text), end='')


if __name__ == '__main__':
    main()
