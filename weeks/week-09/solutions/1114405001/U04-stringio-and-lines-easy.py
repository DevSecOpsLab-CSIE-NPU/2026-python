# U04-easy. 類檔案物件 StringIO 與逐行處理 - 簡化版
# StringIO = 記憶體裡的虛擬檔案

import io
from pathlib import Path

print("=== 1. StringIO 最簡單的用法 ===")
# 想像你有個「記憶體中的檔案」
buf = io.StringIO()

# 可以像檔案一樣 write 或 print
buf.write("第一行\n")
buf.write("第二行\n")
print("第三行", file=buf)

# 取出所有內容
text = buf.getvalue()
print(f"內容：\n{text}")

print("\n=== 2. StringIO 逐行讀取 ===")
# 建立新的 StringIO
buf = io.StringIO("甲\n乙\n丙\n")

# 逐行讀
for i, line in enumerate(buf, 1):
    print(f"第 {i} 行：{line.rstrip()}")

print("\n=== 3. 實用例子：記憶體中的 CSV ===")
# 不想寫到磁碟，直接在記憶體操作
import csv

mem = io.StringIO()
writer = csv.writer(mem)
writer.writerow(["名字", "成績"])
writer.writerow(["alice", 90])
writer.writerow(["bob", 85])

# 看結果
print(f"CSV 內容：\n{mem.getvalue()}")

print("\n=== 4. 逐行處理檔案的標準寫法 ===")
# 建立測試檔案
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n", encoding="utf-8")

# 逐行讀，過濾空行，加行號
dst = Path("numbered.txt")
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    for line in fin:
        line = line.rstrip()
        if not line:
            continue  # 跳過空行
        n += 1
        print(f"{n:02d}. {line}", file=fout)

print(f"處理結果：\n{dst.read_text(encoding='utf-8')}")

print("\n=== 記憶重點 ===")
print("""
StringIO 什麼時候用？
1. 測試：不想寫到磁碟
2. API 相容性：某些函數需要 file-like 物件
3. 快速計算：在記憶體中操作數據

小技巧：
- getvalue() 取所有內容
- seek(0) 指標回到開頭
- StringIO() 是 io 模組
""")