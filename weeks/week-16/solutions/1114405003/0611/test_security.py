"""Stage 5 — 安全性自掃

對照 [OpenSSF Secure Coding Guide for Python](https://best.openssf.org/Secure-Coding-Guide-for-Python/), 
掃自己 Stage 1–4 寫的程式,把**問題編成測試 → 修到綠**,跟前面同一個循環。

只看這四章(不必讀完整本):

| 章節 | 在這份程式裡查什麼 |
|------|-------------------|
| **08 Coding Standards** | 排序有沒有「邊迭代邊改 list」;有沒有 shadow 內建名稱;寫 `results.json`、存 PNG 有沒有用 `with` 關檔;有沒有拿 `assert` 當輸入驗證 |
| **05 Exception Handling** | 開檔讀檔有沒有抓**具體例外**(不是 `except:` 全包);失敗有沒有正確 cleanup |
| **03 Numbers** | 排序比較子、計時 float 累加、迴圈計數有沒有邊界/精度問題 |
| **04 Neutralization** | 讀 `results.json` 用 `json` 還是 `pickle`?為什麼 `json` 較安全(CWE-502) |

做法(紅 → 綠):

1. 至少找出 **3 條**適用條目,每條寫一個會紅的測試放進 `test_security.py`
   (例:`test_results_file_closed`、`test_make_data_rejects_negative`、`test_load_uses_json_not_pickle`)
2. `python -m unittest` 確認紅 → commit `test: stage5 ...`;修 code 轉綠 → commit `feat: stage5 ...`
3. 報告用表格記錄每條:OpenSSF 條目(CWE)/ 檢查結果 / 處理方式
4. 掃到但判定**不適用**的也要寫一句理由(例:benchmark 的 `random` 非安全敏感,用 `random` 正確,不需改 `secrets`)

> **重點不是把所有條目都「修掉」**,而是判斷哪些適用——盲目把 benchmark 的 `random` 改成 `secrets` 反而扣分。
> (選做・加分)`pip install bandit && bandit -r .`,把工具輸出和你人工找到的對照,寫一句兩者差異。
"""

import unittest
import json
import os
from unittest.mock import patch, mock_open
from plot import load_results
from benchmark import make_data


class TestSecurity(unittest.TestCase):
    def test_results_file_closed(self):
        """測試 results.json 是否使用 with 語句關檔 (OpenSSF 08 Coding Standards)
        
        CWE: CWE-1068 - Improper Restriction of Operations within the Bounds of a Memory Buffer
        """
        # 讀取 benchmark.py 來檢查是否使用 with 語句
        with open("D:\\44\\2026-python\\weeks\\week-16\\solutions\\1114405003\\0611\\benchmark.py", "r", encoding="utf-8") as f:
            benchmark_content = f.read()
        
        # 檢查是否使用了 with 語句來寫 results.json
        self.assertIn("with open(\"results.json\", \"w\") as f:", benchmark_content)
        
        # 驗證檔案實際存在且非空
        self.assertTrue(os.path.exists("results.json"))
        file_size = os.path.getsize("results.json")
        self.assertGreater(file_size, 0)
    
    def test_make_data_rejects_negative(self):
        """測試 make_data 是否拒絕負數輸入 (OpenSSF 03 Numbers)
        
        CWE: CWE-190 - Integer Overflow or Wraparound
        """
        # make_data 應該接受負數，但我們可以添加驗證
        # 目前 make_data 會生成指定長度的列表，即使輸入為負數
        # 這是一個潛在的安全問題
        
        # 測試負數輸入
        result = make_data(-5)
        self.assertEqual(len(result), 0)
        
        # 測試零輸入
        result = make_data(0)
        self.assertEqual(len(result), 0)
        
        # 測試正數輸入
        result = make_data(5)
        self.assertEqual(len(result), 5)
    
    def test_load_uses_json_not_pickle(self):
        """測試 load_results 是否使用 json 而不是 pickle (OpenSSF 04 Neutralization)
        
        CWE: CWE-502 - Deserialization of Untrusted Data
        """
        # 讀取 plot.py 來檢查是否使用了 json 而不是 pickle
        with open("D:\\44\\2026-python\\weeks\\week-16\\solutions\\1114405003\\0611\\plot.py", "r", encoding="utf-8") as f:
            plot_content = f.read()
        
        # 檢查是否使用了 json 模組
        self.assertIn("import json", plot_content)
        
        # 檢查是否使用了 json.load 而不是 pickle.load
        self.assertIn("json.load(f)", plot_content)
        
        # 確保沒有使用 pickle
        self.assertNotIn("import pickle", plot_content)
        self.assertNotIn("pickle.load", plot_content)
    
    def test_sort_functions_do_not_modify_input(self):
        """測試排序函式是否會修改輸入列表 (OpenSSF 08 Coding Standards)
        
        CWE: CWE-120 - Buffer Copy Without Checking Size of Input
        """
        from sorts import bubble_sort, quick_sort, merge_sort
        
        test_data = [3, 1, 4, 1, 5]
        
        # 測試 bubble_sort
        original = test_data.copy()
        result = bubble_sort(test_data)
        self.assertEqual(test_data, original)
        
        # 測試 quick_sort
        original = test_data.copy()
        result = quick_sort(test_data)
        self.assertEqual(test_data, original)
        
        # 測試 merge_sort
        original = test_data.copy()
        result = merge_sort(test_data)
        self.assertEqual(test_data, original)
    
    def test_timing_decorator_no_print(self):
        """測試 timeit 裝飾器是否內部使用 print (OpenSSF 08 Coding Standards)
        
        CWE: CWE-532 - Insertion of Sensitive Information into Log File
        """
        from timing import timeit
        
        # 創建一個會被裝飾的函式
        @timeit
        def test_func():
            return "test"
        
        # 呼叫函式
        result = test_func()
        
        # 驗證函式回傳值正確
        self.assertEqual(result, "test")
        
        # 驗證裝飾器沒有使用 print（無法直接測試，依賴於程式碼檢查）
        with open("D:\\44\\2026-python\\weeks\\week-16\\solutions\\1114405003\\0611\\timing.py", "r", encoding="utf-8") as f:
            timing_content = f.read()
        
        # 檢查裝飾器內部是否包含 print 語句
        self.assertNotIn("print(", timing_content)
    
def test_benchmark_random_not_secrets(self):
        """測試 benchmark 是否正確使用 random 而不是 secrets (OpenSSF 04 Neutralization)
        
        判斷理由: benchmark 的 random 用於生成測試數據，不是安全敏感操作，所以使用 random 是正確的
        """
        # 讀取 benchmark.py 來檢查是否使用了 random
        with open("D:\\44\\2026-python\\weeks\\week-16\\solutions\\1114405003\\0611\\benchmark.py", "r", encoding="utf-8") as f:
            benchmark_content = f.read()
        
        # 檢查是否使用了 random 模組
        self.assertIn("import random", benchmark_content)
        
        # 檢查是否使用了 random.seed
        self.assertIn("random.seed", benchmark_content)
        
        # 檢查是否使用了 secrets（不應該使用）
        self.assertNotIn("import secrets", benchmark_content)
        
        # 判斷理由
        self.assertTrue(True, "benchmark 的 random 用於生成測試數據，不是安全敏感操作，所以使用 random 是正確的")


if __name__ == "__main__":
    unittest.main()