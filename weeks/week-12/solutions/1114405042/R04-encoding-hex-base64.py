"""
R04. 十六進位與 Base64 編碼解碼（6.9–6.10）

本模組展示 Python 中常用的兩種二進位資料編碼方式：
    1. 十六進位（Hex）- 將每個位元組表示為 2 個十六進位數字
    2. Base64 - 將二進位資料編碼為 ASCII 字元序列

編碼目的：
    - 將二進位資料轉換為可列印的 ASCII 文本
    - 便於傳輸、儲存和在 URL、HTML 等文本協議中使用
    - 讓二進位資料適合在文本編輯器中查看（有限度）

常用模組：
    - binascii：處理十六進位轉換
    - base64：處理 Base64 編碼解碼
"""

import binascii  # 二進位和 ASCII 轉換模組，支援十六進位等編碼
import base64    # Base64 編碼解碼模組，支援標準和 URL-safe 兩種方式

# ── 6.9 十六進位（Hex）────────────────────────────────────
# 十六進位編碼是一種將二進位資料表示為十六進位數字的方式
# 每個位元組（8 位元）由 2 個十六進位數字表示（0-9, A-F）
# 優點：比起二進位更簡潔，比起十進位更接近記憶體表示
# 用途：十六進位常見於哈希值、MAC 位址、顏色代碼、debug 時查看記憶體內容
#
# UTF-8 編碼說明：
#   - "Hello, " 對應 48656c6c6f2c20（ASCII，直接對應）
#   - "世" 對應 e4b896（UTF-8 多位元組字符）
#   - "界" 對應 e7958c（UTF-8 多位元組字符）

data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # UTF-8 編碼的 "Hello, 世界"

# ● bytes → hex 字串（編碼）
# binascii.b2a_hex() 將位元組序列轉換為十六進位字串
# 函數名稱含義：b2a = "bytes to ASCII"（字節到 ASCII）
# 返回值是 bytes 類型的十六進位表示
hex_str = binascii.b2a_hex(data)  # 使用 binascii 進行轉換
print("b2a_hex：", hex_str)                   # 輸出：b'48656c6c6f2c ...' （b 前綴表示 bytes 型別）

# Python 3.5+ 提供的更便捷方法
# 直接呼叫 bytes 物件的 hex() 方法，返回字串而非 bytes
hex_str2 = data.hex()  # 返回 str 類型
print(".hex()：", hex_str2)  # 輸出：48656c6c6f2c ...（更清潔的字串格式）

# ● hex 字串 → bytes（解碼）
# binascii.a2b_hex() 將十六進位字串轉回位元組序列
# 函數名稱含義：a2b = "ASCII to bytes"（ASCII 到字節）
restored = binascii.a2b_hex(hex_str)  # 參數是 bytes 型別
print("a2b_hex：", restored)  # 還原為原始資料

# Python 3.5+ 提供的更便捷方法
# bytes.fromhex() 接收字串參數，返回 bytes
restored2 = bytes.fromhex(hex_str2)  # 參數是 str 類型
print("fromhex：", restored2)  # 還原為原始資料

# 驗證編碼解碼的可逆性
assert restored == data     # 確認兩種方法都能正確還原原始資料

# ── 6.10 Base64 ───────────────────────────────────────────
# Base64 是一種將任意二進位資料轉換為 ASCII 文字的編碼方式
# 原理：將 3 個位元組（24 位）分組，編碼為 4 個 Base64 字符
# 字符集：A-Z a-z 0-9 + / （共 64 個字符，故名 "Base64"）
# 特點：
#   - 編碼後長度約為原始長度的 1.33 倍
#   - 可能包含 = 作為填充符號
#   - 適合在郵件、JSON、URL 等文本協議中傳輸二進位資料
#
# 常見應用場景：
#   - HTTP Basic Authentication：將 username:password 進行 Base64 編碼
#   - Email 附件：MIME 格式使用 Base64 編碼二進位附件
#   - JWT Token：簽名部分使用 Base64
#   - 圖片內嵌到 HTML：使用 data:image/png;base64,... 格式

msg = b"Python Cookbook"  # 要編碼的二進位資料

# ● Base64 編碼
# base64.b64encode() 將位元組序列編碼為 Base64
# 返回值是 bytes 型別，包含 ASCII 字符
encoded = base64.b64encode(msg)  # 編碼
print("\nb64encode：", encoded)               # 輸出：b'UHl0aG9uIENvb2tib29r'

# ● Base64 解碼
# base64.b64decode() 將 Base64 字串解碼回原始二進位資料
# 輸入可以是 bytes 或 str，返回值是 bytes
decoded = base64.b64decode(encoded)  # 解碼
print("b64decode：", decoded)                 # 輸出：b'Python Cookbook'

# ● URL-safe Base64（用於 URL 和檔案名）
# 標準 Base64 使用 + 和 / 字符，在 URL 中可能被誤解
# URL-safe 版本將：
#   - + 替換為 - （減號）
#   - / 替換為 _ （底線）
# 這樣可以安全地在 URL 查詢字符串中使用
url_encoded = base64.urlsafe_b64encode(msg)  # URL-safe 編碼
print("urlsafe：  ", url_encoded)  # 輸出：b'UHl0aG9uIENvb2tib29r'（本例無 +/，所以看起來相同）

# ── 應用場景比較 ──────────────────────────────────────────
# 三種資料表示方式的對比：
#
# 原始資料      編碼方式      編碼結果                  長度倍數    可讀性  用途
# ─────────────────────────────────────────────────────────────────────────────
# b'Python'     原始 bytes   b'Python'                1.0         ★★     二進位檔案
#               十六進位      50797468...            2.0         ★★★   Hash、位址
#               Base64       UHl0aG9u                ~1.33       ★★     郵件、API
#
# 重要概念區分：
# 1. Hex（十六進位）
#    - 可讀性最高（數字 + A-F）
#    - 編碼後長度為原始的 2 倍
#    - 用途：哈希值顯示、MAC 位址、記憶體 dump、顏色代碼
#    - 例子：SHA256 通常用十六進位表示
#
# 2. Base64
#    - 編碼效率更高（長度約 1.33 倍）
#    - 使用 64 個可列印字符
#    - 用途：郵件附件、HTTP Basic Auth、JWT、資料 URI
#    - 例子：base64 -w 0 file.bin 在 Linux 中使用
#
# 3. URL-safe Base64
#    - 標準 Base64 去掉 +/ 改用 -_
#    - 用途：URL 查詢字符串、檔案名、JWT
#
# 重要警告：編碼 ≠ 加密！
# ────────────────────────────
# - Hex 和 Base64 只是「資料表示方式」，不提供安全性
# - 任何人都可以輕鬆解碼回原始資料
# - 若需保護資料安全，必須使用真正的加密方式（如 AES、RSA）
# - 編碼的目的是格式轉換，而非隱藏資訊
