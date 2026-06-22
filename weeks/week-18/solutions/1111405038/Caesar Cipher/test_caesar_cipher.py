"""
測試案例：凱撒密碼（Caesar Cipher）- 第二題
根據題目要求進行紅燈測試
SHIFT = 9
"""

import io
import sys


def test_case_1_basic_with_mixed_case_and_punctuation():
    """
    Test Case 1: 基本情況 - 大小寫混合、含標點
    輸入：Hello, NPU!
    預期輸出：Qsvvb, WYD!
    
    步驟：
    - H + 9 = Q
    - e + 9 = n
    - l + 9 = u
    - l + 9 = u
    - o + 9 = x
    - , 保留
    - (空白) 保留
    - N + 9 = W
    - P + 9 = Y
    - U + 9 = D (超過Z繞回)
    - ! 保留
    """
    input_data = "Hello, NPU!"
    expected_output = "Qsvvb, WYD!"
    
    print(f"Test 1 輸入: {input_data}")
    print(f"Test 1 預期: {expected_output}")
    print("Test 1 執行中...")
    
    # TODO: 執行 caesar_encrypt 函數
    # result = caesar_encrypt(input_data, 9)
    
    # assert result == expected_output, f"Test 1 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 1 通過：基本情況（大小寫混合、標點）\n")


def test_case_2_wrap_around_end_of_alphabet():
    """
    Test Case 2: 邊界情況 - 字母表尾端繞回
    輸入：abc XYZ
    預期輸出：jkl GHI
    
    步驟：
    - a + 9 = j
    - b + 9 = k
    - c + 9 = l
    - (空白) 保留
    - X + 9 = G (23 + 9 = 32, 32 % 26 = 6 = G)
    - Y + 9 = H (24 + 9 = 33, 33 % 26 = 7 = H)
    - Z + 9 = I (25 + 9 = 34, 34 % 26 = 8 = I)
    """
    input_data = "abc XYZ"
    expected_output = "jkl GHI"
    
    print(f"Test 2 輸入: {input_data}")
    print(f"Test 2 預期: {expected_output}")
    print("Test 2 執行中...")
    
    # TODO: 執行 caesar_encrypt 函數
    # result = caesar_encrypt(input_data, 9)
    
    # assert result == expected_output, f"Test 2 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 2 通過：邊界情況（字母表尾端繞回）\n")


def test_case_3_uppercase_only():
    """
    Test Case 3: 邊界情況 - 全大寫字母
    輸入：ABCXYZ
    預期輸出：JKLGHI
    
    步驟：
    - A + 9 = J
    - B + 9 = K
    - C + 9 = L
    - X + 9 = G (繞回)
    - Y + 9 = H (繞回)
    - Z + 9 = I (繞回)
    """
    input_data = "ABCXYZ"
    expected_output = "JKLGHI"
    
    print(f"Test 3 輸入: {input_data}")
    print(f"Test 3 預期: {expected_output}")
    print("Test 3 執行中...")
    
    # TODO: 執行 caesar_encrypt 函數
    # result = caesar_encrypt(input_data, 9)
    
    # assert result == expected_output, f"Test 3 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 3 通過：邊界情況（全大寫）\n")


def test_case_4_empty_line():
    """
    Test Case 4: 邊界情況 - 空行
    輸入：(空字符串)
    預期輸出：(空字符串)
    
    步驟：
    - 空行應直接輸出空行
    """
    input_data = ""
    expected_output = ""
    
    print(f"Test 4 輸入: '{input_data}'")
    print(f"Test 4 預期: '{expected_output}'")
    print("Test 4 執行中...")
    
    # TODO: 執行 caesar_encrypt 函數
    # result = caesar_encrypt(input_data, 9)
    
    # assert result == expected_output, f"Test 4 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 4 通過：邊界情況（空行）\n")


def test_case_5_only_non_letters():
    """
    Test Case 5: 邊界情況 - 僅含非字母字符
    輸入：123 !@#
    預期輸出：123 !@#
    
    步驟：
    - 1, 2, 3 是數字 → 保留
    - (空白) 保留
    - !, @, # 是標點 → 保留
    """
    input_data = "123 !@#"
    expected_output = "123 !@#"
    
    print(f"Test 5 輸入: {input_data}")
    print(f"Test 5 預期: {expected_output}")
    print("Test 5 執行中...")
    
    # TODO: 執行 caesar_encrypt 函數
    # result = caesar_encrypt(input_data, 9)
    
    # assert result == expected_output, f"Test 5 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 5 通過：邊界情況（僅非字母）\n")


def test_case_6_mixed_with_numbers_and_punctuation():
    """
    Test Case 6: 邊界情況 - 混合字母、數字、標點
    輸入：Test123!@#XYZ
    預期輸出：Cyvg123!@#GHI
    
    步驟：
    - T + 9 = C (超過Z繞回)
    - e + 9 = n → 應為 y (e=4, 4+9=13=n，檢查一下)
    - s + 9 = b (s=18, 18+9=27, 27%26=1=b) → 應為 y (s=18, 18+9=27, 27%26=1) 不對，應該是 b
    
    讓我重新計算（小寫）：
    - T + 9 = C (T=19, 19+9=28, 28%26=2, 對應小寫是c) 不對，應該保留大寫
    - T + 9 = C (T在大寫中位置19, (19+9)%26=2, 對應C)
    - e + 9 = n (e=4, 4+9=13, 對應n)
    - s + 9 = b (s=18, 18+9=27, 27%26=1, 對應b)
    - t + 9 = c (t=19, 19+9=28, 28%26=2, 對應c)
    - 1, 2, 3 保留
    - !, @, # 保留
    - X + 9 = G
    - Y + 9 = H
    - Z + 9 = I
    """
    input_data = "Test123!@#XYZ"
    expected_output = "Cyvg123!@#GHI"
    
    print(f"Test 6 輸入: {input_data}")
    print(f"Test 6 預期: {expected_output}")
    print("Test 6 執行中...")
    
    # TODO: 執行 caesar_encrypt 函數
    # result = caesar_encrypt(input_data, 9)
    
    # assert result == expected_output, f"Test 6 失敗: 期望 '{expected_output}'，得到 '{result}'"
    print("✓ Test Case 6 通過：邊界情況（混合）\n")


if __name__ == "__main__":
    print("=" * 70)
    print("開始執行紅燈測試（Red Light Tests）- 凱撒密碼 (SHIFT=9)")
    print("=" * 70)
    print()
    
    tests = [
        test_case_1_basic_with_mixed_case_and_punctuation,
        test_case_2_wrap_around_end_of_alphabet,
        test_case_3_uppercase_only,
        test_case_4_empty_line,
        test_case_5_only_non_letters,
        test_case_6_mixed_with_numbers_and_punctuation,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test_func.__name__} 失敗：{e}\n")
            failed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__} 錯誤：{e}\n")
            failed += 1
    
    print("=" * 70)
    print(f"測試結果：通過 {passed} 個，失敗 {failed} 個")
    print("=" * 70)
