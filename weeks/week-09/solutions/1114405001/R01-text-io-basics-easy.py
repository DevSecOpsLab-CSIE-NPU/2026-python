# R01-easy. 文本 I/O 基本式 - 簡化版
# 這是最常用的三個操作：寫、讀、逐行讀

from pathlib import Path

print("=== 1. 最簡單的：寫入和讀取 ===")
# 寫入：Path 物件的 write_text() 方法最簡單
path = Path("hello.txt")
path.write_text("你好\n世界\n", encoding="utf-8")

# 讀取整個檔案
content = path.read_text(encoding="utf-8")
print(content)

print("\n=== 2. 大檔案必備：逐行讀取 ===")
# 大檔案不能一次讀完，用 for 迴圈逐行讀
with open(path, "rt", encoding="utf-8") as f:
    for line in f:
        print(f"讀到: {line.rstrip()}")

print("\n=== 3. 寫入到檔案 ===")
# 方法1：用 write_text()
path.write_text("新內容\n", encoding="utf-8")

# 方法2：用 open() + print()，可以多次寫
with open(path, "wt", encoding="utf-8") as f:
    print("第一行", file=f)
    print("第二行", file=f)

print("\n=== 4. 附加到檔案（不覆蓋） ===")
# 'a' 模式 = append，在最後面加
with open(path, "at", encoding="utf-8") as f:
    print("新的最後一行", file=f)

print("最終內容：")
print(path.read_text(encoding="utf-8"))

print("\n=== 記憶重點 ===")
print("""
三個基本模式：
- 'wt' = write text（覆蓋）
- 'at' = append text（附加）
- 'rt' = read text（讀取）
永遠要加 encoding='utf-8'
""")