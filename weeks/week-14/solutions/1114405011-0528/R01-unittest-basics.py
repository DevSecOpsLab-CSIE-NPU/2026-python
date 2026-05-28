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
    """組出網址並直接輸出到 stdout。"""
    print(f"https://{host}.{domain}")


def parse_int(s):
    """將字串轉成整數；若是空字串則主動丟出 ValueError。"""
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    """透過注入的 api 物件取得使用者資料。"""
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        # 建立記憶體文字緩衝區，暫存 print 的輸出內容。
        buf = io.StringIO()
        # 將區塊內所有 stdout 重導向到 buf，避免污染終端輸出。
        with redirect_stdout(buf):
            url_print("www", "example.com")
        # strip() 去除行尾換行，再比對完整字串內容。
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        # 用 MagicMock 建立假的 API 客戶端，完全不需真的打網路。
        fake_api = MagicMock()
        # 先定義 get() 被呼叫時要回傳的假資料。
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        # 驗證功能結果：拿到的 name 應為 Alice。
        self.assertEqual(result["name"], "Alice")
        # 驗證互動行為：get() 是否只被呼叫一次，且路徑完全正確。
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        # patch 後，url_print 內的 print 會被替換成 mock_print。
        url_print("api", "example.com")
        # 驗證 print 的參數是否與預期一致。
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # 確認 parse_int("") 會丟 ValueError。
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # 除了例外型別，也比對訊息中是否包含關鍵字「空字串」。
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 正常輸入應回傳對應整數值。
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    # 直接執行此檔時，啟動 unittest 測試執行器。
    unittest.main()
