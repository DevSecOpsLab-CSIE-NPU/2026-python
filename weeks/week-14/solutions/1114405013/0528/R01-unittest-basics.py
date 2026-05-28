"""
R01：unittest 基本用法（記憶層 — 直接複製可執行）

對應 Cookbook：
- 14.1 測試 stdout 輸出
- 14.2 在單元測試中給物件打補丁 (Mock / Patch)
- 14.3 在單元測試中測試例外情況

涵蓋的主題：
  A. 基本斷言方法（assertEqual / assertTrue / assertIn …）
  B. setUp / tearDown 生命週期
  C. 測試 stdout（redirect_stdout）
  D. Mock：MagicMock、return_value、side_effect
  E. @patch 裝飾器與 patch 上下文管理器
  F. 測試例外（assertRaises / assertRaisesRegex）
  G. 測試套件（TestSuite）與自訂執行

執行：
    python R01-unittest-basics.py
"""
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# ==========================================================
# 被測函式（System Under Test）
# 以下三支函式分別對應到 14.1（stdout）、14.2（mock）、14.3（例外）
# ==========================================================

def url_print(host, domain):
    """把 host 和 domain 組合成 URL 並印出。"""
    print(f"https://{host}.{domain}")


def parse_int(s):
    """將字串轉為整數；空字串時拋出 ValueError。"""
    if not s:
        raise ValueError("空字串無法轉成整數")
    return int(s)


def fetch_user(api, user_id):
    """呼叫 api.get() 取得使用者資料（真實專案中可能是 HTTP 請求）。"""
    return api.get(f"/users/{user_id}")


def is_adult(age):
    """判斷年齡是否成年（>= 18）。"""
    return age >= 18


def get_user_display_name(user):
    """從 dict 中取出顯示名稱，缺少欄位時回傳 '匿名使用者'。"""
    first = user.get("first_name", "")
    last = user.get("last_name", "")
    name = f"{first} {last}".strip()
    return name if name else "匿名使用者"


# ==========================================================
# A — 基本斷言方法（Assert Methods）
# unittest.TestCase 提供數十種斷言，以下是最常用的幾種
# ==========================================================
class TestAssertions(unittest.TestCase):
    """展示各種 assert* 方法的使用時機。"""

    def test_equality(self):
        """assertEqual / assertNotEqual：檢查相等／不相等。"""
        self.assertEqual(1 + 1, 2)
        self.assertNotEqual(1 + 1, 3)

    def test_truthiness(self):
        """assertTrue / assertFalse：檢查布林值。"""
        self.assertTrue(is_adult(20))
        self.assertFalse(is_adult(15))

    def test_identity(self):
        """assertIs / assertIsNot：檢查是否為同一個物件（用 is）。"""
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        self.assertIs(a, b)       # b 就是 a，同一個參照
        self.assertIsNot(a, c)    # c 內容雖相同，但是不同的 list 物件

    def test_membership(self):
        """assertIn / assertNotIn：檢查元素是否在容器中。"""
        self.assertIn(3, [1, 2, 3, 4])
        self.assertNotIn(99, [1, 2, 3, 4])

    def test_none(self):
        """assertIsNone / assertIsNotNone：檢查是否為 None。"""
        result = None
        self.assertIsNone(result)
        result = 42
        self.assertIsNotNone(result)

    def test_type(self):
        """assertIsInstance / assertNotIsInstance：檢查型別。"""
        self.assertIsInstance("hello", str)
        self.assertNotIsInstance("hello", int)

    def test_almost_equal(self):
        """assertAlmostEqual：浮點數近似相等（預設小數 7 位）。
        改用 assertAlmostEqual(a, b, places=2) 指定小數位數。"""
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
        # 注意：0.1 + 0.2 == 0.3 在 float 中是 False！

    def test_collection_equal(self):
        """assertListEqual / assertDictEqual / assertSetEqual：
        比較容器時使用特定方法，錯誤訊息比 assertEqual 更清楚。"""
        self.assertListEqual([1, 2, 3], [1, 2, 3])
        self.assertDictEqual({"a": 1, "b": 2}, {"b": 2, "a": 1})
        self.assertSetEqual({1, 2, 3}, {3, 2, 1})

    def test_greater_less(self):
        """assertGreater / assertLess / assertGreaterEqual / assertLessEqual。"""
        self.assertGreater(10, 5)
        self.assertLess(5, 10)
        self.assertGreaterEqual(5, 5)
        self.assertLessEqual(5, 5)


