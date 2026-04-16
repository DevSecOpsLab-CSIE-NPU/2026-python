"""
UVA 10101（依題目描述版本）
給定錯誤等式（以 # 結尾），只能在「數字的七段顯示」中移動一根木棒。
若可使等式成立，輸出其中一個成立等式（同樣以 # 結尾）；否則輸出 No。
"""

from __future__ import annotations

import sys
from collections import defaultdict


# 七段顯示 bit 定義：a,b,c,d,e,f,g -> bit 0..6
SEG = {
    0: 0b1111110,
    1: 0b0110000,
    2: 0b1101101,
    3: 0b1111001,
    4: 0b0110011,
    5: 0b1011011,
    6: 0b1011111,
    7: 0b1110000,
    8: 0b1111111,
    9: 0b1111011,
}


def build_transitions() -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
    """建立三類轉換：
    - out[d]: 從 d 移走 1 根後可變成哪些數字
    - inn[d]: 往 d 加入 1 根後可變成哪些數字
    - same[d]: 在 d 內部搬動 1 根（移走 1 根再加到別處）可變成哪些數字
    """
    out = [[] for _ in range(10)]
    inn = [[] for _ in range(10)]
    same = [[] for _ in range(10)]

    for d in range(10):
        s1 = SEG[d]
        for nd in range(10):
            if d == nd:
                continue
            s2 = SEG[nd]
            removed = (s1 & ~s2).bit_count()
            added = (s2 & ~s1).bit_count()
            if removed == 1 and added == 0:
                out[d].append(nd)
            elif removed == 0 and added == 1:
                inn[d].append(nd)
            elif removed == 1 and added == 1:
                same[d].append(nd)
    return out, inn, same


OUT_TRANS, IN_TRANS, SAME_TRANS = build_transitions()


def evaluate_side(side: str) -> int:
    """計算只有 + 與 - 的整數表達式值（支援開頭負號）。"""
    i = 0
    n = len(side)
    total = 0
    sign = 1

    while i < n:
        if side[i] == "+":
            sign = 1
            i += 1
            continue
        if side[i] == "-":
            sign = -1
            i += 1
            continue

        j = i
        while j < n and side[j].isdigit():
            j += 1
        num = int(side[i:j])
        total += sign * num
        sign = 1
        i = j

    return total


def extract_digit_coeffs(expr: str) -> tuple[list[int], list[int], int]:
    """回傳：
    - digit_pos: 每個數字字元在 expr 的索引
    - coeff: 該位置數字改變 1 對 F=(left-right) 的影響係數
    - f0: 原始 F 值
    """
    eq = expr.index("=")
    left = expr[:eq]
    right = expr[eq + 1 :]

    f0 = evaluate_side(left) - evaluate_side(right)

    digit_pos: list[int] = []
    coeff: list[int] = []

    def parse_side(side: str, offset: int, side_sign: int) -> None:
        i = 0
        n = len(side)
        term_sign = 1

        while i < n:
            if side[i] == "+":
                term_sign = 1
                i += 1
                continue
            if side[i] == "-":
                term_sign = -1
                i += 1
                continue

            j = i
            while j < n and side[j].isdigit():
                j += 1

            length = j - i
            for k in range(length):
                idx = offset + i + k
                place = 10 ** (length - 1 - k)
                digit_pos.append(idx)
                coeff.append(side_sign * term_sign * place)

            term_sign = 1
            i = j

    parse_side(left, 0, +1)
    parse_side(right, eq + 1, -1)

    return digit_pos, coeff, f0


def solve(text: str) -> str:
    idx = text.find("#")
    if idx == -1:
        return "No"

    expr = "".join(text[:idx].split())
    if not expr or expr.count("=") != 1:
        return "No"

    digit_pos, coeff, f0 = extract_digit_coeffs(expr)
    chars = list(expr)
    digits = [int(chars[p]) for p in digit_pos]

    # 情況 A：同一個數字內部搬動一根（段數不變）
    for i, p in enumerate(digit_pos):
        d = digits[i]
        for nd in SAME_TRANS[d]:
            delta = coeff[i] * (nd - d)
            if f0 + delta == 0:
                chars[p] = str(nd)
                return "".join(chars) + "#"

    # 情況 B：從某位移出 1 根，到另一位移入 1 根
    # 先把所有「可移入」候選整理成 delta -> [(index, new_digit), ...]
    in_map: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for j, _p in enumerate(digit_pos):
        dj = digits[j]
        for ndj in IN_TRANS[dj]:
            delta_j = coeff[j] * (ndj - dj)
            in_map[delta_j].append((j, ndj))

    for i, pi in enumerate(digit_pos):
        di = digits[i]
        for ndi in OUT_TRANS[di]:
            delta_i = coeff[i] * (ndi - di)
            need = -f0 - delta_i
            cands = in_map.get(need, [])
            for j, ndj in cands:
                if j == i:
                    continue
                new_chars = chars[:]
                new_chars[pi] = str(ndi)
                new_chars[digit_pos[j]] = str(ndj)
                return "".join(new_chars) + "#"

    return "No"


def main() -> None:
    text = sys.stdin.read()
    out = solve(text)
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
