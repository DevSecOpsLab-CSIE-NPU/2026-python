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


# ---------- 被測函式 ----------
def url_print(host, domain):
    """將 host 與 domain 組成 URL 並印出。

    這個簡單函式用來示範如何在測試中捕捉 stdout（標準輸出），
    以及如何用 patch 替換內建的 print 以驗證呼叫行為。
    """
    print(f"https://{host}.{domain}")


def parse_int(s):
    """把字串轉成整數，遇到空字串會拋出 ValueError。

    範例中使用此函式來示範單元測試如何檢查例外與例外內容。
    """
    if not s:
        # 當 s 為空（例如空字串或 None 時），明確拋出帶有說明的 ValueError
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    """透過傳入的 api 物件呼叫 get，並回傳結果。

    這裡不實作網路呼叫，而是假設外部會提供一個具有 get 方法的物件（例如 requests-like API），
    方便在測試中使用 MagicMock 進行替身（mock）。
    """
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        # 使用 io.StringIO 捕捉標準輸出，redirect_stdout 會臨時將 stdout 導向該 buffer
        buf = io.StringIO()
        with redirect_stdout(buf):
            url_print("www", "example.com")
        # 以 strip 移除尾端換行，再與期望字串比對
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        # 使用 MagicMock 建立假 API，設定 get 的回傳值
        fake_api = MagicMock()
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        # 呼叫被測函式，並驗證回傳內容與呼叫參數
        result = fetch_user(fake_api, 1)

        self.assertEqual(result["name"], "Alice")
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        # 使用 patch 取代內建的 print，避免實際印出到 stdout，並可驗證呼叫細節
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # 驗證傳入空字串會拋出 ValueError
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # 除了檢查例外類型，也可以檢查例外訊息是否包含特定字串
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 正常情況下應該回傳轉換後的整數
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
