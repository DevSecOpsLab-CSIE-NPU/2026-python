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
    """輸出網址"""
    print(f"https://{host}.{domain}")


def parse_int(s):
    """將字串轉換為整數，空字串會拋出例外"""
    if not s:  # 檢查字串是否為空
        raise ValueError("空字串無法轉成整數")
    return int(s)  # 轉換為整數


def fetch_user(api, user_id):
    """透過 API 取得使用者資料"""
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        """測試函式是否輸出正確的字串到標準輸出"""
        buf = io.StringIO()  # 建立字串緩衝區
        with redirect_stdout(buf):  # 將 stdout 重導向到緩衝區
            url_print("www", "example.com")
        # 檢查輸出內容是否符合預期
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class Te"""使用 MagicMock 模擬 API 物件進行測試"""
        fake_api = MagicMock()  # 建立假的 API 物件
        # 設定 get 方法的返回值
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        # 驗證返回值正確
        self.assertEqual(result["name"], "Alice")
        # 驗證 get 方法是否被正確呼叫
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")  # 使用裝飾器模擬 print 函式
    def test_url_print_via_patch(self, mock_print):
        """使用 patch 模擬全域的 print 函式"""
        url_print("api", "example.com")
        # 驗證 print 是否被正確呼叫
    def test_url_print_via_patch(self, mock_print):
        url_print("api", "example.com")
        """測試函式是否拋出預期的例外"""
        with self.assertRaises(ValueError):  # 驗證會拋出 ValueError
            parse_int("")

    def test_raises_with_message(self):
        """測試例外訊息是否符合預期"""
        with self.assertRaisesRegex(ValueError, "空字串"):  # 驗證例外訊息中包含「空字串」
            parse_int("")

    def test_normal_case(self):
        """測試正常情況——合有效的輸入"""

    def test_raises_with_message(self):
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
