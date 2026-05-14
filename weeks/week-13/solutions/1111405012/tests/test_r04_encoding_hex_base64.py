"""R04-encoding-hex-base64.py 的單元測試。"""

from __future__ import annotations

import unittest

from support import load_module


class TestR04EncodingHexBase64(unittest.TestCase):
    """確認 Hex 與 Base64 範例有正確的編解碼函式。"""

    @classmethod
    def setUpClass(cls):
        cls.module = load_module("R04-encoding-hex-base64.py")

    def test_hex_round_trip_restores_original_bytes(self):
        payload = "Hello, 世界".encode("utf-8")

        hex_text = self.module.bytes_to_hex(payload)
        restored = self.module.hex_to_bytes(hex_text)

        self.assertEqual(payload, restored)
        self.assertEqual("48656c6c6f2c20e4b896e7958c", hex_text)

    def test_base64_round_trip_restores_original_bytes(self):
        payload = b"Python Cookbook"

        encoded = self.module.encode_base64(payload)
        restored = self.module.decode_base64(encoded)

        self.assertEqual(payload, restored)
        self.assertEqual("UHl0aG9uIENvb2tib29r", encoded)

    def test_urlsafe_base64_avoids_plus_and_slash(self):
        payload = b"\xfb\xef\xff"

        encoded = self.module.encode_urlsafe_base64(payload)

        self.assertNotIn("+", encoded)
        self.assertNotIn("/", encoded)
        self.assertEqual(payload, self.module.decode_base64(encoded))


if __name__ == "__main__":
    unittest.main()
