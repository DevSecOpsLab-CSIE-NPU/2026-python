"""
A02-context-manager.py - Context Manager 與資源管理

進階觀念：
  Context Manager 實作了「確保資源正確釋放」的樣板（setup/teardown pattern）。
  無論程式碼區塊中是否發生例外，teardown 邏輯（__exit__ / finally）都會執行。

  兩種實作方式：
    1. 類別方式：實作 __enter__ 和 __exit__ 方法
       優點：可維護狀態（self.xxx），適合複雜資源管理
    2. contextlib.contextmanager 裝飾器方式：用 generator + yield
       優點：程式碼更簡潔，適合簡單的 setup/teardown 邏輯

  __exit__ 的回傳值語義：
    - 回傳 True：壓制（suppress）例外，程式繼續正常執行
    - 回傳 False 或 None：不壓制，例外繼續向上傳播

常見陷阱：
  1. 在類別式 CM 中，__exit__ 忘記回傳 True/False，
     預設回傳 None（等同 False），例外會向上傳播——通常是正確行為，
     但若想壓制特定例外，必須明確回傳 True。
  2. contextmanager 方式中，yield 之後的程式碼必須在 try/finally 中，
     否則例外發生時 teardown 程式碼不會執行。
  3. 巢狀 context manager 建議用 contextlib.ExitStack 管理，
     而非手動巢狀 with 陳述式。

標準寫法：
  - 類別式 CM：適合需要設定複雜狀態或需要 __enter__ 回傳有意義物件的場景
  - 裝飾器式 CM：適合簡單的 setup/yield/teardown 模式
  - 記錄例外資訊時，使用 logging 而非 print（本例為示範用途使用 print）
"""

import time
import io
import sys
import traceback
from contextlib import contextmanager
from typing import Optional, Type


# ─────────────────────────────────────────────
# 實作 1（類別方式）：計時器 Context Manager
# ─────────────────────────────────────────────

class Timer:
    """
    計算程式碼區塊執行時間的計時器，使用類別實作 context manager。

    使用方式：
        with Timer("資料庫查詢") as t:
            results = db.query(...)
        print(f"耗時: {t.elapsed:.3f}s")

    設計說明：
      - __enter__ 記錄開始時間並回傳 self，使 as 子句能存取 elapsed 屬性。
      - __exit__ 計算經過時間，無論是否發生例外都會執行。
      - suppress_errors=True 時，壓制例外讓程式繼續；
        False 時，記錄例外但讓它繼續傳播（預設行為）。
    """

    def __init__(self, name: str = "", suppress_errors: bool = False):
        self.name = name
        self.suppress_errors = suppress_errors
        self.elapsed: float = 0.0
        self._start: float = 0.0

    def __enter__(self) -> "Timer":
        """開始計時，回傳 self 供 as 子句使用。"""
        self._start = time.perf_counter()
        return self  # as 子句接收此回傳值

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[object],
    ) -> bool:
        """
        停止計時，記錄經過時間。

        參數說明：
          exc_type : 例外類型（無例外時為 None）
          exc_val  : 例外實例（無例外時為 None）
          exc_tb   : traceback 物件（無例外時為 None）

        回傳值：
          True  → 壓制例外（suppress_errors=True 時）
          False → 讓例外繼續傳播（預設）
        """
        self.elapsed = time.perf_counter() - self._start
        label = f"[{self.name}] " if self.name else ""

        if exc_type is not None:
            print(f"{label}計時結束（發生例外 {exc_type.__name__}）: {self.elapsed:.6f}s")
            if self.suppress_errors:
                print(f"{label}例外已被壓制: {exc_val}")
                return True  # 壓制例外
            return False     # 讓例外繼續傳播
        else:
            print(f"{label}執行完成: {self.elapsed:.6f}s")
            return False


# ─────────────────────────────────────────────
# 實作 2（contextmanager 裝飾器）：計時器
# ─────────────────────────────────────────────

@contextmanager
def timer(name: str = "", suppress_errors: bool = False):
    """
    與 Timer 類別相同功能的裝飾器版本。

    結構：
      - yield 之前的程式碼 ≡ __enter__
      - yield 回傳的值 ≡ __enter__ 的回傳值（供 as 子句使用）
      - yield 之後的程式碼 ≡ __exit__

    注意：使用 try/finally 確保即使例外發生，teardown 也會執行。
    若想要攔截例外，改用 try/except。
    """
    label = f"[{name}] " if name else ""
    elapsed_holder = [0.0]  # 用 list 讓 finally 區塊能存取（Python 3.9+ 可用 nonlocal）
    start = time.perf_counter()

    try:
        yield elapsed_holder  # 把持有 elapsed 的容器傳出去，讓呼叫端可讀取
    except Exception as e:
        elapsed_holder[0] = time.perf_counter() - start
        print(f"{label}計時結束（例外 {type(e).__name__}）: {elapsed_holder[0]:.6f}s")
        if suppress_errors:
            print(f"{label}例外已被壓制: {e}")
            return  # generator 的 return 等同於 StopIteration，壓制例外
        raise  # 重新拋出例外
    else:
        elapsed_holder[0] = time.perf_counter() - start
        print(f"{label}執行完成: {elapsed_holder[0]:.6f}s")


# ─────────────────────────────────────────────
# 實作 3（類別方式）：捕獲標準輸出（用於測試）
# ─────────────────────────────────────────────

