# test_10226.py
# UVA 10226 的單元測試程式
# 使用 unittest 框架來測試排列生成和輸出格式
# 繁體中文註解：這個檔案用來測試解決方案函數是否正確運作

import unittest
from solution_10226 import generate_valid_permutations, format_compressed_output

class TestUVA10226(unittest.TestCase):
    def test_no_constraints(self):
        # 測試沒有約束的情況
        n = 2
        constraints = [[], []]  # 沒有任何人有約束
        perms = generate_valid_permutations(n, constraints)
        expected = [[1, 2], [2, 1]]  # 所有可能的排列
        self.assertEqual(perms, expected)
        output = format_compressed_output(perms)
        self.assertEqual(output, "12\n21\n")  # 輸出所有排列，每行一個

    def test_with_constraints(self):
        # 測試有約束的情況
        n = 2
        constraints = [[], [2]]  # 人1 無約束，人2 不喜歡位置2
        perms = generate_valid_permutations(n, constraints)
        expected = [[1, 2], [2, 1]]  # 只有這些有效
        self.assertEqual(perms, expected)
        output = format_compressed_output(perms)
        self.assertEqual(output, "12\n21\n")  # 假設輸出格式

    def test_n3_no_constraints(self):
        # 測試 N=3 無約束
        n = 3
        constraints = [[], [], []]
        perms = generate_valid_permutations(n, constraints)
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(perms, expected)
        output = format_compressed_output(perms)
        # 假設壓縮，但這裡簡單輸出
        self.assertEqual(output, "123\n132\n213\n231\n312\n321\n")

if __name__ == '__main__':
    unittest.main()