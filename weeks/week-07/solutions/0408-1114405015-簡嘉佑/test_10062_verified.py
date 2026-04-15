"""
UVA 10062 - 乳牛排序問題 完整單元測試
題目: 根據每頭乳牛前面編號比它小的乳牛數量重建排列

=== 解題演算法 ===
核心思想：
1. 使用回溯法嘗試所有可能的第一頭乳牛
2. 對每個選擇，逐步構建完整排列
3. 使用二分搜尋（bisect）快速判斷約束滿足情況

時間複雜度: O(N^2) 到 O(N^3)
空間複雜度: O(N)
"""

import unittest
from bisect import insort, bisect_left
from typing import List, Optional


def solve_cow_order(n: int, smaller_counts: List[int]) -> List[int]:
    """
    根據每頭乳牛前面比它小的乳牛數量，重建排列。
    
    核心演算法：
      - 嘗試每個編號作為第一個位置
      - 對於後續位置，根據「前面編號比它小的數量」選擇合適編號
      - 使用二分搜尋快速定位滿足條件的編號
    
    Parameters:
      n: 乳牛總數
      smaller_counts: 第 i 個元素 = 第 (i+2) 個位置的乳牛前面
                     編號比它小的乳牛數量
    
    Returns:
      重建後的排列（List[int]）
      
    Raises:
      ValueError: 如果輸入不合法無法重建
    """
    
    def try_build(first_num: int) -> Optional[List[int]]:
        """嘗試以 first_num 開始構建排列"""
        result = [first_num]
        sorted_result = [first_num]
        used = {first_num}
        
        for i in range(1, n):
            c = smaller_counts[i - 1]  # 第 i+1 個位置需要的「小於前置編號數」
            
            found = False
            for num in range(1, n + 1):
                if num not in used:
                    # 計算 num 在已排列編號中有多少個比它小
                    count_smaller = bisect_left(sorted_result, num)
                    
                    if count_smaller == c:
                        result.append(num)
                        insort(sorted_result, num)
                        used.add(num)
                        found = True
                        break
            
            if not found:
                return None  # 此路不通
        
        return result
    
    # 嘗試每個可能的第一個位置
    for first_num in range(1, n + 1):
        result = try_build(first_num)
        if result is not None:
            return result
    
    raise ValueError("無法根據輸入重建排列")


def verify_solution(n: int, smaller_counts: List[int], 
                   solution: List[int]) -> bool:
    """驗證排列是否滿足所有約束"""
    # 檢查排列完整性
    if sorted(solution) != list(range(1, n + 1)):
        return False
    
    # 檢查每個位置的約束
    for i in range(1, n):
        expected = smaller_counts[i - 1]
        actual = sum(1 for x in solution[:i] if x < solution[i])
        if actual != expected:
            return False
    
    return True


class TestCowOrder(unittest.TestCase):
    """UVA 10062 乳牛排序測試套件"""
    
    def test_n2_descending(self):
        """測試: N=2, 降序排列"""
        # [2, 1]: 位置2(值1)前面0個比1小的編號
        result = solve_cow_order(2, [0])
        self.assertEqual(sorted(result), [1, 2])
        self.assertTrue(verify_solution(2, [0], result))
    
    def test_n2_ascending(self):
        """測試: N=2, 升序排列"""
        # [1, 2]: 位置2(值2)前面1個比2小的編號(即1)
        result = solve_cow_order(2, [1])
        self.assertEqual(sorted(result), [1, 2])
        self.assertTrue(verify_solution(2, [1], result))
    
    def test_n3_mixed1(self):
        """測試: N=3, 混合排列"""
        # [2, 1, 3]: 位置2(值1)前面0個, 位置3(值3)前面2個
        result = solve_cow_order(3, [0, 2])
        self.assertEqual(sorted(result), [1, 2, 3])
        self.assertTrue(verify_solution(3, [0, 2], result))
    
    def test_n3_mixed2(self):
        """測試: N=3, 另一個混合排列"""
        # [3, 1, 2]: 位置2(值1)前面0個, 位置3(值2)前面1個
        result = solve_cow_order(3, [0, 1])
        self.assertEqual(sorted(result), [1, 2, 3])
        self.assertTrue(verify_solution(3, [0, 1], result))
    
    def test_n4_complex(self):
        """測試: N=4, 複雜排列"""
        # [4, 1, 2, 3]: 位置2前0個, 位置3前1個, 位置4前2個
        result = solve_cow_order(4, [0, 1, 2])
        self.assertEqual(sorted(result), [1, 2, 3, 4])
        self.assertTrue(verify_solution(4, [0, 1, 2], result))
    
    def test_n5_sequence(self):
        """測試: N=5, 遞增序列"""
        # 完全升序排列的約束
        result = solve_cow_order(5, [1, 2, 3, 4])
        self.assertEqual(sorted(result), [1, 2, 3, 4, 5])
        self.assertTrue(verify_solution(5, [1, 2, 3, 4], result))
    
    def test_invalid_input(self):
        """測試: 無效輸入應拋出異常"""
        # 無法構成合法排列的輸入
        try:
            # [3, 2, 1] 無法產生約束 [0, 0]
            # 因為位置3的值1前面會有2個比1小的編號（但1是最小值）
            solve_cow_order(3, [0, 0])
            self.fail("Should have raised ValueError")
        except ValueError:
            pass  # 期望的異常


class TestAlgorithmProperties(unittest.TestCase):
    """測試演算法的性質和邊界情況"""
    
    def test_permutation_completeness(self):
        """驗證結果是否為完整排列"""
        for n in range(2, 6):
            for num in range(1, n):
                result = solve_cow_order(n, [0] * (n - 1))
                self.assertEqual(len(result), n)
                self.assertEqual(set(result), set(range(1, n + 1)))
    
    def test_ascending_order(self):
        """驗證完全升序情況"""
        result = solve_cow_order(4, [1, 2, 3])
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_constraint_satisfaction(self):
        """驗證所有約束都被滿足"""
        test_cases = [
            (3, [0, 1]),
            (3, [0, 2]),
            (4, [0, 1, 2]),
            (4, [1, 1, 1]),
        ]
        
        for n, counts in test_cases:
            result = solve_cow_order(n, counts)
            
            # 檢查每個位置
            for i in range(1, n):
                expected = counts[i - 1]
                actual = sum(1 for x in result[:i] if x < result[i])
                self.assertEqual(actual, expected,
                               f"Position {i+1} in {result}: expected {expected}, got {actual}")


def run_tests():
    """執行所有測試"""
    print("\n" + "=" * 70)
    print("UVA 10062 - 乳牛排序問題 單元測試")
    print("=" * 70 + "\n")
    
    # 建立測試套件
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 加入所有測試
    suite.addTests(loader.loadTestsFromTestCase(TestCowOrder))
    suite.addTests(loader.loadTestsFromTestCase(TestAlgorithmProperties))
    
    # 執行測試
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 列印總結
    print("\n" + "=" * 70)
    print(f"測試完成: {result.testsRun} 個測試")
    if result.wasSuccessful():
        print("✓ 所有測試通過！")
    else:
        print(f"✗ 失敗: {len(result.failures)} 個, 錯誤: {len(result.errors)} 個")
    print("=" * 70 + "\n")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    import sys
    success = run_tests()
    sys.exit(0 if success else 1)
