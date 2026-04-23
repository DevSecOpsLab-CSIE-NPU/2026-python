# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 寫入：mode='wt'（write text）
# - w: 以「覆寫」方式開檔（檔案存在會清空，不存在會建立）
# - t: 文字模式（預設其實就是 t）
# - encoding='utf-8': 明確指定編碼，避免不同作業系統預設編碼不一致
# 建議習慣：凡是文字檔都主動寫 encoding，降低亂碼風險。
path = Path("hello.txt")
# with 區塊離開時會自動 close()，即使中途發生例外也會關檔，
# 這是 Python 進行檔案 I/O 的標準寫法。
with open(path, "wt", encoding="utf-8") as f:
    # write() 只會寫入字串本身，不會自動補換行，
    # 所以若要分行，通常要自行加上 \n。
    f.write("你好，Python\n")
    f.write("第二行\n")

# 讀回：一次讀完 vs 逐行讀
with open(path, "rt", encoding="utf-8") as f:
    # f.read() 一次把整個檔案內容載入記憶體。
    # 適合小型檔案；若檔案很大，會造成記憶體壓力。
    print(f.read())  # 一次讀完（小檔才適合）

with open(path, "rt", encoding="utf-8") as f:
    # 直接迭代檔案物件會一行一行讀取，
    # 屬於串流式處理，較省記憶體，適合大型檔案。
    for line in f:  # 大檔必備：逐行迭代
        # line 本身通常含有行尾換行符，
        # 用 rstrip() 去除尾端空白/換行，避免 print 再補一個換行造成空白行。
        print(line.rstrip())

# ── 5.2 print 導向檔案 ─────────────────────────────────
with open("log.txt", "wt", encoding="utf-8") as f:
    # print(..., file=f) 可把輸出目標由螢幕改成檔案。
    # 這對快速寫日誌、輸出報表很實用。
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # *fruits 會把串列拆成多個位置參數。
    # sep=","：欄位之間用逗號分隔（CSV 常見格式）
    # end="\n"：本行結尾補換行（預設也是 \n）
    print(*fruits, sep=",", end="\n", file=f)

# end='' 可避免多一個換行
with open("fruits.csv", "at", encoding="utf-8") as f:
    # mode='at'：append text，採「附加」模式，不會覆蓋原內容。
    # 第一行 end=","，可讓下一次 print 接在同一行形成逗號分隔。
    print("date", end=",", file=f)
    print("2026-04-23", file=f)

# 也可用 Path.read_text() 快速讀回整份文字檔。
# 適合教學與小工具；大型檔案仍建議逐行處理。
print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 文字模式與位元組模式的型別必須對應：
# - 'wt' / 'rt'：處理 str（字串）
# - 'wb' / 'rb'：處理 bytes（位元組）
# 若在文字模式寫入 bytes，會拋出 TypeError。
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # ← 會錯
except TypeError as e:
    # 教學示範：攔截型別錯誤並顯示錯誤訊息，幫助理解模式差異。
    print("錯誤示範:", e)
