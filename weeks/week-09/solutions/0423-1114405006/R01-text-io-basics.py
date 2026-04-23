"""R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）

Bloom: Remember
學習目標：能正確使用 open() / print() 完成文字檔的讀寫、附加、與簡單輸出格式控制。

本檔示範四個核心觀念：
1) 文字檔讀寫（write / read / 逐行迭代）
2) 用 print(..., file=f) 直接把文字輸出到檔案
3) 用 sep / end 控制輸出格式（例如 CSV）
4) 文字模式（t）與位元組模式（b）的型別差異

重點原則：
- 文字檔建議明確指定 encoding="utf-8"，避免跨平台亂碼。
- 小檔案可 f.read() 一次讀完；大檔案請用 for line in f 逐行處理。
- 文字模式只能寫 str；位元組模式只能寫 bytes。
"""

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 寫入：mode='wt'（預設 't'），一定要指定 encoding
path = Path("hello.txt")
with open(path, "wt", encoding="utf-8") as f:
    # write() 不會自動補換行，所以這裡手動加上 \n
    f.write("你好，Python\n")
    f.write("第二行\n")

# 讀回：一次讀完 vs 逐行讀
with open(path, "rt", encoding="utf-8") as f:
    print(f.read())  # 一次讀完（小檔才適合）

with open(path, "rt", encoding="utf-8") as f:
    for line in f:  # 大檔必備：逐行迭代
        # rstrip() 去掉每行結尾換行，避免 print 時空一行
        print(line.rstrip())

# ── 5.2 print 導向檔案 ─────────────────────────────────
# print() 預設輸出到螢幕；加上 file=f 會改輸出到檔案
with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # *fruits 會展開成多個參數，sep="," 剛好輸出成 CSV 一列
    print(*fruits, sep=",", end="\n", file=f)

# end='' 可避免多一個換行
with open("fruits.csv", "at", encoding="utf-8") as f:
    # 先寫欄位值與逗號，不換行
    print("date", end=",", file=f)
    # 再寫第二個值並換行，完成第二列
    print("2026-04-23", file=f)

# 快速驗證輸出內容
print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 'wt' 寫 str、'wb' 寫 bytes；寫錯型別會 TypeError
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # 故意示範錯誤：bytes 不能寫入文字模式
except TypeError as e:
    # 捕捉錯誤並印出，讓學習者知道常見型別錯誤長什麼樣子
    print("錯誤示範:", e)
