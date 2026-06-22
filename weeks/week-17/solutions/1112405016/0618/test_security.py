import unittest
import os
import json
import pickle
from benchmark import make_data
from timing import timeit


class TestSecurityStandards(unittest.TestCase):
    def test_make_data_rejects_negative_n(self):
        """測試 1 (03 Numbers): make_data 的 n 邊界防禦。
        當 n 為負數或非整數時，應拋出 ValueError。而不能回傳空 list 或當機。
        """
        with self.assertRaises(ValueError):
            make_data(-5)
        with self.assertRaises(ValueError):
            make_data(3.14)  # type: ignore

    def test_timing_repeat_uses_raise_not_assert(self):
        """測試 2 (08 Coding Standards): 裝飾器輸入驗證不可使用 assert。
        因為 assert 在生產環境的優化編譯（-O 旗標）下會被完全忽略。
        如果我們傳入無效的 repeat，裝飾器應透過 raise 拋出 ValueError。
        """
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def dummy():
                pass

    def test_results_file_load_uses_json_not_pickle(self):
        """測試 3 (04 Neutralization): 防範不可信反序列化漏洞 (CWE-502)。
        讀取或儲存 results.json 評估數據時，必須使用 json 模組，絕對不准使用危險的 pickle，
        因為 pickle 載入惡意檔案會執行任意程式碼。
        """
        # 模擬讀取 results.json，確認使用的是 json
        # 我們可以直接檢測檔案開頭與格式，或者確保我們不含有任何 pickle 的特徵碼
        results_file = "results.json"
        self.assertTrue(os.path.exists(results_file), "results.json 檔案應該存在")
        
        # 讀取並解析
        try:
            with open(results_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertIsInstance(data, dict, "應該成功解析為 JSON dict")
        except json.JSONDecodeError as e:
            self.fail(f"結果檔案不是有效的 JSON 格式！讀取失敗: {e}")

        # 驗證此檔案中絕不可能包含 pickle 的二進位特徵（例如 pickle 的 protocol 標誌）
        with open(results_file, "rb") as f:
            header = f.read(2)
            # pickle module features usually start with b'\x80'
            self.assertNotEqual(header, b'\x80\x02', "偵測到疑似 pickle protocol v2 的特徵碼！不安全")
            self.assertNotEqual(header, b'\x80\x03', "偵測到疑似 pickle protocol v3 的特徵碼！不安全")
            self.assertNotEqual(header, b'\x80\x04', "偵測到疑似 pickle protocol v4 的特徵碼！不安全")


if __name__ == "__main__":
    unittest.main()
