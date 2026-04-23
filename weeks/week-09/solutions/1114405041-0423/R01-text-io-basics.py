# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數
#
# 這份檔案的目的：
# 1) 學會用 open() 讀寫文字檔（含 encoding）
# 2) 學會把 print() 導向檔案，而不是只印到終端機
# 3) 理解 sep / end 如何控制輸出格式
# 4) 知道文字模式（t）與位元組模式（b）的型別限制

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 寫入：mode='wt'（write text）
# - w：若檔案不存在就建立；若已存在會「整個覆蓋」
# - t：文字模式（預設就是 t）
# - encoding='utf-8'：明確指定編碼，避免跨平台亂碼
path = Path("hello.txt")
with open(path, "wt", encoding="utf-8") as f:
    f.write("你好，Python\n")
    f.write("第二行\n")
# 這段會建立（或覆蓋）hello.txt，內容有兩行。
# 注意：f.write() 不會自動加換行，所以要自己寫 "\n"。

# 讀回：一次讀完 vs 逐行讀
# 讀取模式用 rt（read text）：
# - r：讀取
# - t：文字模式
with open(path, "rt", encoding="utf-8") as f:
    print(f.read())  # 一次讀完（小檔才適合）
# 這裡示範 f.read()：把整個檔案一次讀進記憶體。
# 優點是寫法簡單；缺點是檔案很大時會佔用較多 RAM。

with open(path, "rt", encoding="utf-8") as f:
    for line in f:  # 大檔必備：逐行迭代
        print(line.rstrip())
# 這裡示範逐行讀取：每次只讀一行，適合大檔案或串流處理。
# rstrip() 預設會去掉行尾空白與換行，讓輸出更乾淨。

# ── 5.2 print 導向檔案 ─────────────────────────────────
# print(..., file=f) 可以把輸出寫進檔案。
# 這在紀錄 log、輸出報告、產生測試結果檔時非常常見。
with open("log.txt", "wt", encoding="utf-8") as f:
    print("登入成功", file=f)
    print("使用者:", "alice", file=f)
# 這段執行後，log.txt 會有兩行文字。
# 若不加 file=f，print 會印到終端機而不是檔案。

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
# print 兩個很重要的格式參數：
# - sep：多個參數之間用什麼分隔
# - end：輸出結尾是什麼（預設是 "\n"）
fruits = ["apple", "banana", "cherry"]
with open("fruits.csv", "wt", encoding="utf-8") as f:
    print(*fruits, sep=",", end="\n", file=f)
# *fruits 會把清單元素展開成多個參數給 print。
# 配合 sep=","，就會得到 CSV 常見格式：apple,banana,cherry。

# end='' 可避免多一個換行
# 這裡採用附加模式 at（append text）：
# - a：不覆蓋原檔，直接接在檔案尾端
with open("fruits.csv", "at", encoding="utf-8") as f:
    print("date", end=",", file=f)
    print("2026-04-23", file=f)
# 第一個 print 設 end=","，所以不換行、先留下逗號。
# 第二個 print 再把日期接上並在最後換行。

print(Path("fruits.csv").read_text(encoding="utf-8"))
# apple,banana,cherry
# date,2026-04-23
# read_text() 是 Path 物件的便捷讀檔方法。
# 這裡直接印出結果，確認「覆蓋寫入 + 附加寫入」都正確。

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 型別規則：
# - wt / rt：處理 str（文字）
# - wb / rb：處理 bytes（位元組）
# 兩種模式不能混用，否則會拋出 TypeError。
try:
    with open("bad.txt", "wt", encoding="utf-8") as f:
        f.write(b"bytes in text mode")  # ← 會錯
except TypeError as e:
    print("錯誤示範:", e)
# 這段故意示範錯誤用法：在文字模式寫入 bytes。
# 你會看到 TypeError，提醒你要先 decode 成 str，或改用 wb 模式。
