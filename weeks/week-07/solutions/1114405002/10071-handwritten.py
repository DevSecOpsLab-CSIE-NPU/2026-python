#!/usr/bin/env python3
import sys
from collections import Counter

# UVA 10071 手打版：顯式建立二元與三元和的次數分布，然後累加符合條件的解。

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    S = [int(x) for x in tokens[1:1 + n]]

    pairs = Counter()
    for a in S:
        for b in S:
            pairs[a + b] += 1

    triples = Counter()
    for a in S:
        for b in S:
            for c in S:
                triples[a + b + c] += 1

    answer = 0
    for f in S:
        for triple_sum, triple_count in triples.items():
            answer += triple_count * pairs.get(f - triple_sum, 0)

    print(answer)


if __name__ == '__main__':
    main()
