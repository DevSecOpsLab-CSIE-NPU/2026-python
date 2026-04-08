from __future__ import annotations

import sys
from typing import Dict, List, Tuple


# 七段顯示器 bit 定義：a,b,c,d,e,f,g 對應 bit 0..6
SEG_MASK: Dict[str, int] = {
    "0": 0b0111111,  # a b c d e f
    "1": 0b0000110,  # b c
    "2": 0b1011011,  # a b d e g
    "3": 0b1001111,  # a b c d g
    "4": 0b1100110,  # b c f g
    "5": 0b1101101,  # a c d f g
    "6": 0b1111101,  # a c d e f g
    "7": 0b0000111,  # a b c
    "8": 0b1111111,  # a b c d e f g
    "9": 0b1101111,  # a b c d f g
}

DIGITS = "0123456789"


def build_transitions() -> Tuple[Dict[str, List[str]], Dict[str, List[str]], Dict[str, List[str]]]:
    """建立三種可行轉換：移出一根、移入一根、同位數內挪動一根。"""
    remove_map: Dict[str, List[str]] = {d: [] for d in DIGITS}
    add_map: Dict[str, List[str]] = {d: [] for d in DIGITS}
    move_within_map: Dict[str, List[str]] = {d: [] for d in DIGITS}

    for a in DIGITS:
        ma = SEG_MASK[a]
        ca = ma.bit_count()
        for b in DIGITS:
            if a == b:
                continue
            mb = SEG_MASK[b]
            cb = mb.bit_count()
            diff = (ma ^ mb).bit_count()

            # 只差 1 段：可能是移出或移入
            if diff == 1:
                # a 比 b 多 1 段：可視為從 a 拿掉一根變成 b
                if ca == cb + 1:
                    remove_map[a].append(b)
                # b 比 a 多 1 段：可視為在 a 加上一根變成 b
                elif cb == ca + 1:
                    add_map[a].append(b)

            # 差 2 段且段數相同：代表同一數字內「搬一根」
            elif diff == 2 and ca == cb:
                move_within_map[a].append(b)

    # 固定排序，讓輸出穩定可預期
    for d in DIGITS:
        remove_map[d].sort()
        add_map[d].sort()
        move_within_map[d].sort()

    return remove_map, add_map, move_within_map


REMOVE_MAP, ADD_MAP, MOVE_WITHIN_MAP = build_transitions()


def parse_coefficients(expr: str) -> Tuple[int, Dict[int, int], List[int]]:
    """計算等式差值與每個數字位置的係數。

    定義 total = LHS - RHS。
    若 total == 0，等式成立。

    回傳：
    - total: 目前等式差值
    - coef[pos]: 位置 pos 的數字若增加 1，total 會增加多少
    - digit_positions: expr 中所有數字位置（由左到右）
    """
    eq_idx = expr.find("=")
    if eq_idx == -1:
        return 0, {}, []

    coef: Dict[int, int] = {}
    digit_positions: List[int] = []

    def parse_side(side: str, offset: int, side_sign: int) -> None:
        """解析單邊算式，建立每個數字字元在 total 中的權重係數。"""

        i = 0
        n = len(side)
        current_sign = 1

        while i < n:
            ch = side[i]
            if ch == "+":
                current_sign = 1
                i += 1
                continue
            if ch == "-":
                current_sign = -1
                i += 1
                continue

            # 讀取一段連續數字
            j = i
            while j < n and side[j].isdigit():
                j += 1

            # 若遇到非數字且非 +,-，直接跳過（題目正常情況不會發生）
            if j == i:
                i += 1
                continue

            # 對該數字中的每一位建立係數
            for p in range(i, j):
                global_pos = offset + p
                place = j - 1 - p
                # 例如數字 345 的 '4' 在十位，係數要乘上 10^1
                coef[global_pos] = side_sign * current_sign * (10 ** place)
                digit_positions.append(global_pos)

            i = j

    # 左式係數為 +1，右式係數為 -1（因為 total = LHS - RHS）
    parse_side(expr[:eq_idx], 0, +1)
    parse_side(expr[eq_idx + 1 :], eq_idx + 1, -1)

    total = 0
    for pos in digit_positions:
        total += coef[pos] * int(expr[pos])

    return total, coef, digit_positions


def solve(text: str) -> str:
    """主求解函式。

    規則重點：
    1. 只能移動「一根」且僅能動數字部分。
    2. 可以是同一數字內搬移（段數總量不變）。
    3. 或從某個數字移出一根，再加到另一個數字。
    """

    # 只取第一個 # 之前的內容，後面字元忽略
    sharp = text.find("#")
    if sharp == -1:
        expr = text.strip()
    else:
        expr = text[:sharp]

    if not expr:
        return "No"

    total, coef, digit_positions = parse_coefficients(expr)
    if not digit_positions:
        return "No"

    # 轉成可修改字元陣列，找到解後直接替換並回傳
    chars = list(expr)

    # 情況 A：同一個數字內挪動一根木棒
    for i in digit_positions:
        old_di = chars[i]
        for new_di in MOVE_WITHIN_MAP[old_di]:
            # 只需用係數快速更新差值，不必整條式子重算
            delta = coef[i] * (int(new_di) - int(old_di))
            if total + delta == 0:
                chars[i] = new_di
                return "".join(chars) + "#"

    # 情況 B：從某位數字拿一根，放到另一位數字
    for i in digit_positions:
        old_di = chars[i]
        for di2 in REMOVE_MAP[old_di]:
            delta_i = coef[i] * (int(di2) - int(old_di))

            for j in digit_positions:
                if j == i:
                    continue
                old_dj = chars[j]

                for dj2 in ADD_MAP[old_dj]:
                    delta_j = coef[j] * (int(dj2) - int(old_dj))
                    # 兩個改動造成的總差值若剛好抵消 total，即得到合法解
                    if total + delta_i + delta_j == 0:
                        chars[i] = di2
                        chars[j] = dj2
                        return "".join(chars) + "#"

    return "No"


def main() -> None:
    # 題目為單筆輸入，讀完整 stdin 後直接求解輸出。
    data = sys.stdin.read()
    sys.stdout.write(solve(data))


if __name__ == "__main__":
    main()
