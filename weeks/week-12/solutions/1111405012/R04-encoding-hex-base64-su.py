"""R04 Hex 與 Base64 簡化版。"""

import base64


def main():
    data = "Hello, 世界".encode("utf-8")

    # Hex
    hex_text = data.hex()
    print(hex_text)
    print(bytes.fromhex(hex_text))

    # Base64
    msg = b"Python Cookbook"
    encoded = base64.b64encode(msg).decode("ascii")
    print(encoded)
    print(base64.b64decode(encoded))

    # URL-safe Base64
    safe = base64.urlsafe_b64encode(b"\xfb\xef\xff").decode("ascii")
    print(safe)


if __name__ == "__main__":
    main()
