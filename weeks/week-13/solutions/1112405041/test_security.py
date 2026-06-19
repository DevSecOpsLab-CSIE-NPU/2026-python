"""Stage 5: 安全自掃 — OpenSSF 規則檢查"""
import unittest
from pathlib import Path

SOLUTION_DIR = Path(__file__).resolve().parent


class TestSecurityScan(unittest.TestCase):
    def test_data_loader_uses_raise_not_assert(self):
        content = (SOLUTION_DIR / "data_loader.py").read_text(encoding="utf-8")
        self.assertIn("raise ValueError", content)
        self.assertNotIn("assert ", content)

    def test_analysis_uses_raise_not_assert(self):
        content = (SOLUTION_DIR / "analysis.py").read_text(encoding="utf-8")
        self.assertNotIn("assert ", content)

    def test_data_loader_uses_with_for_file(self):
        content = (SOLUTION_DIR / "data_loader.py").read_text(encoding="utf-8")
        self.assertIn("with open(", content)

    def test_no_bare_except(self):
        py_files = list(SOLUTION_DIR.rglob("*.py"))
        for f in py_files:
            if "test_" in f.name:
                continue
            content = f.read_text(encoding="utf-8")
            for i, line in enumerate(content.split("\n"), 1):
                stripped = line.strip()
                if stripped == "except:":
                    self.fail(f"{f.name}:{i} — bare except:")

    def test_no_shadow_builtins(self):
        py_files = list(SOLUTION_DIR.rglob("*.py"))
        shadow = {"list", "dict", "file", "id", "str", "int"}
        for f in py_files:
            content = f.read_text(encoding="utf-8")
            for i, line in enumerate(content.split("\n"), 1):
                stripped = line.strip()
                if stripped.startswith(tuple(shadow)) and "=" in stripped:
                    var = stripped.split("=")[0].strip()
                    if var in shadow:
                        self.fail(f"{f.name}:{i} — shadow built-in '{var}'")


if __name__ == "__main__":
    unittest.main()
