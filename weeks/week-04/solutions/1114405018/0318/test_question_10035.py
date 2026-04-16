"""UVA 10035（Primary Arithmetic）單元測試

使用方式：
1. 把你的解答程式放在同一資料夾，檔名建議為下列其中之一：
   - 10035.py
   - question_10035.py
   - uva10035.py
   - main.py
2. 在此資料夾執行：
   python -m unittest -v test_question_10035.py

測試策略：
- 以 subprocess 執行受測程式，模擬線上評測的 stdin / stdout。
- 驗證進位次數計算與輸出字串格式（No carry operation. / 1 carry operation. / n carry operations.）。
- 驗證輸入終止條件 0 0（該行不產生輸出）。
- 若找不到受測檔案，測試會直接失敗並提示可用檔名。
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


# 依序嘗試這些常見檔名，第一個存在的檔案即作為受測程式
CANDIDATE_FILES = ["10035.py", "question_10035.py", "uva10035.py", "main.py"]


class TestUVA10035(unittest.TestCase):
    """針對 UVA 10035 的進位統計規則進行驗證。"""

    @classmethod
    def setUpClass(cls) -> None:
        """在所有測試開始前，先定位受測解答檔案。"""
        cls.test_dir = Path(__file__).resolve().parent
        cls.solver_path = None

        for filename in CANDIDATE_FILES:
            p = cls.test_dir / filename
            if p.exists() and p.is_file():
                cls.solver_path = p
                break

        if cls.solver_path is None:
            raise FileNotFoundError(
                "找不到 UVA 10035 解答檔案。請在同資料夾放置下列任一檔名："
                + ", ".join(CANDIDATE_FILES)
            )

    def run_solver(self, input_data: str) -> str:
        """執行受測程式並回傳標準輸出（去除尾端換行）。"""
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

        return proc.stdout.rstrip("\n")

    @staticmethod
    def carry_count(a: int, b: int) -> int:
        """參考實作：計算 a+b 的進位次數。"""
        carry = 0
        count = 0

        while a > 0 or b > 0:
            da = a % 10
            db = b % 10
            if da + db + carry >= 10:
                count += 1
                carry = 1
            else:
                carry = 0

            a //= 10
            b //= 10

        return count

    @staticmethod
    def carry_text(cnt: int) -> str:
        """把進位次數轉成題目要求輸出格式。"""
        if cnt == 0:
            return "No carry operation."
        if cnt == 1:
            return "1 carry operation."
        return f"{cnt} carry operations."

    def expected_for_pairs(self, pairs: list[tuple[int, int]]) -> str:
        """依照題目規則產生預期輸出。"""
        lines = []
        for a, b in pairs:
            if a == 0 and b == 0:
                break
            lines.append(self.carry_text(self.carry_count(a, b)))
        return "\n".join(lines)

    def test_known_examples(self) -> None:
        """經典範例：分別有 0 次、3 次、1 次進位。"""
        pairs = [(123, 456), (555, 555), (123, 594), (0, 0)]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
        expected = self.expected_for_pairs(pairs)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_single_carry(self) -> None:
        """只有一次進位的情況。"""
        pairs = [(49, 51), (0, 0)]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
        expected = self.expected_for_pairs(pairs)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_multiple_lines(self) -> None:
        """多行測資：每行都要正確輸出對應進位結果。"""
        pairs = [
            (1, 9999),
            (1111, 8889),
            (1000, 1),
            (250, 750),
            (0, 0),
        ]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
        expected = self.expected_for_pairs(pairs)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)

    def test_termination_only(self) -> None:
        """僅有終止行 0 0 時，輸出應為空。"""
        input_data = "0 0\n"
        actual = self.run_solver(input_data)
        self.assertEqual(actual, "")

    def test_large_numbers_under_10_digits(self) -> None:
        """接近題目上限位數的整數也應正確計算。"""
        pairs = [
            (999999999, 1),
            (987654321, 123456789),
            (400000000, 600000000),
            (0, 0),
        ]
        input_data = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
        expected = self.expected_for_pairs(pairs)

        actual = self.run_solver(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