class CaptureStdout:
    """
    暫時重定向 sys.stdout，捕獲程式碼區塊中的所有 print() 輸出。

    典型用途：測試中驗證 print() 的輸出內容，無需修改被測函數。

    使用方式：
        with CaptureStdout() as cap:
            print("hello")
            print("world")
        assert cap.output == "hello\\nworld\\n"
    """

    def __init__(self):
        self._buffer: Optional[io.StringIO] = None
        self._original_stdout = None
        self.output: str = ""

    def __enter__(self) -> "CaptureStdout":
        self._buffer = io.StringIO()
        self._original_stdout = sys.stdout
        sys.stdout = self._buffer   # 替換標準輸出
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.output = self._buffer.getvalue()
        sys.stdout = self._original_stdout  # 一定要還原，否則後續所有輸出都消失
        self._buffer.close()

        if exc_type is not None:
            # 例外發生時，輸出到真正的 stdout 以免除錯資訊消失
            print(f"[CaptureStdout] 例外發生於捕獲區塊: {exc_type.__name__}: {exc_val}")
        return False  # 不壓制例外


# ─────────────────────────────────────────────
# 實作 4（contextmanager 裝飾器）：捕獲標準輸出
# ─────────────────────────────────────────────

@contextmanager
def capture_stdout():
    """
    與 CaptureStdout 相同功能的裝飾器版本。
    回傳一個 dict 讓呼叫端在 with 區塊結束後能存取捕獲的輸出。
    """
    buffer = io.StringIO()
    original = sys.stdout
    result = {"output": ""}

    sys.stdout = buffer
    try:
        yield result
    finally:
        result["output"] = buffer.getvalue()
        sys.stdout = original  # 無論如何都要還原
        buffer.close()


# ─────────────────────────────────────────────
# 完整示範
# ─────────────────────────────────────────────

print("=" * 60)
print("計時器示範（類別方式）")
print("=" * 60)

# 基本計時
with Timer("正常執行") as t:
    time.sleep(0.05)
    result = sum(range(100_000))
print(f"  加總結果: {result}, elapsed 屬性: {t.elapsed:.6f}s\n")

# 有例外時（不壓制）
print("有例外時（不壓制）:")
try:
    with Timer("例外不壓制") as t:
        time.sleep(0.01)
        raise ValueError("模擬網路逾時")
except ValueError:
    print(f"  例外被重新拋出，elapsed: {t.elapsed:.6f}s\n")

# 有例外時（壓制）
print("有例外時（壓制例外）:")
with Timer("例外壓制", suppress_errors=True) as t:
    raise RuntimeError("模擬硬體錯誤")
print(f"  程式繼續執行，elapsed: {t.elapsed:.6f}s\n")

print("=" * 60)
print("計時器示範（contextmanager 裝飾器方式）")
print("=" * 60)

with timer("裝飾器計時") as elapsed_holder:
    time.sleep(0.03)
print(f"  elapsed_holder[0] = {elapsed_holder[0]:.6f}s\n")

# 壓制例外
print("裝飾器版本壓制例外:")
with timer("裝飾器壓制", suppress_errors=True):
    raise KeyError("模擬設定檔讀取失敗")
print("  程式繼續執行\n")


print("=" * 60)
print("捕獲 stdout 示範（類別方式）")
print("=" * 60)

def simulate_cpe_status_report(devices):
    """模擬 CPE 狀態報告輸出（用於示範 stdout 捕獲）。"""
    print(f"=== CPE 狀態報告 ===")
    for d in devices:
        status = "上線" if d.get("online") else "離線"
        print(f"  [{status}] {d['hostname']:20s}  {d['ip']}")
    print(f"共 {len(devices)} 台裝置")

devices = [
    {"hostname": "cpe-living-room", "ip": "192.168.1.2",  "online": True},
    {"hostname": "cpe-bedroom",     "ip": "192.168.1.3",  "online": False},
    {"hostname": "cpe-kitchen",     "ip": "192.168.1.4",  "online": True},
]

with CaptureStdout() as cap:
    simulate_cpe_status_report(devices)

# 此時輸出已被捕獲，cap.output 包含所有文字
print("捕獲到的輸出（前 80 字元）:")
print(repr(cap.output[:80]))

# 驗證輸出內容（模擬測試用法）
assert "cpe-living-room" in cap.output, "輸出應包含裝置名稱"
assert "共 3 台裝置" in cap.output, "輸出應包含統計"
print("  [測試通過] 輸出內容驗證成功\n")


print("=" * 60)
print("捕獲 stdout 示範（contextmanager 裝飾器方式）")
print("=" * 60)

with capture_stdout() as result:
    print("line 1: 裝置清單")
    print("line 2: 共 3 台")

print(f"捕獲行數: {result['output'].count(chr(10))}")
print(f"捕獲內容: {result['output']!r}\n")


print("=" * 60)
print("巢狀 context manager（ExitStack）")
print("=" * 60)

from contextlib import ExitStack

# ExitStack 允許動態組合多個 context manager，
# 適合「需要同時管理數量不固定的資源」的場景
with ExitStack() as stack:
    t1 = stack.enter_context(Timer("外層計時"))
    cap = stack.enter_context(CaptureStdout())

    print("這行會被捕獲，不會出現在終端機")
    time.sleep(0.02)
    print("捕獲的第二行")

# ExitStack 離開後，兩個 CM 依反序執行 __exit__
print(f"外層計時 elapsed: {t1.elapsed:.6f}s")
print(f"捕獲的輸出行數: {cap.output.count(chr(10))}")
