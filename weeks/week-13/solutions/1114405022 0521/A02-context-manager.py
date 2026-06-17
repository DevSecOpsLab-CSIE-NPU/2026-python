# A02. with 語句與 Context Manager
# 「借東西要還」——確保資源一定會被釋放，就算程式出錯也一樣
# 對應 Bloom's Taxonomy：應用（Apply）— 能設計並使用自訂的 with 區塊

# ── 為什麼需要 with？ ─────────────────────────────────────
# 沒有 with 的開檔方式：如果中途發生例外，close() 可能永遠不會被呼叫

# 不好的寫法
# f = open("demo.txt", "w")   # 手動開啟檔案
# f.write("hello")              # 寫入資料
# f.close()                     # 手動關閉 ← 如果 write 出錯，這行就不會執行了

# 正確的寫法：with 會自動呼叫 close()，即使出錯也一樣
print("=== with 開檔：自動關閉 ===")
# with 區塊結束時（無論正常或異常），open 回傳的檔案物件會自動呼叫 __exit__ 關閉
with open("/tmp/week13_demo.txt", "w") as f:
    f.write("Hello from Week 13\n")  # 寫入一筆資料

# 再次用 with 開啟同一個檔案，以讀取模式（"r"）
with open("/tmp/week13_demo.txt", "r") as f:
    print(f.read().strip())  # 讀取全部內容並去除前後空白後印出

# ── 自己寫 Context Manager（用 class）────────────────────
# 需要實作兩個方法：
#   __enter__：進入 with 區塊時執行，回傳值會被 as 接收
#   __exit__ ：離開 with 區塊時執行（不管有沒有出錯）

import time  # 匯入 time 模組，用於計時

class Timer:
    """計時器：進入 with 時開始，離開時印出經過時間"""

    def __enter__(self):
        """進入 with 區塊時自動呼叫，開始計時"""
        self.start = time.time()  # 記錄當前時間（秒數）到 self.start
        print("⏱  開始計時")     # 提示計時開始
        return self               # 回傳自身，讓 with ... as t 的 t 接收這個物件

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        離開 with 區塊時自動呼叫
        exc_type：例外類型（沒出錯就 None）
        exc_val ：例外實例（沒出錯就 None）
        exc_tb  ：回溯資訊（沒出錯就 None）
        """
        elapsed = time.time() - self.start          # 計算經過時間（現在－開始）
        print(f"⏱  結束：{elapsed:.4f} 秒")        # 印出經過時間，取到小數第 4 位
        return False  # False = 不吃掉例外（讓錯誤繼續往外傳）

print("\n=== 自訂計時器 ===")
with Timer() as t:             # 進入時建立 Timer 並開始計時
    total = sum(range(1_000_000))  # 計算 0 到 999999 的總和（百萬筆資料）
print(f"計算結果：{total}")    # 離開 with 後印出結果

# ── 更簡單的寫法：@contextmanager ─────────────────────────
# 不用寫 class，用 yield 分隔「進入前」和「離開後」

from contextlib import contextmanager  # 匯入裝飾器

@contextmanager  # 將下面的生成器函數變成 Context Manager
def section(title):
    """印出有邊框的區段標題"""
    print(f"\n{'='*40}")    # 印出 40 個等號作為上邊框
    print(f"  {title}")     # 印出標題（縮排兩個空白）
    print(f"{'='*40}")      # 印出 40 個等號
    yield           # ← with 區塊的程式碼在這裡執行（暫停點）
    print(f"{'─'*40}")      # 區塊結束後印出 40 個底線作為下邊框

print()
with section("Week 13 CPE 模擬考"):  # 進入 section，印出上邊框和標題
    print("  題目：UVA 11005 Cheapest Base")  # 區塊內執行的程式碼
    print("  時間限制：20 分鐘")               # 離開區塊後自動印出下邊框

# ── CPE 應用：截取 stdout，方便測試輸出 ─────────────────
# 有些 CPE 題目會直接 print 答案
# 測試時可以截取 print 的輸出來比對

import io     # 匯入 io 模組，用於 StringIO 字串緩衝區
import sys    # 匯入 sys 模組，用於更換 stdout

@contextmanager
def capture_output():
    """暫時把 print 的輸出截取到字串裡"""
    old_stdout = sys.stdout          # 先備份原本的 stdout
    sys.stdout = buffer = io.StringIO()  # 把 stdout 換成 StringIO 物件
    try:
        yield buffer     # with ... as buf 的 buf 就是這個 buffer（StringIO）
    finally:
        sys.stdout = old_stdout   # 一定要還原，finally 保證執行

def solve_parity(n):
    """UVA 10931 Parity：計算 n 的二進位裡有幾個 1"""
    bits = bin(n)[2:]          # bin(10) 回傳 '0b1010'，去掉 '0b' 前綴
    ones = bits.count('1')     # 計算字串中有幾個 '1'
    # 印出結果，格式符合 UVA 10931 的要求
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")

print("\n=== 截取輸出（測試用）===")
with capture_output() as out:    # 進入後，所有 print 會被導向 out
    solve_parity(10)              # 計算 10 的二進位 (1010) 有 2 個 1
    solve_parity(7)               # 計算 7 的二進位 (111) 有 3 個 1

captured = out.getvalue()        # 離開 with 後從 StringIO 取出所有擷取的內容
print("截取到的輸出：")
print(captured)                  # 印出剛才被截取的內容

# 可以直接拿來做 assertEqual（單元測試的斷言）
lines = captured.strip().split('\n')  # 以換行符號分割成多行
print(f"共 {len(lines)} 行輸出")      # 計算總共有幾行輸出

# 記憶重點 ──────────────────────────────────────────────────
# __enter__ → 進入 with 時執行，回傳值被 as 接收
# __exit__  → 離開 with 時執行（出錯也會執行）
# @contextmanager + yield → 更簡單的寫法，yield 前是 enter，yield 後是 exit
# 常用場景：開檔、計時、測試輸出截取、任何「借了要還」的資源
