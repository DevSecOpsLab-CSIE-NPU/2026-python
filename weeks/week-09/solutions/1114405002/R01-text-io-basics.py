# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# ============================================================================
# Bloom: Remember — 會叫出 open/print 的基本參數
# 本檔介紹文本檔案讀寫的基礎操作，是後續所有 I/O 工作的基礎
# ============================================================================

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# open(path, mode, encoding) 是 Python I/O 的核心函數
# mode 參數：
#   - 'r' = 讀（預設）| 'w' = 寫（覆蓋） | 'a' = 附加 | 'x' = 獨佔建立
#   - 't' = 文字（預設） | 'b' = 二進位
# encoding：中文檔案「一定要」指定 encoding='utf-8'，不可省略

path = Path("hello.txt")  # 建立 Path 物件

# 寫入模式：mode='wt'（預設 't' 可省略，但習慣寫全）
with open(path, "wt", encoding="utf-8") as f:  # "wt" = write text
    f.write("你好，Python\n")  # 寫第一行
    f.write("第二行\n")        # 寫第二行

# 讀取方式 1：一次讀完（適合小檔）
with open(path, "rt", encoding="utf-8") as f:  # "rt" = read text
    print(f.read())  # read() 一次讀入整檔到記憶體

# 讀取方式 2：逐行讀取（大檔必備：一次只讀一行到記憶體）
with open(path, "rt", encoding="utf-8") as f:
    for line in f:  # for 迴圈可直接迭代檔案物件
        print(line.rstrip())  # rstrip() 移除行尾換行符

# ── 5.2 print 導向檔案 ─────────────────────────────────
# 除了 f.write()，也可用 print() 函數搭配 file 參數寫檔
# 優點：自動轉換型別、自動加空白 / 換行
# 應用場景：寫日誌、統計報告等純文字輸出

with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)              # print 寫到檔案而不是螢幕
    print("使用者:", "alice", file=f)      # print 自動加空白分隔

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
# print() 的三個重要參數：
#   - sep：多個引數間的分隔符（預設空白 ' '）
#   - end：每行結尾（預設換行 '\n'）
#   - file：輸出目標（預設 sys.stdout，可改為檔案）
# 應用場景：CSV / TSV 格式輸出

fruits = ["apple", "banana", "cherry"]

# 方式 1：以逗號分隔寫 CSV
with open("fruits.csv", "wt", encoding="utf-8") as f:
    print(*fruits, sep=",", end="\n", file=f)  # *fruits 展開列表為多個引數

# 方式 2：附加新行（mode='a'，不覆蓋）
# end='' 避免多一個換行（因為 print 會自動加一個）
with open("fruits.csv", "at", encoding="utf-8") as f:
    print("date", end=",", file=f)  # 不換行，繼續寫
    print("2026-04-23", file=f)     # 這行會自動加 \n

# 驗證寫出的內容
print(Path("fruits.csv").read_text(encoding="utf-8"))
# 輸出：
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 常見錯誤：混淆 str 和 bytes
#   - 文字模式 'wt'：寫入的必須是 str（字串）
#   - 二進位模式 'wb'：寫入的必須是 bytes（位元組）
# 型別不符會拋出 TypeError

try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # ← 錯誤：b"..." 是 bytes，不是 str
except TypeError as e:
    print("錯誤示範:", e)  # 輸出：TypeError: a bytes-like object is required, not 'str'
    # 改正方式 1：改用 'wb' 模式（二進位）
    # 改正方式 2：去掉 b prefix，改成 "bytes in text mode"（str）
