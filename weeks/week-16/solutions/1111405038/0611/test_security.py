"""Stage 5 red tests — 安全性規則測試

對照 OpenSSF 重點:
- Numbers / 邊界條件: n 與 sizes 必須做正值驗證
- Exception Handling: 壞掉的 JSON 需回傳明確錯誤訊息
- Neutralization: 載入結果應使用 json，不可用 pickle
"""

import inspect
import tempfile
import unittest
from pathlib import Path

from benchmark import make_data, run_benchmark
from plot import load_results


class TestSecurityStage5(unittest.TestCase):
    def test_make_data_rejects_zero(self):
        """n=0 應視為無效輸入，避免無意義 benchmark。"""
        with self.assertRaisesRegex(ValueError, "n must be > 0"):
            make_data(0)

    def test_run_benchmark_rejects_zero_size(self):
        """sizes 內若有 0，應主動拒絕而不是默默執行。"""
        with self.assertRaisesRegex(ValueError, "sizes must be positive"):
            run_benchmark(sizes=(0, 10), repeats=1)

    def test_load_results_invalid_json_message(self):
        """壞掉的 JSON 應轉成可讀訊息，避免直接丟底層 parse error。"""
        with tempfile.TemporaryDirectory() as tmp_dir:
            bad_json = Path(tmp_dir) / "bad.json"
            bad_json.write_text("{not-valid-json", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "invalid json"):
                load_results(str(bad_json))

    def test_load_results_uses_json_not_pickle(self):
        """安全需求: 載入 benchmark 結果應使用 json, 不可用 pickle。"""
        source = inspect.getsource(load_results)
        self.assertIn("json.load", source)
        self.assertNotIn("pickle", source)


if __name__ == "__main__":
    unittest.main()
