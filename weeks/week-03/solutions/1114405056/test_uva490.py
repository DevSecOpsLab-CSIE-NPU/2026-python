import os
import subprocess
import sys
import unittest
from pathlib import Path


def rotate_clockwise_90(text: str) -> str:
    """依題意產生參考答案：把文字矩陣順時針旋轉 90 度。"""
    lines = text.splitlines()
    if not lines:
        return ""

    width = max(len(line) for line in lines)
    out = []
    for col in range(width):
        row_chars = []
        for row in range(len(lines) - 1, -1, -1):
            if col < len(lines[row]):
                row_chars.append(lines[row][col])
            else:
                row_chars.append(" ")
        out.append("".join(row_chars).rstrip())
    return "\n".join(out)


class TestUVA490(unittest.TestCase):
    """UVA 490（Rotating Sentences）測試。"""

    @classmethod
    def setUpClass(cls):
        cls.test_dir = Path(__file__).resolve().parent
        cls.solution_path = Path(
            os.environ.get("UVA490_SOLUTION", cls.test_dir / "uva490-easy.py")
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

    def test_simple_case(self):
        input_text = "HELLO\nWORLD\n"
        expected = rotate_clockwise_90(input_text)
        self.assertEqual(self._run_solution(input_text), expected)

    def test_uneven_lines(self):
        input_text = "ABC\nDE\nF\n"
        expected = rotate_clockwise_90(input_text)
        self.assertEqual(self._run_solution(input_text), expected)


if __name__ == "__main__":
    unittest.main()
