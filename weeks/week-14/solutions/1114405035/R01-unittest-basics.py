"""
R01：unittest 基本用法（記憶層 — 直接複製可執行）

對應 Cookbook：
- 14.1 測試 stdout 輸出
- 14.2 在單元測試中給物件打補丁
- 14.3 在單元測試中測試例外情況

執行：
    python R01-unittest-basics.py
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ---------- 被測函式 (Functions to be tested) ----------
def url_print(host, domain):
    """印出完整的 URL 地址"""
    print(f"https://{host}.{domain}")


def parse_int(s):
    """將字串轉換為整數，若字串為空則拋出 ValueError"""
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    """從指定的 API 物件中取得使用者資料"""
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout (Testing Standard Output) ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        """測試 url_print 函式是否正確將輸出印至 stdout"""
        # 建立一個記憶體緩衝區
        buf = io.StringIO()
        # 使用 redirect_stdout 將 print 的輸出導向到 buf
        with redirect_stdout(buf):
            url_print("www", "example.com")
        
        # 驗證輸出內容（移除結尾換行符後進行比較）
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch (模擬物件與補丁) ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        """使用 MagicMock 模擬 API 物件的行為"""
        # 建立一個假的 API 物件
        fake_api = MagicMock()
        # 設定當呼叫 fake_api.get 時應回傳的資料
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        # 執行函式
        result = fetch_user(fake_api, 1)

        # 驗證結果是否與模擬的回傳值一致
        self.assertEqual(result["name"], "Alice")
        # 驗證 api.get 是否被以正確的參數呼叫過一次
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        """使用 @patch 裝飾器來攔截內建的 print 函式"""
        url_print("api", "example.com")
        
        # 驗證 print 是否被以預期的字串呼叫過一次
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 (Testing Exceptions) ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        """驗證當輸入為空字串時，是否會拋出 ValueError"""
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        """驗證拋出的例外是否包含特定的錯誤訊息 (使用正則表達式)"""
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        """驗證正常數字字串的轉換是否正確"""
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
