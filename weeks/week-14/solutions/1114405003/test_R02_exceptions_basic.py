"""
針對 `in_class/R02-exceptions-basic.py` 的單元測試

說明：
- 使用 `importlib` 動態載入原始模組，避免修改原始檔案。
- 測試 `parse_value`、`safe_run`、自定義例外 `NetworkError`、`HostnameError`、`ConnectionTimeout` 及 `connect` 的行為。

執行：
    python -m unittest test_R02_exceptions_basic.py
或：
    python -m unittest discover
"""
import os
import importlib.util
import unittest
from unittest.mock import MagicMock, patch


# 載入原始模組（放在 in_class）
HERE = os.path.dirname(__file__)
SRC_PATH = os.path.normpath(os.path.join(HERE, '..', 'in_class', 'R02-exceptions-basic.py'))

spec = importlib.util.spec_from_file_location('r02_module', SRC_PATH)
r02 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r02)


class TestParseValue(unittest.TestCase):
    """測試 parse_value 對各類輸入的處理"""

    def test_parse_value_valid_integer(self):
        # 整數字串應回傳對應整數
        self.assertEqual(r02.parse_value('123'), 123)

    def test_parse_value_invalid_string_returns_none(self):
        # 非數字字串時函式會捕捉 ValueError 並回傳 None
        self.assertIsNone(r02.parse_value('abc'))

    def test_parse_value_none_type_returns_none(self):
        # 傳入 None（會產生 TypeError）時也應回傳 None
        self.assertIsNone(r02.parse_value(None))


class TestSafeRun(unittest.TestCase):
    """測試 safe_run 在發生例外時的行為"""

    def test_safe_run_returns_value_on_success(self):
        # 成功執行時應回傳函式結果
        result = r02.safe_run(lambda x: x + 1, 1)
        self.assertEqual(result, 2)

    def test_safe_run_handles_exception_and_calls_traceback(self):
        # 當函式拋出例外時，safe_run 應該捕捉並呼叫 traceback.print_exc
        fake_func = lambda: (_ for _ in ()).throw(ValueError('err'))
        with patch.object(r02.traceback, 'print_exc') as mock_tb:
            result = r02.safe_run(fake_func)
            # 發生例外時，函式沒有回傳值（回傳 None）
            self.assertIsNone(result)
            mock_tb.assert_called_once()


class TestConnectAndCustomExceptions(unittest.TestCase):
    """測試自定義例外以及 connect 函式的行為"""

    def test_connect_success(self):
        # 正常情況下回傳連線字串
        self.assertEqual(r02.connect('example.com', 5), 'connected to example.com')

    def test_connect_empty_host_raises_hostnameerror(self):
        # 空主機名稱應拋出 HostnameError
        with self.assertRaises(r02.HostnameError):
            r02.connect('', 5)

    def test_connect_timeout_raises_connectiontimeout(self):
        # timeout 小於 1 應拋出 ConnectionTimeout，且包含 host/seconds 屬性
        with self.assertRaises(r02.ConnectionTimeout) as cm:
            r02.connect('slow.com', 0)
        exc = cm.exception
        self.assertEqual(exc.host, 'slow.com')
        self.assertEqual(exc.seconds, 0)
        # ConnectionTimeout 繼承自 NetworkError
        self.assertIsInstance(exc, r02.NetworkError)


if __name__ == '__main__':
    unittest.main()
