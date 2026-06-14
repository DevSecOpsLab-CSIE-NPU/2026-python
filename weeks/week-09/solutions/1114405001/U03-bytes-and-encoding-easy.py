# U03-easy. 文字 vs 位元組、編碼觀念 - 簡化版
# 只需要記一個原則：文字用 t、二進位用 b

from pathlib import Path

print("=== 1. 文字檔 (text mode) ===")
# 文字模式：用 'wt'、'rt'，要指定 encoding
file = Path("text.txt")

# 寫入
with open(file, "wt", encoding="utf-8") as f:
    f.write("你好世界\n")

# 讀取
with open(file, "rt", encoding="utf-8") as f:
    content = f.read()
print(f"文字內容：{content.strip()}")

print("\n=== 2. 二進位檔 (binary mode) ===")
# 二進位模式：用 'wb'、'rb'，不需要 encoding
# 用於：圖片、ZIP、EXE、任何非文字檔

bin_file = Path("data.bin")

# 寫入位元組
data = bytes([0x89, 0x50, 0x4E, 0x47])  # PNG 檔頭
with open(bin_file, "wb") as f:
    f.write(data)

# 讀取位元組
with open(bin_file, "rb") as f:
    binary_content = f.read()
print(f"二進位內容：{binary_content.hex()}")

print("\n=== 3. 編碼轉換（幾乎不用自己做） ===")
# Python 3 會自動處理，除非特殊需求
text = "中文"
bytes_data = text.encode("utf-8")
print(f"編碼：{text} → {bytes_data}")

recovered = bytes_data.decode("utf-8")
print(f"解碼：{bytes_data} → {recovered}")

print("\n=== 4. 錯誤示範 ===")
# 常見錯誤：用 big5 讀 utf-8 檔
try:
    Path("text.txt").read_text(encoding="big5")
except UnicodeDecodeError:
    print("❌ 編碼錯誤：用 big5 讀 utf-8 檔會爆炸")

print("\n=== 記憶重點（超重要） ===")
print("""
一句話法則：
- 文字檔 → 用 'rt'/'wt' + encoding='utf-8'
- 二進位檔 → 用 'rb'/'wb'（不要 encoding）

常見檔案類型：
- 文字：.txt、.csv、.json、.py、.html
- 二進位：.png、.jpg、.zip、.exe、.pkl
""")