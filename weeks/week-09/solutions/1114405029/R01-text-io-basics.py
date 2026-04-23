# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數

# 匯入 pathlib 的 Path 類別
# Path 可以更方便地操作檔案路徑（比傳統字串更安全、可讀性更高）
from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 寫入：mode='wt'（預設 't' 表示文字模式），一定要指定 encoding（避免亂碼）

# 建立一個 Path 物件，代表 hello.txt 檔案
path = Path("hello.txt")

# 使用 with open(...) 開啟檔案（寫入模式）
# "wt" = write text（寫入文字模式）
# encoding="utf-8" 確保可以正確寫入中文
# with 的好處：區塊結束後會自動關閉檔案（避免資源洩漏）
with open(path, "wt", encoding="utf-8") as f:
    # 將字串寫入檔案（注意：需要自己加 \n 才會換行）
    f.write("你好，Python\n")
    f.write("第二行\n")

# 讀回：一次讀完 vs 逐行讀

# 再次開啟檔案，這次用 "rt"（read text，讀取文字模式）
with open(path, "rt", encoding="utf-8") as f:
    # f.read()：一次把整個檔案內容讀進來（回傳一個大字串）
    # 適合「小檔案」，大檔會吃記憶體
    print(f.read())  # 一次讀完（小檔才適合）

# 再開一次檔案
with open(path, "rt", encoding="utf-8") as f:
    # for line in f：逐行讀取（iterator 機制）
    # 每次只讀一行，適合「大檔案」
    for line in f:  # 大檔必備：逐行迭代
        # rstrip()：去掉右邊的空白與換行（避免 print 重複換行）
        print(line.rstrip())

# ── 5.2 print 導向檔案 ─────────────────────────────────

# 開啟 log.txt 進行寫入
with open("log.txt", "wt", encoding="utf-8") as f:
    # print(..., file=f)
    # 將 print 的輸出「導向檔案」而不是螢幕
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 5.3 調整分隔符與行終止符 ───────────────────────────

# 建立一個水果清單
fruits = ["apple", "banana", "cherry"]

# 開啟 fruits.csv（寫入模式）
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # print(*fruits)
    # *fruits 會把 list 展開成多個參數 → print("apple","banana","cherry")
    # sep="," → 用逗號分隔（CSV 格式）
    # end="\n" → 行結尾（預設就是換行）
    print(*fruits, sep=",", end="\n", file=f)

# end='' 可避免多一個換行
# "at" = append text（附加模式，不會覆蓋原內容）
with open("fruits.csv", "at", encoding="utf-8") as f:
    # 第一行：不換行（end=","）
    print("date", end=",", file=f)
    # 第二行：正常換行
    print("2026-04-23", file=f)

# 直接用 Path.read_text() 讀檔（快速方法）
# 會回傳整個檔案內容（字串）
print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────

# 'wt'（text mode）只能寫入 str（字串）
# 'wb'（binary mode）只能寫入 bytes（位元組）
# 如果型別錯誤會拋出 TypeError

try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        # 這裡故意寫錯：
        # 在「文字模式」寫入 bytes（b""）→ 會發生錯誤
        f.write(b"bytes in text mode")  # ← 會錯
except TypeError as e:
    # 捕捉錯誤並印出訊息
    print("錯誤示範:", e)