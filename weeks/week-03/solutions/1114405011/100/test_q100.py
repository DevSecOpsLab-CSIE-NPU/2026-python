"""
test_q100.py — UVA 100 / ZeroJudge c039 單元測試

測試對象：q100.py 中的三個公開函式
  - cycle_length(n)       : 計算單一整數的 Collatz cycle-length
  - max_cycle_in_range(i, j) : 計算區間內最大 cycle-length
  - solve(input_text)     : 整合輸入／輸出的完整解答函式

執行方式：
  python -m pytest test_q100.py -v
  或
  python test_q100.py
"""

import unittest
from q100 import cycle_length, max_cycle_in_range, solve


class TestCycleLength(unittest.TestCase):
    """測試 cycle_length(n) 函式的正確性。"""

    def test_n_equals_1(self):
        """n=1 時只有 [1]，cycle-length 應為 1。"""
        self.assertEqual(cycle_length(1), 1)

    def test_n_equals_2(self):
        """n=2: 2 → 1，共 2 步。"""
        self.assertEqual(cycle_length(2), 2)

    def test_n_equals_3(self):
        """n=3: 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1，共 8 步。"""
        self.assertEqual(cycle_length(3), 8)

    def test_n_equals_4(self):
        """n=4: 4 → 2 → 1，共 3 步。"""
        self.assertEqual(cycle_length(4), 3)

    def test_n_equals_5(self):
        """n=5: 5 → 16 → 8 → 4 → 2 → 1，共 6 步。"""
        self.assertEqual(cycle_length(5), 6)

    def test_n_equals_22(self):
        """題目範例：22 的 cycle-length 應為 16。"""
        self.assertEqual(cycle_length(22), 16)

    def test_n_equals_9(self):
        """n=9 的 cycle-length 應為 20（(1,10) 區間最大值來源）。"""
        self.assertEqual(cycle_length(9), 20)

    def test_n_large(self):
        """測試較大數值 n=27，其 cycle-length 應為 112。"""
        self.assertEqual(cycle_length(27), 112)


class TestMaxCycleInRange(unittest.TestCase):
    """測試 max_cycle_in_range(i, j) 函式，包含正順序與逆順序輸入。"""

    def test_range_1_to_10(self):
        """區間 [1, 10] 最大 cycle-length 應為 20（來自 n=9）。"""
        self.assertEqual(max_cycle_in_range(1, 10), 20)

    def test_range_100_to_200(self):
        """題目範例：區間 [100, 200] 最大 cycle-length 應為 125。"""
        self.assertEqual(max_cycle_in_range(100, 200), 125)

    def test_range_201_to_210(self):
        """題目範例：區間 [201, 210] 最大 cycle-length 應為 89。"""
        self.assertEqual(max_cycle_in_range(201, 210), 89)

    def test_range_900_to_1000(self):
        """題目範例：區間 [900, 1000] 最大 cycle-length 應為 174。"""
        self.assertEqual(max_cycle_in_range(900, 1000), 174)

    def test_reversed_range(self):
        """題目允許 i > j；逆序輸入應與正順序結果相同。"""
        self.assertEqual(max_cycle_in_range(10, 1), max_cycle_in_range(1, 10))

    def test_reversed_range_100_200(self):
        """逆序輸入 (200, 100) 應與 (100, 200) 結果相同。"""
        self.assertEqual(max_cycle_in_range(200, 100), 125)

    def test_single_element(self):
        """區間只含單一元素時，最大值等於該元素自身的 cycle-length。"""
        self.assertEqual(max_cycle_in_range(22, 22), 16)

    def test_single_element_1(self):
        """區間只含 n=1 時，cycle-length 應為 1。"""
        self.assertEqual(max_cycle_in_range(1, 1), 1)


class TestSolve(unittest.TestCase):
    """測試 solve(input_text) 函式，驗證完整輸入輸出格式。"""

    def test_sample_input(self):
        """題目提供的四組範例，輸出格式需完全一致。"""
        sample_input = (
            "1 10\n"
            "100 200\n"
            "201 210\n"
            "900 1000\n"
        )
        expected_output = (
            "1 10 20\n"
            "100 200 125\n"
            "201 210 89\n"
            "900 1000 174"
        )
        self.assertEqual(solve(sample_input), expected_output)

    def test_single_line(self):
        """單行輸入應正確輸出一行結果。"""
        self.assertEqual(solve("1 10"), "1 10 20")

    def test_reversed_order_in_solve(self):
        """i > j 時，輸出仍保留原始 i j 順序但計算正確範圍。"""
        result = solve("10 1")
        # 輸出第一欄與第二欄應保持原始輸入的 i=10, j=1
        parts = result.split()
        self.assertEqual(parts[0], "10")
        self.assertEqual(parts[1], "1")
        # 最大 cycle-length 應與正順序相同
        self.assertEqual(int(parts[2]), 20)

    def test_empty_lines_ignored(self):
        """輸入中的空行應被忽略，不影響輸出行數。"""
        sample_input = "\n1 10\n\n100 200\n"
        result = solve(sample_input)
        self.assertEqual(result, "1 10 20\n100 200 125")


if __name__ == "__main__":
    # 直接執行此檔案時，顯示詳細測試結果
    unittest.main(verbosity=2)
