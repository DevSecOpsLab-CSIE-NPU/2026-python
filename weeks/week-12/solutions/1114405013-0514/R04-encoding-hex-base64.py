# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# binascii / base64 / bytes.hex() / bytes.fromhex()
#
# Hex 與 Base64 都是「二進位資料 → 可列印字元」的編碼方式，
# 它們不是加密（沒有金鑰），只是為了讓二進位資料能在
# 只有文字通道（如 email、JSON）中安全傳輸。

import binascii
import base64
from typing import Final


# ════════════════════════════════════════════════════════════
#  準備測試資料（bytes 型別）
#  b"Hello, \xe4\xb8\x96\xe7\x95\x8c"
#  其中 \xe4\xb8\x96\xe7\x95\x8c 是「世界」的 UTF-8 編碼
# ════════════════════════════════════════════════════════════

RAW_BYTES: Final[bytes] = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"  # "Hello, 世界"


# ════════════════════════════════════════════════════════════
#  1. 十六進位編碼解碼（Hex）
#  用途：將二進位資料表示為 0-9、a-f 字元
#  特性：每個 byte → 2 個 hex 字元，長度變為 2 倍
#  常用於：hash 摘要（如 SHA256）、MAC 位址、顏色碼
#
#  兩種實作方式：
#    方法 A（binascii 模組）：b2a_hex() / a2b_hex()
#    方法 B（bytes 內建方法）：.hex() / .fromhex()
# ════════════════════════════════════════════════════════════

def demo_hex() -> None:
    """
    十六進位編碼解碼示範。

    binascii.b2a_hex(data)    → bytes → hex 字串（回傳 bytes）
    binascii.a2b_hex(hex_str) → hex 字串 → bytes

    data.hex()                → bytes → hex 字串（回傳 str）
    bytes.fromhex(hex_str)    → hex 字串 → bytes

    b2a = binary to ascii / a2b = ascii to binary
    """
    print("=== 十六進位（Hex）編碼解碼 ===")

    data: bytes = RAW_BYTES
    print(f"原始資料（bytes）：{data!r}")

    # ── 編碼：bytes → 十六進位字串 ────────────────────────

    # 方法 A：binascii.b2a_hex()（回傳 bytes，全部小寫）
    hex_bytes: bytes = binascii.b2a_hex(data)
    print(f"b2a_hex() 輸出型別：{type(hex_bytes).__name__}")
    print(f"b2a_hex() 結果：{hex_bytes}")
    # 註：b2a_hex 等價於 binascii.hexlify()

    # 方法 B：bytes.hex()（Python 3.5+，回傳 str，更直覺）
    hex_str: str = data.hex()
    print(f"data.hex() 輸出型別：{type(hex_str).__name__}")
    print(f"data.hex() 結果：{hex_str}")

    # ── 解碼：十六進位字串 → bytes ───────────────────────

    # 方法 A：binascii.a2b_hex()（接受 str 或 bytes）
    restored_a: bytes = binascii.a2b_hex(hex_bytes)
    print(f"a2b_hex() 還原：{restored_a!r}")

    # 方法 B：bytes.fromhex()（僅接受 str）
    restored_b: bytes = bytes.fromhex(hex_str)
    print(f"fromhex() 還原：{restored_b!r}")

    # ── 驗證 ───────────────────────────────────────────────
    assert restored_a == data
    assert restored_b == data
    print("✅ 編解碼一致")

    # ── 補充：hex 字串可加入空格，fromhex 會自動忽略 ────
    spaced: bytes = bytes.fromhex("48 65 6c 6c 6f")  # "Hello"
    print(f"fromhex 含空格：{spaced!r}")


