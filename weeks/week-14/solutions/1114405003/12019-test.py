import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent
TARGETS = [ROOT / "12019.py", ROOT / "12019-easy.py", ROOT / "12019-hand.py"]


class Test12019(unittest.TestCase):
    # 這題的核心是固定年份的星期換算，所以測試會特別挑幾個可人工驗證的日期。
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

    def test_known_dates(self):
        data = """4
1 1
2 29
3 1
12 25
"""
        expect = """Sunday
Wednesday
Thursday
Tuesday"""
        self.assertEqual(self.run_case(data), expect)

    def test_doomsday_itself(self):
        data = """2
5 9
11 7
"""
        expect = """Wednesday
Wednesday"""
        self.assertEqual(self.run_case(data), expect)


if __name__ == "__main__":
    unittest.main()