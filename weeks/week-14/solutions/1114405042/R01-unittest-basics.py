"""R01：unittest 基本用法（記憶層 — 直接複製可執行）

本檔範例包含三個主題：
- 14.1 測試 stdout 輸出
- 14.2 在單元測試中給物件打補丁（mock/patch）
- 14.3 在單元測試中測試例外情況

執行方式：
    python R01-unittest-basics.py

註：以下所有新增的註解與 docstring 均為繁體中文說明，方便學習與閱讀。
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ---------- 被測函式 ----------
def url_print(host, domain):
    """將 host 與 domain 組合成 https URL 並印出到 stdout。

    參數：
      host (str): 主機名稱或子域（例如 'www' 或 'api'）
      domain (str): 網域名稱（例如 'example.com'）

    回傳：
      無（直接印出字串）
    """
    print(f"https://{host}.{domain}")


def parse_int(s):
    """將字串轉成整數。

    如果輸入為空字串，會丟出 ValueError，呼叫端可用單元測試驗證例外行為。

    參數：
      s (str): 要轉換的字串

    回傳：
      int: 轉換後的整數值

    例外：
      ValueError: 當 s 為空字串時拋出
    """
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    """透過提供的 api 物件取得指定使用者資料。

    參數：
      api: 具有 .get(path) 方法的物件（例如 HTTP client 或 mock 物件）
      user_id: 使用者 ID，會放入 API 路徑中

    回傳：
      api.get 的回傳結果（通常為 dict 或 API 回應物件）
    """
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    """測試輸出到標準輸出的行為。"""

    def test_url_print(self):
        """使用 `redirect_stdout` 捕捉 print 的輸出，確保格式正確。"""
        buf = io.StringIO()
        # 將 stdout 重導到 StringIO，方便在測試中檢查輸出內容
        with redirect_stdout(buf):
            url_print("www", "example.com")
        # 去除前後空白後比對字串
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    """示範用 MagicMock 模擬物件與用 patch 替換內建函式的方法。"""

    def test_fetch_user_with_mock(self):
        """使用 MagicMock 模擬一個簡單的 API client，檢查 fetch_user 的行為。"""
        fake_api = MagicMock()
        # 設定 fake_api.get 的回傳值，模擬 API 回傳的 JSON 物件
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        # 驗證回傳內容與 mock 被正確呼叫
        self.assertEqual(result["name"], "Alice")
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        """使用 patch 替換內建的 print，驗證 url_print 是否呼叫 print 並傳入預期字串。"""
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    """測試函式在錯誤或例外情況下的行為。"""

    def test_raises(self):
        """當輸入為空字串時，parse_int 應該會丟出 ValueError。"""
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        """除了檢查例外類型，也可以檢查例外訊息是否包含特定字串。"""
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        """正常情況，字串 '42' 應該能正確轉成整數 42。"""
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
