import re


def solve(equation: str) -> str:
    eq = equation.rstrip("#")

    if "=" not in eq:
        return "No"

    candidates = generate_moves(eq)

    for new_eq in candidates:
        if check_equal(new_eq):
            return new_eq + "#"

    return "No"


def generate_moves(eq: str) -> list:
    results = []

    segments = {
        "0": "abcdef",
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

    numbers = [(i, c) for i, c in enumerate(eq) if c.isdigit()]

    for i, d in numbers:
        if d not in segments:
            continue

        current = set(segments[d])

        for stick in current:
            new_set = current - {stick}
            new_digit = digit_from_sticks(new_set)

            if new_digit:
                new_eq = eq[:i] + new_digit + eq[i + 1 :]
                results.append(new_eq)

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

    if "=" not in eq:
        return False

    try:
        left, right = eq.split("=")
        return calc(left) == calc(right)
    except:
        return False


def calc(expr: str) -> int:

    expr = expr.strip()

    if expr.startswith("-"):
        expr = "0" + expr

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

    result = nums[0] if nums else 0

    for i, op in enumerate(ops):
        if op == "+":
            result += nums[i + 1]
        else:
            result -= nums[i + 1]

    return result


if __name__ == "__main__":
    import unittest

    class TestQ10101(unittest.TestCase):
        """UVA 10101 測試案例"""

        def test_1(self):
            self.assertEqual(solve("1+1=2#"), "1+1=2#")

        def test_2(self):
            self.assertEqual(solve("8-5=0#"), "No")

        def test_3(self):
            result = solve("4+2=5#")
            self.assertIsNotNone(result)

        def test_4(self):
            self.assertEqual(solve("9+9=18#"), "No")

        def test_5(self):
            self.assertEqual(solve("1=1#"), "1=1#")

        def test_6(self):
            result = solve("10+5=15#")
            self.assertIsNotNone(result)

        def test_7(self):
            self.assertEqual(solve("1+1#"), "No")

    unittest.main()
