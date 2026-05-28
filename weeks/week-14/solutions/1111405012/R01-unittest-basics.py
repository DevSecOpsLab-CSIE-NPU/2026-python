"""
R01：unittest 基本用法（記憶層 — 直接複製可執行）

對應 Cookbook：
- 14.1 測試 stdout 輸出
- 14.2 在單元測試中給物件打補丁
- 14.3 在單元測試中測試例外情況

執行：
    python R01-unittest-basics.py
"""
import io  # 用來建立記憶體中的文本串流，讓我們能夠捕捉 print 的輸出
import unittest  # Python 的單元測試框架，讓我們寫測試時能有一套統一的做法
from contextlib import redirect_stdout  # 臨時改變 stdout 的指向，用來測試 print 輸出
from unittest.mock import MagicMock, patch  # 模擬（mock）物件和函式，讓測試能夠隔離真實的相依性


# ---------- 被測函式（要被測試的函式，像是病人要被醫生檢查一樣） ----------
def url_print(host, domain):
    """組合主機和網域名稱，然後列印成 HTTPS URL"""
    print(f"https://{host}.{domain}")


def parse_int(s):
    """將字串轉成整數，如果是空字串就拋出錯誤"""
    if not s:  # 檢查字串是否為空（空白、None、空列表等都算空的）
        raise ValueError("空字串無法轉成整數")  # 主動拋出錯誤，讓呼叫端知道發生問題
    return int(s)  # 利用 Python 內建的 int() 函式進行轉換


def fetch_user(api, user_id):
    """透過 API 物件取得使用者資訊"""
    return api.get(f"/users/{user_id}")  # 呼叫 api 物件的 get 方法，取得使用者路由的資料


# ---------- 14.1 測試 stdout（標準輸出）----------
# 這裡展示「如何驗證程式是否正確地印出東西」
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        """測試 url_print 函式是否能正確組合並輸出 URL"""
        buf = io.StringIO()  # 建立一個「虛擬的輸出紙張」，模擬標準輸出
        with redirect_stdout(buf):  # 在這個區塊裡，所有 print 輸出都會寫到 buf，不會顯示在螢幕上
            url_print("www", "example.com")  # 執行要測試的函式
        # 從虛擬紙張取出內容、移除首尾空白、檢查是否與預期相符
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch（使用模擬物件替代真實物件） ----------
# 這裡展示「如何用假的 API 物件來測試程式，避免真的去呼叫網路服務"
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        """用模擬的 API 物件測試 fetch_user 函式是否正確"""
        fake_api = MagicMock()  # 建立一個假的 API 物件（它的行為完全由測試程式控制）
        fake_api.get.return_value = {"id": 1, "name": "Alice"}  # 指定這個假物件應該回傳什麼

        result = fetch_user(fake_api, 1)  # 用假物件呼叫要測試的函式

        # 驗證取得的資料是否正確
        self.assertEqual(result["name"], "Alice")
        # 驗證「假物件的 get 方法是否被正確地呼叫了一次，參數是 '/users/1'」
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")  # 使用 @patch 裝飾器暫時替換掉 Python 內建的 print 函式
    def test_url_print_via_patch(self, mock_print):  # 裝飾器會把模擬的 print 作為參數傳入
        """用 patch 直接替換掉 print 函式，測試是否被正確地呼叫"""
        url_print("api", "example.com")  # 執行要測試的函式
        # 驗證「模擬的 print 被呼叫了一次，參數是指定的 URL 字串」
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外（驗證程式是否在對的時機拋出正確的錯誤） ----------
# 這裡展示「如何測試錯誤處理的邏輯"
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        """測試當輸入空字串時，parse_int 是否會拋出 ValueError"""
        with self.assertRaises(ValueError):  # 期望在這個區塊裡會拋出 ValueError
            parse_int("")  # 執行會導致錯誤的程式碼

    def test_raises_with_message(self):
        """測試不只是拋出 ValueError，而且錯誤訊息裡要有『空字串』這個字"""
        # assertRaisesRegex 不但檢查例外類型，也檢查錯誤訊息內容
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        """測試正常情況：輸入有效的數字字串時，是否能正確轉換"""
        self.assertEqual(parse_int("42"), 42)  # 驗證轉換結果是否等於 42


if __name__ == "__main__":
    unittest.main()
