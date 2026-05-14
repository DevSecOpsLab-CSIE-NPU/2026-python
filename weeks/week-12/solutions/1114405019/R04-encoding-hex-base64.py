# R04-encoding-hex-base64.py
# 示範 Hex 與 Base64 的編碼與解碼邏輯

import base64

def encoding_demo():
    original_text = "Hello, Python! 🐍"
    print(f"原始文字: {original_text}")

    # 文字需轉為 bytes 才能編碼
    byte_data = original_text.encode('utf-8')

    # 1. Hex 編碼 (十六進位)
    hex_str = byte_data.hex()
    print(f"Hex 編碼: {hex_str}")
    
    # Hex 解碼
    decoded_hex = bytes.fromhex(hex_str).decode('utf-8')
    print(f"Hex 解碼: {decoded_hex}")

    # 2. Base64 編碼
    b64_bytes = base64.b64encode(byte_data)
    b64_str = b64_bytes.decode('utf-8')
    print(f"Base64 編碼: {b64_str}")

    # Base64 解碼
    decoded_b64 = base64.b64decode(b64_str).decode('utf-8')
    print(f"Base64 解碼: {decoded_b64}")

if __name__ == "__main__":
    print("=== 編碼與解碼示範 ===")
    encoding_demo()
