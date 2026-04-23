#!/usr/bin/env python3
import sys

# UVA 10062 題目：根據每個位置前面較小數量還原排列
# 這個版本使用 Fenwick Tree (Binary Indexed Tree) 來快速取得第 k 個可用的數字。

def bit_add(bit, i, val):
    while i < len(bit):
        bit[i] += val
        i += i & -i


def bit_sum(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & -i
    return s


def bit_find_kth(bit, k):
    idx = 0
    mask = 1 << (len(bit).bit_length() - 1)
    while mask:
        nxt = idx + mask
        if nxt < len(bit) and bit[nxt] < k:
            k -= bit[nxt]
            idx = nxt
        mask >>= 1
    return idx + 1


def main():
    data = sys.stdin.read().strip().split()
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
        remaining = n - i + 1
        rank = remaining - inv[i]
        value = bit_find_kth(bit, rank)
        result[i] = value
        bit_add(bit, value, -1)

    sys.stdout.write("\n".join(str(result[i]) for i in range(1, n + 1)))


if __name__ == "__main__":
    main()
