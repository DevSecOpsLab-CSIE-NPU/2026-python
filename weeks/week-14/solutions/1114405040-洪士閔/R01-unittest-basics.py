"""
R01 - unittest 基礎練習

本檔案示範：
1. 如何測試印到 stdout 的內容
2. 如何使用 mock / patch 模擬外部物件或函式
3. 如何測試例外是否正確被拋出

執行方式：
    python R01-unittest-basics.py
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ---------- 被測試的函式 ----------
def url_print(host, domain):
    """把 host 和 domain 組成網址後印出。"""
    print(f"https://{host}.{domain}")


def parse_int(s):
    """把字串轉成整數；如果傳入空值，就主動丟出 ValueError。"""
    if not s:
        raise ValueError("輸入不可為空")
    return int(s)


def fetch_user(api, user_id):
    """透過傳入的 api 物件取得使用者資料。"""
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        # StringIO 可以暫時當成一個文字緩衝區，用來接住 print 的輸出。
        buf = io.StringIO()

        # redirect_stdout 會把 print 的內容導到 buf，而不是直接顯示在終端機。
        with redirect_stdout(buf):
            url_print("www", "example.com")

        # strip() 移除 print 自動加上的換行，再比對輸出是否正確。
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        # MagicMock 用來建立假的 api 物件，避免測試時真的呼叫外部服務。
        fake_api = MagicMock()
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        # 確認回傳資料正確。
        self.assertEqual(result["name"], "Alice")
        # 確認 get() 只被呼叫一次，且參數是指定的路徑。
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        # patch 會把 builtins.print 暫時換成 mock_print，方便檢查 print 有沒有被呼叫。
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # assertRaises 可以確認指定的例外是否真的被丟出。
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # assertRaisesRegex 除了確認例外類型，也會檢查錯誤訊息是否符合指定文字。
        with self.assertRaisesRegex(ValueError, "不可為空"):
            parse_int("")

    def test_normal_case(self):
        # 一般正常輸入時，應該可以成功轉成整數。
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
