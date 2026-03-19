"""
UVA 10008（Cryptanalysis）單元測試程式。

說明：
1. 檔內提供 `reference_solve`，確保測試可獨立執行。
2. 若同資料夾存在 `solution_10008.py` 且提供 `solve(data: str) -> str`，
   測試會自動改測你的解答函式。
"""

from __future__ import annotations

import importlib.util
import unittest
from collections import Counter
from pathlib import Path


# -------------------------------
# 題目邏輯（參考解）
# -------------------------------
def reference_solve(data: str) -> str:
    """
    依題目規則統計英文字母出現次數。

    規則重點：
    - 大小寫不分（全部轉大寫後統計）。
    - 只統計 A~Z，其它符號、數字、空白都忽略。
    - 輸出先依次數遞減，再依字母遞增。
    """
    lines = data.splitlines()
    if not lines:
        return ""

    n = int(lines[0].strip() or "0")
    counter: Counter[str] = Counter()

    for line in lines[1 : 1 + n]:
        for ch in line.upper():
            if "A" <= ch <= "Z":
                counter[ch] += 1

    ordered = sorted(counter.items(), key=lambda item: (-item[1], item[0]))

    if not ordered:
        return ""

    return "\n".join(f"{ch} {count}" for ch, count in ordered) + "\n"


# -------------------------------
# 可選：自動載入學生解答
# -------------------------------
def _load_candidate_solve():
    """
    若存在 `solution_10008.py` 且有 `solve(data)`，就改用該函式測試；
    否則使用參考解。
    """
    current_dir = Path(__file__).resolve().parent
    candidate = current_dir / "solution_10008.py"

    if not candidate.exists():
        return reference_solve

    spec = importlib.util.spec_from_file_location("solution_10008", candidate)
    if spec is None or spec.loader is None:
        return reference_solve

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    solve_fn = getattr(module, "solve", None)
    if callable(solve_fn):
        return solve_fn

    return reference_solve


SOLVE = _load_candidate_solve()


# -------------------------------
# 單元測試
# -------------------------------
class TestUVA10008(unittest.TestCase):
    """針對 UVA 10008 的核心規則設計測試。"""

    def test_case_insensitive_and_ignore_non_letters(self):
        """大小寫視為同字元，且忽略數字與標點符號。"""
        data = """3
Aaa!!!
bB2B
c-c-c
"""
        expected = """A 3
B 3
C 3
"""
        # 三個字母次數都相同，需依字母順序 A、B、C 輸出。
        self.assertEqual(SOLVE(data), expected)

    def test_sort_by_frequency_then_alphabet(self):
        """先比次數（大到小），同次數時比字母（小到大）。"""
        data = """2
abca
zzYY
"""
        # 統計：A=2, Z=2, B=1, C=1, Y=2
        # 順序應為 A 2, Y 2, Z 2, B 1, C 1
        expected = """A 2
Y 2
Z 2
B 1
C 1
"""
        self.assertEqual(SOLVE(data), expected)

    def test_empty_or_non_letter_lines(self):
        """若沒有任何 A~Z 字母，輸出應為空字串。"""
        data = """3
12345
!!!
   
"""
        self.assertEqual(SOLVE(data), "")

    def test_multiple_lines_combined_count(self):
        """需跨多行累積統計，不是逐行輸出。"""
        data = """4
aA
BbB
A b
z
"""
        # A=3, B=4, Z=1
        expected = """B 4
A 3
Z 1
"""
        self.assertEqual(SOLVE(data), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
