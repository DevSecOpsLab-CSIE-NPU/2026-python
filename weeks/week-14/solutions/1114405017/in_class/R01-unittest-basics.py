"""
R01：unittest 基本用法（記憶層 — 可直接執行的範例）

此檔案示範如何使用 Python 標準庫的 unittest 模組做三種常見任務：
- 測試標準輸出（stdout）的輸出內容
- 在測試中使用 mock 或 patch 來替換外部依賴
- 驗證函式在例外情況下會正確拋出例外

下列註解皆為繁體中文說明，說明每個函式、測試類別的用途與重要細節。

執行：
    python R01-unittest-basics.py
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ---------- 被測函式 ----------
def url_print(host, domain):
    """把 host 與 domain 組成完整 URL 並印出到 stdout。

    - 因為測試會捕捉 stdout，所以此函式以 print 實作而非回傳字串，
      測試範例會示範如何攔截並斷言輸出值。
    - 參數 host / domain 預期為可格式化為字串的值。
    """
    print(f"https://{host}.{domain}")


def parse_int(s):
    """嘗試把字串轉成整數，空字串會拋出 ValueError。

    - 若傳入空字串或 False-y 值，明確拋出 ValueError，方便在測試中使用 assertRaises。
    - 否則使用內建 int() 做轉換，若輸入不能轉換（例如 'a'）會由 int() 拋出 ValueError。
    """
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    """透過傳入的 api 物件呼叫 get，並回傳結果。

    - 在真實應用中 api 可能是 requests.Session 或自訂的 client。
    - 在測試中會使用 MagicMock 來模擬 api，並驗證呼叫參數是否正確。
    """
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        # 使用 StringIO 當作虛擬 stdout，並用 redirect_stdout 將 print 的輸出導向此緩衝區。
        # 測試重點：確保 url_print 實際印出的字串符合預期。
        buf = io.StringIO()
        with redirect_stdout(buf):
            url_print("www", "example.com")
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        # 使用 MagicMock 模擬外部 API，避免在單元測試中做真正的網路請求。
        fake_api = MagicMock()
        # 設定假回傳值，模擬 API 回傳 JSON-like dict
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        # 呼叫被測函式，並檢查回傳與呼叫參數
        result = fetch_user(fake_api, 1)

        self.assertEqual(result["name"], "Alice")
        # 驗證 api.get 是否以正確的路徑被呼叫一次
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        # 以 patch 裝飾器替換 builtins.print，避免實際輸出到 stdout，方便直接檢查呼叫參數
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # 驗證 parse_int 在收到空字串時會拋出 ValueError
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # 除了例外類型，也可以用 assertRaisesRegex 檢查例外訊息內容
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 正常情況下能夠正確轉換
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
