"""10101 單元測試。

會暴力列出小型輸入所有可能的一棒移動結果，
再確認正式版、easy 版與手打版是否回傳其中之一。
"""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load_module(filename: str):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(path.stem.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


MASKS = {
    0: 0b1111110,
    1: 0b0110000,
    2: 0b1101101,
    3: 0b1111001,
    4: 0b0110011,
    5: 0b1011011,
    6: 0b1011111,
    7: 0b1110000,
    8: 0b1111111,
    9: 0b1111011,
}


def build_moves():
    remove = [[] for _ in range(10)]
    add = [[] for _ in range(10)]
    for old_digit, old_mask in MASKS.items():
        for new_digit, new_mask in MASKS.items():
            if (old_mask ^ new_mask).bit_count() != 1:
                continue
            if new_mask < old_mask:
                remove[old_digit].append(new_digit)
            else:
                add[old_digit].append(new_digit)
    return remove, add


REMOVE, ADD = build_moves()


def parse_side(side: str) -> int:
    value = 0
    index = 0
    sign = 1
    if index < len(side) and side[index] == "-":
        sign = -1
        index += 1
    while index < len(side):
        start = index
        while index < len(side) and side[index].isdigit():
            index += 1
        value += sign * int(side[start:index])
        if index >= len(side):
            break
        sign = 1 if side[index] == "+" else -1
        index += 1
    return value


def is_valid(expr: str) -> bool:
    left, right = expr.split("=")
    return parse_side(left) == parse_side(right)


def brute_force_solutions(expr: str):
    positions = [index for index, ch in enumerate(expr) if ch.isdigit()]
    answers = set()

    for source_pos in positions:
        source_digit = int(expr[source_pos])
        for new_source_digit in REMOVE[source_digit]:
            for target_pos in positions:
                if target_pos == source_pos:
                    continue
                target_digit = int(expr[target_pos])
                for new_target_digit in ADD[target_digit]:
                    chars = list(expr)
                    chars[source_pos] = str(new_source_digit)
                    chars[target_pos] = str(new_target_digit)
                    candidate = "".join(chars)
                    if is_valid(candidate):
                        answers.add(candidate + "#")
    return answers


class Test10101(unittest.TestCase):
    def setUp(self):
        self.normal = load_module("10101.py")
        self.easy = load_module("10101-easy.py")
        self.hand = load_module("10101-hand.py")

    def assert_solution(self, expr: str):
        expected = brute_force_solutions(expr)
        output = self.normal.solve(expr + "#")
        self.assertEqual(self.easy.solve(expr + "#"), output)
        self.assertEqual(self.hand.solve(expr + "#"), output)
        if expected:
            self.assertIn(output, expected)
        else:
            self.assertEqual(output, "No")

    def test_solvable_cases(self):
        self.assert_solution("7+2=2")
        self.assert_solution("70+2=13")

    def test_no_solution_case(self):
        self.assertEqual(brute_force_solutions("1=1"), set())
        self.assertEqual(self.normal.solve("1=1#"), "No")
        self.assertEqual(self.easy.solve("1=1#"), "No")
        self.assertEqual(self.hand.solve("1=1#"), "No")


if __name__ == "__main__":
    unittest.main()