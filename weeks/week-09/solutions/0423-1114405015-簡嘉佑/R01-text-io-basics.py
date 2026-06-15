"""
R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
Bloom: Remember

本檔整理最常用的文字檔操作：
1) open 讀寫文字檔。
2) print 輸出導向檔案。
3) 調整 print 的分隔符與結尾。
4) 文字模式與位元組模式型別差異。
"""

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 寫入：mode='wt'（w=write、t=text）
# 建議永遠明確指定 encoding，避免跨平台預設編碼差異。
path = Path("hello.txt")
with open(path, "wt", encoding="utf-8") as f:
    f.write("你好，Python\n")
    f.write("第二行\n")

# 讀回方式一：f.read() 一次把整個檔案讀進記憶體
# 適合小檔；超大檔案不建議。
with open(path, "rt", encoding="utf-8") as f:
    print(f.read())  # 一次讀完（小檔才適合）

# 讀回方式二：逐行迭代，記憶體友善，適合大檔
with open(path, "rt", encoding="utf-8") as f:
    for line in f:
        # rstrip() 去掉尾端換行，印出來版面較乾淨
        print(line.rstrip())

# ── 5.2 print 導向檔案 ─────────────────────────────────
# print(..., file=f) 可以把輸出寫到檔案，而不是終端機。
with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
# sep 參數控制多個值中間怎麼連接；end 參數控制結尾字元。
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    print(*fruits, sep=",", end="\n", file=f)

# 先寫 date,（不換行），再接著寫日期，形成同一行 CSV 資料
with open("fruits.csv", "at", encoding="utf-8") as f:
    print("date", end=",", file=f)
    print("2026-04-23", file=f)

print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# "wt" 只能寫 str；"wb" 才能寫 bytes。
# 寫錯型別時，Python 會丟 TypeError。
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # ← 會錯
except TypeError as e:
    # 用教學方式顯示錯誤訊息，幫助理解型別不相容
    print("錯誤示範:", e)
