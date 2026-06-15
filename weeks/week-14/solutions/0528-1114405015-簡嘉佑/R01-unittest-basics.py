"""
R01：unittest 基本用法（記憶層 — 直接複製可執行）

對應 Cookbook：
- 14.1 測試 stdout 輸出
- 14.2 在單元測試中給物件打補丁
- 14.3 在單元測試中測試例外情況

本檔模組重點：
1) 用 redirect_stdout 截取 print 的輸出來做斷言
2) MagicMock / @patch 讓測試不依賴真實 API
3) assertRaises / assertRaisesRegex 驗證例外行為

執行：
    python R01-unittest-basics.py
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ---------- 被測函式 ----------
# 以下三個函式是被測對象；實際課题中會是專案程式的輸入輸出处理

def url_print(host, domain):
    # 列印完整 URL，第一個測試案例要驗證此函式的輸出是否正確
    print(f"https://{host}.{domain}")


def parse_int(s):
    # 將字串轉成整數，空字串則丟出 ValueError。
    # 第三個測試案例要驗證此例外行為。
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    # 經由外部 API 物件取得使用者資料。
    # 測試時不需要真實 API，用 MagicMock 取代。
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        # redirect_stdout 會把 print 導向 buf，而不是終端機
        # 這樣就能用 buf.getvalue() 取得字串來做斷言，不需要真的輸出
        buf = io.StringIO()
        with redirect_stdout(buf):
            url_print("www", "example.com")
        # strip() 去除尾端换行，再比對期望字串
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        # MagicMock() 建立一個假的 API 物件，任何方法呼叫都不會實际執行
        fake_api = MagicMock()
        # 設定 fake_api.get() 被呼叫時的回傳値
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        # 驗證回傳內容是否正確
        self.assertEqual(result["name"], "Alice")
        # 驗證 get 只被呼叫一次，且參數正確
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        # @patch 裝飾器會暫時把指定名稱的物件替換成 Mock
        # 這裡把內建的 print 替換，讓它不真正輸出并可驗證被呼叫的內容
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # assertRaises 用 with 語法，確認 with 區塊內確實丟出指定型別的例外
        # 若不丟就測試失敗（代表函式未如預期拋錯）
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # assertRaisesRegex 除了驗證型別，還會用正視表達式比對錯誤訊息
        # 確認錯誤訊息內容符合預期，避免是別的 ValueError 誤觸發
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 一般斷言：確認正常輸入的輸出是否正確
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
