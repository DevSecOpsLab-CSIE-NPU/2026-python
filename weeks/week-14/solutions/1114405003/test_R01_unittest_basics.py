"""
針對 `in_class/R01-unittest-basics.py` 的單元測試檔案

說明：
- 使用 `importlib` 動態載入原始範例模組，避免修改原始檔案或依賴 package 結構。
- 使用 `unittest` 編寫測試案例，並加入繁體中文註解說明每個測試目的。

執行：
    python -m unittest test_R01_unittest_basics.py
或：
    python -m unittest discover
"""
import os
import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


# 動態載入位於 in_class 的原始模組（路徑相對於本檔案）
HERE = os.path.dirname(__file__)
SRC_PATH = os.path.normpath(os.path.join(HERE, '..', 'in_class', 'R01-unittest-basics.py'))

spec = importlib.util.spec_from_file_location('r01_module', SRC_PATH)
r01 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r01)


class TestUrlPrintStdout(unittest.TestCase):
    """測試 `url_print` 是否印出正確的 URL 到 stdout"""

    def test_url_print_outputs_correct_url(self):
        buf = io.StringIO()
        # redirect_stdout 可擷取 print 的輸出，方便在測試中比較
        with redirect_stdout(buf):
            r01.url_print('www', 'example.com')
        self.assertEqual(buf.getvalue().strip(), 'https://www.example.com')


class TestParseIntExceptions(unittest.TestCase):
    """測試 `parse_int` 正常與例外行為"""

    def test_parse_int_valid(self):
        # 正常情況下字串 '42' 應轉為整數 42
        self.assertEqual(r01.parse_int('42'), 42)

    def test_parse_int_empty_raises(self):
        # 傳入空字串應拋出 ValueError
        with self.assertRaises(ValueError):
            r01.parse_int('')

    def test_parse_int_error_message_contains_keyword(self):
        # 檢查例外訊息包含「空字串」關鍵字
        with self.assertRaisesRegex(ValueError, '空字串'):
            r01.parse_int('')


class TestFetchUserWithMock(unittest.TestCase):
    """測試 `fetch_user` 在使用外部 API 時的行為（以 mock 模擬 API）"""

    def test_fetch_user_calls_api_get(self):
        fake_api = MagicMock()
        fake_api.get.return_value = {'id': 1, 'name': 'Alice'}

        result = r01.fetch_user(fake_api, 1)

        # 驗證回傳值與呼叫參數
        self.assertEqual(result['name'], 'Alice')
        fake_api.get.assert_called_once_with('/users/1')


class TestUrlPrintPatch(unittest.TestCase):
    """示範使用 patch 替換內建 print，避免實際輸出到 stdout"""

    @patch('builtins.print')
    def test_url_print_patch_print(self, mock_print):
        r01.url_print('api', 'example.com')
        mock_print.assert_called_once_with('https://api.example.com')


if __name__ == '__main__':
    unittest.main()
