"""Stage 5 — 安全性自掃測試"""

import unittest
import ast
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_FILES = [
    "timing.py",
    "sorts.py",
    "sorts_fast.py",
    "plot.py",
    "benchmark.py",
]


def _read_source(name):
    path = os.path.join(BASE_DIR, name)
    if not os.path.isfile(path):
        return None
    with open(path, "r") as f:
        return f.read()


class TestSecurity(unittest.TestCase):
    def test_no_bare_except(self):
        for fname in SOURCE_FILES:
            src = _read_source(fname)
            if src is None:
                continue
            tree = ast.parse(src)
            for node in ast.walk(tree):
                if isinstance(node, ast.ExceptHandler) and node.type is None:
                    self.fail(f"{fname}: bare except 在第 {node.lineno} 行")

    def test_load_uses_json_not_pickle(self):
        src = _read_source("plot.py")
        self.assertIsNotNone(src)
        self.assertIn("import json", src)
        self.assertNotIn("import pickle", src)

    def test_benchmark_py_uses_with_for_files(self):
        src = _read_source("benchmark.py")
        self.assertIsNotNone(src, "benchmark.py 不存在，請先建立")
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and getattr(node.func, "id", None) == "open":
                self.fail("benchmark.py: 使用 open() 需搭配 with 陳述式")

    def test_edge_case_no_assert_validation(self):
        for fname in SOURCE_FILES:
            src = _read_source(fname)
            if src is None:
                continue
            tree = ast.parse(src)
            for node in ast.walk(tree):
                if isinstance(node, ast.Assert):
                    self.fail(f"{fname}: 第 {node.lineno} 行使用 assert（不可作為輸入驗證）")


if __name__ == "__main__":
    unittest.main()
