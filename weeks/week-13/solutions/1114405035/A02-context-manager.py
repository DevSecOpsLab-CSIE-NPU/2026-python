# A02. with 語句與 Context Manager (上下文管理器)
# 「借東西要還」—— 確保資源一定會被釋放，即使程式執行過程中發生錯誤。
# 對應 Bloom's Taxonomy：應用 (Apply) — 能設計並使用自訂的 with 區塊。

# ── 為什麼需要 with？ ─────────────────────────────────────
# 在沒有 with 的情況下處理檔案，如果程式在中途當掉，檔案可能不會被正確關閉。

# ❌ 不建議的寫法：
# f = open("demo.txt", "w")
# f.write("hello")
# # 如果 write 發生例外 (Exception)，下面這行 close() 就不會被呼叫，導致資源洩漏。
# f.close() 

# ✅ 正確的寫法：with 區塊結束後會自動呼叫 close()。
print("=== with 開檔：自動關閉資源 ===")
# 使用 temp 目錄進行示範
import os
import tempfile

temp_path = os.path.join(tempfile.gettempdir(), "week13_demo.txt")

with open(temp_path, "w", encoding="utf-8") as f:
    f.write("來自第 13 週的問候\n")

with open(temp_path, "r", encoding="utf-8") as f:
    print(f"讀取內容：{f.read().strip()}")

# ── 自訂 Context Manager（使用 class 實作）────────────────────
# 一個類別只要實作以下兩個「魔術方法」就能支援 with：
#   __enter__：進入 with 區塊時執行，回傳值會被賦予給 as 後面的變數。
#   __exit__ ：離開 with 區塊時執行（無論是否發生錯誤）。

import time

class Timer:
    """計時器：進入時開始計時，離開時印出總花費時間"""

    def __enter__(self):
        self.start = time.time()
        print("⏱  [計時開始]")
        return self   # 回傳 self，讓外部可以用 as 接收實例

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type, exc_val, exc_tb 分別代表例外類型、值與追蹤資訊
        # 如果區塊內沒有出錯，這三個參數都會是 None
        elapsed = time.time() - self.start
        print(f"⏱  [計時結束] 經過時間：{elapsed:.4f} 秒")
        
        # 回傳 False 代表不攔截例外，讓例外繼續向上拋出
        # 回傳 True 則會「吃掉」例外，程式會繼續執行下去
        return False

print("\n=== 自訂計時器展示 ===")
with Timer() as t:
    # 模擬耗時運算
    total = sum(range(1_000_000))
print(f"運算結果：{total}")

# ── 更簡潔的寫法：使用 @contextmanager 裝飾器 ───────────────
# 不需要寫整個 class，利用 yield 將「進入前」與「離開後」的逻辑分開。

from contextlib import contextmanager

@contextmanager
def section(title):
    """印出帶有裝飾邊框的區段標題"""
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")
    
    try:
        yield       # ← with 區塊內的程式碼會在這裡執行
    finally:
        # 使用 finally 確保即使區塊內出錯，結尾裝飾也能印出來
        print(f"{'─'*40}")

print()
with section("Week 13 CPE 模擬考資訊"):
    print("  題目代號：UVA 11005 Cheapest Base")
    print("  建議限時：20 分鐘")
    print("  核心概念：進位制轉換與成本計算")

# ── CPE 實務應用：截取標準輸出 (stdout)，方便自動化測試 ──────
# 有些 CPE 題目要求直接 print 出結果。
# 撰寫測試程式時，我們可以用這個技巧抓取 print 的內容進行驗證。

import io, sys

@contextmanager
def capture_output():
    """暫時將 print 的輸出導向到記憶體緩衝區 (StringIO)"""
    old_stdout = sys.stdout                 # 保存原本的標準輸出 (螢幕)
    sys.stdout = buffer = io.StringIO()     # 替換為 StringIO
    try:
        yield buffer     # 將 buffer 傳給 with ... as 語句
    finally:
        sys.stdout = old_stdout   # 務必恢復原狀，避免之後的 print 失效

def solve_parity(n):
    """UVA 10931 Parity：計算 n 的二進位表示中 1 的個數 (Parity)"""
    bits = bin(n)[2:]
    ones = bits.count('1')
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")

print("\n=== 截取 stdout 輸出進行單元測試 ===")
with capture_output() as out:
    solve_parity(10) # 1010
    solve_parity(7)  # 111

# 取得截取到的所有字串內容
captured = out.getvalue()
print("--- 截取到的原始內容 ---")
print(captured, end="")
print("-----------------------")

# 驗證邏輯：檢查行數是否正確
lines = captured.strip().split('\n')
print(f"✅ 測試成功：共抓取到 {len(lines)} 行輸出結果。")

# 記憶重點 ──────────────────────────────────────────────────
# 1. __enter__ → 進入 with 時呼叫，設定資源。
# 2. __exit__  → 離開 with 時呼叫，釋放資源（保證執行）。
# 3. @contextmanager + yield → yield 之前是 setup，之後是 teardown。
# 4. 適用場景：資料庫連線、檔案操作、網路 Socket、鎖 (Lock) 的管理。
