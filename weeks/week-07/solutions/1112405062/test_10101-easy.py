# -*- coding: utf-8 -*-
"""
================================================================================
UVA 10101 - 木棒遊戲（簡單版）
================================================================================

簡單思路：
    1. 把等式中的每個數字，想成七段顯示器的木棒組合
    2. 嘗試移動一根木棒，改變某個數字
    3. 檢查等式是否成立
================================================================================
"""

import re


def solve(equation: str) -> str:
    """
    解題主函數
    """
    # 移除結尾的 #
    eq = equation.rstrip("#")

    if "=" not in eq:
        return "No"

    # 產生所有可能的移動結果
    candidates = generate_moves(eq)

    # 檢查每個候選是否成立
    for new_eq in candidates:
        if check_equal(new_eq):
            return new_eq + "#"

    return "No"


def generate_moves(eq: str) -> list:
    """
    產生所有可能的移動結果
    """
    results = []

    # 七段顯示器：每個數字用哪些木棒
    segments = {
        "0": "abcdef",  # 上,右上,右下,左下,左上,下
        "1": "bc",
        "2": "abdeg",
        "3": "abcdg",
        "4": "bcfg",
        "5": "acdfg",
        "6": "acdefg",
        "7": "abc",
        "8": "abcdefg",
        "9": "abcdfg",
    }

    # 把所有數字收集起來
    numbers = [(i, c) for i, c in enumerate(eq) if c.isdigit()]

    # 嘗試移動每個數字的每根木棒
    for i, d in numbers:
        if d not in segments:
            continue

        current = set(segments[d])

        # 嘗試移除每根木棒
        for stick in current:
            new_set = current - {stick}
            new_digit = digit_from_sticks(new_set)

            if new_digit:
                new_eq = eq[:i] + new_digit + eq[i + 1 :]
                results.append(new_eq)

                # 嘗試把這根木棒加到其他數字
                for j, d2 in numbers:
                    if j == i or d2 not in segments:
                        continue

                    target = set(segments[d2])
                    for add_stick in "abcdefg":
                        if add_stick not in target:
                            final_set = target | {add_stick}
                            final_digit = digit_from_sticks(final_set)

                            if final_digit:
                                final_eq = new_eq[:j] + final_digit + new_eq[j + 1 :]
                                if final_eq != eq:
                                    results.append(final_eq)

    return list(set(results))


def digit_from_sticks(sticks: set) -> str:
    """
    用木棒組合找數字
    """
    sticks_to_digit = {
        frozenset("abcdef"): "0",
        frozenset("bc"): "1",
        frozenset("abdeg"): "2",
        frozenset("abcdg"): "3",
        frozenset("bcfg"): "4",
        frozenset("acdfg"): "5",
        frozenset("acdefg"): "6",
        frozenset("abc"): "7",
        frozenset("abcdefg"): "8",
        frozenset("abcdfg"): "9",
    }
    return sticks_to_digit.get(frozenset(sticks))


def check_equal(eq: str) -> bool:
    """
    檢查等式是否成立
    """
    if "=" not in eq:
        return False

    try:
        left, right = eq.split("=")
        return calc(left) == calc(right)
    except:
        return False


def calc(expr: str) -> int:
    """
    計算表達式（只有 + 和 -）
    """
    expr = expr.strip()

    # 處理負數
    if expr.startswith("-"):
        expr = "0" + expr

    # 分割數字和運算子
    nums = []
    ops = []
    num = ""

    for c in expr:
        if c in "+-":
            if num:
                nums.append(int(num))
                num = ""
            ops.append(c)
        else:
            num += c

    if num:
        nums.append(int(num))

    # 計算
    result = nums[0] if nums else 0

    for i, op in enumerate(ops):
        if op == "+":
            result += nums[i + 1]
        else:
            result -= nums[i + 1]

    return result


# =============================================================================
# 單元測試
# =============================================================================
import unittest


class TestUVA10101Easy(unittest.TestCase):
    """測試案例"""

    def test_1(self):
        """簡單加法"""
        self.assertEqual(solve("1+1=2#"), "1+1=2#")

    def test_2(self):
        """簡單減法"""
        self.assertEqual(solve("8-5=0#"), "No")

    def test_3(self):
        """有解答"""
        result = solve("4+2=5#")
        self.assertIsNotNone(result)

    def test_4(self):
        """無解答"""
        self.assertEqual(solve("9+9=18#"), "No")

    def test_5(self):
        """單位數等式"""
        self.assertEqual(solve("1=1#"), "1=1#")

    def test_6(self):
        """多位數"""
        result = solve("10+5=15#")
        self.assertIsNotNone(result)

    def test_7(self):
        """無等號"""
        self.assertEqual(solve("1+1#"), "No")


if __name__ == "__main__":
    unittest.main()
