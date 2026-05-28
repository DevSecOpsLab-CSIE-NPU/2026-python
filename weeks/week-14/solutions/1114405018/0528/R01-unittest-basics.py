"""
R01：unittest 基本用法（記憶層，直接複製可執行）

本檔案示範三個最常見的單元測試情境：
1) 如何驗證 print 到終端機的文字內容
2) 如何使用 mock/patch 隔離外部相依（例如 API 物件）
3) 如何測試函式是否正確拋出例外與錯誤訊息

對應 Cookbook：
- 14.1 測試 stdout 輸出
- 14.2 在單元測試中給物件打補丁
- 14.3 在單元測試中測試例外情況

執行方式：
    python R01-unittest-basics.py
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ---------- 被測函式 ----------
def url_print(host, domain):
    # 將 host 與 domain 組成完整網址並輸出到 stdout。
    # 此函式本身沒有回傳值，測試時要改抓輸出內容。
    print(f"https://{host}.{domain}")


def parse_int(s):
    # 示範「先檢查再轉型」：空字串時主動拋出可讀性較高的錯誤。
    # 這讓呼叫端能知道錯誤原因，而不是得到較模糊的 int() 例外。
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    # 將資料存取責任交給傳入的 api 物件，便於測試時注入假物件（mock）。
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
class TestStdout(unittest.TestCase):
    def test_url_print(self):
        # 建立記憶體緩衝區，暫存 print 輸出，不污染實際終端機。
        buf = io.StringIO()
        # redirect_stdout 會在 with 區塊內，將所有 print 導向 buf。
        with redirect_stdout(buf):
            url_print("www", "example.com")
        # getvalue() 取回完整輸出字串；strip() 去除尾端換行符號後比對。
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
class TestPatch(unittest.TestCase):
    def test_fetch_user_with_mock(self):
        # MagicMock 可快速建立「可記錄呼叫行為」的假物件。
        fake_api = MagicMock()
        # 指定當 get 被呼叫時，回傳固定假資料。
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        # 驗證函式輸出是否符合預期。
        self.assertEqual(result["name"], "Alice")
        # 驗證依賴物件是否用正確參數被呼叫（行為測試）。
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        # 這個測試直接替換內建 print，避免真的輸出到終端機。
        # 好處是可精準檢查 print 是否被呼叫、呼叫次數與參數內容。
        url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
class TestExceptions(unittest.TestCase):
    def test_raises(self):
        # 只驗證「有拋出 ValueError」即可，不檢查訊息內容。
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        # 除了例外型別，也驗證錯誤訊息是否包含關鍵字。
        # 有助於確保錯誤訊息對使用者或除錯流程仍然友善。
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_normal_case(self):
        # 正常輸入時應回傳整數值，不應拋出例外。
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    # 直接執行此檔案時，啟動 unittest 測試探索與執行流程。
    unittest.main()
