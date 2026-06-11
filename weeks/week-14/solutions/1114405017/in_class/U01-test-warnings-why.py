"""
U01：測試流程與警告的「為什麼」（理解層）

此檔以範例與說明的方式回答教材中常見疑問：
- 為什麼使用 unittest 的 skip 裝飾器而不是簡單地以 if 包起來？
- expectedFailure 與刪掉測試的差別為何？
- warnings.warn 的 stacklevel 參數為何重要？
- 應該選用哪種警告類別（DeprecationWarning、UserWarning 等）？

執行：
    python U01-test-warnings-why.py
    python U01-test-warnings-why.py --log
"""
import sys
import unittest
import warnings


# ---------- 14.5 為什麼用裝飾器而不是 if ----------
class WhySkip(unittest.TestCase):
    """示範 skipIf / skipUnless / expectedFailure 的用途與理由。

    主要理由：
    1. 用裝飾器會在測試報告中明確標記 skipped，而不是把測試假裝成通過。
    2. 若測試有 setUp / tearDown，if 可能造成測試前後副作用不同步。
    3. expectedFailure 可以保留壞掉的測試案例，當修好時會提醒開發者移除標記。
    """

    @unittest.skipIf(sys.version_info < (3, 10), "需要 Python 3.10+")
    def test_match_case(self):
        # 此測試示範 Python 3.10+ 才有的 match/case 語法。
        x = 1
        match x:
            case 1:
                self.assertTrue(True)

    @unittest.skipUnless(sys.platform.startswith("darwin"), "只在 macOS")
    def test_mac_only(self):
        # 只在 macOS 執行的測試；示範 skipUnless 的使用情境。
        import os
        self.assertTrue(os.path.exists("/Users"))

    @unittest.expectedFailure
    def test_known_bug(self):
        """已知失敗的測試保留在測試集中，並用 expectedFailure 標記。

        - 若 bug 修好，該測試會變成 Unexpected Success（提醒你移除標記）。
        - 與刪掉測試的差別是保留了問題的文件化紀錄。
        """
        self.assertEqual(2 + 2, 5)


# ---------- 14.4 為什麼要把測試結果寫檔 ----------
def run_and_log(logfile="test_result.log"):
    """把測試輸出寫成檔案，適合在 CI 或背景任務中保存測試記錄。

    - unittest.TextTestRunner 的 stream 參數接受任何類 file-like 的物件，
      因此可以把輸出重定向到檔案或自訂的緩衝區。
    - 這有助於後續分析完整輸出，或在失敗時作為證據保留。
    """
    with open(logfile, "w", encoding="utf-8") as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        suite = unittest.TestLoader().loadTestsFromTestCase(WhySkip)
        runner.run(suite)
    print(f"結果寫入 {logfile}")


# ---------- 14.11 為什麼 stacklevel=2 ----------
def old_api_bad(x):
    """示範錯誤的寫法：不指定 stacklevel，警告會指向此函式內部的行號，使用者難以追蹤呼叫端。

    - warnings.warn 的預設 stacklevel=1，會把位置標示在 warn 呼叫本身。
    """
    warnings.warn("old_api_bad 已棄用", DeprecationWarning)
    return x


def old_api_good(x):
    """推薦寫法：設 stacklevel=2，讓警告指向呼叫者，使使用者能快速定位到自己程式中需要修改的地方。"""
    warnings.warn("old_api_good 已棄用", DeprecationWarning, stacklevel=2)
    return x


def demo_stacklevel():
    """執行範例顯示兩種 stacklevel 的差異（在終端可觀察到 file:line 的差別）。"""
    warnings.simplefilter("always")
    print("--- stacklevel=1（差）：行號指向函式內部 ---")
    old_api_bad(1)
    print("--- stacklevel=2（好）：行號指向呼叫端 ---")
    old_api_good(1)


# ---------- 14.11 warning 種類選擇 ----------
def category_guide():
    """說明何時選擇不同的 warning 類別。

    - DeprecationWarning：給開發者看的棄用提示（通常在 library code 使用，預設可能不顯示於一般使用者）。
    - UserWarning：給使用者看的提示，會被顯示出來。
    - RuntimeWarning：執行期間可能有異常行為但非致命錯誤，可用於提醒精度或邊界情況。

    選錯類別會導致提示被忽略或被過度顯示，因此選擇需符合目標受眾。
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
