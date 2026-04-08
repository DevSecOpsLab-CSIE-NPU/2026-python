"""
UVA 10101 / ZeroJudge a094 單元測試

題意：
給一個以 # 結尾的等式字串，若能「只移動一根木棒」（且只能動數字七段顯示）
讓等式成立，輸出新的等式；否則輸出 No。

測試策略：
1. 被測函式 solve_fast：用七段轉換表搜尋答案。
2. 對照函式 solve_oracle：位元層級暴力枚舉「拿一根 + 放一根」。
3. 單元測試驗證：
   - fast 與 oracle 在「有解 / 無解」一致。
   - 若 fast 回傳解，必須真的是一根木棒移動且等式成立。
"""

from __future__ import annotations

import random
import unittest


# segment: a,b,c,d,e,f,g -> 0..6
DIGIT_TO_MASK: dict[str, int] = {
    "0": 0b1111110,
    "1": 0b0110000,
    "2": 0b1101101,
    "3": 0b1111001,
    "4": 0b0110011,
    "5": 0b1011011,
    "6": 0b1011111,
    "7": 0b1110000,
    "8": 0b1111111,
    "9": 0b1111011,
}
MASK_TO_DIGIT: dict[int, str] = {v: k for k, v in DIGIT_TO_MASK.items()}


def _trim_expr(raw: str) -> str:
    """只保留第一個 # 前的式子，並補回 #。"""
    p = raw.find("#")
    if p == -1:
        return raw + "#"
    return raw[:p] + "#"


def _eval_side(side: str) -> int:
    """計算單邊算式值，支援開頭正負號。"""
    i = 0
    total = 0
    n = len(side)

    while i < n:
        sign = 1
        if side[i] == "+":
            i += 1
        elif side[i] == "-":
            sign = -1
            i += 1

        j = i
        while j < n and side[j].isdigit():
            j += 1
        if j == i:
            raise ValueError("invalid expression side")

        total += sign * int(side[i:j])
        i = j

    return total


def _equation_true(body: str) -> bool:
    """判斷不含 # 的等式是否成立。"""
    if body.count("=") != 1:
        return False
    left, right = body.split("=", 1)
    return _eval_side(left) == _eval_side(right)


def _replace_char(s: str, idx: int, ch: str) -> str:
    return s[:idx] + ch + s[idx + 1 :]


def _build_transitions() -> tuple[dict[str, list[str]], dict[str, list[str]], dict[str, list[str]]]:
    """
    預建三種轉換表：
    - remove1[d]: d 移除一根後可變成哪些數字
    - add1[d]:    d 增加一根後可變成哪些數字
    - move1[d]:   d 內部搬一根可變成哪些數字
    """
    remove1: dict[str, list[str]] = {str(i): [] for i in range(10)}
    add1: dict[str, list[str]] = {str(i): [] for i in range(10)}
    move1: dict[str, list[str]] = {str(i): [] for i in range(10)}

    for d in range(10):
        dch = str(d)
        dm = DIGIT_TO_MASK[dch]

        for nd in range(10):
            nch = str(nd)
            nm = DIGIT_TO_MASK[nch]

            removed = (dm & ~nm).bit_count()
            added = (nm & ~dm).bit_count()

            if removed == 1 and added == 0:
                remove1[dch].append(nch)
            if removed == 0 and added == 1:
                add1[dch].append(nch)
            if removed == 1 and added == 1:
                move1[dch].append(nch)

    return remove1, add1, move1


REMOVE1, ADD1, MOVE1 = _build_transitions()


def solve_fast(raw_expr: str) -> str:
    """
    回傳新等式（含 #）或 No。

    流程：
    1) 嘗試同一個數字內搬一根。
    2) 嘗試從某數字拿一根，移到另一數字。
    """
    expr = _trim_expr(raw_expr)
    body = expr[:-1]
    digits = [i for i, ch in enumerate(body) if ch.isdigit()]

    for i in digits:
        old = body[i]
        for nd in MOVE1[old]:
            cand = _replace_char(body, i, nd)
            if _equation_true(cand):
                return cand + "#"

    for i in digits:
        src_old = body[i]
        for src_new in REMOVE1[src_old]:
            removed_body = _replace_char(body, i, src_new)

            for j in digits:
                if i == j:
                    continue

                dst_old = body[j]
                for dst_new in ADD1[dst_old]:
                    cand = _replace_char(removed_body, j, dst_new)
                    if _equation_true(cand):
                        return cand + "#"

    return "No"