# ==========================================================
# B — setUp / tearDown 生命週期
# 可以在每個測試方法前後準備／清理資源
# ==========================================================
class TestLifecycle(unittest.TestCase):
    """展示 setUp 與 tearDown 的執行順序。"""

    def setUp(self):
        """每個 test_* 方法執行前會先跑 setUp()。
        適合用來建立共用的測試資料、開啟檔案、建立資料庫連線等。"""
        self.data = {"name": "Alice", "age": 30}
        self.users = [
            {"first_name": "John", "last_name": "Doe"},
            {"first_name": "Jane", "last_name": ""},
            {},
        ]

    def tearDown(self):
        """每個 test_* 方法執行後會跑 tearDown()。
        適合用來清理資源（關檔案、刪暫存資料等）。"""
        pass

    def test_get_display_name_full(self):
        """測試有完整姓名的情况。"""
        result = get_user_display_name(self.users[0])
        self.assertEqual(result, "John Doe")

    def test_get_display_name_no_last(self):
        """測試只有 first_name 的情况。"""
        result = get_user_display_name(self.users[1])
        self.assertEqual(result, "Jane")

    def test_get_display_name_anonymous(self):
        """測試完全沒有姓名欄位的情况。"""
        result = get_user_display_name(self.users[2])
        self.assertEqual(result, "匿名使用者")

    @classmethod
    def setUpClass(cls):
        """在整個類別的第一個測試執行前跑一次（只跑一次）。
        適合用來建立開銷較大的共用資源（例如資料庫連線池）。"""
        pass

    @classmethod
    def tearDownClass(cls):
        """在整個類別的最後一個測試執行後跑一次（只跑一次）。"""
        pass


# ==========================================================
# C — 14.1 測試 stdout 輸出
# 使用 redirect_stdout 把 print 的輸出捕捉到 StringIO
# ==========================================================
class TestStdout(unittest.TestCase):
    """測試函式是否印出預期的字串。"""

    def test_url_print(self):
        """使用 redirect_stdout 捕捉 print 的輸出。"""
        buf = io.StringIO()
        with redirect_stdout(buf):
            url_print("www", "example.com")
        # redirect_stdout 會暫時把 sys.stdout 換成 buf
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")


