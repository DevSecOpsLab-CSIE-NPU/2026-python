# R04. 十六進位與 Base64 編碼解碼（6.9–6.10）
# binascii / base64 / bytes.hex() / bytes.fromhex()
#
# 這個範例主要示範兩種常見的「位元組表示法」：
# 1. Hex（十六進位）適合閱讀與檢查原始 bytes。
# 2. Base64 適合把二進位資料轉成可傳輸的文字格式。
#
# 這些方法都不是加密，只是資料的編碼與表示方式。

import binascii
import base64

# ── 6.9 十六進位（Hex）────────────────────────────────────
# 這裡先準備一段 bytes 資料。
# b"..." 表示這是原始位元組資料，而不是一般的文字字串。
# 範例中的 \xe4\xb8\x96\xe7\x95\x8c 是「世界」的 UTF-8 編碼。
data = b"Hello, \xe4\xb8\x96\xe7\x95\x8c"   # "Hello, 世界" in UTF-8

# bytes → hex 字串
# b2a_hex() 的意思是 binary to ASCII hex，會把 bytes 轉成十六進位表示法。
# 轉換後的結果仍然是 bytes 型別，只是內容變成可讀的 hex 文字。
hex_str = binascii.b2a_hex(data)
# 印出來可以看到每個 byte 都變成兩位十六進位字元。
print("b2a_hex：", hex_str)                   # b'48656c6c6f2c ...'

# bytes.hex() 是 Python 內建的方便寫法，功能與 b2a_hex 類似，但回傳的是字串。
hex_str2 = data.hex()                         # Python 3.5+ 內建方法
# 這種寫法更直觀，當你只需要把 bytes 顯示成 hex 字串時很常用。
print(".hex()：", hex_str2)

# hex 字串 → bytes
# a2b_hex() 的意思是 ASCII hex to binary，會把 hex 表示法還原回 bytes。
restored = binascii.a2b_hex(hex_str)
# 還原後應該與原始 data 完全一致。
print("a2b_hex：", restored)

# bytes.fromhex() 是另一個內建方法，功能等同於把 hex 字串轉回 bytes。
restored2 = bytes.fromhex(hex_str2)           # Python 3.5+
# 這裡同樣會得到與原始 bytes 相同的內容。
print("fromhex：", restored2)

# assert 用來做一致性檢查，確認編碼與解碼結果沒有失真。
assert restored == data     # 確認一致

# ── 6.10 Base64 ───────────────────────────────────────────
# Base64 常用於把二進位資料轉成較安全的 ASCII 字元集合，方便在文字協定中傳輸。
# 例如 email、HTTP、JSON 字串或某些 token 格式。
msg = b"Python Cookbook"

# 編碼
# b64encode() 會把 bytes 轉成 Base64 bytes，輸出內容通常只含英數字與少數符號。
encoded = base64.b64encode(msg)
# Base64 編碼後的內容仍然是 bytes，不過通常可以直接解讀成 ASCII 文字。
print("\nb64encode：", encoded)               # b'UHl0aG9uIENvb2tib29r'

# 解碼
# b64decode() 則是把 Base64 bytes 還原成原始 bytes。
decoded = base64.b64decode(encoded)
# 如果編碼與解碼正確，這裡應該會回到原本的 b"Python Cookbook"。
print("b64decode：", decoded)                 # b'Python Cookbook'

# URL-safe Base64（不含 +/，改用 -_）
# 標準 Base64 會使用 + 和 /，但這兩個字元在 URL 中有時不方便直接使用。
# urlsafe_b64encode() 會把字元集改成較適合 URL 的版本：用 - 取代 +，用 _ 取代 /。
url_encoded = base64.urlsafe_b64encode(msg)
# 這種格式常用於網址參數、JWT 片段或需要避免特殊字元的情境。
print("urlsafe：  ", url_encoded)

# ── 應用場景比較 ──────────────────────────────────────────
# Hex 的特性：
# - 可讀性高，因為每個 byte 都對應成兩個十六進位字元。
# - 長度會變成原始資料的 2 倍。
# - 常見於雜湊值、MAC 位址、除錯輸出、二進位檔檢視。
#
# Base64 的特性：
# - 長度約為原始資料的 1.33 倍，比 Hex 更省空間。
# - 常見於 email 附件、HTTP Basic Auth、JSON 中的二進位內容、JWT。
#
# 兩者都只是「編碼」：把資料換一種表示法，方便傳輸或閱讀。
# 它們不是加密，不能拿來保密資料。
