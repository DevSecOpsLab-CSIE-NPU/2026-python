# R01. unittest 基本用法示範
# 這個檔案展示 Python `unittest` 的基礎功能：
# - 捕捉標準輸出檢查輸出結果
# - 使用 `unittest.mock` 補丁 (patch) 取代物件或函式
# - 測試例外是否依預期被丟出

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ---------- 被測函式 ----------

def url_print(host, domain):
    """輸出組合成的 URL。"""
    print(f"https://{host}.{domain}")


def parse_int(s):
    """將字串轉成整數，空字串會丟出 ValueError。"""
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    """從傳入的 API 物件呼叫 get()，取得使用者資料。"""
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout 輸出 ----------

class TestStdout(unittest.TestCase):
    def test_url_print(self):
        # 利用 StringIO 暫時接住 print 的 stdout
        buf = io.StringIO()
        with redirect_stdout(buf):
            url_print("www", "example.com")

        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 使用 mock.patch 補丁 ----------

class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        # 建立假的 API 物件，並指定 get() 回傳值
        fake_api = MagicMock()
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        self.assertEqual(result["name"], "Alice")
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        # patch 內建 print，確認 url_print 會呼叫 print() 並輸出正確字串
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------

class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # 只要 parse_int 傳入空字串，就應該丟出 ValueError
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # 更進一步檢查例外訊息是否包含特定文字
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 一般正常輸入應該回傳對應整數
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
