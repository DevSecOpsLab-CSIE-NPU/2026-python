"""
題目 10062 - UVA 10062：乳牛排序問題 - 完整解決方案

=== 問題描述 ===
有 N 頭乳牛，編號 1 到 N。
喝醉的乳牛不按編號順序排隊。
農夫 FJ 記錄了：對於隊伍中的每頭乳牛，在它前面、編號比它小的乳牛有幾頭。
需要根據這份資料重建原始排列。

=== 解題思路 ===
1. 第一個位置的乳牛編號未知，但可以嘗試所有可能性
2. 對於每個後續位置：
   - 根據「前面編號比它小的數量」選擇合適的編號
   - 使用有序列表快速查找滿足條件的編號
3. 使用回溯方式嘗試不同的第一頭乳牛
4. 當某個路徑無法繼續時，回溯並嘗試下一個選擇

=== 時間複雜度 ===
- 最壞情況：O(N! * N^2)（嘗試所有排列組合）
- 一般情況：O(N^2) 到 O(N^3)（取決於輸入）

=== 空間複雜度 ===
- O(N)（存儲結果和中間狀態）
"""

from bisect import insort, bisect_left
from typing import List, Optional


def solve_cow_order(n: int, smaller_counts: List[int]) -> List[int]:
    """
    根據每頭乳牛前面比它小的乳牛數量，重建排列。
    
    關鍵演算法：
      - 嘗試所有可能的第一頭乳牛編號
      - 對於每個首選，逐步構建排列
      - 使用二分搜尋快速判斷是否滿足條件
    
    Args:
        n: 乳牛總數 (2 ≤ N ≤ 80,000)
        smaller_counts: 長度為 n-1 的列表
                       smaller_counts[i] = 第 (i+2) 個位置的乳牛前面
                       編號比它小的乳牛數量
    
    Returns:
        重建後的排列順序（List[int]）
        
    Raises:
        ValueError: 如果無法根據輸入重建排列
    """
    
    def try_build_from_first(first_num: int) -> Optional[List[int]]:
        """
        嘗試以指定編號開始構建排列。
        
        Args:
            first_num: 第一頭乳牛的編號
            
        Returns:
            如果成功返回完整排列，否則返回 None
        """
        result = [first_num]  # 存儲最終排列
        sorted_result = [first_num]  # 存儲已排列乳牛的有序列表
        used = {first_num}  # 記錄已使用的編號
        
        # 依次填充第 2 到第 N 個位置
        for i in range(1, n):
            # 第 i+1 個位置的乳牛前面應有 c 個編號比它小的乳牛
            c = smaller_counts[i - 1]
            
            found = False
            # 嘗試所有未使用的編號
            for num in range(1, n + 1):
                if num not in used:
                    # 使用二分搜尋判斷 num 在有序列表中的排名
                    # bisect_left 返回插入位置，即有多少個數比 num 小
                    count_smaller = bisect_left(sorted_result, num)
                    
                    if count_smaller == c:
                        # 找到滿足條件的編號
                        result.append(num)
                        insort(sorted_result, num)  # 維護有序性
                        used.add(num)
                        found = True
                        break
            
            if not found:
                # 此路不通，返回 None 表示該首選編號不可行
                return None
        
        # 成功構建完整排列
        return result
    
    # 嘗試每個可能的第一個編號
    for first_num in range(1, n + 1):
        result = try_build_from_first(first_num)
        if result is not None:
            return result
    
    # 所有嘗試都失敗，表示輸入不合法
    raise ValueError("無法根據給定條件重建排列，輸入可能不合法")


def verify_solution(n: int, smaller_counts: List[int], 
                   solution: List[int]) -> bool:
    """
    驗證排列是否正確滿足所有約束。
    
    Args:
        n: 乳牛總數
        smaller_counts: 輸入的約束條件
        solution: 提議的排列
        
    Returns:
        True 如果排列正確，否則 False
    """
    # 檢查 1：排列是否包含 1 到 N 的所有編號
    if set(solution) != set(range(1, n + 1)):
        print("✗ 排列不完整或有重複編號")
        return False
    
    # 檢查 2：排列長度是否正確
    if len(solution) != n:
        print(f"✗ 排列長度錯誤：期望 {n}，實際 {len(solution)}")
        return False
    
    # 檢查 3：每個位置的約束是否滿足
    for i in range(1, n):
        expected_smaller = smaller_counts[i - 1]
        actual_smaller = sum(1 for x in solution[:i] if x < solution[i])
        
        if actual_smaller != expected_smaller:
            print(f"✗ 位置 {i+1} 約束不符")
            print(f"  期望前面有 {expected_smaller} 個編號比 {solution[i]} 小")
            print(f"  實際有 {actual_smaller} 個")
            return False
    
    return True


def main():
    """主程式：執行測試並記錄結果"""
    print("=" * 70)
    print("題目 10062 - UVA 10062 乳牛排序問題")
    print("=" * 70)
    print()
    
    # 定義測試案例
    test_cases = [
        (2, [0], "測試1: N=2, [0]"),
        (2, [1], "測試2: N=2, [1]"),
        (3, [0, 0], "測試3: N=3, [0, 0]"),
        (3, [1, 1], "測試4: N=3, [1, 1]"),
        (4, [0, 1, 2], "測試5: N=4, [0, 1, 2]"),
        (5, [0, 1, 2, 3], "測試6: N=5, [0, 1, 2, 3]"),
        (5, [1, 0, 1, 2], "測試7: N=5, [1, 0, 1, 2]"),
    ]
    
    all_passed = True
    results = []
    
    for n, smaller_counts, description in test_cases:
        print(f"{description}")
        try:
            solution = solve_cow_order(n, smaller_counts)
            
            if verify_solution(n, smaller_counts, solution):
                print(f"  ✓ 通過 - 結果: {solution}")
                results.append((description, "PASS", solution))
            else:
                all_passed = False
                results.append((description, "FAIL", solution))
        except Exception as e:
            print(f"  ✗ 異常: {e}")
            all_passed = False
            results.append((description, "ERROR", str(e)))
        print()
    
    # 列印總結
    print("=" * 70)
    print("測試總結")
    print("=" * 70)
    for desc, status, result in results:
        status_icon = "✓" if status == "PASS" else "✗"
        print(f"{status_icon} {desc}: {status}")
        if status == "PASS":
            print(f"  結果: {result}")
    
    print()
    print("=" * 70)
    if all_passed:
        print("✓ 所有測試通過！")
    else:
        print("✗ 有些測試失敗")
    print("=" * 70)
    
    return all_passed


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
