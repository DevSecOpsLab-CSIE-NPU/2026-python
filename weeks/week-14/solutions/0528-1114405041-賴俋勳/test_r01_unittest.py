"""r01_unittest.py 的單元測試。"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch

import r01_unittest as r01


class TestR01Unittest(unittest.TestCase):
    """驗證 stdout、mock 與例外測試。"""

    def test_url_print_stdout(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            r01.url_print("www", "example.com")
        self.assertEqual(buf.getvalue().strip(), "https://www.example.com")

    @patch("builtins.print")
    def test_url_print_patch(self, mock_print):
        r01.url_print("api", "example.com")
        mock_print.assert_called_once_with("https://api.example.com")

    def test_fetch_user(self):
        fake_api = MagicMock()
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = r01.fetch_user(fake_api, 1)

        self.assertEqual(result["name"], "Alice")
        fake_api.get.assert_called_once_with("/users/1")

    def test_parse_int_success(self):
        self.assertEqual(r01.parse_int("42"), 42)

    def test_parse_int_raises(self):
        with self.assertRaisesRegex(ValueError, "空字串"):
            r01.parse_int("")


if __name__ == "__main__":
    unittest.main(verbosity=2)
