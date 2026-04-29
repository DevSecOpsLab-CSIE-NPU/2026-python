"""
UVA 10226 - 排列生成問題 (DFS + 去重)
"""

import unittest
from io import StringIO
import sys

# 導入要測試的解決方案
from solution_10226 import generate_permutations


class TestUVA10226(unittest.TestCase):
    """UVA 10226 排列生成問題的單位測試"""
    
    @classmethod
    def setUpClass(cls):
        """一次性設置測試環境"""
        pass
    
    def test_single_person(self):
        """測試單人情況：一個人 A，無限制，應只有排列 A"""
        # 輸入：1 人，無位置限制
        restrictions = [set()]  # A 無限制
        result = generate_permutations(1, restrictions)
        # 期望：只有一個排列 [A]
        self.assertEqual(len(result), 1)
        self.assertIn(['A'], result)
    
    def test_two_persons_no_restrictions(self):
        """測試兩人無限制：應有 AB 和 BA"""
        restrictions = [set(), set()]  # A, B 無限制
        result = generate_permutations(2, restrictions)
        # 期望：2 個排列 AB, BA
        self.assertEqual(len(result), 2)
        self.assertIn(['A', 'B'], result)
        self.assertIn(['B', 'A'], result)
    
    def test_two_persons_with_restriction(self):
        """測試 A 不想在位置 1, B 無限制：應只有 BA"""
        restrictions = [{0}, set()]  # A 不想在位置 0, B 無限制
        result = generate_permutations(2, restrictions)
        # 期望：只有 BA 一個排列
        self.assertEqual(len(result), 1)
        self.assertIn(['B', 'A'], result)
    
    def test_three_persons_with_restrictions(self):
        """測試三人，各自有限制"""
        # A 不想在位置 0, B 不想在位置 1, C 無限制
        restrictions = [{0}, {1}, set()]
        result = generate_permutations(3, restrictions)
        # 期望：有多個有效排列（不包含違反限制的）
        self.assertGreater(len(result), 0)
        for perm in result:
            # 檢查 A 不在位置 0
            self.assertNotEqual(perm[0], 'A')
            # 檢查 B 不在位置 1
            self.assertNotEqual(perm[1], 'B')
    
    def test_all_restricted_same_position(self):
        """測試都不想在同一位置（位置 0）"""
        # 三人都不想在位置 0
        restrictions = [{0}, {0}, {0}]
        result = generate_permutations(3, restrictions)
        # 期望：沒有排列（無解）
        self.assertEqual(len(result), 0)
    
    def test_lexicographic_order(self):
        """測試結果是否按字典序"""
        restrictions = [set(), set(), set()]  # 無限制
        result = generate_permutations(3, restrictions)
        # 檢查結果是否按字典序
        sorted_result = sorted([tuple(perm) for perm in result])
        for i in range(len(result) - 1):
            self.assertLessEqual(
                tuple(result[i]), tuple(result[i + 1]),
                f"排列 {result[i]} 應在 {result[i+1]} 之前"
            )


if __name__ == '__main__':
    unittest.main()
