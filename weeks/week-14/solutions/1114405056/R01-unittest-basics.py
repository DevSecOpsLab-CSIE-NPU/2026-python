"""R01: unittest basics examples.

Run:
    python R01-unittest-basics.py
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import MagicMock, patch


def url_print(host: str, domain: str) -> None:
    """Print a full URL from host + domain."""
    print(f"https://{host}.{domain}")


def parse_int(text: str) -> int:
    """Parse an int, rejecting empty input."""
    if not text:
        raise ValueError("empty input is not allowed")
    return int(text)


def fetch_user(api, user_id: int):
    """Fetch user data through an API-like object."""
    return api.get(f"/users/{user_id}")


class TestStdout(unittest.TestCase):
    def test_url_print(self) -> None:
        stream = io.StringIO()
        with redirect_stdout(stream):
            url_print("www", "example.com")
        self.assertEqual(stream.getvalue().strip(), "https://www.example.com")


class TestMocking(unittest.TestCase):
    def test_fetch_user_with_magicmock(self) -> None:
        fake_api = MagicMock()
        fake_api.get.return_value = {"id": 1, "name": "Alice"}

        result = fetch_user(fake_api, 1)

        self.assertEqual(result["name"], "Alice")
        fake_api.get.assert_called_once_with("/users/1")

    @patch("builtins.print")
    def test_url_print_with_patch(self, mocked_print) -> None:
        url_print("api", "example.com")
        mocked_print.assert_called_once_with("https://api.example.com")


class TestExceptions(unittest.TestCase):
    def test_parse_int_raises(self) -> None:
        with self.assertRaises(ValueError):
            parse_int("")

    def test_parse_int_raises_regex(self) -> None:
        with self.assertRaisesRegex(ValueError, "empty"):
            parse_int("")

    def test_parse_int_normal(self) -> None:
        self.assertEqual(parse_int("42"), 42)


if __name__ == "__main__":
    unittest.main()