# ════════════════════════════════════════════════════════════
#  2. Base64 編碼解碼
#  用途：將二進位資料表示為 A-Z、a-z、0-9、+、/ 字元（共 64 字元）
#  特性：每 3 個 byte → 4 個 Base64 字元，長度約為原來的 4/3 倍
#  常用於：Email 附件（MIME）、HTTP Basic 認證、JWT Token
#
#  標準 Base64：b64encode / b64decode
#  URL-safe Base64：urlsafe_b64encode / urlsafe_b64decode
#    → 將 + 改為 -，/ 改為 _，避免 URL 編碼問題
# ════════════════════════════════════════════════════════════

def demo_base64() -> None:
    """
    標準 Base64 與 URL-safe Base64 編碼解碼。

    base64.b64encode(data)       → bytes → Base64 字串（回傳 bytes）
    base64.b64decode(encoded)    → Base64 字串 → bytes

    base64.urlsafe_b64encode(data)  → 使用 -_ 取代 +/
    base64.urlsafe_b64decode(data)  → 還原 URL-safe Base64
    """
    print("\n=== Base64 編碼解碼 ===")

    msg: bytes = b"Python Cookbook"
    print(f"原始資料（bytes）：{msg!r}")

    # ── 編碼 ───────────────────────────────────────────────

    # 標準 Base64：b64encode（回傳 bytes）
    encoded: bytes = base64.b64encode(msg)
    print(f"b64encode() 輸出型別：{type(encoded).__name__}")
    print(f"b64encode() 結果：{encoded}")
    print(f"長度：原始={len(msg)} → Base64={len(encoded)}")

    # ── 解碼 ───────────────────────────────────────────────

    decoded: bytes = base64.b64decode(encoded)
    print(f"b64decode() 還原：{decoded!r}")

    assert decoded == msg
    print("✅ 編解碼一致")


def demo_urlsafe_base64() -> None:
    """
    URL-safe Base64：適用於 URL、檔案名稱、JWT 等場合。

    標準 Base64 使用 + 和 /，在 URL 中有特殊含義。
    URL-safe 版本將其替換為 - 和 _，不需額外 URL 編碼。
    """
    print("\n=== URL-safe Base64 ===")

    msg: bytes = b"Python Cookbook"

    # URL-safe 編碼（結果不含 +/）
    url_encoded: bytes = base64.urlsafe_b64encode(msg)
    print(f"urlsafe_b64encode()：{url_encoded}")

    # 標準 Base64（可能含 +/）
    std_encoded: bytes = base64.b64encode(msg)
    print(f"b64encode()        ：{std_encoded}")

    # 兩者在這個例子可能相同（因為輸入不含產生 +/ 的位元組模式）
    # 用包含特殊位元組模式的資料來展示差異
    special: bytes = bytes([0xfb, 0xff, 0xff])     # 會產生 +/ 的資料
    print(f"\n含 +/ 的資料：base64({special.hex()}) = {base64.b64encode(special)}")
    print(f"URL-safe 版本：urlsafe({special.hex()}) = {base64.urlsafe_b64encode(special)}")

    # URL-safe 解碼（也能解標準 Base64，因為 -_ 會被反向轉換）
    restored: bytes = base64.urlsafe_b64decode(url_encoded)
    assert restored == msg
    print("✅ URL-safe 編解碼一致")


# ════════════════════════════════════════════════════════════
#  3. Hex vs Base64 長度比較
#  Hex：    1 byte → 2 chars（200%）
#  Base64： 3 bytes → 4 chars（約 133%）
#
#  結論：Base64 空間效率較佳（約 67% 的節省 vs Hex），
#  但 Hex 可讀性較高，適合人類檢視。
# ════════════════════════════════════════════════════════════

