"""
R01：unittest 基本用法（加強繁中註解版）

本檔示範三件單元測試最常見的事情：
1. 測試函式印出的文字（stdout）
2. 用 mock 取代真實外部依賴（例如 API）
3. 驗證函式是否拋出正確例外與訊息

執行方式：
    python R01-unittest-basics.py
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ============================================================
# 被測函式（Production Code）
# ============================================================
def url_print(host, domain):
    """
    將 host 與 domain 組成完整網址後印出。

    範例：
        host="www", domain="example.com"
        -> 印出 "https://www.example.com"
    """
    print(f"https://{host}.{domain}")


def parse_int(s):
    """
    把字串轉成整數。

    教學重點：
    - 主動對空字串做防呆，丟出 ValueError。
    - 讓測試可以驗證「拋出例外」與「例外訊息」兩件事。
    """
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    """
    透過注入的 api 物件查詢使用者。

    教學重點：
    - 讓外部依賴（api）從參數傳入，
      測試時就能換成 MagicMock，不必真的打網路。
    """
    return api.get(f"/users/{user_id}")


# ============================================================
# 14.1 測試 stdout 輸出
# ============================================================
class TestStdout(unittest.TestCase):
    """示範如何驗證 print 的實際輸出內容。"""

    def test_url_print(self):
        # StringIO 可以當作記憶體中的「假終端輸出緩衝區」。
        buf = io.StringIO()

        # redirect_stdout 會把 with 區塊內的 print 都導到 buf。
        with redirect_stdout(buf):
            url_print("www", "example.com")

        # strip() 去掉尾端換行，避免因為換行差異導致測試失敗。
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ============================================================
# 14.2 mock.patch 與 MagicMock
# ============================================================
class TestPatch(unittest.TestCase):
    """示範如何用 mock 測試「呼叫行為」與「參數是否正確」。"""

    def test_fetch_user_with_mock(self):
        # 建立假的 API 物件。
        fake_api = MagicMock()

        # 預先指定 fake_api.get() 被呼叫時要回傳的資料。
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        # 呼叫被測函式。
        result = fetch_user(fake_api, 1)

        # 驗證回傳資料內容。
        self.assertEqual(result["name"], "Alice")

        # 驗證 get() 被呼叫一次，且參數正確。
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        """
        用 patch 暫時把內建 print 換成 mock 版本。
        這樣不需要真的輸出到終端，也能驗證呼叫內容。
        """
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ============================================================
# 14.3 測試例外
# ============================================================
class TestExceptions(unittest.TestCase):
    """示範 assertRaises 與 assertRaisesRegex。"""

    def test_raises(self):
        # 只驗證「有拋出 ValueError」。
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # 進一步驗證錯誤訊息是否包含指定關鍵字。
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 一般成功路徑也要測，避免只測錯誤情境。
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    # 直接執行此檔案時，unittest 會自動收集 TestCase 並執行。
    unittest.main()
