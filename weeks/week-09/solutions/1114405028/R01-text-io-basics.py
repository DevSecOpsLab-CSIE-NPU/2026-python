# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 以 Path 物件搭配 open() 讀寫文字檔，建議都指定 encoding
path = Path("hello.txt")
with open(path, "wt", encoding="utf-8") as f:
    # mode='wt' = write text；若檔案不存在會建立；若已存在會覆蓋
    f.write("你好，Python\n")
    f.write("第二行\n")

# 讀回：一次讀完
with open(path, "rt", encoding="utf-8") as f:
    print(f.read())  # 適合小檔案，一次把整個內容讀入記憶體

# 逐行讀取，更適合較大的檔案
with open(path, "rt", encoding="utf-8") as f:
    for line in f:  # 直接對檔案物件迭代，逐行讀出
        print(line.rstrip())  # 去掉末尾換行，避免 print 多出空行

# ── 5.2 print 導向檔案 ─────────────────────────────────
# print() 可以透過 file 參數把輸出寫入檔案
with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # sep=',' 將多個值用逗號分隔；end='\n' 為預設的換行
    print(*fruits, sep=",", end="\n", file=f)

# 使用 append 模式 'at' 加新內容到既有檔案末尾
with open("fruits.csv", "at", encoding="utf-8") as f:
    print("date", end=",", file=f)   # 先印出 date, 但不換行
    print("2026-04-23", file=f)        # 再補上一行日期

print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# open(..., "wt") 接收 str；open(..., "wb") 接收 bytes
# 兩種模式不能混用，否則會得到 TypeError
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # 這裡寫 bytes 到 text 模式會失敗
except TypeError as e:
    print("錯誤示範:", e)
