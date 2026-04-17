import os
import subprocess
import sys
import unittest
from pathlib import Path


class TestUVA272(unittest.TestCase):
    """UVA 272（TeX Quotes）測試。"""

    @classmethod
    def setUpClass(cls):
        cls.test_dir = Path(__file__).resolve().parent
        cls.solution_path = Path(
            os.environ.get("UVA272_SOLUTION", cls.test_dir / "uva272-easy.py")
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
        return result.stdout

    def test_sample_style_text(self):
        input_text = '"To be or not to be," quoth the bard, "that is the question."\n'
        expected = "``To be or not to be,'' quoth the bard, ``that is the question.''\n"
        self.assertEqual(self._run_solution(input_text), expected)

    def test_multi_line_quotes(self):
        input_text = '"A"\n"B"\n'
        expected = "``A''\n``B''\n"
        self.assertEqual(self._run_solution(input_text), expected)


if __name__ == "__main__":
    unittest.main()
