import subprocess
import sys
import unittest
from pathlib import Path

BASE = Path(__file__).resolve().parent
PY = sys.executable


def run(filename, input_data):
    proc = subprocess.run(
        [PY, str(BASE / filename)],
        input=input_data, text=True, capture_output=True, check=True,
    )
    return proc.stdout.strip()


class TestQ11332Hand(unittest.TestCase):
    def test_single_mirror_visible(self):
        # 水平鏡子橫跨多個角度，從原點必定可見
        result = run("q11332-hand.py", "1\n1 1 1 3\n")
        self.assertEqual(result.strip(), "1")

    def test_closer_mirror_blocks_farther(self):
        result = run("q11332-hand.py", "2\n1 1 1 3\n2 2 2 4\n")
        self.assertEqual(result.strip(), "1 0")

    def test_same_as_easy(self):
        data = "2\n1 1 2 1\n-2 -1 -1 -2\n"
        self.assertEqual(
            run("q11332-hand.py", data),
            run("q11332-easy.py", data),
        )


if __name__ == "__main__":
    unittest.main()
