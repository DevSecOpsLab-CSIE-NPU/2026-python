#!/usr/bin/env python3
import sys

# UVA 10101：移動一根木棒使等式成立。
# 只允許改變數字的七段顯示，運算符號與等號不能變。

SEGMENTS = [0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F]
SEGMENT_TO_DIGIT = {mask: digit for digit, mask in enumerate(SEGMENTS)}


def evaluate_expression(expr):
    total = 0
    sign = 1
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch == '+':
            sign = 1
            i += 1
            continue
        if ch == '-':
            sign = -1
            i += 1
            continue
        j = i
        while j < len(expr) and expr[j].isdigit():
            j += 1
        total += sign * int(expr[i:j])
        i = j
    return total


def build_result_string(base, positions, new_digits):
    chars = list(base)
    for pos, digit in zip(positions, new_digits):
        chars[pos] = str(digit)
    return ''.join(chars)


def find_solution(expr):
    digits_positions = [i for i, ch in enumerate(expr) if ch.isdigit()]
    digit_masks = [SEGMENTS[int(expr[pos])] for pos in digits_positions]

    lit_segments = [
        [bit for bit in range(7) if mask >> bit & 1]
        for mask in digit_masks
    ]
    unlit_segments = [
        [bit for bit in range(7) if not (mask >> bit & 1)]
        for mask in digit_masks
    ]

    for src_idx, src_mask in enumerate(digit_masks):
        for removed in lit_segments[src_idx]:
            new_src_mask = src_mask & ~(1 << removed)
            if new_src_mask not in SEGMENT_TO_DIGIT:
                continue
            for tgt_idx, tgt_mask in enumerate(digit_masks):
                for added in unlit_segments[tgt_idx]:
                    if src_idx == tgt_idx and added == removed:
                        continue
                    new_tgt_mask = tgt_mask | (1 << added)
                    if new_tgt_mask not in SEGMENT_TO_DIGIT:
                        continue
                    new_masks = list(digit_masks)
                    new_masks[src_idx] = new_src_mask
                    new_masks[tgt_idx] = new_tgt_mask
                    if new_masks[src_idx] == src_mask and new_masks[tgt_idx] == tgt_mask:
                        continue
                    new_digits = [SEGMENT_TO_DIGIT[mask] for mask in new_masks]
                    candidate = build_result_string(expr, digits_positions, new_digits)
                    if '=' not in candidate:
                        continue
                    lhs, rhs = candidate.split('=', 1)
                    try:
                        if evaluate_expression(lhs) == evaluate_expression(rhs):
                            return candidate
                    except ValueError:
                        continue
    return None


def main():
    raw = sys.stdin.readline()
    if not raw:
        return
    expr = raw.strip()
    if '#' in expr:
        expr = expr[:expr.index('#')]

    solution = find_solution(expr)
    if solution is None:
        print('No')
    else:
        print(solution + '#')


if __name__ == '__main__':
    main()