# ==========================================================
# D — 14.2 Mock 基本用法：MagicMock 與 return_value / side_effect
# Mock 用來取代真實物件，讓我們隔離外部相依來測試
# ==========================================================
class TestMockBasic(unittest.TestCase):
    """展示 MagicMock 的基本用法。"""

    def test_fetch_user_with_mock(self):
        """用 MagicMock 取代真實的 API 物件。"""
        # 建立一個假的 API 物件
        fake_api = MagicMock()
        # 設定呼叫 .get() 時要回傳的內容
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        # 執行被測函式（傳入假的 API）
        result = fetch_user(fake_api, 1)

        # 驗證回傳值是否正確
        self.assertEqual(result["name"], "Alice")
        # 驗證 .get() 是否「剛好被呼叫一次」且傳入正確的參數
        fake_api.get.assert_called_once_with("/users/1")

    def test_mock_side_effect(self):
        """side_effect 可以用來模擬：
        - 每次呼叫回傳不同值
        - 拋出例外
        - 或執行一個自訂函式
        """
        mock_obj = MagicMock()

        # -- 用法 1：傳入可迭代物件，每次呼叫輪流回傳不同值 --
        mock_obj.fetch.side_effect = [10, 20, 30]
        self.assertEqual(mock_obj.fetch(), 10)
        self.assertEqual(mock_obj.fetch(), 20)
        self.assertEqual(mock_obj.fetch(), 30)

        # -- 用法 2：傳入例外類別，呼叫時直接拋出 --
        mock_obj.query.side_effect = ValueError("查詢失敗")
        with self.assertRaises(ValueError):
            mock_obj.query()

        # -- 用法 3：傳入自訂函式，根據輸入動態決定回傳值 --
        def custom_side_effect(url):
            if "admin" in url:
                return {"role": "admin"}
            return {"role": "user"}

        mock_obj.get_user.side_effect = custom_side_effect
        self.assertEqual(mock_obj.get_user("/admin/dashboard")["role"], "admin")
        self.assertEqual(mock_obj.get_user("/home")["role"], "user")

    def test_mock_spec(self):
        """spec 參數可以限制 Mock 只能存取指定的屬性／方法。
        有助於防止打錯字而沒被發現。"""
        # 給定 spec 後，存取不存在的屬性會噴 AttributeError
        mock_obj = MagicMock(spec=["allowed_method", "another_method"])
        mock_obj.allowed_method()   # OK
        mock_obj.another_method()   # OK
        with self.assertRaises(AttributeError):
            mock_obj.typo_method()  # 不存在，噴錯！

    def test_mock_call_count(self):
        """Mock 提供多種呼叫次數的斷言方法。"""
        mock_obj = MagicMock()

        mock_obj.run()
        mock_obj.run()
        mock_obj.run(1)
        mock_obj.run(1, 2)

        # 總共被呼叫了幾次
        self.assertEqual(mock_obj.run.call_count, 4)

        # 斷言「至少被呼叫一次」
        mock_obj.run.assert_called()

        # === 關於 assert_called_once() 的重要提醒 ===
        # 因為這裡 run() 被呼叫了 4 次，
        # 如果呼叫 mock_obj.run.assert_called_once() 會拋出 AssertionError 讓測試失敗。
        # 改用 assert_any_call() 來檢查「曾經被呼叫過」即可。

        # 斷言特定的呼叫
        mock_obj.run.assert_any_call()              # 曾經被呼叫過（不管參數）
        mock_obj.run.assert_any_call(1, 2)          # 曾經以 (1, 2) 呼叫過
        mock_obj.run.assert_any_call(1)             # 曾經以 (1,) 呼叫過


# ==========================================================
# E — 14.2 patch：取代真實模組／物件的裝飾器與上下文管理器
# patch 可以裝飾一個測試方法，或作為上下文管理器使用
# ==========================================================
class TestPatch(unittest.TestCase):
    """展示 @patch 裝飾器與 patch 上下文管理器。"""

    @patch("builtins.print")
    def test_url_print_via_patch(self, mock_print):
        """使用 @patch 裝飾器把 builtins.print 換成 Mock。
        測試方法必須多一個參數接收這個 Mock 物件。"""
        url_print("api", "example.com")
        # 驗證 print 是否剛好被呼叫一次且傳入正確字串
        mock_print.assert_called_once_with("https://api.example.com")

    def test_patch_with_context_manager(self):
        """patch() 也可以當上下文管理器使用，作用範圍限縮在 with 區塊內。"""
        with patch("builtins.print") as mock_print:
            url_print("blog", "test.org")
            mock_print.assert_called_once_with("https://blog.test.org")

        # 離開 with 區塊後，builtins.print 恢復成原本的函式
        # 所以在外面 print 是正常的

    def test_patch_object(self):
        """patch.object 可以取代特定物件上的某個方法。"""
        class Calculator:
            def add(self, a, b):
                return a + b

        calc = Calculator()

        with patch.object(calc, "add", return_value=999):
            self.assertEqual(calc.add(1, 2), 999)

        # 離開 with 後恢復正常
        self.assertEqual(calc.add(1, 2), 3)

    def test_patch_multiple(self):
        """多個 patch 可以疊加使用，從最外層到最內層依序生效。
        參數順序與裝飾器順序相反（離方法最近的裝飾器最先傳入）。"""
        with patch("builtins.print") as mock_print, \
             patch("builtins.open") as mock_open:
            # 這裡 print 和 open 都被換掉了
            print("hello")
            open("file.txt")
            mock_print.assert_called_once_with("hello")
            mock_open.assert_called_once_with("file.txt")

    def test_patch_with_spec(self):
        """patch 搭配 spec 參數，確保被 mock 的物件符合預期介面。"""
        with patch("builtins.print", spec=True) as mock_print:
            mock_print("hello")
            mock_print.assert_called_once_with("hello")


