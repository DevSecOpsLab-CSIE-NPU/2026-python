"""r02_exceptions.py 的單元測試。"""

import unittest

import r02_exceptions as r02


class TestR02Exceptions(unittest.TestCase):
    """驗證多重例外、安全執行與自訂例外。"""

    def test_parse_value(self):
        self.assertEqual(r02.parse_value("8"), 8)
        self.assertIsNone(r02.parse_value("abc"))
        self.assertIsNone(r02.parse_value(None))

    def test_safe_run_success(self):
        ok, result = r02.safe_run(lambda x, y: x + y, 3, 4)
        self.assertTrue(ok)
        self.assertEqual(result, 7)

    def test_safe_run_error(self):
        ok, err = r02.safe_run(lambda: 1 / 0)
        self.assertFalse(ok)
        self.assertEqual(err, "ZeroDivisionError")

    def test_connect_success(self):
        self.assertEqual(r02.connect("example.com", 3), "connected to example.com")

    def test_connect_hostname_error(self):
        with self.assertRaises(r02.HostnameError):
            r02.connect("", 3)

    def test_connect_timeout_error(self):
        with self.assertRaises(r02.ConnectionTimeout) as cm:
            r02.connect("slow.com", 0)

        self.assertEqual(cm.exception.host, "slow.com")
        self.assertEqual(cm.exception.seconds, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
