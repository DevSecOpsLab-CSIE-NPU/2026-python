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
# 說明：以下為範例中要被測試的簡單函式。這些函式刻意保持簡潔，方便示範如何
# 使用 `unittest` 捕捉輸出、使用 mock，以及檢查例外情況。
def url_print(host, domain):
    # 將 host 與 domain 組合成完整 URL 並輸出到 stdout
    # 例：host='www', domain='example.com' -> 輸出 'https://www.example.com'
    print(f"https://{host}.{domain}")


def parse_int(s):
    # 將字串轉成整數，若傳入空字串則會拋出 ValueError
    # 注意：此函式不處理非數字字串（會由 int() 本身拋出例外）
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    # 範例：模擬一個簡單的 API 客戶端介面，呼叫其 `get` 方法取得使用者資料
    # 這樣的設計方便在單元測試中以 MagicMock 或 patch 替代 `api`，驗證呼叫與回傳
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        # 示範如何捕捉函式的 stdout 輸出：
        # 1) 建立一個 StringIO 當作暫時的輸出緩衝區
        # 2) 使用 contextlib.redirect_stdout 將 stdout 重導向到該緩衝區
        # 3) 呼叫要測試的函式，最後比對緩衝區的內容
        buf = io.StringIO()
        with redirect_stdout(buf):
            url_print("www", "example.com")
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        # 使用 MagicMock 來模擬一個簡單的 API 物件：
        # - 設定 fake_api.get 的回傳值
        # - 呼叫 fetch_user 並驗證回傳內容與 mock 的呼叫參數
        fake_api = MagicMock()
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        self.assertEqual(result["name"], "Alice")
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        # 使用 patch 直接替換內建的 print 函式，避免實際輸出到 stdout
        # 這可以用來驗證 print 是否以預期的字串被呼叫
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # 驗證對空字串會拋出 ValueError
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # 進一步檢查拋出的例外訊息包含指定文字
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 正常情況：可將數字字串轉為整數
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
