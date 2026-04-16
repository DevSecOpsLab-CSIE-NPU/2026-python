from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SCRIPT_MAIN = BASE_DIR / "QUESTION-10101.py"
SCRIPT_EASY = BASE_DIR / "QUESTION-10101-easy.py"

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


def run_script(script_path: Path, input_data: str) -> str:
    cp = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return cp.stdout.strip()


def eval_side(side: str) -> int:
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
        total += sign * int(side[i:j])
        sign = 1
        i = j
    return total


def eq_true(expr: str) -> bool:
    eq = expr.index("=")
    return eval_side(expr[:eq]) == eval_side(expr[eq + 1 :])


def one_stick_possible_change(a: str, b: str) -> bool:
    """檢查兩個同長字串（只含數字與固定運算符）是否剛好是一次移棒變化。"""
    if len(a) != len(b):
        return False

    diff_digit_idx = [i for i in range(len(a)) if a[i] != b[i]]
    if not diff_digit_idx:
        return False

    # 非數字字元不可改動
    for i in diff_digit_idx:
        if not (a[i].isdigit() and b[i].isdigit()):
            return False

    if len(diff_digit_idx) == 1:
        i = diff_digit_idx[0]
        da, db = int(a[i]), int(b[i])
        s1, s2 = SEG[da], SEG[db]
        rm = (s1 & ~s2).bit_count()
        ad = (s2 & ~s1).bit_count()
        return rm == 1 and ad == 1

    if len(diff_digit_idx) == 2:
        i, j = diff_digit_idx
        d1, n1 = int(a[i]), int(b[i])
        d2, n2 = int(a[j]), int(b[j])
        s1, t1 = SEG[d1], SEG[n1]
        s2, t2 = SEG[d2], SEG[n2]

        rm1 = (s1 & ~t1).bit_count()
        ad1 = (t1 & ~s1).bit_count()
        rm2 = (s2 & ~t2).bit_count()
        ad2 = (t2 & ~s2).bit_count()

        # 一位拿掉一根，另一位補上一根
        return (rm1 == 1 and ad1 == 0 and rm2 == 0 and ad2 == 1) or (
            rm2 == 1 and ad2 == 0 and rm1 == 0 and ad1 == 1
        )

    return False


def brute_exists(expr: str) -> bool:
    """暴力驗證是否至少存在一個可行解（測試用小字串）。"""
    chars = list(expr)
    digit_pos = [i for i, ch in enumerate(chars) if ch.isdigit()]

    # 一位改動（同位移棒）
    for i in digit_pos:
        d = int(chars[i])
        for nd in range(10):
            if nd == d:
                continue
            s1, s2 = SEG[d], SEG[nd]
            rm = (s1 & ~s2).bit_count()
            ad = (s2 & ~s1).bit_count()
            if rm == 1 and ad == 1:
                t = chars[:]
                t[i] = str(nd)
                if eq_true("".join(t)):
                    return True

    # 兩位改動（一拿一放）
    for x in range(len(digit_pos)):
        i = digit_pos[x]
        di = int(chars[i])
        for y in range(len(digit_pos)):
            if x == y:
                continue
            j = digit_pos[y]
            dj = int(chars[j])
            for ni in range(10):
                if ni == di:
                    continue
                s1, t1 = SEG[di], SEG[ni]
                rm1 = (s1 & ~t1).bit_count()
                ad1 = (t1 & ~s1).bit_count()
                if not (rm1 == 1 and ad1 == 0):
                    continue
                for nj in range(10):
                    if nj == dj:
                        continue
                    s2, t2 = SEG[dj], SEG[nj]
                    rm2 = (s2 & ~t2).bit_count()
                    ad2 = (t2 & ~s2).bit_count()
                    if not (rm2 == 0 and ad2 == 1):
                        continue
                    t = chars[:]
                    t[i] = str(ni)
                    t[j] = str(nj)
                    if eq_true("".join(t)):
                        return True
    return False


class TestQuestion10101(unittest.TestCase):
    def assert_script_output_valid(self, expr_with_hash: str, out: str) -> None:
        expr = expr_with_hash[: expr_with_hash.index("#")]

        if out == "No":
            self.assertFalse(brute_exists(expr))
            return

        self.assertTrue(out.endswith("#"))
        out_expr = out[:-1]

        # 運算符位置不可改變
        for i, ch in enumerate(expr):
            if not ch.isdigit():
                self.assertEqual(out_expr[i], ch)

        self.assertTrue(eq_true(out_expr))
        self.assertTrue(one_stick_possible_change(expr, out_expr))

    def test_solvable_simple(self) -> None:
        inp = "9=0#"
        out_main = run_script(SCRIPT_MAIN, inp)
        out_easy = run_script(SCRIPT_EASY, inp)
        self.assert_script_output_valid(inp, out_main)
        self.assert_script_output_valid(inp, out_easy)

    def test_unsolvable_simple(self) -> None:
        inp = "1+1=2#"
        out_main = run_script(SCRIPT_MAIN, inp)
        out_easy = run_script(SCRIPT_EASY, inp)
        self.assert_script_output_valid(inp, out_main)
        self.assert_script_output_valid(inp, out_easy)

    def test_with_negative(self) -> None:
        inp = "-9+0=0#"
        out_main = run_script(SCRIPT_MAIN, inp)
        out_easy = run_script(SCRIPT_EASY, inp)
        self.assert_script_output_valid(inp, out_main)
        self.assert_script_output_valid(inp, out_easy)

    def test_extra_trailing_text_after_hash(self) -> None:
        inp = "9=0#ignore_this_part"
        out_main = run_script(SCRIPT_MAIN, inp)
        out_easy = run_script(SCRIPT_EASY, inp)
        self.assert_script_output_valid("9=0#", out_main)
        self.assert_script_output_valid("9=0#", out_easy)


if __name__ == "__main__":
    unittest.main(verbosity=2)
