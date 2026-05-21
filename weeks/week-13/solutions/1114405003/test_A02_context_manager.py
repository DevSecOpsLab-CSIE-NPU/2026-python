# 測試檔：test_A02_context_manager.py
# 目的：為 A02-context-manager.py 的教學範例撰寫單元測試，並加入詳細繁體中文註解
# 放置位置：weeks/week-13/solutions/1114405003
#
# 測試重點：
# - 使用 @contextmanager 的 section() 是否在 enter/exit 輸出正確的邊框與標題
# - capture_output() 是否能暫時接管 stdout 並在結束時還原
# - solve_parity() 的輸出格式與內容是否正確
# - Timer 類別作為 context manager 的行為（enter/exit、是否吞例外）
#
# 設計說明：
# A02 原始檔在匯入時會執行一些示範程式（包含使用 /tmp 路徑寫檔），
# 為了讓測試在不同平台（例如 Windows）也能順利載入，我們在載入模組時
# 暫時替換 builtins.open：當遇到原檔嘗試開啟 "/tmp/week13_demo.txt" 時，
# 會改用系統暫存資料夾（tempfile.gettempdir()）下的對應檔案，其他 open 行為不變。

import builtins
import importlib.util
import os
import tempfile
import unittest


def _load_a02_module_safely():
    """安全載入 A02-context-manager.py 的輔助函式。

    - 若原檔嘗試打開 /tmp/week13_demo.txt，會導向到系統暫存目錄，避免平台差異。
    - 載入完成後會還原原先的 builtins.open，不會污染全域狀態。
    """
    module_path = os.path.join(os.path.dirname(__file__), '..', '..', 'in-class', 'A02-context-manager.py')
    module_path = os.path.normpath(module_path)
    spec = importlib.util.spec_from_file_location('a02_context_manager', module_path)
    module = importlib.util.module_from_spec(spec)

    # 保存原本 open，並建立一個針對 /tmp 的轉址器
    original_open = builtins.open
    redirected_tmp_file = os.path.join(tempfile.gettempdir(), 'week13_demo.txt')

    def patched_open(file, *args, **kwargs):
        # 若程式要打開 /tmp/week13_demo.txt，改為系統暫存目錄路徑
        if isinstance(file, str) and file == '/tmp/week13_demo.txt':
            file = redirected_tmp_file
        return original_open(file, *args, **kwargs)

    builtins.open = patched_open
    try:
        spec.loader.exec_module(module)
    finally:
        # 一定要還原，避免影響其他測試
        builtins.open = original_open

    return module


# 在模組層級載入一次，供所有測試重複使用
A02 = _load_a02_module_safely()


class TestCaptureOutput(unittest.TestCase):
    """測試 capture_output() 的核心功能：截取與還原 stdout"""

    def test_capture_collects_prints(self):
        # 驗證：with capture_output() 可捕捉 print 的內容
        with A02.capture_output() as buf:
            print('第一行')
            print('第二行')
        captured = buf.getvalue().splitlines()
        self.assertEqual(captured, ['第一行', '第二行'])

    def test_capture_restores_stdout(self):
        # 驗證：離開 with 後 stdout 被還原為原本的 sys.stdout
        import sys
        real_stdout = sys.stdout
        with A02.capture_output() as _:
            print('內部')
        self.assertIs(sys.stdout, real_stdout)


class TestSolveParity(unittest.TestCase):
    """測試 solve_parity() 的輸出內容與格式。"""

    def test_solve_parity_for_10(self):
        # 10 的二進位為 1010，1 的個數為 2，2 mod 2 = 0
        with A02.capture_output() as buf:
            A02.solve_parity(10)
        out = buf.getvalue().strip()
        expected = 'The parity of 1010 is 2 (mod 2 is 0).'
        self.assertEqual(out, expected)

    def test_solve_parity_for_7(self):
        # 7 的二進位為 111，1 的個數為 3，3 mod 2 = 1
        with A02.capture_output() as buf:
            A02.solve_parity(7)
        out = buf.getvalue().strip()
        expected = 'The parity of 111 is 3 (mod 2 is 1).'
        self.assertEqual(out, expected)


class TestSectionContextManager(unittest.TestCase):
    """測試 section() enter/exit 的輸出（邊框與標題）。"""

    def test_section_prints_title_and_border(self):
        title = '測試區段'
        with A02.capture_output() as buf:
            with A02.section(title):
                print('內文')
        out = buf.getvalue()
        # 檢查是否包含 40 個等號的上框與標題文字
        self.assertIn('=' * 40, out)
        self.assertIn(title, out)
        # 也應該包含離開時印出的短橫分隔線（有平台/字元差異，接受 ASCII '-' 或繪圖字元 '─'）
        self.assertTrue(('-' * 40) in out or ('─' * 40) in out)


class TestTimerContextManager(unittest.TestCase):
    """測試 Timer class 作為 context manager 的基本行為與例外傳遞。"""

    def test_timer_enter_returns_instance(self):
        # __enter__ 回傳 self，可當作 as t 使用
        with A02.Timer() as t:
            self.assertIsInstance(t, A02.Timer)

    def test_timer_prints_start_and_end(self):
        # 測試 Timer 會在 enter/exit 印出訊息（以 capture 檢查是否含關鍵字）
        with A02.capture_output() as buf:
            with A02.Timer():
                pass
        out = buf.getvalue()
        self.assertIn('開始計時', out)
        self.assertIn('結束：', out)

    def test_timer_does_not_suppress_exception(self):
        # Timer.__exit__ 回傳 False，表示不吞例外；with 區塊拋出的例外應往外傳
        with self.assertRaises(RuntimeError):
            with A02.Timer():
                raise RuntimeError('測試例外')


if __name__ == '__main__':
    unittest.main(verbosity=2)
