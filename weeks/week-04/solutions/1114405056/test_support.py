"""Week 04 測試輔助工具。"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import unittest


class DualSolutionTestCase(unittest.TestCase):
    """讓同一組測試同時驗證正式版與 easy 版。"""

    solution_names: tuple[str, ...] = ()

    @classmethod
    def setUpClass(cls) -> None:
        base_dir = Path(__file__).resolve().parent
        cls.solution_paths = []

        for name in cls.solution_names:
            path = base_dir / name
            if not path.is_file():
                raise unittest.SkipTest(f"找不到解答檔：{name}")
            cls.solution_paths.append(path)

    def run_solution(self, script_path: Path, input_data: str) -> str:
        completed = subprocess.run(
            [sys.executable, str(script_path)],
            input=input_data,
            text=True,
            capture_output=True,
            cwd=script_path.parent,
            timeout=5,
            check=False,
        )

        if completed.returncode != 0:
            self.fail(
                "解答程式執行失敗。\n"
                f"檔案：{script_path.name}\n"
                f"return code：{completed.returncode}\n"
                f"stderr：\n{completed.stderr}"
            )

        return self.normalize_output(completed.stdout)

    @staticmethod
    def normalize_output(text: str) -> str:
        normalized = text.replace("\r\n", "\n").replace("\r", "\n")
        stripped = normalized.strip()
        if not stripped:
            return ""
        return "\n".join(line.rstrip() for line in stripped.split("\n"))

    def assert_output_for_all(self, input_data: str, expected_output: str) -> None:
        expected = self.normalize_output(expected_output)

        for script_path in self.solution_paths:
            with self.subTest(script=script_path.name):
                actual = self.run_solution(script_path, input_data)
                self.assertEqual(actual, expected)