def demo_compare() -> None:
    """
    Hex 與 Base64 的長度與可讀性比較。

    測試各種長度的資料，觀察編碼後的長度比例：
      - Hex：固定 2x
      - Base64：約 4/3 ≈ 1.33x（無填充時）
    """
    print("\n=== Hex vs Base64 比較 ===")

    test_sizes: list[int] = [3, 6, 15, 30, 60]
    header: str = f"{'原始長度':>8}  {'Hex 長度':>8}  {'Hex 倍率':>8}  {'B64 長度':>8}  {'B64 倍率':>8}"
    print(header)
    print("-" * len(header))

    for n in test_sizes:
        data: bytes = bytes(range(n))  # 產生 n bytes 測試資料
        hex_len: int = len(data.hex())
        b64_len: int = len(base64.b64encode(data))

        print(f"{n:>8}  {hex_len:>8}  {hex_len/n:>8.2f}x  "
              f"{b64_len:>8}  {b64_len/n:>8.2f}x")


# ════════════════════════════════════════════════════════════
#  4. Base64 實務應用：編碼/解碼圖片
#  實務上常將圖片或檔案編碼為 Base64，嵌入 JSON 或 HTML 中。
# ════════════════════════════════════════════════════════════

def demo_base64_image() -> None:
    """
    模擬將圖片二進位資料編碼為 Base64（例如 data: URI）。

    情境：在前端顯示圖片時，可將圖片直接嵌入 HTML：
      <img src="data:image/png;base64,iVBORw0KGgo...">
    避免額外 HTTP 請求。
    """
    print("\n=== Base64 模擬圖片編碼 ===")

    # 模擬一張小圖片的二進位資料（實際應用中來自 open("photo.png","rb")）
    fake_image: bytes = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A] +  # PNG header
                               [0x00] * 100)  # 其餘填充

    # 編碼為 Base64
    b64_str: str = base64.b64encode(fake_image).decode("ascii")

    # 製作 data URI（可直接在瀏覽器中使用）
    data_uri: str = f"data:image/png;base64,{b64_str}"
    print(f"Base64 長度：{len(b64_str)}")
    print(f"data URI 前 80 字元：{data_uri[:80]}...")


# ════════════════════════════════════════════════════════════
#  5. 錯誤處理
#  輸入不合法的 Hex 或 Base64 字串時，對應函式會拋出例外。
# ════════════════════════════════════════════════════════════

def demo_error_handling() -> None:
    """
    不合法輸入的錯誤處理。

    binascii.Error：
      - hex 字串長度為奇數
      - hex 字串含非十六進位字元

    binascii.Error（Base64 錯誤時也是此例外）：
      - 字串含不合法的 Base64 字元
    """
    print("\n=== 錯誤處理 ===")

    # ── Hex 錯誤 ───────────────────────────────────────────
    bad_inputs_hex: list[str] = [
        "48656c6c",          # "Hell"（合法，但少一個 o）
        "48656c6c6",         # 奇數長度 → 錯誤
        "48 65 6c 6c 6f",   # 含空格 → bytes.fromhex 可處理，但 a2b_hex 不行
        "xyz",               # 非 hex 字元 → 錯誤
    ]

    print("Hex 錯誤示範：")
    for s in bad_inputs_hex:
        try:
            result: bytes = binascii.a2b_hex(s)
            print(f"  ✅ a2b_hex({s!r}) → {result!r}")
        except binascii.Error as e:
            print(f"  ❌ a2b_hex({s!r}) 錯誤：{e}")

    # ── Base64 錯誤 ────────────────────────────────────────
    bad_inputs_b64: list[str] = [
        "UHl0aG9uIENvb2tib29",      # 長度不對（非 4 的倍數含填充）
        "!!!invalid!!!",             # 不含 Base64 字元集
    ]

    print("\nBase64 錯誤示範：")
    for s in bad_inputs_b64:
        try:
            result: bytes = base64.b64decode(s)
            print(f"  ✅ b64decode({s!r}) → {result!r}")
        except binascii.Error as e:
            print(f"  ❌ b64decode({s!r}) 錯誤：{e}")


# ════════════════════════════════════════════════════════════
#  主程式：依序執行各示範函式
# ════════════════════════════════════════════════════════════

if __name__ == "__main__":
    demo_hex()
    demo_base64()
    demo_urlsafe_base64()
    demo_compare()
    demo_base64_image()
    demo_error_handling()
