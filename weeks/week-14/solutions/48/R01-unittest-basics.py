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
    print(f"https://{host}.{domain}")


def parse_int(s):
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        buf = io.StringIO()  # 建立記憶體中的文字緩衝區，接住 print 輸出
        with redirect_stdout(buf):
            url_print("www", "example.com")
        # strip() 去掉換行，避免平台差異造成測試不穩定
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        fake_api = MagicMock()  # 建立假的 API 物件，避免真的發送請求
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        self.assertEqual(result["name"], "Alice")
        # 驗證呼叫次數與參數都正確
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # 驗證指定輸入會拋出 ValueError
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # 同時驗證例外訊息包含關鍵字
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
