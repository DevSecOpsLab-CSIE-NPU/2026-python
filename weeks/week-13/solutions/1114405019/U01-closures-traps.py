"""
U01-closures-traps.py - 閉包與常見陷阱

進階觀念：
  閉包（Closure）是一個函數，它記住了定義時所在的詞法作用域（lexical scope），
  即使那個作用域已經執行完畢。閉包「捕獲」的是「變數本身」（name binding），
  而非變數當時的值，這正是「晚期綁定」的根源。

  本檔示範三大陷阱與對應解法：
    1. 可變動預設參數（Mutable default arguments）
    2. 閉包晚期綁定（Late binding in closures）
    3. nonlocal 關鍵字的正確使用時機

常見陷阱：
  1. def f(x=[])：預設參數在「函數定義時」只求值一次，
     所有呼叫共用同一個 list 物件，導致狀態在呼叫間積累。
  2. 在迴圈中建立 lambda 捕獲迴圈變數：
     所有 lambda 共用同一個 i 的綁定，結束後 i 是最終值。
  3. 在巢狀函數中對外部變數賦值而不加 nonlocal：
     Python 會視為在本地作用域新建一個同名變數，
     導致 UnboundLocalError 或修改無效。

標準寫法：
  - 預設參數用 None，函數體內再初始化可變物件。
  - 迴圈中的閉包，用預設參數 (i=i) 強制在定義時複製當前值。
  - 需要修改外層區域變數時，明確加 nonlocal 宣告。
"""


# ─────────────────────────────────────────────
# 陷阱 1：可變動預設參數（Mutable Default Argument）
# ─────────────────────────────────────────────

print("=" * 60)
print("陷阱 1：可變動預設參數")
print("=" * 60)

# ── 錯誤示範 ──
def add_device_BAD(device, device_list=[]):
    """
    問題：device_list=[] 這個 [] 只在函數「定義時」建立一次。
    所有呼叫（未傳入 device_list 時）共用同一個 list 物件。
    結果：後續呼叫會看到前次呼叫留下的資料！
    """
    device_list.append(device)
    return device_list

print("\n[錯誤] add_device_BAD:")
print(add_device_BAD("CPE-001"))    # ['CPE-001']
print(add_device_BAD("CPE-002"))    # ['CPE-001', 'CPE-002']  ← 預期只有 CPE-002！
print(add_device_BAD("CPE-003"))    # ['CPE-001', 'CPE-002', 'CPE-003'] ← 越來越長

# 檢查預設參數物件的 id（證明是同一個物件）
print(f"預設 list 的 id: {id(add_device_BAD.__defaults__[0])}")
print(f"預設 list 的現況: {add_device_BAD.__defaults__[0]}")  # 已被污染

# ── 正確解法 ──
def add_device_GOOD(device, device_list=None):
    """
    解法：預設值設為 None（不可變，無污染問題），
    函數體內每次呼叫時再建立新的 list。
    """
    if device_list is None:
        device_list = []     # 每次呼叫都建立全新的 list
    device_list.append(device)
    return device_list

print("\n[正確] add_device_GOOD:")
print(add_device_GOOD("CPE-001"))   # ['CPE-001']
print(add_device_GOOD("CPE-002"))   # ['CPE-002']  ← 正確！各呼叫互不影響

# 仍可傳入現有 list 進行追加
existing = ["CPE-000"]
print(add_device_GOOD("CPE-001", existing))  # ['CPE-000', 'CPE-001']

# 使用可變預設參數的唯一合理情境：刻意共享狀態（效能快取）
def cached_lookup(key, _cache={}):
    """
    此處刻意利用共享 dict 作為快取，是有意為之的設計。
    但應在註解中明確說明，避免後人誤認為 bug。
    """
    if key not in _cache:
        _cache[key] = f"computed_{key}"
    return _cache[key]

print("\n[刻意共享] 快取示範:")
print(cached_lookup("a"))  # computed_a
print(cached_lookup("a"))  # computed_a（從快取取）
print(cached_lookup("b"))  # computed_b


# ─────────────────────────────────────────────
# 陷阱 2：閉包晚期綁定（Late Binding）
# ─────────────────────────────────────────────

print("\n" + "=" * 60)
print("陷阱 2：閉包晚期綁定")
print("=" * 60)

# ── 錯誤示範 ──
def make_handlers_BAD():
    """
    在迴圈中建立 lambda（或一般函數），每個 lambda 都捕獲了「i 這個名字」，
    而不是「i 當時的值」。迴圈結束後，i=4（最後一個值），
    所以所有 lambda 呼叫時都查詢到 i=4。
    """
    handlers = []
    for i in range(5):
        handlers.append(lambda: i)  # 捕獲了 i 的「名字」，而非當時值
    return handlers

print("\n[錯誤] make_handlers_BAD（預期 0,1,2,3,4）:")
bad_handlers = make_handlers_BAD()
print([h() for h in bad_handlers])  # [4, 4, 4, 4, 4] ← 全都是 4！

# 具體的 CPE 情境：動態建立不同埠號的連線函數
def make_port_connectors_BAD(ports):
    """
    為每個埠建立一個「連線函數」，但晚期綁定導致所有函數都用最後一個埠號。
    """
    connectors = {}
    for port in ports:
        connectors[port] = lambda: f"connecting to port {port}"
    return connectors

