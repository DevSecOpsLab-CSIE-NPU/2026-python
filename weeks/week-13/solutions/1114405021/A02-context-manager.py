# A02. with 語句與 Context Manager
# 說明：
# 本檔展示各種建立與使用 context manager 的方式，包括：
# 1) 直接用 with 管理系統資源（例如檔案）以確保自動關閉；
# 2) 使用 class 來定義具有 __enter__/__exit__ 的 context manager；
# 3) 用 @contextmanager（generator-based）以更簡潔的方式撰寫；
# 4) 在測試情境下截取 stdout 的應用範例。


# ---------- 為什麼要用 with ----------
# 使用 with 的主要目的是「確保資源被正確釋放（借了要還）」，
# 包括檔案描述符、鎖（threading.Lock）、網路連線、暫存資源等。
# 如果不使用 with，當發生例外時程式可能跳過釋放資源的程式碼，導致資源洩漏。
print("=== with 開檔：自動關閉（範例） ===")
# 注意：範例使用 /tmp 目錄做示範，在 Windows 環境可能不存在；
# 真正使用時請改用相對路徑或平台適用的暫存目錄（例如 tempfile 模組）。
with open("/tmp/week13_demo.txt", "w") as f:
    f.write("Hello from Week 13\n")

with open("/tmp/week13_demo.txt", "r") as f:
    # 讀取並去除尾端換行以利輸出展示
    print(f.read().strip())


# ---------- 自己實作 Context Manager（用 class） ----------
# 透過 class 我們可以在 __enter__ 做初始化（例如開檔、取得鎖），
# 在 __exit__ 做清理（關檔、釋放鎖）。__exit__ 的參數可用來處理例外。
import time

class Timer:
    """
    計時器 Context Manager（class 版）。

    使用方式：
        with Timer() as t:
            ...  # 這裡是要計時的程式區塊

    行為說明：
    - __enter__：紀錄起始時間並回傳 self（讓使用者可以取得計時器物件）。
    - __exit__：計算並印出經過時間；回傳 False 表示若有例外，例外會被重新拋出。

    為何回傳 False：若你想吞掉（處理）例外，可以回傳 True，但通常我們希望錯誤被顯示，
    所以預設回傳 False。
    """

    def __enter__(self):
        self.start = time.time()
        print("⏱  開始計時")
        return self   # 這個值會被 as 接收，例如 as t

    def __exit__(self, exc_type, exc_val, exc_tb):
        # exc_type, exc_val, exc_tb 分別代表是否有發生例外及其內容
        elapsed = time.time() - self.start
        print(f"⏱  結束：{elapsed:.4f} 秒")
        return False  # False = 不吃掉例外（讓錯誤繼續往外傳）


print("\n=== 自訂計時器 ===")
with Timer() as t:
    # 這裡放要被計時的工作，示範為計算 1+2+...+999999
    total = sum(range(1_000_000))
print(f"計算結果：{total}")


# ---------- 用 @contextmanager（更簡潔） ----------
# @contextmanager 的實作方式是撰寫一個 generator，yield 前的程式為 enter，
# yield 後（通常在 finally）則為 exit；這樣可以避免撰寫完整的 class。
from contextlib import contextmanager

@contextmanager
def section(title):
    """
    簡單的區段標題 Context Manager，示範 enter/exit 動作。

    用法：
        with section("標題"):
            ...

    在 enter 時印出標題框；在 exit 時印出分隔線。
    """
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")
    try:
        yield           # ← with 區塊的程式碼在這裡執行
    finally:
        # 無論 with 區塊是否拋出例外，都會執行到這裡
        print(f"{'─'*40}")


print()
with section("Week 13 CPE 模擬考"):
    print("  題目：UVA 11005 Cheapest Base")
    print("  時間限制：20 分鐘")


# ---------- CPE 應用：截取 stdout（測試用） ----------
# 有些題目直接用 print 輸出答案；在單元測試時我們常需要截取輸出以比對結果。
import io, sys

@contextmanager
def capture_output():
    """
    將標準輸出暫時替換成 StringIO，回傳該 buffer 供外部讀取。

    使用者通常這樣用：
        with capture_output() as buf:
            some_printing_function()
        output = buf.getvalue()

    實作注意：一定要在 finally 區塊把 sys.stdout 還原，否則會破壞全域輸出狀態。
    """
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        yield buffer     # with ... as buf 的 buf 就是這個 buffer
    finally:
        # 無論是否發生例外，都要把 stdout 還原
        sys.stdout = old_stdout


def solve_parity(n):
    """
    範例題：計算 n 的二進位表示中 1 的個數，並印出 parity 訊息。

    輸出格式模擬 UVA 10931 題目的輸出：
        The parity of <bits> is <count> (mod 2 is <count%2>). 
    """
    bits = bin(n)[2:]
    ones = bits.count('1')
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")


print("\n=== 截取輸出（測試用）===")
with capture_output() as out:
    # 在此區塊中的所有 print 都會被 capture_output 捕捉
    solve_parity(10)
    solve_parity(7)

captured = out.getvalue()
print("截取到的輸出：")
print(captured)

# 範例：把輸出分割成行，方便做 assert 或後續比對
lines = captured.strip().split('\n')
print(f"共 {len(lines)} 行輸出")


# ---------- 記憶重點 ----------
# - __enter__ → 進入 with 時執行，回傳值被 as 接收
# - __exit__  → 離開 with 時執行（出錯也會執行）；可透過回傳值決定是否吞掉例外
# - @contextmanager + yield → 更簡潔的寫法，yield 前為 enter，yield 後為 exit
# - 常用場景：開檔、鎖、網路連線、計時、測試輸出截取等任何需要釋放資源的情境
