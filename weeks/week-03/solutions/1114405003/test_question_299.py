"""
題目 299 - 火車車廂置換 測試程式

此測試模組驗證火車車廂置換解決方案的正確性。
包含基本測試案例、邊界案例和進階案例。
"""

import sys
import os

# 添加父目錄到路徑，以便導入 solution 模組
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution_question_299 import TrainSwapper, solve_train_swapping


def test_basic_case():
    """測試基本案例：簡單的三元素排列"""
    print("測試 1: 基本案例 [2, 3, 1]")
    
    swapper = TrainSwapper()
    cars = [2, 3, 1]
    result = swapper.count_swaps(cars)
    expected = 2
    
    print(f"  輸入: {cars}")
    print(f"  預期: {expected} swaps")
    print(f"  實際: {result} swaps")
    
    assert result == expected, f"測試失敗：期望 {expected}，得到 {result}"
    print("  ✓ 通過\n")


def test_sorted_case():
    """測試已排序的案例"""
    print("測試 2: 已排序案例 [1, 2, 3]")
    
    swapper = TrainSwapper()
    cars = [1, 2, 3]
    result = swapper.count_swaps(cars)
    expected = 0
    
    print(f"  輸入: {cars}")
    print(f"  預期: {expected} swaps")
    print(f"  實際: {result} swaps")
    
    assert result == expected, f"測試失敗：期望 {expected}，得到 {result}"
    print("  ✓ 通過\n")


def test_reverse_case():
    """測試完全反向的案例"""
    print("測試 3: 完全反向案例 [3, 2, 1]")
    
    swapper = TrainSwapper()
    cars = [3, 2, 1]
    result = swapper.count_swaps(cars)
    expected = 3  # (3,2)->3, (3,1)->3, (2,1)->1 = 3 total
    
    print(f"  輸入: {cars}")
    print(f"  預期: {expected} swaps")
    print(f"  實際: {result} swaps")
    
    assert result == expected, f"測試失敗：期望 {expected}，得到 {result}"
    print("  ✓ 通過\n")


def test_single_element():
    """測試單個元素"""
    print("測試 4: 單個元素 [1]")
    
    swapper = TrainSwapper()
    cars = [1]
    result = swapper.count_swaps(cars)
    expected = 0
    
    print(f"  輸入: {cars}")
    print(f"  預期: {expected} swaps")
    print(f"  實際: {result} swaps")
    
    assert result == expected, f"測試失敗：期望 {expected}，得到 {result}"
    print("  ✓ 通過\n")


def test_two_elements_unsorted():
    """測試兩個元素，未排序"""
    print("測試 5: 兩個未排序元素 [2, 1]")
    
    swapper = TrainSwapper()
    cars = [2, 1]
    result = swapper.count_swaps(cars)
    expected = 1
    
    print(f"  輸入: {cars}")
    print(f"  預期: {expected} swaps")
    print(f"  實際: {result} swaps")
    
    assert result == expected, f"測試失敗：期望 {expected}，得到 {result}"
    print("  ✓ 通過\n")


def test_larger_case():
    """測試較大的案例"""
    print("測試 6: 較大案例 [4, 2, 1, 3]")
    
    swapper = TrainSwapper()
    cars = [4, 2, 1, 3]
    result = swapper.count_swaps(cars)
    # 計算：4203 -> 2043 -> 2034 -> 2304 -> 2314 -> 1234 = 5 swaps
    expected = 5
    
    print(f"  輸入: {cars}")
    print(f"  預期: {expected} swaps")
    print(f"  實際: {result} swaps")
    
    assert result == expected, f"測試失敗：期望 {expected}，得到 {result}"
    print("  ✓ 通過\n")


def test_process_input():
    """測試完整的輸入處理"""
    print("測試 7: 完整輸入處理")
    
    input_text = """2
3
2 3 1
4
4 2 1 3"""
    
    output = solve_train_swapping(input_text)
    expected_lines = [
        "Optimal train swapping takes 2 swaps.",
        "Optimal train swapping takes 5 swaps."
    ]
    
    output_lines = output.strip().split('\n')
    
    print(f"  輸入:\n{input_text}\n")
    print(f"  預期輸出:")
    for line in expected_lines:
        print(f"    {line}")
    print(f"\n  實際輸出:")
    for line in output_lines:
        print(f"    {line}")
    
    for i, (actual, expected) in enumerate(zip(output_lines, expected_lines)):
        assert actual == expected, f"第 {i+1} 行不匹配"
    
    print("\n  ✓ 通過\n")


def test_zero_length():
    """測試長度為 0 的情況"""
    print("測試 8: 長度為 0 的情況")
    
    input_text = """1
0"""
    
    output = solve_train_swapping(input_text)
    expected = "Optimal train swapping takes 0 swaps."
    
    print(f"  輸入: 長度 0")
    print(f"  預期: {expected}")
    print(f"  實際: {output}")
    
    assert output.strip() == expected, f"測試失敗"
    print("  ✓ 通過\n")


def run_all_tests():
    """執行所有測試"""
    print("=" * 50)
    print("題目 299 - 火車車廂置換 測試套件")
    print("=" * 50 + "\n")
    
    test_functions = [
        test_basic_case,
        test_sorted_case,
        test_reverse_case,
        test_single_element,
        test_two_elements_unsorted,
        test_larger_case,
        test_process_input,
        test_zero_length,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in test_functions:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ 失敗: {e}\n")
            failed += 1
        except Exception as e:
            print(f"  ✗ 錯誤: {e}\n")
            failed += 1
    
    print("=" * 50)
    print(f"測試結果: {passed} 通過, {failed} 失敗")
    print("=" * 50)
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
