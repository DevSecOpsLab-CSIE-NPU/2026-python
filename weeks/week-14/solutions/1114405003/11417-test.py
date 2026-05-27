import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent
TARGETS = [ROOT / "11417.py", ROOT / "11417-easy.py", ROOT / "11417-hand.py"]


class Test11417(unittest.TestCase):
    # 這題的重點是表格預處理，所以測試會把三個版本的答案一起比對。
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
        data = """10
100
500
0
"""
        expect = """67
13015
442011"""
        self.assertEqual(self.run_case(data), expect)

    def test_small_values(self):
        data = """2
3
0
"""
        expect = """1
3"""
        # 2 的答案是 gcd(1,2)=1；3 的答案是 1+1+1=3。
        self.assertEqual(self.run_case(data), expect)


if __name__ == "__main__":
    unittest.main()