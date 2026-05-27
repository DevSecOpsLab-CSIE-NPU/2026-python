import subprocess
import sys
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent
TARGETS = [ROOT / "11349.py", ROOT / "11349-easy.py", ROOT / "11349-hand.py"]


class Test11349(unittest.TestCase):
    # 測試只要覆蓋樣本與幾個邊界情況，就能快速驗證中心對稱的判斷是否正確。
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

        # 三個版本必須完全一致，才算通過。
        self.assertEqual(outputs[0], outputs[1])
        self.assertEqual(outputs[0], outputs[2])
        return outputs[0]

    def test_sample(self):
        data = """2
N = 3
5 1 3
2 0 2
3 1 5
N = 3
5 1 3
2 0 2
0 1 5
"""
        expect = """Test #1: Symmetric.
Test #2: Non-symmetric."""
        self.assertEqual(self.run_case(data), expect)

    def test_negative_number_is_invalid(self):
        data = """1
N = 2
1 -1
1 1
"""
        self.assertEqual(self.run_case(data), "Test #1: Non-symmetric.")

    def test_single_cell(self):
        data = """1
N = 1
0
"""
        self.assertEqual(self.run_case(data), "Test #1: Symmetric.")


if __name__ == "__main__":
    unittest.main()