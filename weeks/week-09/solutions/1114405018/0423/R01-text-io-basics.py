# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 寫入：mode='wt'（write text）
# - w: 寫入模式。若檔案存在會「覆蓋舊內容」；不存在就建立新檔。
# - t: 文字模式（text mode），處理的是 str（字串）而非 bytes。
# - encoding='utf-8': 明確指定編碼，避免不同作業系統預設編碼不一致。
#   尤其寫中文時，強烈建議固定 utf-8。
path = Path("hello.txt")
with open(path, "wt", encoding="utf-8") as f:
    # f.write(...) 會回傳「實際寫入的字元數」，這裡我們不特別使用。
    # \n 是換行符號，寫入檔案後會形成下一行。
    f.write("你好，Python\n")
    f.write("第二行\n")

# 讀回：一次讀完 vs 逐行讀
with open(path, "rt", encoding="utf-8") as f:
    # f.read()：一次把整個檔案讀成一個字串。
    # 優點是直觀；缺點是大檔時會吃記憶體。
    print(f.read())  # 一次讀完（小檔才適合）

with open(path, "rt", encoding="utf-8") as f:
    # 檔案物件本身可迭代，for line in f 會一行一行讀。
    # 這種方式更省記憶體，適合大型檔案與日誌處理。
    for line in f:  # 大檔必備：逐行迭代
        # line 通常自帶行尾換行符，rstrip() 用來去除右側空白/換行。
        # 若不去掉，print() 會再補一個換行，看起來像多空一行。
        print(line.rstrip())

# ── 5.2 print 導向檔案 ─────────────────────────────────
with open("log.txt", "wt", encoding="utf-8") as f:
    # print(..., file=f) 可把輸出從螢幕改成寫入檔案。
    # 這在快速產生報表、記錄 log 時非常常用。
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # print(*fruits, sep=",") 等同把清單展開後用逗號連接。
    # 輸出結果：apple,banana,cherry
    # end="\n" 是每次 print 結尾字元（預設就是換行）。
    print(*fruits, sep=",", end="\n", file=f)

# end='' 可避免多一個換行
with open("fruits.csv", "at", encoding="utf-8") as f:
    # mode='at'：append text，採「附加」模式，不覆蓋原檔案。
    # 第一個 print 設定 end=","，代表不換行而是接逗號，
    # 下一個 print 會接在同一行後方。
    print("date", end=",", file=f)
    print("2026-04-23", file=f)

# 直接用 Path.read_text() 快速讀完整文字內容。
# 等價於 open(...).read()，但語法更精簡。
print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 'wt' 寫 str、'wb' 寫 bytes；寫錯型別會 TypeError
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        # 這裡刻意示範錯誤：
        # - 文字模式 wt 只接受 str
        # - b"..." 是 bytes
        # 因此會丟出 TypeError。
        f.write(b"bytes in text mode")  # ← 會錯
except TypeError as e:
    # 教學示範：攔截例外並印出訊息，讓學習者知道錯在哪。
    print("錯誤示範:", e)
