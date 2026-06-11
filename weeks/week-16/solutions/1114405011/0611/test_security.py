"""Stage 5 — 安全性自掃測試

對照 OpenSSF Secure Coding Guide for Python 四章：
  Ch03 Numbers    — 邊界 / 精度問題
  Ch05 Exception  — 具體例外處理
  Ch08 Standards  — 邊迭代邊改、shadow、with 關檔、assert 驗證
  Ch04 Neutral    — CWE-502 json vs pickle

三條適用條目（均為紅燈 → 綠燈）：
  1. make_data 對 n<=0 未拋 ValueError（Ch03 boundary）
  2. plot_results 對空 dict 拋 IndexError 而非 ValueError（Ch08 coding standards）
  3. load_results 讓 json.JSONDecodeError 直接外洩，沒有包裝成 ValueError（Ch05 exception）
"""

import json
import os
import tempfile
import unittest

from benchmark import make_data
from plot import load_results, plot_results


class TestSecurityMakeData(unittest.TestCase):
    """Ch03 Numbers — make_data 應對 n<=0 拋出 ValueError"""

    def test_make_data_rejects_negative_n(self):
        """n 為負數時應拋 ValueError，不應靜默回傳空 list。"""
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_make_data_rejects_zero_n(self):
        """n 為 0 時應拋 ValueError，0 筆資料無法做有意義的 benchmark。"""
        with self.assertRaises(ValueError):
            make_data(0)


class TestSecurityPlotResults(unittest.TestCase):
    """Ch08 Coding Standards — plot_results 應對空 dict 拋 ValueError 而非 IndexError"""

    def test_plot_results_rejects_empty_results(self):
        """空的 results dict 應拋 ValueError（而非 IndexError），讓呼叫端知道真正原因。"""
        with self.assertRaises(ValueError):
            plot_results({}, "assets/benchmark_test.png")


class TestSecurityLoadResults(unittest.TestCase):
    """Ch05 Exception Handling — load_results 應把 json.JSONDecodeError 包成 ValueError"""

    def test_load_results_wraps_json_error_as_value_error(self):
        """
        給定損壞的 JSON 時，load_results 應拋 ValueError（附說明），
        而非直接外洩底層 json.JSONDecodeError（Ch05 具體例外）。
        """
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as tmp:
            tmp.write("this is not valid json {{{")
            fname = tmp.name
        try:
            with self.assertRaises(ValueError):
                load_results(fname)
        finally:
            os.unlink(fname)

    def test_load_results_does_not_use_pickle(self):
        """
        CWE-502 — 給定 pickle 二進位內容時，load_results 應因 json 解析失敗而拋例外，
        確認 load_results 不會靜默接受 pickle 格式（不適用 pickle，使用 json 才安全）。
        """
        import pickle

        payload = pickle.dumps({"key": "value"})
        with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as tmp:
            tmp.write(payload)
            fname = tmp.name
        try:
            with self.assertRaises((ValueError, json.JSONDecodeError, UnicodeDecodeError)):
                load_results(fname)
        finally:
            os.unlink(fname)


if __name__ == "__main__":
    unittest.main()
