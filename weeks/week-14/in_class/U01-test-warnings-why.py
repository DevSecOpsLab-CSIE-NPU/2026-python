"""
U01：測試流程與警告的「為什麼」（理解層）

對應 Cookbook：
- 14.4 將測試輸出寫到日誌檔
- 14.5 跳過或預期失敗
- 14.11 輸出警告訊息

核心問題：
- 為什麼要 skipIf / skipUnless 而不是 if 包起來？
- expectedFailure 和註解掉測試的差別？
- warnings.warn 的 stacklevel 為什麼幾乎一定要設 2？
- DeprecationWarning vs UserWarning 怎麼選？

執行：
    python U01-test-warnings-why.py
    python U01-test-warnings-why.py --log
"""
import sys
import unittest
import warnings


# ---------- 14.5 為什麼用裝飾器而不是 if ----------
class WhySkip(unittest.TestCase):
    """
    用 skipIf 而不是 `if sys.version_info < ...: return` 的理由：
    1. 報表上會明確標 's'（skipped），而不是假裝通過。
    2. 統計時可以區分「沒測」和「測過了」。
    3. 不會誤把 setUp 副作用留下來。
    """

    @unittest.skipIf(sys.version_info < (3, 10), "需要 Python 3.10+")
    def test_match_case(self):
        x = 1
        match x:
            case 1:
                self.assertTrue(True)

    @unittest.skipUnless(sys.platform.startswith("darwin"), "只在 macOS")
    def test_mac_only(self):
        import os
        self.assertTrue(os.path.exists("/Users"))

    @unittest.expectedFailure
    def test_known_bug(self):
        """
        已知 bug 的測試「留著」而不是刪掉，這樣：
        - 真的修好時，會以「unexpected success」提醒你拔掉裝飾器
        - 文件化「這個 case 目前壞掉」這件事
        """
        self.assertEqual(2 + 2, 5)


# ---------- 14.4 為什麼要把測試結果寫檔 ----------
def run_and_log(logfile="test_result.log"):
    """
    場景：CI 環境想保留每次測試的完整輸出，或者在無人監控的
    背景任務裡跑測試。重點是 TextTestRunner 接受任何 file-like
    物件，不只有 stderr。
    """
    with open(logfile, "w", encoding="utf-8") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        suite = unittest.TestLoader().loadTestsFromTestCase(WhySkip)
        runner.run(suite)
    print(f"結果寫入 {logfile}")


# ---------- 14.11 為什麼 stacklevel=2 ----------
def old_api_bad(x):
    """stacklevel 預設 1 → warning 指向這一行；使用者不知道是誰呼叫的"""
    warnings.warn("old_api_bad 已棄用", DeprecationWarning)
    return x


def old_api_good(x):
    """stacklevel=2 → warning 指向「呼叫端」，使用者一眼能定位到自己的程式"""
    warnings.warn("old_api_good 已棄用", DeprecationWarning, stacklevel=2)
    return x


def demo_stacklevel():
    """比較兩種寫法的警告位置（執行時觀察 file:line 訊息）"""
    warnings.simplefilter("always")
    print("--- stacklevel=1（差）：行號指向函式內部 ---")
    old_api_bad(1)
    print("--- stacklevel=2（好）：行號指向呼叫端 ---")
    old_api_good(1)


# ---------- 14.11 warning 種類選擇 ----------
def category_guide():
    """
    DeprecationWarning：給「開發者」看的（預設在 __main__ 才顯示）
    UserWarning：給「使用者」看的（總是顯示）
    RuntimeWarning：執行期奇怪但非錯誤的事（如 0 當除數的某些情況）

    選錯類別的後果：開發者看不到棄用提醒，或一般使用者被技術細節嚇到。
    """
    warnings.warn("這是給開發者：API 即將移除", DeprecationWarning, stacklevel=2)
    warnings.warn("這是給使用者：輸入值偏大，結果可能不準", UserWarning, stacklevel=2)


if __name__ == "__main__":
    if "--log" in sys.argv:
        run_and_log()
    else:
        demo_stacklevel()
        print("\n--- 警告種類選擇 ---")
        warnings.simplefilter("default")
        category_guide()
        print("\n--- 跑 WhySkip 測試 ---")
        unittest.main(argv=[sys.argv[0]], exit=False)
