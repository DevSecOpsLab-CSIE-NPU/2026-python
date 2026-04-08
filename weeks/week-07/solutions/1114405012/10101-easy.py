"""題目 10101（easy 版，詳細註解）。

給一個以 # 結尾的等式字串，要求「只移動一根數字木棒」讓等式成立。

此版流程：
1. 先把 # 前面的式子取出。
2. 建立 0~9 的七段顯示集合。
3. 枚舉所有合法的一根木棒移動：
   - 同一數字內搬動（移掉一段、加到另一段）
   - 從數字 A 拿一段，補到數字 B
4. 產生候選式子後檢查算式是否成立。
5. 找到第一個可行解就輸出，否則輸出 No。
"""

from __future__ import annotations

import sys


SEG = {
    # 每個數字在七段顯示器上會亮起的 segment 集合。
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


def parse_side(side: str) -> int | None:
    """解析只有 + / - 的整數運算字串，回傳數值。

    若字串格式不合法（例如運算子位置錯誤），回傳 None。
    """
    i = 0
    n = len(side)
    sign = 1
    total = 0

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
            return total

        op = side[j]
        if op not in "+-":
            return None
        sign = 1 if op == "+" else -1
        i = j + 1

    return total


def ok_equation(expr: str) -> bool:
    """檢查是否為合法且成立的等式。"""
    if expr.count("=") != 1:
        return False
    left, right = expr.split("=", 1)
    lv = parse_side(left)
    rv = parse_side(right)
    return lv is not None and rv is not None and lv == rv


def transitions(d: str) -> tuple[list[str], list[str], list[str]]:
    """回傳 (remove_to, add_to, move_to)。

    - remove_to：拿掉一根木棒可轉成的數字
    - add_to：新增一根木棒可轉成的數字
    - move_to：在同一數字內部搬一根可轉成的數字
    """
    s = SEG[d]
    rem, add, mov = [], [], []
    for e, t in SEG.items():
        if e == d:
            continue
        if len(s) == len(t) + 1 and t.issubset(s):
            rem.append(e)
        if len(s) + 1 == len(t) and s.issubset(t):
            add.append(e)
        if len(s) == len(t) and len(s ^ t) == 2:
            mov.append(e)
    return rem, add, mov


def solve(raw: str) -> str:
    """嘗試所有合法的一根木棒移動，找到任一可行解。"""
    # 只看第一個 # 之前的內容。
    p = raw.find("#")
    expr = raw[:p] if p != -1 else raw.strip()
    chars = list(expr)

    digit_pos = [i for i, ch in enumerate(chars) if ch.isdigit()]
    trans = {d: transitions(d) for d in SEG}

    # 情況 A：在同一個數字內搬動一根。
    # 只改一個字元，先嘗試這類情況。
    for i in digit_pos:
        d = chars[i]
        _rem, _add, mov = trans[d]
        for nd in mov:
            cand = chars[:]
            cand[i] = nd
            cexpr = "".join(cand)
            if ok_equation(cexpr):
                return cexpr + "#"

    # 情況 B：從一個數字拿一根，補到另一個數字。
    # 會改兩個字元，但仍符合「只移動一根」規則。
    for i in digit_pos:
        d1 = chars[i]
        rem1, _add1, _mov1 = trans[d1]
        for nd1 in rem1:
            for j in digit_pos:
                if i == j:
                    continue
                d2 = chars[j]
                _rem2, add2, _mov2 = trans[d2]
                for nd2 in add2:
                    cand = chars[:]
                    cand[i] = nd1
                    cand[j] = nd2
                    cexpr = "".join(cand)
                    if ok_equation(cexpr):
                        return cexpr + "#"

    return "No"


def main() -> None:
    raw = sys.stdin.buffer.read().decode(errors="ignore")
    if not raw:
        return
    print(solve(raw))


if __name__ == "__main__":
    main()
