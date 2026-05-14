"""R04 Hex 與 Base64 詳細註解版。"""

import base64


def main():
    # 先把中文字串轉成 UTF-8 bytes，
    # 因為 Hex / Base64 處理的都是位元組資料。
    data = "Hello, 世界".encode("utf-8")

    # bytes.hex() 會把每個 byte 轉成兩位十六進位文字。
    hex_text = data.hex()
    print(hex_text)

    # bytes.fromhex() 則會把十六進位文字還原回原本的 bytes。
    print(bytes.fromhex(hex_text))

    # Base64 常用在需要把 bytes 變成可傳輸文字的情境。
    msg = b"Python Cookbook"
    encoded = base64.b64encode(msg).decode("ascii")
    print(encoded)

    # 解碼後會回到原本的 bytes。
    print(base64.b64decode(encoded))

    # URL-safe Base64 會把 + / 改成 - _，比較適合放在網址中。
    safe = base64.urlsafe_b64encode(b"\xfb\xef\xff").decode("ascii")
    print(safe)


if __name__ == "__main__":
    main()
