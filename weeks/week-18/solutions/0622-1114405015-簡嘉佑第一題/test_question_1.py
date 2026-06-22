"""
測試用例驗證
根據題目範例進行測試
"""

import sys
sys.path.insert(0, '.')
from question_1_solution import solve_data_cleaning


def test_example_case_1():
    """測試範例第1組：8個數字"""
    n = 8
    numbers = [4, 7, 4, 2, 9, 2, 6, 7]
    d = 2
    
    # 期望輸出：2 4 6
    result = solve_data_cleaning(n, numbers, d)
    assert result == "2 4 6", f"Expected '2 4 6', got '{result}'"
    print("✓ 範例第1組通過")


def test_example_case_2():
    """測試範例第2組：3個奇數"""
    n = 3
    numbers = [1, 3, 5]
    d = 2
    
    # 期望輸出：NONE（都是奇數）
    result = solve_data_cleaning(n, numbers, d)
    assert result == "NONE", f"Expected 'NONE', got '{result}'"
    print("✓ 範例第2組通過")


def test_example_case_3():
    """測試範例第3組：0個數字"""
    n = 0
    numbers = []
    d = 2
    
    # 期望輸出：NONE
    result = solve_data_cleaning(n, numbers, d)
    assert result == "NONE", f"Expected 'NONE', got '{result}'"
    print("✓ 範例第3組通過")


def test_with_duplicates():
    """測試去重功能"""
    n = 5
    numbers = [2, 4, 2, 4, 6]
    d = 2
    
    # 去重後：[2, 4, 6]，排序後：[2, 4, 6]
    result = solve_data_cleaning(n, numbers, d)
    assert result == "2 4 6", f"Expected '2 4 6', got '{result}'"
    print("✓ 去重測試通過")


def test_all_even():
    """測試所有偶數"""
    n = 4
    numbers = [8, 2, 6, 4]
    d = 2
    
    # 期望：2 4 6 8
    result = solve_data_cleaning(n, numbers, d)
    assert result == "2 4 6 8", f"Expected '2 4 6 8', got '{result}'"
    print("✓ 全偶數測試通過")


def test_negative_numbers():
    """測試負數"""
    n = 5
    numbers = [-4, -2, 0, 2, 4]
    d = 2
    
    # 負偶數和正偶數都應該被篩選出來，排序：-4, -2, 0, 2, 4
    result = solve_data_cleaning(n, numbers, d)
    assert result == "-4 -2 0 2 4", f"Expected '-4 -2 0 2 4', got '{result}'"
    print("✓ 負數測試通過")


if __name__ == "__main__":
    print("開始測試第一題解決方案...\n")
    
    test_example_case_1()
    test_example_case_2()
    test_example_case_3()
    test_with_duplicates()
    test_all_even()
    test_negative_numbers()
    
    print("\n✅ 所有測試都通過了！")
