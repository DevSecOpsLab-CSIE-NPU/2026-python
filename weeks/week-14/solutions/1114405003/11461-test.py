import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent
TARGETS = [ROOT / "11461.py", ROOT / "11461-easy.py", ROOT / "11461-hand.py"]


class Test11461(unittest.TestCase):
    # 這題的答案可以直接用整數平方根算出來，因此很適合用樣本與極值來驗證。
    def run_case(self, input_data: str) -> str:
        outputs = []
        for target in TARGETS:
            completed = subprocess.run(
                [sys.executable, str(target)],
                input=input_data,
                text=True,
                capture_output=True,
                check=True,
            )
            outputs.append(completed.stdout.strip())

        self.assertEqual(outputs[0], outputs[1])
        self.assertEqual(outputs[0], outputs[2])
        return outputs[0]

    def test_sample(self):
        data = """1 4
1 10
1 100000
0 0
"""
        expect = """2
3
316"""
        self.assertEqual(self.run_case(data), expect)

    def test_boundary(self):
        data = """16 16
17 24
0 0
"""
        expect = """1
0"""
        self.assertEqual(self.run_case(data), expect)


if __name__ == "__main__":
    unittest.main()