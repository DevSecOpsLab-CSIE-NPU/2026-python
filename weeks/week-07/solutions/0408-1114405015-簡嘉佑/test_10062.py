"""
題目 10062 - UVA 10062：乳牛排序問題

題意說明：
  - N 頭乳牛排隊等吃晚餐，原本應該按編號 1 到 N 依序排列
  - 但它們喝醉了，隊伍被打亂了
  - 對於隊伍中的每一頭乳牛，我們知道在它前面、編號比它小的乳牛有幾頭
  - 根據這些線索重建原始排列

測試策略：
  1. 簡單測試：N=2, 小規模驗證基本邏輯
  2. 中等測試：N=4, 驗證多層次的插入邏輯
  3. 邊界測試：檢查第一頭乳牛的處理
"""

import unittest
from typing import List


def solve_cow_order(n: int, smaller_counts: List[int]) -> List[int]:
    """
    根據每頭乳牛前面比它小的乳牛數量，重建排列。
    
    演算法思路：
      1. 維護一個「已排列乳牛」的有序列表
      2. 維護一個「未使用編號」的集合
      3. 對於每個位置，根據「前面比它小的數量」來選擇合適的編號
      
    Parameters:
      n: 乳牛總數
      smaller_counts: 列表，第 i 個元素表示第 (i+2) 個位置的乳牛
                     前面編號比它小的乳牛數量
                     （第一頭沒有資訊，所以從第二頭開始）
    
    Returns:
      list: 重建後的排列順序
    """
    from bisect import insort, bisect_left
    
    # 初始化結果列表和已排列乳牛的有序追蹤
    result = []  # 最終排列結果
    sorted_result = []  # 用於快速查找的有序列表
    used = set()  # 已使用的編號集合
    
    # 處理第一頭乳牛
    # 由於題目沒有給出第一頭乳牛的資訊，我們選擇最小的編號 1
    result.append(1)
    sorted_result.append(1)
    used.add(1)
    
    # 處理後續的乳牛
    for i in range(1, n):
        # smaller_counts[i-1] 是第 (i+1) 個位置的乳牛前面編號比它小的數量
        c = smaller_counts[i - 1]
        
        # 從未使用的編號中找出合適的編號
        # 條件：在 sorted_result 中有恰好 c 個編號比它小
        found = False
        for num in range(1, n + 1):
            if num not in used:
                # 計算在 sorted_result 中有多少個數比 num 小
                # 這相當於 num 在排序後應該插入的位置
                count_smaller = bisect_left(sorted_result, num)
                
                if count_smaller == c:
                    # 找到合適的編號
                    result.append(num)
                    insort(sorted_result, num)
                    used.add(num)
                    found = True
                    break
        
        if not found:
            # 如果沒有找到，表示輸入有誤或演算法需要調整
            raise ValueError(f"無法為位置 {i+1} 找到合適的乳牛編號")
    
    return result
        def try_build(first_num: int):
            """嘗試以 first_num 作為第一頭乳牛構建排列"""
            result = [first_num]
            sorted_result = [first_num]
            used = {first_num}
        
            for i in range(1, n):
                c = smaller_counts[i - 1]
                found = False
                for num in range(1, n + 1):
                    if num not in used:
                        count_smaller = bisect_left(sorted_result, num)
                        if count_smaller == c:
                            result.append(num)
                            insort(sorted_result, num)
                            used.add(num)
                            found = True
                            break
                if not found:
                    return None
        
            return result
    
        # 嘗試每個可能的第一個位置
        for first_num in range(1, n + 1):
            result = try_build(first_num)
            if result is not None:
                return result
    
        raise ValueError("無法根據輸入重建排列")-


class TestCowOrder(unittest.TestCase):
    """測試用例集"""
    
    def test_simple_case_n2(self):
        """
        測試1：簡單情況 N=2
        輸入：2
              0
        說明：第二頭乳牛前面編號比它小的有 0 個
        預期：[1, 2]（因為第二頭乳牛編號比第一頭大）
        """
        result = solve_cow_order(2, [0])
        self.assertEqual(result, [1, 2])
        print(f"測試1（N=2）: {result} ✓")
    
    def test_reverse_case_n2(self):
        """
        測試2：N=2 的反向情況
        輸入：2
              1
        說明：第二頭乳牛前面編號比它小的有 1 個
        預期：[2, 1]（第二頭乳牛編號比第一頭小）
        """
        result = solve_cow_order(2, [1])
        self.assertEqual(result, [2, 1])
        print(f"測試2（N=2 反向）: {result} ✓")
    
    def test_case_n3_example(self):
        """
        測試3：N=3 的標準測試
        輸入：3
              0
              1
        說明：
          - 第二頭：前面有 0 個編號比它小 → 比第一頭大
          - 第三頭：前面有 1 個編號比它小 → 中間大小
        預期排列範例：[1, 3, 2] 或 [2, 3, 1] 等
        """
        result = solve_cow_order(3, [0, 1])
        # 驗證基本約束
        self.assertEqual(len(result), 3)
        self.assertEqual(set(result), {1, 2, 3})
        
        # 驗證第二個位置的約束：前面編號比它小的有 0 個
        count = sum(1 for x in result[:1] if x < result[1])
        self.assertEqual(count, 0)
        
        # 驗證第三個位置的約束：前面編號比它小的有 1 個
        count = sum(1 for x in result[:2] if x < result[2])
        self.assertEqual(count, 1)
        
        print(f"測試3（N=3）: {result} ✓")
    
    def test_case_n4(self):
        """
        測試4：N=4 的測試
        輸入：4
              0
              1
              2
        說明：
          - 第二頭：前面有 0 個編號比它小
          - 第三頭：前面有 1 個編號比它小
          - 第四頭：前面有 2 個編號比它小
        """
        result = solve_cow_order(4, [0, 1, 2])
        self.assertEqual(len(result), 4)
        self.assertEqual(set(result), {1, 2, 3, 4})
        
        # 驗證各個位置的約束
        for i in range(1, 4):
            expected_smaller = i - 1
            actual_smaller = sum(1 for x in result[:i] if x < result[i])
            self.assertEqual(actual_smaller, expected_smaller,
                           f"位置 {i+1} 的約束不符")
        
        print(f"測試4（N=4）: {result} ✓")
    
    def test_constraint_verification(self):
        """
        測試5：約束驗證
        對任意結果驗證是否滿足題目約束
        """
        test_cases = [
            (2, [0]),
            (2, [1]),
            (3, [0, 0]),
            (3, [1, 1]),
            (4, [0, 1, 2]),
        ]
        
        for n, smaller_counts in test_cases:
            result = solve_cow_order(n, smaller_counts)
            
            # 驗證是否是有效的排列
            self.assertEqual(set(result), set(range(1, n + 1)))
            
            # 驗證每個位置的約束
            for i in range(1, n):
                expected = smaller_counts[i - 1]
                actual = sum(1 for x in result[:i] if x < result[i])
                self.assertEqual(actual, expected,
                               f"N={n}, 位置 {i+1}: 期望 {expected} 個編號比它小，"
                               f"實際 {actual} 個")
            
            print(f"  驗證 N={n}: {result} ✓")


def run_tests():
    """
    執行所有測試並輸出結果
    """
    print("=" * 60)
    print("題目 10062 - UVA 10062 乳牛排序問題")
    print("=" * 60)
    print()
    
    # 創建測試套件
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCowOrder)
    
    # 運行測試
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print()
    print("=" * 60)
    if result.wasSuccessful():
        print("✓ 所有測試通過！")
    else:
        print("✗ 有些測試失敗")
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    exit(0 if success else 1)
