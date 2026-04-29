import subprocess
import sys
import unittest
from pathlib import Path


BASE = Path(__file__).resolve().parent
PYTHON = sys.executable


def run_case(filename, data):
    result = subprocess.run(
        [PYTHON, str(BASE / filename)],
        input=data,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


class TestWeek10Solutions(unittest.TestCase):
    def test_10226(self):
        data = """3
0
0
0
3
1 0
3 0
0
"""
        want = """ABC
CB
BAC
CA
CAB
BA

BAC
CA
CBA"""
        self.assertEqual(run_case("10226.py", data), want)
        self.assertEqual(run_case("10226-easy.py", data), want)

    def test_10235(self):
        data = """3
6 3
1 1 1
1 0 1
1 1 1
1 1 1
1 0 1
1 1 1
2 4
1 1 1 1
1 1 1 1
1 1
0
"""
        want = """Case 1: 3
Case 2: 2
Case 3: 1"""
        self.assertEqual(run_case("10235.py", data), want)
        self.assertEqual(run_case("10235-easy.py", data), want)

    def test_10242(self):
        data = """6 7
1 2
2 3
3 5
2 4
4 1
2 6
6 5
10
12
8
16
1
5
1 4
4 3 5 6
"""
        want = "47"
        self.assertEqual(run_case("10242.py", data), want)
        self.assertEqual(run_case("10242-easy.py", data), want)

    def test_10252(self):
        data = """2
3
0 0
1 1
2 2
4
0 0
0 2
2 0
2 2
"""
        want = """4 1
8 9"""
        self.assertEqual(run_case("10252.py", data), want)
        self.assertEqual(run_case("10252-easy.py", data), want)

    def test_10268(self):
        data = """2 100
10 786599
4 786599
60 1844674407370955161
63 9223372036854775807
0 0
"""
        want = """14
21
More than 63 trials needed.
61
63"""
        self.assertEqual(run_case("10268.py", data), want)
        self.assertEqual(run_case("10268-easy.py", data), want)


if __name__ == "__main__":
    unittest.main()