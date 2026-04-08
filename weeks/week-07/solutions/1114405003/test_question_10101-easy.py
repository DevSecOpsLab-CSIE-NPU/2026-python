"""
UVA 10101 / ZeroJudge a094 單元測試（-easy 版）

題目重點（好記版）：
- 只允許「移動一根木棒」。
- 只能動數字（0~9 的七段顯示），不能動 + - =。
- 目標是把原本不成立的等式，改成成立。

這份檔案提供：
1) solve_fast：較快、結構清楚的求解版本（用數字轉換表）。
2) solve_oracle_bruteforce：直接以七段 bit 操作暴力枚舉，作為正確性對照。
3) unittest：用固定案例 + 隨機案例檢查 fast 與 oracle 的「有解/無解一致性」，
   並驗證 fast 輸出確實是「只移動一根木棒」得到的合法解。
"""

from __future__ import annotations

import random
import unittest


# =========================
# 一、七段顯示定義
# =========================
# segment index: a,b,c,d,e,f,g -> 0..6
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


def _trim_to_expr(raw: str) -> str:
    """取出第一個 # 以前的內容，並保留結尾 #。"""
    p = raw.find("#")
    if p == -1:
        body = raw
    else:
        body = raw[:p]
    return body + "#"


def _eval_side(side: str) -> int:
    """
    計算單邊（只含 + / - / 數字）的值。
    支援開頭負號，例如 -12+3-4。
    """
    i = 0
    n = len(side)
    total = 0

    while i < n:
        sign = 1
        if side[i] == "+":
            sign = 1
            i += 1
        elif side[i] == "-":
            sign = -1
            i += 1

        j = i
        while j < n and side[j].isdigit():
            j += 1

        # 理論上不會發生（題目保證格式），但保守處理
        if j == i:
            raise ValueError("invalid side expression")

        total += sign * int(side[i:j])
        i = j

    return total


def _is_equation_true(expr_body: str) -> bool:
    """檢查不含 # 的等式是否成立。"""
    if expr_body.count("=") != 1:
        return False
    left, right = expr_body.split("=", 1)
    return _eval_side(left) == _eval_side(right)


def _replace_char(s: str, idx: int, ch: str) -> str:
    return s[:idx] + ch + s[idx + 1 :]


# =========================
# 二、轉換表（給 fast 用）
# =========================


def _build_transition_tables() -> tuple[dict[str, list[str]], dict[str, list[str]], dict[str, list[str]]]:
    """
    建三種轉換：
    - remove1[d]: 從 d 拿掉一根後可變成哪些數字
    - add1[d]:    在 d 加上一根後可變成哪些數字
    - move1[d]:   在 d 內部搬一根（先拿掉一根再加到別處）可變成哪些數字
    """
    remove1: dict[str, list[str]] = {str(x): [] for x in range(10)}
    add1: dict[str, list[str]] = {str(x): [] for x in range(10)}
    move1: dict[str, list[str]] = {str(x): [] for x in range(10)}

    for d in range(10):
        dch = str(d)
        mask = DIGIT_TO_MASK[dch]

        for nd in range(10):
            nch = str(nd)
            nmask = DIGIT_TO_MASK[nch]

            removed_bits = (mask & ~nmask).bit_count()
            added_bits = (nmask & ~mask).bit_count()

            if removed_bits == 1 and added_bits == 0:
                remove1[dch].append(nch)
            if removed_bits == 0 and added_bits == 1:
                add1[dch].append(nch)
            if removed_bits == 1 and added_bits == 1:
                move1[dch].append(nch)

    return remove1, add1, move1


REMOVE1, ADD1, MOVE1 = _build_transition_tables()


# =========================
# 三、被測試邏輯（fast）
# =========================


def solve_fast(raw_expr: str) -> str:
    """
    回傳：
    - 找到解就回傳新的等式（結尾含 #）
    - 否則回傳 "No"

    策略（好記）：
    1) 先試「同一個數字內部搬一根」
    2) 再試「A 數字拿掉一根，B 數字加上一根」
    3) 一旦等式成立就回傳
    """
    expr = _trim_to_expr(raw_expr)
    body = expr[:-1]

    digit_pos = [i for i, ch in enumerate(body) if ch.isdigit()]

    # 情況 1：同一數字內移動一根
    for i in digit_pos:
        old = body[i]
        for new_d in MOVE1[old]:
            cand = _replace_char(body, i, new_d)
            if _is_equation_true(cand):
                return cand + "#"

    # 情況 2：從 i 拿掉一根，搬到 j（i != j）
    for i in digit_pos:
        src_old = body[i]
        for src_new in REMOVE1[src_old]:
            body_after_remove = _replace_char(body, i, src_new)

            for j in digit_pos:
                if j == i:
                    continue
                dst_old = body[j]
                for dst_new in ADD1[dst_old]:
                    cand = _replace_char(body_after_remove, j, dst_new)
                    if _is_equation_true(cand):
                        return cand + "#"

    return "No"


# =========================
# 四、暴力 oracle（小資料）
# =========================


