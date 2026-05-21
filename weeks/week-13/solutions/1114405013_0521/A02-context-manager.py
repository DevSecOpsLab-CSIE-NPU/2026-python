# A02. with 語句與 Context Manager
# 「借東西要還」——確保資源一定會被釋放，就算程式出錯也一樣
# 對應 Bloom's Taxonomy：應用（Apply）— 能設計並使用自訂的 with 區塊

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
        self.start = time.time()
        print("⏱  開始計時")
        return self   # 這個值會被 as 接收，例如 as t

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"⏱  結束：{elapsed:.4f} 秒")
        return False  # False = 不吃掉例外（讓錯誤繼續往外傳）

print("\n=== 自訂計時器 ===")
with Timer() as t:
    total = sum(range(1_000_000))
print(f"計算結果：{total}")

# 範例：自訂一個會「吞掉」例外的 context manager
# 如果 __exit__ 回傳 True，則 with 區塊中發生的例外會被視為已處理，不會向外拋出
class Suppressor:
    """Suppressor: 把指定的例外類型消化掉

    用法：with Suppressor(ValueError):
             # 若發生 ValueError，不會中斷程式
    """
    def __init__(self, *exc_types):
        self.exc_types = exc_types

    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 如果發生的例外屬於我們要 suppress 的類型，就回傳 True（吃掉例外）
        if exc_type is None:
            return False
        return issubclass(exc_type, self.exc_types)

print("\n=== Suppressor 範例（吃掉 ValueError） ===")
with Suppressor(ValueError):
    int('not-a-number')  # ValueError 被 Suppressor 吃掉，不會中斷
print("繼續執行，未被中斷")

# 範例：參數化的 contextmanager（用 @contextmanager）
# 可以把資源建立的細節包起來，讓使用者專注在 with 區塊的邏輯
from contextlib import contextmanager

@contextmanager
def resource_opener(name):
    """開啟一個假想資源並在離開時關閉它

    這個範例示範如何在 contextmanager 中傳遞參數與回傳值給 as
    """
    print(f"打開資源: {name}")
    try:
        yield {'name': name, 'opened': True}
    finally:
        print(f"關閉資源: {name}")

print() 
with resource_opener('my-db') as res:
    print('在 with 區塊內使用資源：', res)

# ── 更簡單的寫法：@contextmanager ─────────────────────────
# 不用寫 class，用 yield 分隔「進入前」和「離開後」

from contextlib import contextmanager

@contextmanager
def section(title):
    """印出有邊框的區段標題"""
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")
    yield           # ← with 區塊的程式碼在這裡執行
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
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer     # with ... as buf 的 buf 就是這個 buffer
    finally:
        sys.stdout = old_stdout   # 一定要還原，finally 保證執行

def solve_parity(n):
    """UVA 10931 Parity：計算 n 的二進位裡有幾個 1"""
    bits = bin(n)[2:]
    ones = bits.count('1')
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")

print("\n=== 截取輸出（測試用）===")
with capture_output() as out:
    solve_parity(10)
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
