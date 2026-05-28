"""
R01：unittest 基本用法（記憶層 — 直接複製可執行）

對應 Cookbook：
- 14.1 測試 stdout 輸出
- 14.2 在單元測試中給物件打補丁
- 14.3 在單元測試中測試例外情況

執行：
    python R01-unittest-basics.py
"""
import io  # 用於在記憶體中建立字串緩衝區 (StringIO)
import unittest  # Python 內建的單元測試框架
from contextlib import redirect_stdout  # 用於將標準輸出 (stdout) 重新導向到指定物件
from unittest.mock import MagicMock, patch  # 用於建立假物件 (mock) 和替換目標 (patch)


# ---------- 被測函式 ----------
# 這些是我們接下來要進行單元測試的目標函式
def url_print(host, domain):
    """將組合好的 URL 直接印出到標準輸出 (stdout)"""
    print(f"https://{host}.{domain}")


def parse_int(s):
    """將字串解析為整數。如果傳入空字串或 None，則主動拋出 ValueError 例外"""
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    """模擬透過某個 API 物件呼叫 get 方法來取得使用者資料"""
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    """示範如何測試會將結果輸出到終端機 (stdout) 的函式"""
    def test_url_print(self):
        buf = io.StringIO()  # 準備一個存在記憶體中的字串緩衝區來攔截輸出
        with redirect_stdout(buf):  # 攔截區塊內所有的 print 輸出，導向到 buf
            url_print("www", "example.com")  # 執行被測函式
        
        # 驗證緩衝區內的文字是否與預期相符 (使用 strip() 去除尾部換行符號)
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    """示範如何使用 Mock (假物件) 來隔離外部依賴 (如 API 呼叫、系統函式)"""
    def test_fetch_user_with_mock(self):
        # 建立一個假的 API 物件，這樣測試時就不會真的發出網路請求
        fake_api = MagicMock()
        # 設定當這個假物件的 get 方法被呼叫時，要回傳什麼固定資料
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        # 傳入假物件來執行被測函式
        result = fetch_user(fake_api, 1)

        # 驗證回傳結果是否符合我們在 mock 設定的資料
        self.assertEqual(result["name"], "Alice")
        # 驗證假物件的 get 方法是否曾經被正確的參數呼叫過「恰好一次」
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")  # 攔截並替換內建的 print 函式，將其轉為 mock 物件傳入測試
    def test_url_print_via_patch(self, mock_print):
        url_print("api", "example.com")  # 執行會呼叫 print 的函式
        # 驗證內建的 print 是否被正確的字串呼叫
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    """示範如何測試程式是否在特定情況下正確拋出錯誤 (Exception)"""
    def test_raises(self):
        # assertRaises 用於確認區塊內的程式會拋出指定的例外型別
        with self.assertRaises(ValueError):
            parse_int("")  # 預期傳入空字串會引發 ValueError

    def test_raises_with_message(self):
        # assertRaisesRegex 不只確認例外型別，還利用正規表示式比對錯誤訊息內容是否正確
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 除了測試例外，也應該保留正常的測試案例 (Happy path)
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()  # 當直接執行此檔案時，啟動 unittest 測試執行器
