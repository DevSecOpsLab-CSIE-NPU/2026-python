"""R04. 十六進位與 Base64 編碼解碼（6.9–6.10）"""

from __future__ import annotations

import base64
import binascii


SAMPLE_BYTES = "Hello, 世界".encode("utf-8")
BASE64_MESSAGE = b"Python Cookbook"


def bytes_to_hex(data: bytes) -> str:
    """把 bytes 轉成十六進位字串。"""
    return data.hex()


def hex_to_bytes(hex_text: str) -> bytes:
    """把十六進位字串還原成 bytes。"""
    return bytes.fromhex(hex_text)


def encode_base64(data: bytes) -> str:
    """把 bytes 轉成標準 Base64 文字。"""
    return base64.b64encode(data).decode("ascii")


def decode_base64(encoded_text: str) -> bytes:
    """把 Base64 文字還原成 bytes。"""
    return base64.urlsafe_b64decode(encoded_text.encode("ascii"))


def encode_urlsafe_base64(data: bytes) -> str:
    """把 bytes 轉成 URL-safe Base64。"""
    return base64.urlsafe_b64encode(data).decode("ascii")


def main() -> None:
    """印出課堂上示範的編解碼結果。"""
    hex_bytes = binascii.b2a_hex(SAMPLE_BYTES)
    print("b2a_hex：", hex_bytes)
    print(".hex()：", bytes_to_hex(SAMPLE_BYTES))
    print("a2b_hex：", binascii.a2b_hex(hex_bytes))
    print("fromhex：", hex_to_bytes(bytes_to_hex(SAMPLE_BYTES)))

    print("\nb64encode：", encode_base64(BASE64_MESSAGE).encode("ascii"))
    print("b64decode：", decode_base64(encode_base64(BASE64_MESSAGE)))
    print("urlsafe：  ", encode_urlsafe_base64(BASE64_MESSAGE).encode("ascii"))

    print("# Hex    → 可讀性高，長度 2x，常見於 hash / MAC 位址")
    print("# Base64 → 長度約 1.33x，常見於 email 附件、HTTP 認證、JWT")
    print("# 兩者都只是表示方式，不是加密。")


if __name__ == "__main__":
    main()