def solve_oracle(raw_expr: str) -> str | None:
    """
    暴力對照：
    以七段位元操作枚舉「來源段移除 + 目的段加上」。
    找到任一合法解就回傳，找不到回傳 None。
    """
    expr = _trim_expr(raw_expr)
    body = expr[:-1]

    digit_pos = [i for i, ch in enumerate(body) if ch.isdigit()]
    masks = [DIGIT_TO_MASK[body[p]] for p in digit_pos]

    for i, pos_i in enumerate(digit_pos):
        src_mask = masks[i]

        for src_seg in range(7):
            if ((src_mask >> src_seg) & 1) == 0:
                continue

            removed_mask = src_mask & ~(1 << src_seg)

            for j, pos_j in enumerate(digit_pos):
                dst_base = removed_mask if i == j else masks[j]

                for dst_seg in range(7):
                    if ((dst_base >> dst_seg) & 1) == 1:
                        continue
                    if i == j and src_seg == dst_seg:
                        continue

                    added_mask = dst_base | (1 << dst_seg)

                    if i == j:
                        digit = MASK_TO_DIGIT.get(added_mask)
                        if digit is None:
                            continue
                        cand = _replace_char(body, pos_i, digit)
                    else:
                        src_digit = MASK_TO_DIGIT.get(removed_mask)
                        dst_digit = MASK_TO_DIGIT.get(added_mask)
                        if src_digit is None or dst_digit is None:
                            continue
                        cand = _replace_char(body, pos_i, src_digit)
                        cand = _replace_char(cand, pos_j, dst_digit)

                    if _equation_true(cand):
                        return cand + "#"

    return None


def _is_one_stick_move(original_body: str, new_body: str) -> bool:
    """檢查是否真的是只移動一根木棒。"""
    if len(original_body) != len(new_body):
        return False

    removed = 0
    added = 0

    for oc, nc in zip(original_body, new_body):
        if oc.isdigit() != nc.isdigit():
            return False
        if not oc.isdigit() and oc != nc:
            return False

        if oc.isdigit():
            om = DIGIT_TO_MASK[oc]
            nm = DIGIT_TO_MASK[nc]
            removed += (om & ~nm).bit_count()
            added += (nm & ~om).bit_count()

    return removed == 1 and added == 1


def _valid_solution(raw_expr: str, result: str) -> bool:
    """驗證結果字串是否為合法解。"""
    if result == "No":
        return False

    ori = _trim_expr(raw_expr)
    res = _trim_expr(result)

    ori_body = ori[:-1]
    res_body = res[:-1]

    if not _is_one_stick_move(ori_body, res_body):
        return False

    return _equation_true(res_body)


class TestQuestion10101(unittest.TestCase):
    """UVA 10101 測試集合。"""

    def test_ignore_suffix_after_hash(self) -> None:
        expr = "1+1=3#ignore_this_part"
        fast = solve_fast(expr)
        oracle = solve_oracle(expr)

        if oracle is None:
            self.assertEqual(fast, "No")
        else:
            self.assertNotEqual(fast, "No")
            self.assertTrue(_valid_solution(expr, fast))

    def test_explicit_case(self) -> None:
        expr = "9-5=3#"
        fast = solve_fast(expr)
        oracle = solve_oracle(expr)

        if oracle is None:
            self.assertEqual(fast, "No")
        else:
            self.assertNotEqual(fast, "No")
            self.assertTrue(_valid_solution(expr, fast))

    def test_random_existence_matches_oracle(self) -> None:
        random.seed(1010101)
        ops = ["+", "-"]

        for _ in range(150):
            # 單位數格式，讓暴力對照執行快速且穩定
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            c = random.randint(0, 9)
            d = random.randint(0, 9)
            op1 = random.choice(ops)
            op2 = random.choice(ops)
            expr = f"{a}{op1}{b}={c}{op2}{d}#"

            fast = solve_fast(expr)
            oracle = solve_oracle(expr)

            if oracle is None:
                self.assertEqual(fast, "No")
            else:
                self.assertNotEqual(fast, "No")
                self.assertTrue(_valid_solution(expr, fast))


if __name__ == "__main__":
    unittest.main()
