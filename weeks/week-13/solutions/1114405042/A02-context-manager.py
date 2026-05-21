"""
A02. with 語句與 Context Manager 範例檔

說明：示範如何使用 `with` 來管理資源（例如檔案、計時器、輸出截取），
以及如何自行實作 context manager（class 或使用 @contextmanager 裝飾器）。

此檔案包含教學用註解與多個可執行範例，方便在課堂或作業中直接執行觀察行為。
"""

# 範例一：使用 with 開檔（自動關閉檔案，安全）
print("=== with 開檔：自動關閉 ===")
with open("/tmp/week13_demo.txt", "w") as f:
    # 進入 with 區塊時會回傳檔案物件給 f，離開時自動呼叫 f.close()
    f.write("Hello from Week 13\n")

with open("/tmp/week13_demo.txt", "r") as f:
    # 讀取示範檔案內容並印出（rstrip 去掉結尾換行）
    print(f.read().strip())

# ── 自己寫 Context Manager（用 class）────────────────────
import time

class Timer:
    """計時器 context manager。

    使用方式：
        with Timer() as t:
            # 在此區塊計時

    行為：
    - __enter__: 紀錄開始時間，並可回傳 self（或其他物件）給 as
    - __exit__: 計算並印出經過時間；回傳值決定是否要吞掉例外
    """

    def __enter__(self):
        # 記錄開始時間，並回傳 self 讓使用者可以存取（例如 t.start）
        self.start = time.time()
        print("⏱  開始計時")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # __exit__ 在退出 with 區塊時被呼叫；不論區塊內是否發生例外都會執行
        elapsed = time.time() - self.start
        print(f"⏱  結束：{elapsed:.4f} 秒")
        # 回傳 False 表示不吞掉例外（若有例外會往外拋）
        return False

print("\n=== 自訂計時器 ===")
with Timer() as t:
    # 範例計算：1 到 999999 的總和（用來產生可觀的耗時）
    total = sum(range(1_000_000))
print(f"計算結果：{total}")

# ── 更簡單的寫法：使用 @contextmanager（function-based）────────
from contextlib import contextmanager

@contextmanager
def section(title):
    """以簡單的文字框印出區段標題，並在結束時印出分隔線。

    使用 yield 將 with 區塊的執行插入到函式中。yield 之前為 enter，之後為 exit。
    """
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")
    yield
    # yield 後的程式碼在離開 with 區塊時執行
    print(f"{'─'*40}")

print()
with section("Week 13 CPE 模擬考"):
    print("  題目：UVA 11005 Cheapest Base")
    print("  時間限制：20 分鐘")

# ── CPE 應用：截取 stdout，方便測試輸出（以 context manager 模擬測試框架）
import io, sys

@contextmanager
def capture_output():
    """暫時把 `sys.stdout` 交換為一個 StringIO，收集 print 的輸出。

    回傳值：yield 出的物件是該 StringIO，可以透過 .getvalue() 取得全部輸出字串。
    finally 區塊中會確保無論是否發生例外都會還原原本的 stdout。
    """
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer
    finally:
        sys.stdout = old_stdout

def solve_parity(n):
    """UVA 10931 Parity 類型的範例：印出二進位表示與 1 的個數。

    這裡用 print 模擬競程題目的輸出格式，方便搭配 `capture_output` 做測試。
    """
    bits = bin(n)[2:]
    ones = bits.count('1')
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")

print("\n=== 截取輸出（測試用）===")
with capture_output() as out:
    # 在 capture_output 範圍內的 print 都會被寫入到 out（StringIO）
    solve_parity(10)
    solve_parity(7)

captured = out.getvalue()
print("截取到的輸出：")
print(captured)

# 可以把 captured 的內容拆成多行，用於單元測試的比對或 assert
lines = captured.strip().split('\n')
print(f"共 {len(lines)} 行輸出")

# 記憶重點：
# - __enter__ → 進入 with 時執行，回傳值被 as 接收
# - __exit__  → 離開 with 時執行（出錯也會執行）；可選擇是否吞掉例外
# - @contextmanager + yield → 用函式寫 context manager，yield 前為 enter、yield 後為 exit
# - 常見用途：開檔、計時、測試輸出截取、資料庫連線、鎖定資源等「借了要還」的場景
