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
import sys  # 提供系統資訊（Python 版本、作業系統等）
import unittest  # Python 的單元測試框架
import warnings  # 用來發出警告訊息（比錯誤輕一些，程式還能繼續跑）


# ---------- 14.5 為什麼用裝飾器而不是 if ----------
# 這個主題是「在編寫測試時，如何處理某些測試在某些情境下不適用的問題」
class WhySkip(unittest.TestCase):
    """解釋為什麼要用 @unittest.skipIf 而不是在測試裡面寫 if 敍述

    用 skipIf 而不是 `if sys.version_info < ...: return` 的理由：
    1. 報表上會明確標 's'（skipped），而不是假裝通過（pass）
       → 這樣看測試結果時能分清楚「真的測過沒問題」和「沒測"。
    2. 統計時可以區分「沒測"和「測過了"。
       → 好的測試工具會跟蹤有多少測試沒有被執行。
    3. 不會誤把 setUp 副作用(註：setup 的準備工作）留下來。
       → 跳過的測試根本不會執行 setUp，所以不會有殘留效果。
    """

    @unittest.skipIf(sys.version_info < (3, 10), "需要 Python 3.10+")
    # 裝飾器：如果 Python 版本低於 3.10，這個測試會被跳過
    def test_match_case(self):
        """測試 Python 3.10+ 才有的 match-case 敍述（類似 switch-case）"""
        x = 1  # 設定測試資料
        match x:  # match-case 是 Python 3.10 新語法
            case 1:  # 如果 x 等於 1
                self.assertTrue(True)  # 測試總是通過（1 == 1）

    @unittest.skipUnless(sys.platform.startswith("darwin"), "只在 macOS")
    # 裝飾器：只有在 macOS 時才執行這個測試，其他系統會跳過
    def test_mac_only(self):
        """測試 macOS 特有的功能（例如 /Users 目錄）"""
        import os  # 作業系統相關的函式庫
        # macOS 的使用者目錄在 /Users，而 Linux 和 Windows 位置不同
        self.assertTrue(os.path.exists("/Users"))  # 檢查 /Users 是否存在

    @unittest.expectedFailure
    # 裝飾器：標記「這個測試目前是失敗的，這是預期的"
    def test_known_bug(self):
        """測試某個已知的 bug（目前還沒修）

        為什麼要留著這個失敗的測試而不是刪掉？
        - 真的修好 bug 時，會以「unexpected success「提醒你刪掉這個裝飾器
        - 文件化「這個功能目前有問題，需要修復"這個事實
        - 防止某人意外地修好但沒注意到
        """
        self.assertEqual(2 + 2, 5)  # 這個測試「故意」失敗（2+2=4，不等於 5）


# ---------- 14.4 為什麼要把測試結果寫檔 ----------
def run_and_log(logfile="test_result.log"):
    """執行測試並把所有輸出寫進檔案裡

    場景：
    - CI（持續整合）環境想保留每次測試的完整輸出，供後續查詢
    - 在背景任務裡跑測試（沒人在電腦前看螢幕）
    - 需要把測試結果歸檔或發送給其他人

    重點是 TextTestRunner 接受任何 file-like 物件（像是檔案或 StringIO），
    不只限於標準的 stderr，這讓測試非常靈活。
    """
    with open(logfile, "w", encoding="utf-8") as f:  # 開啟檔案作為寫入流
        # TextTestRunner 是 unittest 內建的測試執行器
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        # verbosity=2 表示詳細輸出（包括每個測試的名稱、結果等）

        # TestLoader 載入 WhySkip 類別裡的所有測試方法
        suite = unittest.TestLoader().loadTestsFromTestCase(WhySkip)
        runner.run(suite)  # 執行測試，輸出會寫進 f（即檔案）
    print(f"結果寫入 {logfile}")  # 通知使用者結果已存檔


# ---------- 14.11 為什麼 stacklevel=2 ----------
# 這是關於「警告訊息指向哪裡」的問題
def old_api_bad(x):
    """示範：stacklevel 預設 1 時的情況

    stacklevel=1（預設值）→ 警告會指向「這一行" （函式內部）
    使用者看到警告時，會看到函式庫的內部程式碼位置，
    而不知道是「誰呼叫的"，難以定位問題。
    """
    warnings.warn("old_api_bad 已棄用", DeprecationWarning)  # 預設 stacklevel=1
    return x


def old_api_good(x):
    """示範：stacklevel=2 時的情況

    stacklevel=2 → 警告會指向「呼叫端"（使用者的程式碼）
    使用者一眼就能看到「我的程式的第幾行呼叫了這個舊 API"，
    方便快速定位和修改。
    """
    warnings.warn("old_api_good 已棄用", DeprecationWarning, stacklevel=2)
    return x


def demo_stacklevel():
    """演示兩種警告方式，比較輸出的行號位置

    當你執行這個程式時，看看警告訊息指向的行號：
    - stacklevel=1 會指向函式內部的 warnings.warn 那一行
    - stacklevel=2 會指向這個 demo_stacklevel 函式旁邊的呼叫行
    """
    warnings.simplefilter("always")  # 確保所有警告都會顯示（包括 DeprecationWarning）
    print("--- stacklevel=1（差）：行號指向函式內部 ---")
    old_api_bad(1)  # 這裡會發出警告，指向 old_api_bad 函式內部
    print("--- stacklevel=2（好）：行號指向呼叫端 ---")
    old_api_good(1)  # 這裡會發出警告，指向這一行（更有用！）


# ---------- 14.11 warning 種類選擇 ----------
def category_guide():
    """解釋警告訊息的不同類型，以及何時使用哪一種

    警告類型：

    1. DeprecationWarning
       - 給「開發者」看的（即「你寫 Python 程式碼的人"）
       - 表示「你正在用的 API 將來會消失，趕快改用新版本"
       - 預設在 __main__（直接執行的程式）才顯示，在函式庫中被隱藏
       - 使用情景：舊版本的函式庫功能即將移除

    2. UserWarning（最通用）
       - 給「使用者」看的（「執行已編譯程式的人"）
       - 表示「執行過程中發生了奇怪的事，但程式可能還能繼續"]
       - 總是顯示（除非使用者主動關閉）
       - 使用情景：輸入不太對勁但可以接受、檔案不存在但有預設等

    3. RuntimeWarning
       - 給「誰」都可以，但針對執行期的異常情況
       - 例如：浮點數計算的精度問題、0 當除數導致無窮大等
       - 表示「嚴格來說這不是錯誤，但你需要知道"

    選錯類別的後果：
    - 用 DeprecationWarning 給一般使用者 → 使用者看不到棄用提醒
    - 用 UserWarning 警告開發者 → 開發者每次都被提醒，很煩
    - 用 RuntimeWarning 表示 API 過時 → 該看的人看不到
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
