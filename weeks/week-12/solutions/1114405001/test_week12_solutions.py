import unittest

from uva10812 import solve as solve_10812
from uva10908 import solve as solve_10908
from uva10922 import solve as solve_10922
from uva10929 import solve as solve_10929
from uva10931 import solve as solve_10931


class TestWeek12Solutions(unittest.TestCase):
    def test_10812(self):
        data = """4
40 20
20 40
20 0
9 1
"""
        expected = "\n".join([
            "30 10",
            "impossible",
            "10 10",
            "5 4",
        ])
        self.assertEqual(solve_10812(data), expected)

    def test_10908(self):
        data = """1
7 10 4
abbbaaaaaa
abbbaaaaaa
abbbaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaccaaaaaa
aaccaaaaaa
1 2
2 4
4 6
5 2
"""
        expected = "\n".join([
            "7 10 4",
            "3",
            "1",
            "5",
            "1",
        ])
        self.assertEqual(solve_10908(data), expected)

    def test_10922(self):
        data = """999999999999999999999999
999999999999999999999991
9
0
"""
        expected = "\n".join([
            "999999999999999999999999 is a multiple of 9 and has 9-degree 2.",
            "999999999999999999999991 is not a multiple of 9.",
            "9 is a multiple of 9 and has 9-degree 1.",
        ])
        self.assertEqual(solve_10922(data), expected)

    def test_10929(self):
        data = """112233
12345678901
0
"""
        expected = "\n".join([
            "112233 is a multiple of 11.",
            "12345678901 is not a multiple of 11.",
        ])
        self.assertEqual(solve_10929(data), expected)

    def test_10931(self):
        data = """1
2
10
21
0
"""
        expected = "\n".join([
            "The parity of 1 is 1 (mod 2).",
            "The parity of 10 is 1 (mod 2).",
            "The parity of 1010 is 2 (mod 2).",
            "The parity of 10101 is 3 (mod 2).",
        ])
        self.assertEqual(solve_10931(data), expected)


if __name__ == "__main__":
    unittest.main()
