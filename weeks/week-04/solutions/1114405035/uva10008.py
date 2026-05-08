#!/usr/bin/env python3


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    results = []
    for line in lines:
        words = line.split()
        count = int(words[0])
        words_sorted = sorted(words[1:count + 1])
        for word in words_sorted:
            results.append(word)
    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
from collections import Counter
from typing import List


def process_input(input_text: str) -> str:
    lines = input_text.splitlines()
    if not lines:
        return ''

    try:
        n = int(lines[0].strip())
    except ValueError:
        return ''

    counter = Counter()
    for line in lines[1 : 1 + n]:
        for ch in line:
            if ch.isalpha():
                counter[ch.upper()] += 1

    items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    return '\n'.join(f"{letter} {count}" for letter, count in items)


def main() -> None:
    import sys
    text = sys.stdin.read()
    print(process_input(text), end='')


if __name__ == '__main__':
    main()
