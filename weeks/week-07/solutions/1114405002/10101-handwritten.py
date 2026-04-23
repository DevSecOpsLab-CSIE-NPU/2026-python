#!/usr/bin/env python3
import sys

# UVA 10101 手打版：遍歷所有可行的木棒移動位置，檢查是否能讓等式成立。
# 由於只能移動一根木棒，因此來源與目標位置要嚴格符合七段顯示器的數字。

SEGMENTS = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]
MASK_TO_DIGIT = {mask: d for d, mask in enumerate(SEGMENTS)}


def eval_expr(s):
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
    expr = line.strip()
    if '#' in expr:
        expr = expr[:expr.index('#')]

    digit_positions = [idx for idx, ch in enumerate(expr) if ch.isdigit()]
    digit_masks = [SEGMENTS[int(expr[pos])] for pos in digit_positions]

    lit_list = []
    dark_list = []
    for mask in digit_masks:
        lit_list.append([b for b in range(7) if mask >> b & 1])
        dark_list.append([b for b in range(7) if not mask >> b & 1])

    for src_idx, src_mask in enumerate(digit_masks):
        for remove_bit in lit_list[src_idx]:
            new_src_mask = src_mask & ~(1 << remove_bit)
            if new_src_mask not in MASK_TO_DIGIT:
                continue
            for tgt_idx, tgt_mask in enumerate(digit_masks):
                for add_bit in dark_list[tgt_idx]:
                    if src_idx == tgt_idx and add_bit == remove_bit:
                        continue
                    new_tgt_mask = tgt_mask | (1 << add_bit)
                    if new_tgt_mask not in MASK_TO_DIGIT:
                        continue

                    candidate_masks = digit_masks.copy()
                    candidate_masks[src_idx] = new_src_mask
                    candidate_masks[tgt_idx] = new_tgt_mask

                    new_digits = [str(MASK_TO_DIGIT[mask]) for mask in candidate_masks]
                    chars = list(expr)
                    for pos, d in zip(digit_positions, new_digits):
                        chars[pos] = d
                    candidate = ''.join(chars)
                    if '=' not in candidate:
                        continue
                    left, right = candidate.split('=', 1)
                    if eval_expr(left) == eval_expr(right):
                        print(candidate + '#')
                        return
    print('No')


if __name__ == '__main__':
    main()
