"""
測試案例：資料清理（Data Cleaning）- 第一題
根據題目要求進行紅燈測試
"""

import io
import sys
from contextlib import redirect_stdout


def test_case_1_basic_with_duplicates_and_mixed_numbers():
    """
    Test Case 1: 基本情況 - 有重複、有偶數、有奇數
    輸入：8
         4 7 4 2 9 2 6 7
    預期輸出：2 4 6
    
    步驟：
    - 原始數列：4 7 4 2 9 2 6 7
    - 去除重複：4 7 2 9 6 (保留第一次出現順序)
    - 篩選被2整除：4 2 6
    - 排序：2 4 6
    """
    input_data = """8
4 7 4 2 9 2 6 7
0
"""
    expected_output = "2 4 6"
    
    # 模擬輸入和執行
    sys.stdin = io.StringIO(input_data)
    output = io.StringIO()
    sys.stdout = output
    
    # TODO: 執行 data_cleaning 主程序
    
    sys.stdout = sys.__stdout__
    result = output.getvalue().strip().split('\n')[0]
    
    assert result == expected_output, f"Test 1 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 1 通過：基本情況（重複、混合數字）")


def test_case_2_all_odd_numbers():
    """
    Test Case 2: 邊界情況 - 全是奇數
    輸入：3
         1 3 5
    預期輸出：NONE
    
    步驟：
    - 原始數列：1 3 5
    - 去除重複：1 3 5 (沒有重複)
    - 篩選被2整除：(空)
    - 結果：NONE
    """
    input_data = """3
1 3 5
0
"""
    expected_output = "NONE"
    
    # 模擬輸入和執行
    sys.stdin = io.StringIO(input_data)
    output = io.StringIO()
    sys.stdout = output
    
    # TODO: 執行 data_cleaning 主程序
    
    sys.stdout = sys.__stdout__
    result = output.getvalue().strip().split('\n')[0]
    
    assert result == expected_output, f"Test 2 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 2 通過：邊界情況（全奇數）")


def test_case_3_single_even_element():
    """
    Test Case 3: 邊界情況 - 單個偶數元素
    輸入：1
         4
    預期輸出：4
    
    步驟：
    - 原始數列：4
    - 去除重複：4
    - 篩選被2整除：4
    - 排序：4
    """
    input_data = """1
4
0
"""
    expected_output = "4"
    
    # 模擬輸入和執行
    sys.stdin = io.StringIO(input_data)
    output = io.StringIO()
    sys.stdout = output
    
    # TODO: 執行 data_cleaning 主程序
    
    sys.stdout = sys.__stdout__
    result = output.getvalue().strip().split('\n')[0]
    
    assert result == expected_output, f"Test 3 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 3 通過：邊界情況（單個偶數）")


def test_case_4_all_even_numbers_with_duplicates():
    """
    Test Case 4: 邊界情況 - 全是偶數且有重複
    輸入：5
         2 4 2 6 4
    預期輸出：2 4 6
    
    步驟：
    - 原始數列：2 4 2 6 4
    - 去除重複：2 4 6 (保留第一次出現順序)
    - 篩選被2整除：2 4 6
    - 排序：2 4 6
    """
    input_data = """5
2 4 2 6 4
0
"""
    expected_output = "2 4 6"
    
    # 模擬輸入和執行
    sys.stdin = io.StringIO(input_data)
    output = io.StringIO()
    sys.stdout = output
    
    # TODO: 執行 data_cleaning 主程序
    
    sys.stdout = sys.__stdout__
    result = output.getvalue().strip().split('\n')[0]
    
    assert result == expected_output, f"Test 4 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 4 通過：邊界情況（全偶數有重複）")


def test_case_5_negative_even_numbers():
    """
    Test Case 5: 邊界情況 - 負偶數
    輸入：5
         -4 -2 -4 3 -2
    預期輸出：-4 -2
    
    步驟：
    - 原始數列：-4 -2 -4 3 -2
    - 去除重複：-4 -2 3 (保留第一次出現順序)
    - 篩選被2整除：-4 -2
    - 排序：-4 -2
    """
    input_data = """5
-4 -2 -4 3 -2
0
"""
    expected_output = "-4 -2"
    
    # 模擬輸入和執行
    sys.stdin = io.StringIO(input_data)
    output = io.StringIO()
    sys.stdout = output
    
    # TODO: 執行 data_cleaning 主程序
    
    sys.stdout = sys.__stdout__
    result = output.getvalue().strip().split('\n')[0]
    
    assert result == expected_output, f"Test 5 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 5 通過：邊界情況（負偶數）")


def test_case_6_multiple_test_groups():
    """
    Test Case 6: 多組測資
    輸入：
         8
         4 7 4 2 9 2 6 7
         3
         1 3 5
         5
         2 4 2 6 4
         0
    預期輸出：
         2 4 6
         NONE
         2 4 6
    """
    input_data = """8
4 7 4 2 9 2 6 7
3
1 3 5
5
2 4 2 6 4
0
"""
    expected_outputs = ["2 4 6", "NONE", "2 4 6"]
    
    # 模擬輸入和執行
    sys.stdin = io.StringIO(input_data)
    output = io.StringIO()
    sys.stdout = output
    
    # TODO: 執行 data_cleaning 主程序
    
    sys.stdout = sys.__stdout__
    results = output.getvalue().strip().split('\n')
    
    for i, expected in enumerate(expected_outputs):
        assert results[i] == expected, f"Test 6 第{i+1}組失敗: 期望 '{expected}'，得到 '{results[i]}'"
    
    print("✓ Test Case 6 通過：多組測資")


if __name__ == "__main__":
    print("=" * 60)
    print("開始執行紅燈測試（Red Light Tests）")
    print("=" * 60)
    
    tests = [
        test_case_1_basic_with_duplicates_and_mixed_numbers,
        test_case_2_all_odd_numbers,
        test_case_3_single_even_element,
        test_case_4_all_even_numbers_with_duplicates,
        test_case_5_negative_even_numbers,
        test_case_6_multiple_test_groups,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test_func.__name__} 失敗：{e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__} 錯誤：{e}")
            failed += 1
    
    print("=" * 60)
    print(f"測試結果：通過 {passed} 個，失敗 {failed} 個")
    print("=" * 60)
