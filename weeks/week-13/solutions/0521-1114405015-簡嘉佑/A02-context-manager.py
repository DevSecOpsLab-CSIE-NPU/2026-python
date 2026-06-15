# A02. with 語句與 Context Manager
# 「借東西要還」——確保資源一定會被釋放，就算程式出錯也一樣
# 對應 Bloom's Taxonomy：應用（Apply）— 能設計並使用自訂的 with 區塊
#
# 主要場景：檔案、資料庫連線、鎖、計時器——
# 任何「用完要幸平幸還」的資源都適合用 with 管理。

# ── 為什麼需要 with？ ─────────────────────────────────────
# 沒有 with 的開檔方式：如果中途發生例外，close() 可能永遠不會被呼叫

# 不好的寫法
# f = open("demo.txt", "w")
# f.write("hello")
# f.close()   # 如果 write 出錯，這行就不會執行了

# 正確的寫法：with 會自動呼叫 close()，即使出錯也一樣
print("=== with 開檔：自動關閉 ===")
with open("/tmp/week13_demo.txt", "w") as f:
    f.write("Hello from Week 13\n")

with open("/tmp/week13_demo.txt", "r") as f:
    print(f.read().strip())

# ── 自己寫 Context Manager（用 class）────────────────────
# 需要實作兩個方法：
#   __enter__：進入 with 區塊時執行，回傳值會被 as 接收
#   __exit__ ：離開 with 區塊時執行（不管有沒有出錯）

import time

class Timer:
    """計時器：進入 with 時開始，離開時印出經過時間"""

    def __enter__(self):
        # with Timer() as t 進入時執行，回傳 self 讓 t 指向此物件
        self.start = time.time()
        print("⏱  開始計時")
        return self   # 這個值會被 as 接收，例如 as t

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 三個參數對應「例外型別、例外內容、追蹤資訊」
        # 如果 with 區塊沒有出錯，三個參數全是 None
        elapsed = time.time() - self.start
        print(f"⏱  結束：{elapsed:.4f} 秒")
        return False  # False = 不吞掉例外（讓錯誤繼續往外傳）

print("\n=== 自訂計時器 ===")
with Timer() as t:
    # with 區塊內執行任意程式碼，離開後 __exit__ 自動印出耗時
    total = sum(range(1_000_000))
print(f"計算結果：{total}")

# ── 更簡單的寫法：@contextmanager ─────────────────────────
# 不用寫 class，用 yield 分隔「進入前」和「離開後」

from contextlib import contextmanager

@contextmanager
def section(title):
    """印出有邊框的區段標題"""
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")；yield 前是「進入」，yield 後是「離開」
    print(f"{'─'*40}")  # 離開 with 後執行此行← with 區塊的程式碼在這裡執行
    print(f"{'─'*40}")

print()
with section("Week 13 CPE 模擬考"):
    print("  題目：UVA 11005 Cheapest Base")
    print("  時間限制：20 分鐘")

# ── CPE 應用：截取 stdout，方便測試輸出 ─────────────────
# 有些 CPE 題目會直接 print 答案
# 測試時可以截取 print 的輸出來比對

import io, sys

@contextmanager
def capture_output():
    """暫時把 print 的輸出截取到字串裡"""
    old_stdout = sys.stdout
    # 把標準輸出導向記憶體緩衝區，之後所有 print 都寫進 buffer
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer     # with ... as buf 的 buf 就是這個 buffer
    finally:
        # finally 保證即使出錯也一定會還原 stdout
        # 不還原的話，之後所有 print 都不會出現在終端機
        sys.stdout = old_stdout   # 一定要還原，finally 保證執行

def solve_parity(n):
    """計算 n 的二進位裡有幾個 1"""
    bits = bin(n)[2:]      # bin(10) 得 '0b1010'，[2:] 去掉 '0b'
    ones = bits.count('1') # 數 1 的個數
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")
   # 這裡的 print 會被截取，不出現在終端機
    solve_parity(7)

captured = out.getvalue()   # 一次取出全部截取內容
    solve_parity(7)

captured = out.getvalue()
print("截取到的輸出：")
print(captured)

# 可以直接拿來做 assertEqual
lines = captured.strip().split('\n')
print(f"共 {len(lines)} 行輸出")

# 記憶重點 ──────────────────────────────────────────────────
# __enter__ → 進入 with 時執行，回傳值被 as 接收
# __exit__  → 離開 with 時執行（出錯也會執行）
# @contextmanager + yield → 更簡單的寫法，yield 前是 enter，yield 後是 exit
# 常用場景：開檔、計時、測試輸出截取、任何「借了要還」的資源
