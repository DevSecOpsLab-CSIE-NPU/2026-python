# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# binascii / base64 / bytes.hex() / bytes.fromhex()

import binascii
import base64

# 這份示範重點：
# 1) 為什麼要把二進制轉成可讀的文字格式（Hex / Base64）
# 2) Hex 與 Base64 的編碼/解碼方式與使用場景
# 3) Python 內建方法 vs binascii / base64 模組的對應關係

# ── 6.9 十六進位（Hex）────────────────────────────────────
# Hex 編碼常見於：hash 值、MAC 位址、儲存二進制資料以便傳輸或顯示
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" in UTF-8 編碼的二進制

# bytes → hex 字串
# b2a_hex：bytes to ascii (hex)，把二進制轉成 16 進位的 ASCII 字符串
# 每個字節轉成 2 位十六進位（例如 \x48 → 48）
hex_str = binascii.b2a_hex(data)
print("b2a_hex：", hex_str)                   # b'48656c6c6f2c ...' (依然是 bytes)

# Python 3.5+ 內建方法，功能等同 binascii.b2a_hex()，但更簡潔
# 回傳的是 str 而非 bytes
hex_str2 = data.hex()
print(".hex()：", hex_str2)                    # 和 b2a_hex 相同，但型態是 str

# hex 字串 → bytes
# a2b_hex：ascii (hex) to bytes，反向操作，把 Hex 文字轉回二進制
restored = binascii.a2b_hex(hex_str)
print("a2b_hex：", restored)                  # 回到原始的 bytes

# Python 3.5+ 內建方法，功能等同 binascii.a2b_hex()
# 注意：fromhex() 只接受 str，不接受 bytes
restored2 = bytes.fromhex(hex_str2)
print("fromhex：", restored2)                 # 也回到原始的 bytes

# 驗證：編碼後再解碼，應該回到原始資料
assert restored == data     # 確認 a2b_hex 成功還原
assert restored2 == data    # 確認 fromhex 也成功還原

# ── 6.10 Base64 ───────────────────────────────────────────
# Base64 是另一種常見的二進制編碼方式，在 email / HTTP 認證 / JWT 中廣泛使用
# 相比 Hex（2x 長度），Base64 的長度約為 1.33x，更節省空間
msg = b"Python Cookbook"

# 編碼：把二進制轉成 Base64 字符集（A-Z, a-z, 0-9, +, /）
# b64encode 會自動處理字節對齊（末尾可能有 = 填充符）
encoded = base64.b64encode(msg)
print("\nb64encode：", encoded)               # b'UHl0aG9uIENvb2tib29r' (已編碼的 bytes)

# 解碼：把 Base64 字符串轉回二進制
# b64decode 會忽略空白與換行，所以即使有格式化，也能正常解碼
decoded = base64.b64decode(encoded)
print("b64decode：", decoded)                 # b'Python Cookbook' (回到原始資料)

# URL-safe Base64：用 - 和 _ 替代 + 和 /
# 這樣可以直接在 URL 或 JSON 中使用，無需額外跳脫
url_encoded = base64.urlsafe_b64encode(msg)
print("urlsafe：  ", url_encoded)             # 可能與普通 Base64 略不同，取決於原始資料

# ── 應用場景比較 ──────────────────────────────────────────
# Hex：
#   - 可讀性最高（只用 0-9, a-f）
#   - 長度是原資料的 2 倍
#   - 常見用途：hash 值、MAC 位址、記憶體傾印
#
# Base64：
#   - 長度約 1.33x（比 Hex 更緊湊）
#   - 字符集：A-Z, a-z, 0-9, +, /
#   - 常見用途：email 附件、HTTP Basic Auth、JWT、資料庫 blob 儲存
#
# URL-safe Base64：
#   - 改用 - 和 _ 代替 +/ 
#   - 常見用途：URL 參數、JSON 中的 Base64 字段
#
# 重要提醒：這些都只是「表示方式」，不提供任何安全性！
# 如果需要保護敏感資料，還是要用加密算法（如 AES）
