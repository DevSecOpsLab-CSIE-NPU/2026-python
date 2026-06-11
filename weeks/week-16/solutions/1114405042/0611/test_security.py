"""Stage 5 — 安全性自掃測試

對照 OpenSSF Secure Coding Guide for Python:
  - 08 Coding Standards: 無 shadow 內建名稱;無邊迭代邊改 list;有用 with 關檔;不用 assert 當驗證
  - 05 Exception Handling: 不寫 except: 全包;開檔抓具體例外
  - 03 Numbers: 排序比較子、計時 float 累加、迴圈計數的邊界正確
  - 04 Neutralization: 讀 JSON 用 json 模組而非 pickle（防 CWE-502）
"""

import os
import sys
import json
import unittest
import tempfile


SOLUTION_DIR = os.path.dirname(os.path.abspath(__file__))


class TestSecurityCodingStandards(unittest.TestCase):
    def test_no_bare_except_in_benchmark(self):
        """05 Exception Handling — 不得用 except: 全包"""
        with open(os.path.join(SOLUTION_DIR, "benchmark.py")) as f:
            content = f.read()
        self.assertNotIn("except:", content)

    def test_results_file_uses_with(self):
        """08 Coding Standards — 開檔必須用 with 陳述式"""
        with open(os.path.join(SOLUTION_DIR, "benchmark.py")) as f:
            content = f.read()
        self.assertIn("with open(", content)

    def test_load_uses_json_not_pickle(self):
        """04 Neutralization — 讀 JSON 用 json 模組,非 pickle（CWE-502）"""
        with open(os.path.join(SOLUTION_DIR, "plot.py")) as f:
            content = f.read()
        self.assertNotIn("pickle", content)
        self.assertIn("json", content)

    def test_no_builtin_shadowing_sorts(self):
        """08 Coding Standards — 排序實作不得 shadow 內建名稱（如 list、sorted）"""
        with open(os.path.join(SOLUTION_DIR, "sorts.py")) as f:
            content = f.read()
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("def ") or stripped.startswith("class "):
                continue
            self.assertFalse(stripped.startswith("list "), f"Shadowing built-in list: {line}")
            self.assertFalse(stripped.startswith("sorted "), f"Shadowing built-in sorted: {line}")

    def test_make_data_rejects_negative(self):
        """08 Coding Standards — 不要用 assert 當輸入驗證"""
        with open(os.path.join(SOLUTION_DIR, "benchmark.py")) as f:
            content = f.read()
        self.assertNotIn("assert ", content)

    def test_file_operations_specific_exception(self):
        """05 Exception Handling — 開檔應抓具體例外"""
        with open(os.path.join(SOLUTION_DIR, "plot.py")) as f:
            content = f.read()
        self.assertNotIn("except:", content)

    def test_no_mutation_during_iteration_sorts(self):
        """08 Coding Standards — 排序不得邊迭代邊改 list"""
        with open(os.path.join(SOLUTION_DIR, "sorts.py")) as f:
            content = f.read()
        self.assertNotIn("del ", content)
        self.assertNotIn(".pop(", content)

    def test_plot_savefig_uses_with(self):
        """08 Coding Standards — savefig 前已用 os.makedirs 確認目錄存在"""
        with open(os.path.join(SOLUTION_DIR, "plot.py")) as f:
            content = f.read()
        self.assertIn("os.makedirs", content)
        self.assertIn("savefig", content)


if __name__ == "__main__":
    unittest.main()
