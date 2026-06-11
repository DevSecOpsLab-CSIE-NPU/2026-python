# R01-text-io-basics.py
# 完整繁體中文註釋版：示範文字檔案讀寫、print 導向檔案、分隔符與行終止符

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 使用 pathlib 建立路徑物件，方便跨平台操作
path = Path("hello.txt")
# 用文字寫入模式 'wt' 開啟檔案，並指定 encoding='utf-8'
with open(path, "wt", encoding="utf-8") as f:
    f.write("你好，Python\n")  # 寫入第一行
    f.write("第二行\n")      # 寫入第二行

# 讀回：一次讀完整個檔案內容
with open(path, "rt", encoding="utf-8") as f:
    print(f.read())  # 這種方式適合小檔案，一次讀入全部內容

# 讀回：逐行讀取，適合較大檔案或逐行處理時使用
with open(path, "rt", encoding="utf-8") as f:
    for line in f:              # 逐行迭代檔案
        print(line.rstrip())    # 去除末尾換行再印出

# ── 5.2 print 導向檔案 ─────────────────────────────────
with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)           # 將內容輸出到檔案
    print("使用者:", "alice", file=f)  # print 內建換行

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # sep="," 讓多個值以逗號分隔，end="\n" 讓 print 以換行結尾
    print(*fruits, sep=",", end="\n", file=f)

# 如果要追加內容，使用附加模式 'at'
with open("fruits.csv", "at", encoding="utf-8") as f:
    # end='' 代表這一行不自動加換行，方便接著寫
    print("date", end=",", file=f)
    print("2026-04-23", file=f)

# 直接讀取檔案內容，確認結果
print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 文字模式 'wt' 只能寫入 str，位元組模式 'wb' 才能寫入 bytes
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # 這裡會丟出 TypeError
except TypeError as e:
    print("錯誤示範:", e)
