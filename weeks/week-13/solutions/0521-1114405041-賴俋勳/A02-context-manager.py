# ===================================================================
# A02. with 語句與 Context Manager
# 學生：賴俋勳 1114405041
# 日期：2026-05-21
# 主題：with 語句 / 上下文管理器 — 確保資源一定會被釋放
# ===================================================================
# 【學習心得】
#   with 語句的核心概念是「借東西一定要還」。
#   無論中途是否發生例外，with 區塊結束時一定會執行清理動作。
#   可以用 class 實作（定義 __enter__/__exit__），
#   也可以用 @contextmanager + yield 更簡潔地實作。
# ===================================================================

# ── 為什麼需要 with？ ──────────────────────────────────────
# 不好的寫法：如果 write 發生例外，close() 就永遠不會被呼叫，
# 造成「檔案被鎖住」或「緩衝區的資料沒被寫入磁碟」。
# 正確的做法是用 with，它會自動呼叫 close()。

print("=== with 開檔：自動關閉 ===")
# with 進入時呼叫 open()，離開時自動呼叫 f.close()
# 即使 write 出錯，close 也會被呼叫（確保資源釋放）
with open("/tmp/week13_demo.txt", "w") as f:
    f.write("Hello from Week 13\n")

with open("/tmp/week13_demo.txt", "r") as f:
    print(f.read().strip())

# ── 自己寫 Context Manager（用 class）─────────────────────
# 要實作的兩個魔術方法：
#   __enter__(self)                     → 進入 with 時呼叫，回傳值被 as 接收
#   __exit__(self, exc_type, exc_val, exc_tb) → 離開時呼叫（無論有無例外）
#
# __exit__ 的三個參數是「例外資訊」：
#   exc_type：例外的類型（例如 ValueError）
#   exc_val ：例外的值（具體的錯誤訊息）
#   exc_tb  ：Traceback 物件
# 若 __exit__ 回傳 True，例外會被「吃掉」（不繼續往上傳）。
# 通常回傳 False，讓例外正常傳播。

import time

class Timer:
    """計時器：進入 with 時開始，離開時印出經過時間"""

    def __enter__(self):
        # 記錄開始時間，並回傳 self（讓 as 能接收這個物件）
        self.start = time.time()
        print("⏱  開始計時")
        return self   # as t → t 就是這個 Timer 物件

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 不論有沒有發生例外，都會計算並印出經過時間
        elapsed = time.time() - self.start
        print(f"⏱  結束：{elapsed:.4f} 秒")
        return False  # 不吃掉例外，讓錯誤繼續往外傳

print("\n=== 自訂計時器 ===")
with Timer() as t:
    # with 區塊的程式碼跑完後，自動呼叫 t.__exit__()
    total = sum(range(1_000_000))
print(f"計算結果：{total}")

# ── 更簡單的寫法：@contextmanager ─────────────────────────
# 不用寫 class，用生成器函數 + yield 分隔「進入前」和「離開後」：
#   yield 之前的程式碼 → __enter__ 做的事
#   yield 的回傳值     → as 接收到的值
#   yield 之後的程式碼 → __exit__ 做的事

from contextlib import contextmanager

@contextmanager
def section(title):
    """印出有邊框的區段標題，離開時印分隔線"""
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")
    yield           # with 區塊的程式碼在這裡執行
    # yield 後面的程式碼在 with 區塊結束後執行
    print(f"{'─'*40}")

print()
with section("Week 13 CPE 模擬考"):
    print("  題目：UVA 11005 Cheapest Base")
    print("  時間限制：20 分鐘")

# ── CPE 應用：截取 stdout，方便測試輸出 ──────────────────
# 有些 CPE 題目會直接 print 答案，測試時需要截取 print 的輸出來比對。
# 做法：暫時把 sys.stdout 替換成 StringIO buffer，
#       with 結束後再還原。用 finally 確保一定還原。

import io, sys

@contextmanager
def capture_output():
    """
    暫時截取 print 的輸出到字串 buffer。
    with capture_output() as buf: → buf 是 StringIO 物件
    buf.getvalue() → 取得截取到的全部輸出字串
    """
    old_stdout = sys.stdout          # 先保存原本的 stdout
    sys.stdout = buffer = io.StringIO()   # 替換成 buffer
    try:
        yield buffer     # with 區塊裡的 print 都會寫到 buffer
    finally:
        sys.stdout = old_stdout   # 無論如何一定還原（finally 保證）

def solve_parity(n):
    """UVA 10931 Parity：計算 n 的二進位裡有幾個 1"""
    bits = bin(n)[2:]       # bin(10) = '0b1010'，[2:] 去掉 '0b' 前綴
    ones = bits.count('1')  # 計算 '1' 的個數
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")

print("\n=== 截取輸出（測試用）===")
with capture_output() as out:
    solve_parity(10)   # 輸出被截取，不會印在螢幕上
    solve_parity(7)

captured = out.getvalue()   # 取得截取到的所有輸出
print("截取到的輸出：")
print(captured)

lines = captured.strip().split('\n')
print(f"共 {len(lines)} 行輸出")

# ─── 記憶重點 ──────────────────────────────────────────────
# __enter__ → 進入 with 時執行，回傳值被 as 接收
# __exit__  → 離開 with 時執行（出錯也會執行）
# @contextmanager + yield → 更簡單的寫法，yield 前是 enter，yield 後是 exit
# 常用場景：開檔、計時、測試輸出截取、任何「借了要還」的資源
