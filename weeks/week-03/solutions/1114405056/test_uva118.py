import os
import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA118(unittest.TestCase):
    """UVA 118（Mutant Flatworld Explorers）測試。"""

    @classmethod
    def setUpClass(cls):
        cls.test_dir = Path(__file__).resolve().parent
        cls.solution_path = Path(
            os.environ.get("UVA118_SOLUTION", cls.test_dir / "uva118-easy.py")
        )

    def _run_solution(self, input_text: str) -> str:
        if not self.solution_path.exists():
            self.skipTest(f"找不到受測程式：{self.solution_path}")

        result = subprocess.run(
            [sys.executable, str(self.solution_path)],
            input=input_text,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr)
        return result.stdout.strip()

    def test_sample_case(self):
        input_text = "\n".join(
            [
                "5 3",
                "1 1 E",
                "RFRFRFRF",
                "3 2 N",
                "FRRFLLFFRRFLL",
                "0 3 W",
                "LLFFFLFLFL",
            ]
        )
        expected = "\n".join(["1 1 E", "3 3 N LOST", "2 3 S"])
        self.assertEqual(self._run_solution(input_text), expected)

    def test_scent_prevents_second_loss(self):
        # 第一台在 (0,0,S) 往南掉落，留下 scent；第二台同點同向前進應被忽略。
        input_text = "\n".join(["1 1", "0 0 S", "F", "0 0 S", "F"])
        expected = "\n".join(["0 0 S LOST", "0 0 S"])
        self.assertEqual(self._run_solution(input_text), expected)


if __name__ == "__main__":
    unittest.main()
