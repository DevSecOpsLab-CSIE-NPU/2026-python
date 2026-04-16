"""UVA 100 / Collatz cycle-length 的單元測試。

這個檔案採用 Python 內建 `unittest`，會直接驗證正式解答模組，
確保程式邏輯與題目敘述一致。
"""

from __future__ import annotations

import unittest

from question_100 import CollatzSolver, solve_text


class TestQuestion100(unittest.TestCase):
    def setUp(self) -> None:
        # 每個測試都使用新的 solver，避免快取狀態互相影響。
        self.solver = CollatzSolver()

    def test_cycle_length_of_one_is_one(self) -> None:
        # 題目定義的最小正整數 1，cycle-length 應該是 1。
        self.assertEqual(self.solver.cycle_length(1), 1)

    def test_cycle_length_of_known_values(self) -> None:
        # 這些值是 UVA 100 / Collatz 常見的標準檢查點。
        self.assertEqual(self.solver.cycle_length(2), 2)
        self.assertEqual(self.solver.cycle_length(3), 8)
        self.assertEqual(self.solver.cycle_length(22), 16)

    def test_sample_case_1_to_10(self) -> None:
        # 題目與常見題解中最基本的範例，驗證區間查詢是否正確。
        self.assertEqual(self.solver.max_cycle_length(1, 10), 20)

    def test_sample_case_100_to_200(self) -> None:
        # 第二組標準樣本，確認程式在較大區間仍可得到正確答案。
        self.assertEqual(self.solver.max_cycle_length(100, 200), 125)

    def test_sample_case_201_to_210(self) -> None:
        # 第三組樣本，補強對較短區間的驗證。
        self.assertEqual(self.solver.max_cycle_length(201, 210), 89)

    def test_sample_case_900_to_1000(self) -> None:
        # 第四組樣本，確認高數值區間也能正常處理。
        self.assertEqual(self.solver.max_cycle_length(900, 1000), 174)

    def test_reverse_range_should_match_forward_range(self) -> None:
        # 題目允許 i 與 j 順序不固定，因此要先做區間正規化。
        self.assertEqual(self.solver.max_cycle_length(10, 1), 20)
        self.assertEqual(self.solver.max_cycle_length(200, 100), 125)

    def test_single_number_range(self) -> None:
        # 當 i == j 時，答案就等於單一數字的 cycle-length。
        self.assertEqual(self.solver.max_cycle_length(22, 22), 16)
        self.assertEqual(self.solver.max_cycle_length(1, 1), 1)

    def test_invalid_input_rejected(self) -> None:
        # 題目只定義正整數，因此 0 與負數都應該被明確拒絕。
        with self.assertRaises(ValueError):
            self.solver.cycle_length(0)

        with self.assertRaises(ValueError):
            self.solver.cycle_length(-7)

    def test_cli_output_format_matches_samples(self) -> None:
        # 直接驗證文字輸入輸出的格式，避免主程式入口寫錯。
        input_text = """1 10
100 200
201 210
900 1000
"""
        expected = """1 10 20
100 200 125
201 210 89
900 1000 174"""
        self.assertEqual(solve_text(input_text), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)