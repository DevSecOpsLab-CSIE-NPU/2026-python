# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# open() 讀寫文本檔時，最常見的模式為 'rt' 與 'wt'
# 'r' = read, 'w' = write, 't' = text。寫入時要指定 encoding，否則在非 UTF-8 預設環境會出錯。
path = Path("hello.txt")
with open(path, "wt", encoding="utf-8") as f:
    # write() 不會自動加換行，必須手動加 '\n'
    f.write("你好，Python\n")
    f.write("第二行\n")

# 讀回檔案：一次讀完適合小檔案
with open(path, "rt", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 逐行讀：適合較大檔案、節省記憶體
with open(path, "rt", encoding="utf-8") as f:
    for line in f:
        # rstrip() 預設會去掉右側空白與換行符
        print(line.rstrip())

# ── 5.2 print 導向檔案 ─────────────────────────────────
# print() 的 file 參數可以把輸出導向到檔案，而不是標準輸出
with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
# print() 支援 sep 與 end 參數，可以控制欄位分隔和結尾行為
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # 將清單元素用逗號連接，並寫入 CSV 格式
    print(*fruits, sep=",", end="\n", file=f)

# 以附加模式 'at' 再加一行資料
# end='' 表示這次 print() 不會自動加上換行，方便與下一個 print 接續同一行
with open("fruits.csv", "at", encoding="utf-8") as f:
    print("date", end=",", file=f)
    print("2026-04-23", file=f)

# 讀出 fruits.csv，確認寫入結果
print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 在 text 模式 ('t') 中，write() 只能寫入 str；
# 在 binary 模式 ('b') 中，write() 只能寫入 bytes。
# 寫錯類型會造成 TypeError。
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # ← 這裡會失敗
except TypeError as e:
    print("錯誤示範:", e)

# 進階提醒：
# - 要讀寫二進位檔案（例如影像、壓縮檔）請使用 'rb' / 'wb'
# - 若檔案含非 UTF-8 字元，可改用 encoding='utf-8', errors='replace' 或 'ignore'
