"""題目 10101：移動一根數字木棒讓等式成立。

- 只允許改變數字（0~9）的七段顯示
- 運算符 + - = 不可改
- 輸入以 # 結尾，# 後面忽略
- 若存在解，輸出任一可行等式（同樣以 # 結尾）；否則輸出 No
"""

from __future__ import annotations

import sys


SEG = {
    # 七段顯示對應：每個數字對應到亮起的 segment 集合。
    "0": frozenset("abcefd"),
    "1": frozenset("bc"),
    "2": frozenset("abdeg"),
    "3": frozenset("abcdg"),
    "4": frozenset("bcfg"),
    "5": frozenset("acdfg"),
    "6": frozenset("acdefg"),
    "7": frozenset("abc"),
    "8": frozenset("abcdefg"),
    "9": frozenset("abcdfg"),
}


def build_transitions() -> tuple[dict[str, list[str]], dict[str, list[str]], dict[str, list[str]]]:
    """預先建表：每個數字在一根木棒操作下能變成哪些數字。

    回傳三張表：
    - remove_to[d]：從 d 拿掉一根後可變成的數字
    - add_to[d]：對 d 加上一根後可變成的數字
    - move_to[d]：在 d 內部搬一根（總根數不變）可變成的數字
    """
    remove_to: dict[str, list[str]] = {d: [] for d in SEG}
    add_to: dict[str, list[str]] = {d: [] for d in SEG}
    move_to: dict[str, list[str]] = {d: [] for d in SEG}

    digits = list(SEG.keys())
    for d in digits:
        sd = SEG[d]
        for e in digits:
            if d == e:
                continue
            se = SEG[e]
            if len(sd) == len(se) + 1 and se.issubset(sd):
                remove_to[d].append(e)
            if len(sd) + 1 == len(se) and sd.issubset(se):
                add_to[d].append(e)
            # 同一個數字內「搬動」：總根數不變，且只換一進一出。
            if len(sd) == len(se) and len(sd ^ se) == 2:
                move_to[d].append(e)

    return remove_to, add_to, move_to


def parse_side_total(side: str) -> int | None:
    """解析單側算式（只含 +、- 與整數），回傳數值。

    若格式不合法，回傳 None。
    """
    i = 0
    n = len(side)
    total = 0
    sign = 1

    if i < n and side[i] in "+-":
        sign = 1 if side[i] == "+" else -1
        i += 1

    while i < n:
        j = i
        while j < n and side[j].isdigit():
            j += 1
        if j == i:
            return None

        total += sign * int(side[i:j])
        if j == n:
            break

        op = side[j]
        if op not in "+-":
            return None
        sign = 1 if op == "+" else -1
        i = j + 1

    return total


def is_valid_equation(expr: str) -> bool:
    """檢查字串是否為合法且成立的等式。"""
    if expr.count("=") != 1:
        return False
    left, right = expr.split("=", 1)
    lv = parse_side_total(left)
    rv = parse_side_total(right)
    return lv is not None and rv is not None and lv == rv


def build_digit_coeffs(expr: str) -> tuple[list[int], list[int], int] | None:
    """回傳 (digit_char_indices, coeffs, base_F)。

    定義 F = 左邊值 - 右邊值。
    每個數字改變時，F 的變化量可以用線性係數快速計算。
    """
    if expr.count("=") != 1:
        return None

    eq = expr.index("=")
    sides = [(expr[:eq], 0, +1), (expr[eq + 1 :], eq + 1, -1)]

    digit_indices: list[int] = []
    coeffs: list[int] = []
    total_f = 0

    for side, offset, side_factor in sides:
        i = 0
        n = len(side)
        sign = 1
        if i < n and side[i] in "+-":
            sign = 1 if side[i] == "+" else -1
            i += 1

        while i < n:
            j = i
            while j < n and side[j].isdigit():
                j += 1
            if j == i:
                return None

            token = side[i:j]
            coeff_num = side_factor * sign
            total_f += coeff_num * int(token)

            l = len(token)
            for k, ch in enumerate(token):
                global_idx = offset + i + k
                place = l - 1 - k
                digit_indices.append(global_idx)
                coeffs.append(coeff_num * (10 ** place))

            if j == n:
                break
            op = side[j]
            if op not in "+-":
                return None
            sign = 1 if op == "+" else -1
            i = j + 1

    return digit_indices, coeffs, total_f


def solve_expression(raw: str) -> str:
    """求解主流程：嘗試所有一根木棒移動，找到任一可行解。"""
    cut = raw.find("#")
    expr = raw[:cut] if cut != -1 else raw.strip()

    base = build_digit_coeffs(expr)
    if base is None:
        return "No"

    digit_indices, coeffs, f0 = base

    remove_to, add_to, move_to = build_transitions()
    chars = list(expr)

    # 先試「同一個數字內搬動一根」的情況。
    # 這種情況改動一個位置，速度較快。
    for i, idx in enumerate(digit_indices):
        old_d = chars[idx]
        coeff = coeffs[i]
        for new_d in move_to[old_d]:
            if f0 + coeff * (int(new_d) - int(old_d)) != 0:
                continue
            candidate = chars[:]
            candidate[idx] = new_d
            cand_expr = "".join(candidate)
            if is_valid_equation(cand_expr):
                return cand_expr + "#"

    # 再試「從某數字拿一根，移到另一數字」的情況。
    # 這種情況會改動兩個位置，但仍然只移動一根棒子。
    m = len(digit_indices)
    for i in range(m):
        idx_i = digit_indices[i]
        old_i = chars[idx_i]
        coeff_i = coeffs[i]

        for new_i in remove_to[old_i]:
            delta_i = coeff_i * (int(new_i) - int(old_i))

            for j in range(m):
                if i == j:
                    continue
                idx_j = digit_indices[j]
                old_j = chars[idx_j]
                coeff_j = coeffs[j]

                for new_j in add_to[old_j]:
                    delta = delta_i + coeff_j * (int(new_j) - int(old_j))
                    if f0 + delta != 0:
                        continue

                    candidate = chars[:]
                    candidate[idx_i] = new_i
                    candidate[idx_j] = new_j
                    cand_expr = "".join(candidate)
                    if is_valid_equation(cand_expr):
                        return cand_expr + "#"

    return "No"


def main() -> None:
    # 題目只關心第一個 # 之前的式子。
    raw = sys.stdin.buffer.read().decode(errors="ignore")
    if not raw:
        return
    print(solve_expression(raw))


if __name__ == "__main__":
    main()