def solve_oracle_bruteforce(raw_expr: str) -> str | None:
    """
    直接在七段位元層級枚舉「拿一根 + 放一根」：
    - 可以同一數字內搬，也可以跨數字搬。
    - 若找到第一個成立等式，回傳該等式（含 #）。
    - 找不到回傳 None。

    這個版本較慢，但做測試對照很可靠。
    """
    expr = _trim_to_expr(raw_expr)
    body = expr[:-1]

    digit_pos = [i for i, ch in enumerate(body) if ch.isdigit()]
    masks = [DIGIT_TO_MASK[body[p]] for p in digit_pos]

    # 枚舉「來源數字 i 的哪一根被拿走」
    for i, pos_i in enumerate(digit_pos):
        src_mask = masks[i]

        for src_seg in range(7):
            if ((src_mask >> src_seg) & 1) == 0:
                continue

            removed_mask = src_mask & ~(1 << src_seg)

            # 枚舉「目的數字 j 的哪一段被點亮」
            for j, pos_j in enumerate(digit_pos):
                dst_base = removed_mask if i == j else masks[j]

                for dst_seg in range(7):
                    if ((dst_base >> dst_seg) & 1) == 1:
                        continue

                    added_mask = dst_base | (1 << dst_seg)

                    # 不允許把木棒拿下來又放回同一段（整體無變化）
                    if i == j and src_seg == dst_seg:
                        continue

                    # 兩端結果都要是合法數字
                    if removed_mask not in MASK_TO_DIGIT and i != j:
                        continue
                    if added_mask not in MASK_TO_DIGIT:
                        continue

                    # 建立候選字串
                    cand = body

                    if i == j:
                        # 同一數字內搬一根：結果就是 added_mask
                        cand_digit = MASK_TO_DIGIT.get(added_mask)
                        if cand_digit is None:
                            continue
                        cand = _replace_char(cand, pos_i, cand_digit)
                    else:
                        src_digit = MASK_TO_DIGIT.get(removed_mask)
                        dst_digit = MASK_TO_DIGIT.get(added_mask)
                        if src_digit is None or dst_digit is None:
                            continue
                        cand = _replace_char(cand, pos_i, src_digit)
                        cand = _replace_char(cand, pos_j, dst_digit)

                    if _is_equation_true(cand):
                        return cand + "#"

    return None


# =========================
# 五、驗證器（檢查 fast 輸出是否真合法）
# =========================


def _is_one_stick_move(original_body: str, cand_body: str) -> bool:
    """
    檢查 cand_body 是否可由 original_body 透過「只移動一根木棒」得到。

    檢查重點：
    - 長度相同
    - 運算符位置不變（只能改數字）
    - 全域只有 1 根被拿走、1 根被加上（總段數守恆）
    """
    if len(original_body) != len(cand_body):
        return False

    removed = 0
    added = 0

    for oc, nc in zip(original_body, cand_body):
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


def _is_valid_solution(original_raw: str, result: str) -> bool:
    """確認 result 是 original_raw 的合法解。"""
    if result == "No":
        return False

    ori = _trim_to_expr(original_raw)
    res = _trim_to_expr(result)

    ori_body = ori[:-1]
    res_body = res[:-1]

    if not _is_one_stick_move(ori_body, res_body):
        return False

    return _is_equation_true(res_body)


# =========================
# 六、單元測試
# =========================


class TestQuestion10101Easy(unittest.TestCase):
    """UVA 10101（a094）-easy 測試。"""

    def test_trim_after_hash(self) -> None:
        # # 後面的垃圾字元要被忽略
        expr = "1+1=3#THIS_PART_SHOULD_BE_IGNORED"
        out = solve_fast(expr)

        oracle = solve_oracle_bruteforce(expr)
        if oracle is None:
            self.assertEqual(out, "No")
        else:
            self.assertNotEqual(out, "No")
            self.assertTrue(_is_valid_solution(expr, out))

    def test_random_small_compare_existence(self) -> None:
        # 小型隨機等式，檢查 fast 與 oracle 的「有解/無解」一致。
        random.seed(10101)

        ops = ["+", "-"]
        for _ in range(120):
            # 建立格式：a op b = c op d（皆單位數，避免 oracle 過慢）
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            c = random.randint(0, 9)
            d = random.randint(0, 9)
            op1 = random.choice(ops)
            op2 = random.choice(ops)

            expr = f"{a}{op1}{b}={c}{op2}{d}#"

            fast = solve_fast(expr)
            oracle = solve_oracle_bruteforce(expr)

            if oracle is None:
                self.assertEqual(fast, "No")
            else:
                self.assertNotEqual(fast, "No")
                self.assertTrue(_is_valid_solution(expr, fast))

    def test_explicit_known_case(self) -> None:
        # 固定案例：不要求唯一答案，只要求 fast 回傳合法解或正確 No。
        expr = "9-5=3#"
        fast = solve_fast(expr)
        oracle = solve_oracle_bruteforce(expr)

        if oracle is None:
            self.assertEqual(fast, "No")
        else:
            self.assertNotEqual(fast, "No")
            self.assertTrue(_is_valid_solution(expr, fast))


if __name__ == "__main__":
    unittest.main()
