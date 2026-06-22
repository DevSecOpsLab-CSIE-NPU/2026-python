import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent


class TestSearchPerfProgram(unittest.TestCase):
    def run_program(self, input_text):
        result = subprocess.run(
            [sys.executable, "main.py"],
            input=input_text,
            text=True,
            capture_output=True,
            cwd=PROJECT_DIR,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=f"程式應正常結束，但 stderr 是：{result.stderr}",
        )
        return result.stdout

    def test_found_case_outputs_found_index_and_comparison_count(self):
        output = self.run_program("8\n1 20 37 80 113 150 200 300\n")
        first_line = output.splitlines()[0]

        self.assertRegex(first_line, r"^FOUND\s+\d+\s+cmp=\d+$")
        self.assertIn("linear :", output)
        self.assertIn("binary :", output)
        self.assertRegex(output, r"=> (binary|linear) faster")

    def test_not_found_edge_case_outputs_not_found_and_comparison_count(self):
        output = self.run_program("5\n1 20 37 80 150\n")
        first_line = output.splitlines()[0]

        self.assertRegex(first_line, r"^NOT FOUND\s+cmp=\d+$")

    def test_program_generates_radar_image_and_readme(self):
        radar_path = PROJECT_DIR / "assets" / "radar.png"
        readme_path = PROJECT_DIR / "README.md"

        if radar_path.exists():
            radar_path.unlink()
        if readme_path.exists():
            readme_path.unlink()

        self.run_program("8\n1 20 37 80 113 150 200 300\n")

        self.assertTrue(radar_path.exists())
        self.assertGreater(radar_path.stat().st_size, 0)
        self.assertTrue(readme_path.exists())
        readme_text = readme_path.read_text(encoding="utf-8")
        self.assertIn("維度", readme_text)
        self.assertIn("正規化", readme_text)


if __name__ == "__main__":
    unittest.main()
