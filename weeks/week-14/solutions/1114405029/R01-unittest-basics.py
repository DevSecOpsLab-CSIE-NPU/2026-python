"""
R01：unittest 基本用法（記憶層 — 直接複製可執行）

對應 Cookbook：
- 14.1 測試 stdout 輸出
- 14.2 在單元測試中給物件打補丁
- 14.3 在單元測試中測試例外情況

執行：
    python R01-unittest-basics.py
"""

# io 模組：
# 這裡主要使用 io.StringIO()
# StringIO 可以建立一個「像檔案一樣的字串緩衝區」
# 用來暫時接收 print() 印出來的內容
import io

# unittest 是 Python 內建的單元測試框架
# 可以用來建立測試類別、測試方法、斷言 assertEqual / assertRaises 等
import unittest

# redirect_stdout 可以暫時把標準輸出 stdout 重新導向到指定物件
# 也就是說，原本 print() 會印到終端機
# 但使用 redirect_stdout(buf) 後，print() 的內容會被存到 buf 裡
from contextlib import redirect_stdout

# MagicMock：
# 用來建立假的物件，模擬真實物件的方法與回傳值
#
# patch：
# 用來暫時替換某個函式、方法或物件
# 常用在測試時避免真的呼叫外部功能
from unittest.mock import MagicMock, patch


# ---------- 被測函式 ----------
# 這一區放的是「真正要被 unittest 測試的函式」
# 單元測試通常會先準備一些功能函式
# 再另外寫測試類別去驗證這些函式是否正確


# url_print(host, domain)：
# 功能：
#   根據傳入的 host 與 domain 組合出網址
#   並使用 print() 輸出
#
# 例如：
#   url_print("www", "example.com")
#
# 會輸出：
#   https://www.example.com
#
# 注意：
#   這個函式不是 return 字串
#   而是直接 print() 到標準輸出
#   所以測試時不能直接用 result = url_print(...)
#   必須測試 stdout 輸出的內容
def url_print(host, domain):
    print(f"https://{host}.{domain}")


# parse_int(s)：
# 功能：
#   將字串 s 轉換成整數
#
# 正常情況：
#   parse_int("42") 會回傳整數 42
#
# 例外情況：
#   如果 s 是空字串或空值
#   就主動丟出 ValueError
#
# raise ValueError(...)：
#   表示程式遇到不合法的資料
#   主動拋出錯誤，讓呼叫者知道這個輸入不能處理
def parse_int(s):
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


# fetch_user(api, user_id)：
# 功能：
#   模擬呼叫 API 取得使用者資料
#
# api：
#   代表一個有 get() 方法的物件
#
# user_id：
#   使用者編號
#
# 例如：
#   fetch_user(api, 1)
#
# 會呼叫：
#   api.get("/users/1")
#
# 測試時通常不會真的連線到外部 API
# 而是使用 MagicMock 建立假的 api 物件
def fetch_user(api, user_id):
    return api.get(f"/users/{user_id}")


