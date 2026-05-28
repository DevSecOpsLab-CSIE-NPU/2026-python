"""
R01：unittest 基本用法（記憶層 — 直接複製可執行）

這個範例把三個最常見的單元測試情境放在同一個檔案裡：
- 驗證函式是否有印出正確內容到標準輸出
- 使用 mock / patch 隔離外部依賴，避免真的打到 API 或真實函式
- 驗證例外是否真的被丟出，而且錯誤訊息是否符合預期

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
# 這一段故意保持簡單，讓焦點集中在「怎麼測」而不是「業務邏輯有多複雜」。
def url_print(host, domain):
    # 直接把網址印到標準輸出，方便示範如何攔截 print 的結果。
    print(f"https://{host}.{domain}")


def parse_int(s):
    # 空字串不應該被當成合法整數，先主動丟出 ValueError，讓呼叫端可以明確處理。
    if not s:
        raise ValueError("空字串無法轉成整數")
    # 其餘情況交給 Python 內建 int() 處理，讓測試同時覆蓋正常與錯誤流程。
    return int(s)


def fetch_user(api, user_id):
    # 這裡把 api 當成外部依賴，測試時可以用 mock 替代，避免真的發送請求。
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        # StringIO 是記憶體中的文字緩衝區，可以暫時接住標準輸出內容。
        buf = io.StringIO()
        # redirect_stdout 會把 print 的輸出導向 buf，測試完成後就能檢查內容。
        with redirect_stdout(buf):
            url_print("www", "example.com")
        # strip() 是為了去掉結尾換行，避免測試只因為換行字元不同而失敗。
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        # MagicMock 可以模擬一個有 get 方法的 api 物件，讓測試不依賴真實服務。
        fake_api = MagicMock()
        # 先設定回傳值，等下呼叫 fetch_user 時，就會拿到我們預先安排好的資料。
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        # 被測函式只需要知道 api 有 get 這個方法，不需要知道它背後是不是網路請求。
        result = fetch_user(fake_api, 1)

        # 驗證回傳資料是否正確，確認程式真的拿到了 mock 設定的內容。
        self.assertEqual(result["name"], "Alice")
        # 同時檢查方法呼叫參數，確認程式組出的路徑格式也正確。
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        # patch 會把 builtins.print 換成 mock，所以這裡不會真的印到終端機。
        # 測試重點是確認 print 是否被呼叫，以及傳入的字串是否正確。
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # assertRaises 會檢查區塊內是否真的丟出指定例外。
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # 如果不只要例外型別，還要確認錯誤訊息內容，可以用 assertRaisesRegex。
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 也要保留正常路徑的測試，避免函式只在錯誤情況下被驗證。
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    # 直接執行這個檔案時，unittest.main() 會自動收集並執行所有測試案例。
    unittest.main()
