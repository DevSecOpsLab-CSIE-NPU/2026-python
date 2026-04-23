# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數
# 本範例介紹 Python 中文字檔的讀寫操作

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
#  mode='wt' 表示以文字模式寫入（text write），'t' 是預設值
#  encoding="utf-8" 是必要的參數，確保中文字能正確編碼
path = Path("hello.txt")
with open(path, "wt", encoding="utf-8") as f:
    f.write("你好，Python\n")
    f.write("第二行\n")
# 讀回檔案：有兩種方式
# 方式一：一次讀完（適用於小檔案）
with open(path, "rt", encoding="utf-8") as f:
    print(f.read())  # 一次讀完（小檔才適合）

# 方式二：逐行讀取（適用於大檔案，避免佔用過多記憶體）
with open(path, "rt", encoding="utf-8") as f:
    for line in f:  # 大檔必備：逐行迭代
        print(line.rstrip())

# ── 5.2 print 導向檔案 ─────────────────────────────────
#  使用 print() 函數的 file 參數可以將輸出寫入檔案
with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
#  sep 參數：設定元素之間的分隔符（預設是空白）
#  end 參數：設定行終止符（預設是換行符 \n）
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    print(*fruits, sep=",", end="\n", file=f)

#  mode='at' 表示附加模式（append text），在檔案末尾新增內容
#  end='' 表示不換行，讓下一個 print 接在該行之後
with open("fruits.csv", "at", encoding="utf-8") as f:
    print("date", end=",", file=f)
    print("2026-04-23", file=f)

print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
#  'wt' 寫入資料類型為 str（文字）
#  'wb' 寫入資料類型為 bytes（位元組）
#  如果寫錯資料型別會引發 TypeError
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # ← 會錯：文字模式不能寫入 bytes
except TypeError as e:
    print("錯誤示範:", e)