# ==========================================================
# F — 14.3 測試例外情況
# 使用 assertRaises 與 assertRaisesRegex 驗證函式是否拋出預期例外
# ==========================================================
class TestExceptions(unittest.TestCase):
    """測試 parse_int 在各種輸入下的行為。"""

    def test_raises(self):
        """assertRaises 檢查是否拋出特定例外類型。"""
        with self.assertRaises(ValueError):
            parse_int("")

    def test_raises_with_message(self):
        """assertRaisesRegex 額外檢查例外訊息的文字內容。"""
        with self.assertRaisesRegex(ValueError, "空字串"):
            parse_int("")

    def test_raises_wrong_type_fails(self):
        """示範：如果預期例外型別不符，assertRaises 會讓測試失敗。
        這裡故意預期 TypeError，但 parse_int 只會拋 ValueError，
        所以 assertRaises 會捕捉到 ValueError 且型別不吻合，導致測試失敗。
        取消下行註解可看到失敗結果。"""
        # with self.assertRaises(TypeError):
        #     parse_int("abc")   # 實際上拋 ValueError，測試會 FAIL

    def test_normal_case(self):
        """正常輸入應該回傳正確的整數，不拋例外。"""
        self.assertEqual(parse_int("42"), 42)

    def test_exception_context_manager(self):
        """從 assertRaises 的上下文管理器取得例外物件，進一步檢查其屬性。"""
        with self.assertRaises(ValueError) as ctx:
            parse_int("")
        # ctx.exception 就是被拋出的 ValueError 實例
        self.assertEqual(str(ctx.exception), "空字串無法轉成整數")

    def test_assert_raises_as_decorator(self):
        """assertRaises 也可以當裝飾器使用（如果整個測試方法只測一種例外）。"""
        # 以下等價於用 with self.assertRaises(ValueError): parse_int("")
        # 但較少用，因為無法同時測試正常路徑
        pass


# ==========================================================
# G — 測試套件（TestSuite）與自訂執行
# 可以用 TestLoader / TestSuite 手動選擇要執行哪些測試
# ==========================================================
class TestSuiteDemo(unittest.TestCase):
    """展示如何手動組織測試套件。"""

    def test_passes(self):
        self.assertEqual(1, 1)

    def test_fails_demo(self):
        """故意失敗來演示測試結果。若要看到這個失敗，取消下面這行的註解。"""
        # self.assertEqual(1, 2)


# ==========================================================
# 入口：執行所有測試
# ==========================================================
if __name__ == "__main__":
    # 最簡單的方式：自動發現並執行所有 unittest.TestCase 子類別
    unittest.main()

    # 進階用法（可取消下方註解來試試自訂套件）：
    #
    # # 用法 1：只執行特定 TestCase
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestAssertions)
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    #
    # # 用法 2：自訂 TestSuite，任意組合測試
    # suite = unittest.TestSuite()
    # suite.addTest(TestExceptions("test_raises"))
    # suite.addTest(TestExceptions("test_normal_case"))
    # unittest.TextTestRunner(verbosity=2).run(suite)
