"""
簡化的測試驗證腳本
直接運行測試邏輯
"""

from typing import List
from bisect import insort, bisect_left


def solve_cow_order(n: int, smaller_counts: List[int]) -> List[int]:
    """解決乳牛排序問題"""
    result = []
    sorted_result = []
    used = set()
    
    # 處理第一頭乳牛
    result.append(1)
    sorted_result.append(1)
    used.add(1)
    
    # 處理後續的乳牛
    for i in range(1, n):
        c = smaller_counts[i - 1]
        
        # 從未使用的編號中找出合適的編號
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
            raise ValueError(f"無法為位置 {i+1} 找到合適的乳牛編號")
    
    return result


def verify_result(n: int, smaller_counts: List[int], result: List[int]) -> bool:
    """驗證結果是否正確"""
    # 檢查排列完整性
    if set(result) != set(range(1, n + 1)):
        print(f"✗ 排列不完整或有重複")
        return False
    
    # 檢查約束條件
    for i in range(1, n):
        expected = smaller_counts[i - 1]
        actual = sum(1 for x in result[:i] if x < result[i])
        if actual != expected:
            print(f"✗ 位置 {i+1} 約束不符: 期望 {expected}, 實際 {actual}")
            return False
    
    return True


def main():
    """主測試函式"""
    print("=" * 70)
    print("題目 10062 - UVA 10062 乳牛排序問題 - 測試執行")
    print("=" * 70)
    print()
    
    test_cases = [
        (2, [0], "測試1: N=2, 第二頭前面有 0 個比它小的"),
        (2, [1], "測試2: N=2, 第二頭前面有 1 個比它小的"),
        (3, [0, 0], "測試3: N=3, 都是 0"),
        (3, [1, 1], "測試4: N=3, 都是 1"),
        (4, [0, 1, 2], "測試5: N=4, 遞增序列"),
    ]
    
    all_passed = True
    for n, smaller_counts, description in test_cases:
        print(f"{description}")
        try:
            result = solve_cow_order(n, smaller_counts)
            if verify_result(n, smaller_counts, result):
                print(f"  ✓ 通過 - 結果: {result}")
            else:
                all_passed = False
                print(f"  ✗ 失敗")
        except Exception as e:
            print(f"  ✗ 異常: {e}")
            all_passed = False
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
