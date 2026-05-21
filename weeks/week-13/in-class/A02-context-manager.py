# A02. with 語句與 Context Manager
# 範例與說明（繁體中文）：
# Context Manager 的核心概念是「取得資源→使用→釋放資源」，
# 使用 with 語句可以保證離開區塊時會執行清理（即使中途發生例外），
# 因此常用於檔案、網路連線、鎖（locks）、或任何需要明確釋放的資源。

# ── 為什麼需要 with？ ─────────────────────────────────────
# 傳統的資源管理（手動 open/close）容易在程式發生例外時遺漏清理步驟，
# with 透過 context manager 的協定保證 __exit__ 一定會被執行，避免資源洩漏。

# 不好的寫法
# f = open("demo.txt", "w")
# f.write("hello")
# f.close()   # 如果 write 出錯，這行就不會執行了

# 正確的寫法：with 會自動呼叫 close()，即使出錯也一樣
print("=== with 開檔：自動關閉 ===")
# 注意：Windows 路徑可改成相對路徑或使用 r"path"，示範使用 /tmp 只是跨平台範例
with open("/tmp/week13_demo.txt", "w") as f:
    # with 區塊結束時，f.close() 會自動被呼叫
    f.write("Hello from Week 13\n")

with open("/tmp/week13_demo.txt", "r") as f:
    # 讀取並去除末尾換行顯示
    print(f.read().strip())

# ── 自己寫 Context Manager（用 class）────────────────────
# 需要實作兩個方法：
#   __enter__：進入 with 區塊時執行，回傳值會被 as 接收
#   __exit__ ：離開 with 區塊時執行（不管有沒有出錯）

import time

class Timer:
    """
    計時器 Context Manager（class 實作範例）。

    使用方式：
      with Timer() as t:
          do_something()

    行為：
      - __enter__ 記錄開始時間並回傳 self（可由 as 取得）
      - __exit__ 計算經過時間並印出；回傳 False 表示若區塊內拋出例外，例外會繼續向外傳
    """

    def __enter__(self):
        # 記錄起始時間，並在進入時印出開始訊息
        self.start = time.time()
        print("⏱  開始計時")
        return self   # 這個值會被 as 接收，例如 as t

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 無論是否發生例外，__exit__ 都會被呼叫；這裡計算並印出經過時間
        elapsed = time.time() - self.start
        print(f"⏱  結束：{elapsed:.4f} 秒")
        # 如果回傳 True，表示吃掉（suppress）例外；通常我們不想吃掉例外，因此回傳 False
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
    """
    簡易的 context manager（使用 @contextmanager 包裝器）。

    說明：yield 前面的程式在進入 with 前執行（enter），
    yield 後面的程式在離開 with 時執行（exit）。
    此範例用於在輸出中產生區段樣式框線，方便閱讀測試或範例輸出。
    """
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
    """
    將 sys.stdout 暫時替換為 StringIO，截取 with 區塊內所有 print 的輸出，
    並在結束時把 stdout 還原。

    回傳值：yield 的 buffer（io.StringIO），可用於取得輸出字串進行測試比對。
    注意：此做法會影響整個程序的 stdout（全域），因此必須在 finally 區塊中保證還原，
    以免影響後續的輸出。
    """
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer     # with ... as buf 的 buf 就是這個 buffer
    finally:
        sys.stdout = old_stdout   # 一定要還原，finally 保證執行

def solve_parity(n):
    """
    UVA 10931 Parity：示範題目函式。

    功能：將 n 轉為二進位字串，計算其中 1 的個數，並印出指定格式的結果。
    回傳：無（直接使用 print 輸出，方便示範 capture_output 的使用情境）
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
# - __enter__ → 在 with 進入時執行，回傳值由 as 接收，通常用於建立或回傳資源
# - __exit__  → 在 with 離開時執行，會收到 (exc_type, exc_val, exc_tb) 以判斷是否有例外發生
#              若 __exit__ 回傳 True，會抑制（suppress）例外；通常我們選擇回傳 False
# - 使用 @contextmanager 時：yield 前的程式視為 enter，yield 後的程式視為 exit
# - 常用場景：檔案管理（open/close）、鎖（acquire/release）、計時器、截取輸出、資料庫連線等
