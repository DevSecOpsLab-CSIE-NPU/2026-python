#!/usr/bin/env python3
import sys

# UVA 10101：更簡單的版本，用更直觀的流程去嘗試移動一根木棒。
# 如果找到能讓左右兩邊相等的結果，就直接輸出。

SEGMENTS = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]
MASK_TO_DIGIT = {mask: digit for digit, mask in enumerate(SEGMENTS)}


def eval_line(s):
    total = 0
    sign = 1
    i = 0
    while i < len(s):
        if s[i] == '+':
            sign = 1
            i += 1
            continue
        if s[i] == '-':
            sign = -1
            i += 1
            continue
        j = i
        while j < len(s) and s[j].isdigit():
            j += 1
        total += sign * int(s[i:j])
        i = j
    return total


def main():
    line = sys.stdin.readline()
    if not line:
        return
    expression = line.strip()
    if '#' in expression:
        expression = expression[:expression.index('#')]

    digits_positions = [i for i, ch in enumerate(expression) if ch.isdigit()]
    masks = [SEGMENTS[int(expression[pos])] for pos in digits_positions]

    lit = [[bit for bit in range(7) if masks[i] >> bit & 1] for i in range(len(masks))]
    dark = [[bit for bit in range(7) if not (masks[i] >> bit & 1)] for i in range(len(masks))]

    for i, src_mask in enumerate(masks):
        for remove_bit in lit[i]:
            after_src = src_mask & ~(1 << remove_bit)
            if after_src not in MASK_TO_DIGIT:
                continue
            for j, tgt_mask in enumerate(masks):
                for add_bit in dark[j]:
                    if i == j and add_bit == remove_bit:
                        continue
                    after_tgt = tgt_mask | (1 << add_bit)
                    if after_tgt not in MASK_TO_DIGIT:
                        continue
                    new_masks = masks.copy()
                    new_masks[i] = after_src
                    new_masks[j] = after_tgt
                    new_digits = [str(MASK_TO_DIGIT[mask]) for mask in new_masks]
                    chars = list(expression)
                    for pos, d in zip(digits_positions, new_digits):
                        chars[pos] = d
                    candidate = ''.join(chars)
                    if '=' not in candidate:
                        continue
                    left, right = candidate.split('=', 1)
                    if eval_line(left) == eval_line(right):
                        print(candidate + '#')
                        return
    print('No')


if __name__ == '__main__':
    main()
