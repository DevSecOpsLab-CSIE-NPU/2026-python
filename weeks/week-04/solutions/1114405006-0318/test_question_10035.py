"""
UVA 10035（Primary Arithmetic）單元測試程式。

說明：
1. 檔案內建 `reference_solve`，讓測試可獨立執行。
2. 若同資料夾存在 `solution_10035.py` 且提供 `solve(data: str) -> str`，
   測試會自動改測你的解答。
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


def _count_carry(a: str, b: str) -> int:
    """計算兩個非負整數字串相加時的進位次數。"""
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    count = 0

    while i >= 0 or j >= 0:
        da = ord(a[i]) - ord("0") if i >= 0 else 0
        db = ord(b[j]) - ord("0") if j >= 0 else 0

        s = da + db + carry
        if s >= 10:
            carry = 1
            count += 1
        else:
            carry = 0

        i -= 1
        j -= 1

    return count


def _format_answer(c: int) -> str:
    """依題目格式輸出 carry 次數文字。"""
    if c == 0:
        return "No carry operation."
    if c == 1:
        return "1 carry operation."
    return f"{c} carry operations."


def reference_solve(data: str) -> str:
    """
    依題目規則：每行兩整數，直到 `0 0` 結束。
    每組輸出該加法的進位次數敘述。
    """
    out: list[str] = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        a, b = line.split()
        if a == "0" and b == "0":
            break

        out.append(_format_answer(_count_carry(a, b)))

    if not out:
        return ""

    return "\n".join(out) + "\n"


def _load_candidate_solve():
    """若有 `solution_10035.py` 且含 `solve`，就改測該函式。"""
    current_dir = Path(__file__).resolve().parent
    candidate = current_dir / "solution_10035.py"

    if not candidate.exists():
        return reference_solve

    spec = importlib.util.spec_from_file_location("solution_10035", candidate)
    if spec is None or spec.loader is None:
        return reference_solve

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    solve_fn = getattr(module, "solve", None)
    if callable(solve_fn):
        return solve_fn

    return reference_solve


SOLVE = _load_candidate_solve()


class TestQuestion10035(unittest.TestCase):
    """針對 UVA 10035 核心規則設計測試。"""

    def test_sample_style_cases(self):
        """常見範例型測資。"""
        data = """123 456
555 555
123 594
0 0
"""
        expected = """No carry operation.
3 carry operations.
1 carry operation.
"""
        self.assertEqual(SOLVE(data), expected)

    def test_different_lengths(self):
        """不同位數加法也要正確計算進位。"""
        data = """1 99999
999 1
0 0
"""
        expected = """5 carry operations.
3 carry operations.
"""
        self.assertEqual(SOLVE(data), expected)

    def test_all_nines_chain_carry(self):
        """連鎖進位情境。"""
        data = """999999999 1
0 0
"""
        expected = """9 carry operations.
"""
        self.assertEqual(SOLVE(data), expected)

    def test_ignore_lines_after_terminator(self):
        """遇到 0 0 後，後續資料必須忽略。"""
        data = """5 5
0 0
9 9
"""
        expected = """1 carry operation.
"""
        self.assertEqual(SOLVE(data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
