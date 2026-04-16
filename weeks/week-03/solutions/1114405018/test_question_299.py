"""UVA 299（Train Swapping）單元測試

使用方式：
1. 把你的解答程式放在同一資料夾，檔名建議為下列其中之一：
   - 299.py
   - question_299.py
   - uva299.py
   - main.py
2. 在此資料夾執行：
   python -m unittest -v test_question_299.py

測試策略：
- 以 subprocess 執行受測程式，模擬線上評測的 stdin / stdout 互動。
- 驗證逆序對計算邏輯（相鄰交換最少次數 = 逆序對數量）。
- 測試已排序、完全反序、隨機排列等情境。
- 若找不到受測檔案，會直接失敗並提示可用檔名。
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


# 依序嘗試這些常見檔名，第一個存在的檔案即作為受測程式
CANDIDATE_FILES = ["299.py", "question_299.py", "uva299.py", "main.py"]


class TestUVA299(unittest.TestCase):
    """針對 UVA 299 火車車廂置換進行驗證。"""

    @classmethod
    def setUpClass(cls) -> None:
        """在所有測試前先定位受測解答檔案。"""
        cls.test_dir = Path(__file__).resolve().parent
        cls.solver_path = None

        for filename in CANDIDATE_FILES:
            candidate = cls.test_dir / filename
            if candidate.exists() and candidate.is_file():
                cls.solver_path = candidate
                break

        if cls.solver_path is None:
            raise FileNotFoundError(
                "找不到 UVA 299 解答檔案。請在同資料夾放置下列任一檔名："
                + ", ".join(CANDIDATE_FILES)
            )

    def run_solver(self, input_data: str) -> str:
        """執行受測程式，回傳標準輸出（去除尾端空白）。

        設計重點：
        - 使用 sys.executable 確保以目前 Python 環境執行。
        - 若程式非正常結束，會帶出 stdout/stderr 方便除錯。
        """
        proc = subprocess.run(
            [sys.executable, str(self.solver_path)],
            input=input_data,
            text=True,
            capture_output=True,
            check=False,
            cwd=str(self.test_dir),
        )

        if proc.returncode != 0:
            self.fail(
                "受測程式執行失敗（return code != 0）。\n"
                f"stdout:\n{proc.stdout}\n"
                f"stderr:\n{proc.stderr}"
            )

        return proc.stdout.rstrip('\n')

    def count_inversions(self, perm: list[int]) -> int:
        """參考實作：計算排列中的逆序對數量。

        逆序對：任何 i < j 但 perm[i] > perm[j] 的 (i, j) 對。
        相鄰交換最少次數等於逆序對數量。
        """
        count = 0
        n = len(perm)
        for i in range(n):
            for j in range(i + 1, n):
                if perm[i] > perm[j]:
                    count += 1
        return count

    def test_already_sorted(self) -> None:
        """驗證已排序的列表需要 0 次交換。"""
        input_data = "1\n3\n1 2 3\n"
        expected = "Optimal train swapping takes 0 swaps."

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_single_element(self) -> None:
        """驗證單個元素需要 0 次交換。"""
        input_data = "1\n1\n1\n"
        expected = "Optimal train swapping takes 0 swaps."

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_completely_reversed(self) -> None:
        """驗證完全反序的列表。

        3 2 1 -> 逆序對：(0,1), (0,2), (1,2) = 3 對
        """
        input_data = "1\n3\n3 2 1\n"
        expected = "Optimal train swapping takes 3 swaps."

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_two_elements_swapped(self) -> None:
        """驗證只需一次交換的情況。

        2 1 -> 逆序對：(0,1) = 1 對
        """
        input_data = "1\n2\n2 1\n"
        expected = "Optimal train swapping takes 1 swaps."

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_four_elements_partial(self) -> None:
        """驗證部分排序的四元素列表。

        2 1 3 4 -> 逆序對：(0,1) = 1 對
        """
        input_data = "1\n4\n2 1 3 4\n"
        expected = "Optimal train swapping takes 1 swaps."

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_four_elements_mixed(self) -> None:
        """驗證混亂排列的四元素列表。

        3 1 4 2 -> 逆序對：(0,1), (0,3), (2,3) = 3 對
        """
        input_data = "1\n4\n3 1 4 2\n"
        expected = "Optimal train swapping takes 3 swaps."

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_multiple_test_cases(self) -> None:
        """驗證多組測資的輸入輸出。

        測資 1：1 2 -> 0 swaps
        測資 2：2 1 -> 1 swaps
        測資 3：3 2 1 -> 3 swaps
        """
        input_data = "3\n2\n1 2\n2\n2 1\n3\n3 2 1\n"
        expected = "\n".join(
            [
                "Optimal train swapping takes 0 swaps.",
                "Optimal train swapping takes 1 swaps.",
                "Optimal train swapping takes 3 swaps.",
            ]
        )

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_random_like_five_elements(self) -> None:
        """驗證隨機排列的五元素列表。

        4 2 1 3 5 -> 逆序對：(0,1), (0,2), (0,3), (1,2) = 4 對
        """
        input_data = "1\n5\n4 2 1 3 5\n"
        # 手工驗算逆序對
        perm = [4, 2, 1, 3, 5]
        inversions = self.count_inversions(perm)
        expected = f"Optimal train swapping takes {inversions} swaps."

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