# ---------- 14.1 測試 stdout ----------
# TestStdout 是一個測試類別
#
# unittest 的測試類別通常要繼承 unittest.TestCase
# 這樣類別裡面才能使用：
#   self.assertEqual()
#   self.assertRaises()
#   self.assertRaisesRegex()
# 等測試方法
class TestStdout(unittest.TestCase):

    # 測試方法名稱必須以 test_ 開頭
    # unittest.main() 執行時，才會自動找到並執行這個測試
    def test_url_print(self):

        # 建立一個 StringIO 緩衝區
        # 用來接收 print() 輸出的文字
        buf = io.StringIO()

        # redirect_stdout(buf)：
        # 暫時把標準輸出 stdout 導向 buf
        #
        # 在 with 區塊裡面的 print()
        # 不會真的印到終端機
        # 而是會寫入 buf
        with redirect_stdout(buf):

            # 呼叫被測函式
            # 這個函式會 print("https://www.example.com")
            url_print("www", "example.com")

        # buf.getvalue()：
        # 取得剛剛被 print() 寫入 buf 的完整字串
        #
        # strip()：
        # 去掉前後空白與換行
        #
        # 因為 print() 預設會在最後加上換行符號 \n
        # 所以這裡用 strip() 移除換行，方便比對
        #
        # assertEqual(a, b)：
        # 檢查 a 是否等於 b
        # 如果不相等，測試就會失敗
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ---------- 14.2 mock.patch ----------
# 這一區示範如何使用 mock 物件與 patch
#
# mock 的用途：
#   在測試時建立假的物件或假的函式
#   避免真的呼叫外部 API、資料庫、網路、檔案系統等
#
# 好處：
#   1. 測試速度更快
#   2. 測試結果更穩定
#   3. 可以精準檢查某個方法是否有被正確呼叫
class TestPatch(unittest.TestCase):

    # 測試 fetch_user() 是否正確呼叫 api.get()
    def test_fetch_user_with_mock(self):

        # 建立一個假的 api 物件
        # MagicMock 可以模擬任何物件的方法
        fake_api = MagicMock()

        # 設定 fake_api.get() 的回傳值
        # 也就是說，只要程式呼叫 fake_api.get(...)
        # 就會回傳 {"id": 1, "name": "Alice"}
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        # 呼叫被測函式
        # 這裡傳入的是假的 api，不是真正的 API
        result = fetch_user(fake_api, 1)

        # 檢查回傳結果中的 name 是否為 Alice
        self.assertEqual(result["name"], "Alice")

        # assert_called_once_with(...)：
        # 檢查 fake_api.get 是否「剛好被呼叫一次」
        # 而且呼叫時的參數必須是 "/users/1"
        #
        # 這可以確認 fetch_user() 內部有正確組出 API 路徑
        fake_api.get.assert_called_once_with("/users/1")

    # @patch("builtins.print")：
    # 這會暫時把 Python 內建的 print 函式替換成 mock 物件
    #
    # 也就是說，在這個測試方法執行期間
    # url_print() 裡面的 print() 不會真的印出文字
    # 而是會被 mock_print 記錄下來
    #
    # mock_print 會由 patch 自動傳入測試方法
    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):

        # 呼叫被測函式
        # 這裡的 print 已經被 patch 成 mock_print
        url_print("api", "example.com")

        # 檢查 print 是否被呼叫一次
        # 且輸出的內容是否正確
        mock_print.assert_called_once_with("https://api.example.com")


# ---------- 14.3 測試例外 ----------
# 這一區示範如何測試「錯誤情況」
#
# 單元測試不只要測正常輸入
# 也要測錯誤輸入是否會產生預期的例外
class TestExceptions(unittest.TestCase):

    # 測試 parse_int("") 是否會丟出 ValueError
    def test_raises(self):

        # assertRaises(ValueError)：
        # 表示 with 區塊內的程式預期應該要丟出 ValueError
        #
        # 如果真的丟出 ValueError：
        #   測試通過
        #
        # 如果沒有丟出 ValueError：
        #   測試失敗
        #
        # 如果丟出其他錯誤：
        #   測試也會失敗
        with self.assertRaises(ValueError):
            parse_int("")

    # 測試例外訊息是否符合指定文字
    def test_raises_with_message(self):

        # assertRaisesRegex(ValueError, "空字串")：
        # 除了檢查是否丟出 ValueError
        # 還會檢查錯誤訊息是否包含或符合「空字串」
        #
        # parse_int("") 會丟出：
        #   ValueError("空字串無法轉成整數")
        #
        # 因為錯誤訊息中包含「空字串」
        # 所以這個測試會通過
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    # 測試正常情況
    def test_normal_case(self):

        # parse_int("42") 應該要回傳整數 42
        #
        # 注意：
        #   "42" 是字串
        #   42 是整數
        #
        # parse_int() 內部使用 int(s)
        # 所以最後結果應該是整數型態
        self.assertEqual(parse_int("42"), 42)


# 這是 Python 常見的主程式進入點寫法
#
# __name__：
#   代表目前這個檔案是怎麼被執行的
#
# 如果這個檔案是直接被執行：
#   __name__ 會等於 "__main__"
#
# 如果這個檔案是被其他檔案 import：
#   __name__ 不會等於 "__main__"
#
# 因此這樣寫可以避免：
#   其他檔案 import 這個檔案時，自動執行 unittest.main()
if __name__ == "__main__":

    # unittest.main()：
    # 自動尋找目前檔案中所有繼承 unittest.TestCase 的測試類別
    # 並執行所有以 test_ 開頭的測試方法
    unittest.main()