print("\n[錯誤] make_port_connectors_BAD（埠號 80, 443, 8080）:")
bad_connectors = make_port_connectors_BAD([80, 443, 8080])
for p, conn in bad_connectors.items():
    print(f"  connector[{p}]() = {conn()}")  # 全都輸出 8080！

# ── 正確解法 1：預設參數強制即時綁定 ──
def make_handlers_GOOD_v1():
    """
    解法：lambda 加上預設參數 (i=i)。
    Python 在「定義 lambda」時就求值預設參數，將當時的 i 值複製一份。
    """
    handlers = []
    for i in range(5):
        handlers.append(lambda val=i: val)  # i=i 在定義時就確定了值
    return handlers

print("\n[正確 v1] make_handlers_GOOD_v1（預設參數）:")
good_handlers_v1 = make_handlers_GOOD_v1()
print([h() for h in good_handlers_v1])  # [0, 1, 2, 3, 4] ← 正確！

# ── 正確解法 2：使用工廠函數（更清晰的閉包用法）──
def make_handler(i):
    """
    工廠函數：每次呼叫都建立一個新的作用域，i 在這個作用域中是「本地變數」，
    不受迴圈後續迭代的影響。
    """
    def handler():
        return i  # 捕獲的是 make_handler 作用域中的 i，每次呼叫都不同
    return handler

def make_handlers_GOOD_v2():
    return [make_handler(i) for i in range(5)]

print("\n[正確 v2] make_handlers_GOOD_v2（工廠函數）:")
good_handlers_v2 = make_handlers_GOOD_v2()
print([h() for h in good_handlers_v2])  # [0, 1, 2, 3, 4] ← 正確！

# ── 正確解法 3：partial（最具語義的寫法）──
from functools import partial

def make_port_connectors_GOOD(ports):
    """
    使用 partial 固定參數，避免晚期綁定，同時具有最清楚的 repr。
    """
    def connect(port):
        return f"connecting to port {port}"
    return {port: partial(connect, port) for port in ports}

print("\n[正確 v3] make_port_connectors_GOOD（partial）:")
good_connectors = make_port_connectors_GOOD([80, 443, 8080])
for p, conn in good_connectors.items():
    print(f"  connector[{p}]() = {conn()}")  # 各自輸出正確的埠號


# ─────────────────────────────────────────────
# nonlocal 關鍵字：修改外部區域變數
# ─────────────────────────────────────────────

print("\n" + "=" * 60)
print("nonlocal 關鍵字示範")
print("=" * 60)

# ── 沒有 nonlocal 的問題 ──
def make_counter_BAD():
    count = 0

    def increment():
        count = count + 1   # Python 把 count 視為本地變數（因為有賦值操作）
        return count        # 但本地 count 在賦值前被讀取 → UnboundLocalError

    return increment

print("\n[錯誤] make_counter_BAD（UnboundLocalError）:")
bad_counter = make_counter_BAD()
try:
    bad_counter()
except UnboundLocalError as e:
    print(f"  {e}")

# ── 正確：使用 nonlocal ──
def make_counter():
    """
    nonlocal 告訴 Python：count 不是本地變數，
    而是在最近的「非全域的外層作用域」中尋找。
    """
    count = 0

    def increment(step: int = 1):
        nonlocal count        # 宣告 count 是外層作用域的變數
        count += step
        return count

    def reset():
        nonlocal count
        count = 0

    def get():
        return count          # 讀取不需要 nonlocal（只有「賦值」才需要）

    return increment, reset, get

print("\n[正確] make_counter（nonlocal）:")
inc, rst, get = make_counter()
print(f"  inc()    = {inc()}")     # 1
print(f"  inc()    = {inc()}")     # 2
print(f"  inc(5)   = {inc(5)}")    # 7
print(f"  get()    = {get()}")     # 7
rst()
print(f"  reset → get() = {get()}")  # 0

# ── 實際應用：CPE 連線重試計數器 ──
def make_retry_manager(max_retries: int = 3):
    """
    閉包實作的重試管理器，使用 nonlocal 追蹤重試次數。
    比類別更輕量，適合簡單的有狀態行為。
    """
    attempts = 0

    def try_connect(host: str) -> str:
        nonlocal attempts
        attempts += 1
        if attempts <= max_retries:
            result = f"嘗試連線 {host}（第 {attempts}/{max_retries} 次）"
        else:
            result = f"已超過最大重試次數 {max_retries}，放棄連線 {host}"
        return result

    def get_attempts() -> int:
        return attempts   # 只讀，不需要 nonlocal

    def reset_attempts() -> None:
        nonlocal attempts
        attempts = 0

    return try_connect, get_attempts, reset_attempts

print("\n[應用] CPE 連線重試管理器:")
connect, get_attempts, reset = make_retry_manager(max_retries=3)
print(connect("192.168.1.1"))
print(connect("192.168.1.1"))
print(connect("192.168.1.1"))
print(connect("192.168.1.1"))  # 超過限制
print(f"共嘗試: {get_attempts()} 次")
reset()
print(f"重置後嘗試次數: {get_attempts()}")
