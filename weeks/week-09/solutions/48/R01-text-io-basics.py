# R01. 文字檔 I/O 基礎示範
# 主題：open() 讀寫文字檔、print() 輸出到檔案、sep/end 參數、文字模式與位元組模式差異

from pathlib import Path

# ── 1) 讀寫文本檔（對應 5.1） ─────────────────────────
# 建議：文字檔一律明確指定 encoding='utf-8'，避免跨平台亂碼
path = Path("hello.txt")

# 寫入模式 'wt'：
# w = 覆蓋寫入（檔案存在會清空），t = text 文字模式
with open(path, "wt", encoding="utf-8") as f:
    f.write("你好，Python\n")
    f.write("第二行\n")

# 讀取方式 A：一次讀完整個檔案（小檔案適合）
with open(path, "rt", encoding="utf-8") as f:
    print(f.read())

# 讀取方式 B：逐行讀取（大檔案更省記憶體）
with open(path, "rt", encoding="utf-8") as f:
    for line in f:
        # rstrip() 去掉行尾換行，讓輸出更乾淨
        print(line.rstrip())

# ── 2) print 導向檔案（對應 5.2） ─────────────────────
# print(..., file=f) 可以直接把輸出寫進檔案，而不是終端機
with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 3) sep 與 end 參數（對應 5.3） ───────────────────
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # *fruits 會展開成多個參數，sep=',' 讓欄位以逗號分隔
    print(*fruits, sep=",", end="\n", file=f)

# 追加模式 'at'：a = append，保留既有內容再加到尾端
with open("fruits.csv", "at", encoding="utf-8") as f:
    # end='' 先不換行，讓下一個 print 接在同一列
    print("date", end=",", file=f)
    print("2026-04-23", file=f)

# pathlib 快速讀文字內容
print(Path("fruits.csv").read_text(encoding="utf-8"))
# 預期：
# apple,banana,cherry
# date,2026-04-23

# ── 4) 文字模式與位元組模式差異（對應 5.17） ───────────
# 規則：
# - 'wt' / 'rt' 處理 str
# - 'wb' / 'rb' 處理 bytes
# 若模式與資料型別不匹配，會出現 TypeError
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # 故意示範錯誤：bytes 不能寫入文字模式
except TypeError as e:
    print("錯誤示範:", e)
