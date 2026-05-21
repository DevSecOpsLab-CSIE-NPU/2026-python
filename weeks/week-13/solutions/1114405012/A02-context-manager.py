# A02. with 語句與 Context Manager
#
# 「借東西要還」的程式設計原則：當我們開啟資源（檔案、網路連線、鎖等）時，
# 必須確保在程式結束或發生例外時能正確釋放資源。`with` 與 Context Manager 正是為
# 這類情境設計的語法糖，能把「進入」與「離開」的行為包裝起來，讓資源管理更安全且易讀。
#
# 學習要點：
#  - 實作一個 class-based 的 Context Manager（實作 `__enter__` / `__exit__`）
#  - 使用 `contextlib.contextmanager` 以 yield 實作簡易版 Context Manager
#  - 利用 context manager 截取 stdout，方便在測試時驗證程式輸出

# ── 為什麼需要 with？ ─────────────────────────────────────
# 沒有 with 的開檔方式：如果中途發生例外，close() 可能永遠不會被呼叫

# 不好的寫法
# f = open("demo.txt", "w")
# f.write("hello")
# f.close()   # 如果 write 出錯，這行就不會執行了

# 正確的寫法：with 會自動呼叫 close()，即使出錯也一樣
print("=== with 開檔：自動關閉 ===")
with open("/tmp/week13_demo.txt", "w") as f:
    # with 會在離開區塊時自動執行 f.close()，即使寫入時發生例外也會被關閉
    f.write("Hello from Week 13\n")

with open("/tmp/week13_demo.txt", "r") as f:
    # 讀取檔案內容示範（同樣由 with 管理資源）
    print(f.read().strip())

# ── 自己寫 Context Manager（用 class）────────────────────
# 需要實作兩個方法：
#   __enter__：進入 with 區塊時執行，回傳值會被 as 接收
#   __exit__ ：離開 with 區塊時執行（不管有沒有出錯）

import time

class Timer:
    """簡單的計時 Context Manager（class-based 範例）。

    使用方式：
      with Timer() as t:
          # 這裡執行被計時的程式碼

    實作細節：
      - __enter__ 在進入 with 區塊時呼叫，通常用來建立或初始化資源；
      - __exit__ 在離開 with 區塊時呼叫（不論是否發生例外），可用於釋放或清理資源；
      - __exit__ 的回傳值決定是否要吞掉例外（回傳 True 則吞掉，不會再往外傳）。
    """

    def __enter__(self):
        # 記錄開始時間並回傳 self，讓使用者能在 with as t 中存取計時器物件
        self.start = time.time()
        print("⏱  開始計時")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 計算並印出經過時間；此處回傳 False，表示若 with 區塊發生例外，該例外仍會被拋出
        elapsed = time.time() - self.start
        print(f"⏱  結束：{elapsed:.4f} 秒")
        return False

print("\n=== 自訂計時器 ===")
with Timer() as t:
    total = sum(range(1_000_000))
print(f"計算結果：{total}")

# ── 更簡單的寫法：@contextmanager ─────────────────────────
# 不用寫 class，用 yield 分隔「進入前」和「離開後」

from contextlib import contextmanager

@contextmanager
def section(title):
    """用 `contextmanager` decorator 實作的簡易區段 context。

    使用 `yield` 將 enter（yield 前）與 exit（yield 後）邏輯分開，語意清楚且程式量少。
    """
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")
    # 交出控制權給 with 區塊，with 裡的程式碼會在這個 yield 暫停處執行
    yield
    # 當 with 區塊結束（或發生例外）會回到這裡執行 exit 的清理工作
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
    """暫時截取 `sys.stdout`，將所有 print 的輸出導到一個 StringIO 中。

    常見用途：在單元測試中捕捉輸出，方便做 assert。

    使用範例：
      with capture_output() as buf:
          print('hello')
      s = buf.getvalue()
    """
    old_stdout = sys.stdout
    buffer = io.StringIO()
    # 將 stdout 指向臨時 buffer
    sys.stdout = buffer
    try:
        # 傳出 buffer 給 with ... as buf 使用
        yield buffer
    finally:
        # 無論是否發生例外，都要把 stdout 還原回原本的物件
        sys.stdout = old_stdout

def solve_parity(n):
    """示範題：計算整數 n 的二進位表示中 1 的個數並印出結果。

    這個函式會把結果 print 出來；在測試時可用 `capture_output()` 截取輸出內容。
    """
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
