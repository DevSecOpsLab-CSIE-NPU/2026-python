"""
題目 490 - 旋轉文字 測試程式

此測試模組驗證旋轉文字解決方案的正確性。
包含基本測試案例、邊界案例和進階案例。
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution_question_490 import SentenceRotator, solve_rotating_sentence


def test_basic_rotation():
    """測試基本旋轉案例"""
    print("Test 1: Basic rotation")

    rotator = SentenceRotator()
    lines = ["HELLO", "WORLD"]
    result = rotator.rotate_text(lines)
    expected = ["WH", "OE", "RL", "LL", "DO"]

    print(f"  Input: {lines}")
    print(f"  Expected: {expected}")
    print(f"  Actual: {result}")

    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("  PASS\n")


def test_single_line():
    """測試單行輸入"""
    print("Test 2: Single line")

    rotator = SentenceRotator()
    lines = ["ABC"]
    result = rotator.rotate_text(lines)
    expected = ["A", "B", "C"]

    print(f"  Input: {lines}")
    print(f"  Expected: {expected}")
    print(f"  Actual: {result}")

    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("  PASS\n")


def test_equal_length_lines():
    """測試等長行的旋轉"""
    print("Test 3: Equal length lines [ABC, DEF, GHI]")

    rotator = SentenceRotator()
    lines = ["ABC", "DEF", "GHI"]
    result = rotator.rotate_text(lines)
    expected = ["GDA", "HEB", "IFC"]

    print(f"  Input: {lines}")
    print(f"  Expected: {expected}")
    print(f"  Actual: {result}")

    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("  PASS\n")


def test_different_length_lines():
    """測試不同長度的行"""
    print("Test 4: Different length lines")

    rotator = SentenceRotator()
    lines = ["AB", "CDEF", "GHIJ"]
    result = rotator.rotate_text(lines)
    expected = ["GCA", "HDB", "IE ", "JF "]

    print(f"  Input: {lines}")
    print(f"  Expected: {expected}")
    print(f"  Actual: {result}")

    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("  PASS\n")


def test_empty_lines():
    """測試空行"""
    print("Test 5: Empty lines")

    rotator = SentenceRotator()
    lines = ["", ""]
    result = rotator.rotate_text(lines)
    expected = []

    print(f"  Input: empty lines")
    print(f"  Expected: {expected}")
    print(f"  Actual: {result}")

    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("  PASS\n")


def test_single_char():
    """測試單個字符"""
    print("Test 6: Single char")

    rotator = SentenceRotator()
    lines = ["X"]
    result = rotator.rotate_text(lines)
    expected = ["X"]

    print(f"  Input: {lines}")
    print(f"  Expected: {expected}")
    print(f"  Actual: {result}")

    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("  PASS\n")


def test_longer_matrix():
    """測試較大的矩陣"""
    print("Test 7: Longer matrix")

    rotator = SentenceRotator()
    lines = ["ONE", "TWO", "THREE", "FOUR", "FIVE"]
    result = rotator.rotate_text(lines)
    expected = ["FFTTO", "IOHWN", "VUROE", "ERE  ", "  E  "]

    print(f"  Input: {lines}")
    print(f"  Expected: {expected}")
    print(f"  Actual: {result}")

    assert result == expected, f"Test failed: expected {expected}, got {result}"
    print("  PASS\n")


def test_process_input():
    """測試完整的輸入處理"""
    print("Test 8: Full input processing")

    input_text = """HELLO
WORLD"""
    output = solve_rotating_sentence(input_text)
    expected = "WH\nOE\nRL\nLL\nDO"

    print(f"  Input:\n{input_text}")
    print(f"  Expected:\n{expected}")
    print(f"  Actual:\n{output}")

    assert output == expected, f"Test failed"
    print("  PASS\n")


def run_all_tests():
    """執行所有測試"""
    print("=" * 50)
    print("Question 490 - Rotating Text Test Suite")
    print("=" * 50 + "\n")

    test_functions = [
        test_basic_rotation,
        test_single_line,
        test_equal_length_lines,
        test_different_length_lines,
        test_empty_lines,
        test_single_char,
        test_longer_matrix,
        test_process_input,
    ]

    passed = 0
    failed = 0

    for test_func in test_functions:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"  FAIL: {e}\n")
            failed += 1
        except Exception as e:
            print(f"  ERROR: {e}\n")
            failed += 1

    print("=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 50)

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
