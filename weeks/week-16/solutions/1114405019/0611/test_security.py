"""Stage 5 — 安全性自掃測試

依據：OpenSSF Secure Coding Guide for Python（第 03、04、05、08 章）
掃描範圍：timing.py / sorts.py / sorts_fast.py / benchmark.py / plot.py
"""
import ast
import inspect
import json
import os
import tempfile
import unittest


class TestFileHandlingWithContext(unittest.TestCase):
    """08 Coding Standards: 檔案操作應使用 with 確保資源釋放"""

    def test_load_results_uses_with_open(self):
        import plot
        src = inspect.getsource(plot.load_results)
        self.assertIn("with open", src,
                      "load_results 應使用 with open(...) as f 確保檔案釋放")

    def test_benchmark_write_uses_with_open(self):
        with open("benchmark.py", "r", encoding="utf-8") as f:
            src = f.read()
        self.assertIn("with open", src,
                      "benchmark.py 寫 results.json 應使用 with open")
        self.assertIn("json.dump", src)


class TestNoBareExcept(unittest.TestCase):
    """05 Exception Handling: 不使用 bare except:（會吞掉 KeyboardInterrupt 等）"""

    def _check_no_bare_except(self, filename):
        if not os.path.exists(filename):
            self.skipTest(f"{filename} 不存在")
        with open(filename, "r", encoding="utf-8") as f:
            src = f.read()
        tree = ast.parse(src, filename=filename)
        for node in ast.walk(tree):
            if isinstance(node, ast.ExceptHandler) and node.type is None:
                self.fail(f"{filename}:{node.lineno} 發現 bare except:")

    def test_timing_py(self):
        self._check_no_bare_except("timing.py")

    def test_sorts_py(self):
        self._check_no_bare_except("sorts.py")

    def test_sorts_fast_py(self):
        self._check_no_bare_except("sorts_fast.py")

    def test_benchmark_py(self):
        self._check_no_bare_except("benchmark.py")

    def test_plot_py(self):
        self._check_no_bare_except("plot.py")


class TestJsonNotPickle(unittest.TestCase):
    """04 Neutralization (CWE-502): 外部資料應用 json 讀取，不用 pickle"""

    def test_load_results_uses_json_not_pickle(self):
        import plot
        src = inspect.getsource(plot.load_results)
        self.assertNotIn("pickle", src)
        self.assertIn("json", src)

    def test_benchmark_does_not_import_pickle(self):
        with open("benchmark.py", "r", encoding="utf-8") as f:
            src = f.read()
        self.assertNotIn("import pickle", src,
                         "benchmark.py 不應 import pickle（CWE-502）")

    def test_load_results_roundtrip(self):
        """json 序列化/反序列化正確，且不依賴 pickle 的不安全反序列化"""
        from plot import load_results
        sample = {"algo": {"500": 0.1, "1000": 0.4}}
        tmp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        )
        json.dump(sample, tmp)
        tmp.close()
        try:
            self.assertEqual(load_results(tmp.name), sample)
        finally:
            os.unlink(tmp.name)


class TestMakeDataBoundary(unittest.TestCase):
    """03 Numbers: make_data 邊界條件與輸入驗證（不用 assert，用 raise）"""

    def test_make_data_rejects_negative_n(self):
        """負數 n 應 raise ValueError，而非讓 randint 靜默產生空 range"""
        from benchmark import make_data
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_make_data_zero_returns_empty(self):
        """n=0 應回傳空 list（明確定義邊界行為）"""
        from benchmark import make_data
        self.assertEqual(make_data(0), [])

    def test_make_data_reproducible_with_same_seed(self):
        """固定 seed 必須產生相同序列（實驗可重現性）"""
        from benchmark import make_data
        self.assertEqual(make_data(100, seed=7), make_data(100, seed=7))


if __name__ == "__main__":
    unittest.main()
