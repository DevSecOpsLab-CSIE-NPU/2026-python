#!/usr/bin/env python3
import sys

# UVA 10062 手打版程式：使用 BIT 來還原牛的排列。
# 這個版本與正式解答相同，但保留手打習慣的排版與註解。

def bit_add(bit, idx, delta):
    while idx < len(bit):
        bit[idx] += delta
        idx += idx & -idx


def bit_find(bit, k):
    idx = 0
    bit_mask = 1 << (len(bit).bit_length() - 1)
    while bit_mask:
        next_idx = idx + bit_mask
        if next_idx < len(bit) and bit[next_idx] < k:
            k -= bit[next_idx]
            idx = next_idx
        bit_mask >>= 1
    return idx + 1


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    inv = [0] * (n + 1)
    for i in range(2, n + 1):
        inv[i] = int(data[i - 1])

    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit_add(bit, i, 1)

    result = [0] * (n + 1)
    for i in range(n, 0, -1):
        order = n - i + 1 - inv[i]
        value = bit_find(bit, order)
        result[i] = value
        bit_add(bit, value, -1)

    print("\n".join(str(result[i]) for i in range(1, n + 1)))


if __name__ == '__main__':
    main()
