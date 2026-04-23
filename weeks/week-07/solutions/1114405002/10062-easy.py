#!/usr/bin/env python3
import sys

# UVA 10062：用更容易理解的寫法來還原排列。
# 我們把可用的牛編號放到 Fenwick Tree，從右往左選出對應排名的數字。

def add(bit, pos, value):
    while pos < len(bit):
        bit[pos] += value
        pos += pos & -pos


def prefix_sum(bit, pos):
    total = 0
    while pos > 0:
        total += bit[pos]
        pos -= pos & -pos
    return total


def find_kth(bit, k):
    idx = 0
    step = 1 << (len(bit).bit_length() - 1)
    while step:
        next_idx = idx + step
        if next_idx < len(bit) and bit[next_idx] < k:
            k -= bit[next_idx]
            idx = next_idx
        step >>= 1
    return idx + 1


def main():
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return

    n = int(tokens[0])
    inversions = [0] * (n + 1)
    for position in range(2, n + 1):
        inversions[position] = int(tokens[position - 1])

    tree = [0] * (n + 1)
    for number in range(1, n + 1):
        add(tree, number, 1)

    answer = [0] * (n + 1)
    for position in range(n, 0, -1):
        remaining = n - position + 1
        rank = remaining - inversions[position]
        cow_id = find_kth(tree, rank)
        answer[position] = cow_id
        add(tree, cow_id, -1)

    print("\n".join(str(answer[i]) for i in range(1, n + 1)))


if __name__ == "__main__":
    main()
