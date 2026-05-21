"""
A01-partial.py - functools.partial 的進階應用

進階觀念：
  functools.partial 可以「預先填入」函數的部分引數，產生一個新的可呼叫物件。
  這種技巧稱為「偏函數 (Partial Function Application)」，能讓程式碼更具語義性。

常見陷阱：
  1. partial 不會複製函數的 __doc__，除非手動設定。
  2. partial 保留參數綁定的「執行時機」語義，與 lambda 不同（見下方比較）。
  3. 不能用 partial 覆蓋已由位置決定的關鍵字引數順序。

標準寫法：
  - 優先使用 partial 而非 lambda，因為 partial 有更清楚的 repr() 輸出，便於除錯。
  - 當需要動態建立多個「變體函數」時，partial 比 lambda 更為直觀。
"""

from functools import partial
import urllib.request
import json


# ─────────────────────────────────────────────
# 基本示範：用 partial 固定函數引數
# ─────────────────────────────────────────────

def power(base, exponent):
    """計算 base 的 exponent 次方。"""
    return base ** exponent

# 用 partial 固定 exponent=2，產生「平方函數」
square = partial(power, exponent=2)

# 用 partial 固定 exponent=3，產生「立方函數」
cube = partial(power, exponent=3)

print("=== 基本 partial 示範 ===")
print(f"square(5) = {square(5)}")   # 25
print(f"cube(3)   = {cube(3)}")     # 27

# partial 物件有清楚的 repr，有助於除錯
print(f"repr(square) = {square!r}")


# ─────────────────────────────────────────────
# 與 sorted() 結合：更具語義的排序 key
# ─────────────────────────────────────────────

def get_field(record: dict, field: str):
    """從字典中取出指定欄位的值（可設定預設值）。"""
    return record.get(field, "")

# 情境：對網路裝置清單依不同欄位排序
devices = [
    {"hostname": "router-01", "ip": "192.168.1.1",  "port": 8080, "vendor": "Cisco"},
    {"hostname": "switch-03", "ip": "10.0.0.3",     "port": 22,   "vendor": "Juniper"},
    {"hostname": "ap-02",     "ip": "172.16.0.2",   "port": 443,  "vendor": "Cisco"},
    {"hostname": "fw-01",     "ip": "10.0.0.1",     "port": 22,   "vendor": "Palo Alto"},
]

# 用 partial 固定 field，產生專用的排序 key 函數
sort_by_hostname = partial(get_field, field="hostname")
sort_by_port     = partial(get_field, field="port")
sort_by_vendor   = partial(get_field, field="vendor")

print("\n=== 依 hostname 排序 ===")
for d in sorted(devices, key=sort_by_hostname):
    print(f"  {d['hostname']:10s}  {d['ip']}")

print("\n=== 依 port 排序 ===")
for d in sorted(devices, key=sort_by_port):
    print(f"  port={d['port']:4d}  {d['hostname']}")


# ─────────────────────────────────────────────
# 網路 / CPE 應用：固定 API base URL
# ─────────────────────────────────────────────

def build_api_request(base_url: str, endpoint: str, method: str = "GET") -> str:
    """
    模擬建立 API 請求的 URL 字串（實際應用中會呼叫 requests.get / requests.post）。
    """
    return f"[{method}] {base_url.rstrip('/')}/{endpoint.lstrip('/')}"

# CPE 管理平台的 base URL（ACS / TR-069 場景）
ACS_BASE_URL = "http://acs.example.com:7547/api/v1"

# 用 partial 固定 base_url，產生針對此平台的請求函數
acs_request = partial(build_api_request, base_url=ACS_BASE_URL)

print("\n=== CPE ACS API 請求（固定 base_url）===")
print(acs_request(endpoint="devices"))
print(acs_request(endpoint="devices/00:11:22:33:44:55/reboot", method="POST"))
print(acs_request(endpoint="firmware/latest"))

# 也可以進一步固定 method，產生更具語義的函數
acs_post = partial(acs_request, method="POST")
print("\n=== 固定 method=POST 的 ACS 請求 ===")
print(acs_post(endpoint="devices/00:11:22:33:44:55/factory-reset"))


# ─────────────────────────────────────────────
# 對照組：lambda vs partial 的比較
# ─────────────────────────────────────────────

print("\n=== lambda vs partial 比較 ===")

# ── 用 lambda 達成相同效果 ──
square_lambda = lambda base: power(base, 2)
acs_request_lambda = lambda endpoint, method="GET": build_api_request(ACS_BASE_URL, endpoint, method)

print(f"square_lambda(5)     = {square_lambda(5)}")
print(f"acs_request_lambda('devices') = {acs_request_lambda('devices')}")

"""
比較摘要：

┌─────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│ 面向             │ partial                          │ lambda                          │
├─────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ 可讀性           │ 語義更明確，repr 顯示原函數與綁定值  │ 較簡短但可能隱藏意圖               │
│ repr 輸出        │ functools.partial(<func>, ...)   │ <function <lambda> at 0x...>    │
│ 引數執行時機     │ 引數在 partial() 呼叫時就已綁定     │ 引數在 lambda 被呼叫時才求值       │
│                 │（除了預設值的晚期綁定問題不存在）   │（注意閉包晚期綁定陷阱）             │
│ pickle 支援      │ 可 pickle（模組層級函數）           │ 通常無法 pickle                  │
│ 適用場景         │ 需要多次重用、需要除錯、需序列化     │ 簡單的一次性轉換、inline 使用      │
└─────────────────┴─────────────────────────────────┴─────────────────────────────────┘

關鍵差異 - 執行時機（晚期綁定）：
  partial 在建立時就確定了綁定值，之後不受外部變數變動影響。
  lambda 若捕獲外部變數（閉包），該變數的值在 lambda 被呼叫時才讀取，
  可能產生「晚期綁定陷阱」（詳見 U01-closures-traps.py）。
"""

# 示範執行時機差異
multiplier = 3
partial_times3 = partial(power, exponent=multiplier)  # exponent=3 已在此時綁定
lambda_times3  = lambda base: power(base, multiplier)  # multiplier 在呼叫時才查詢

multiplier = 10  # 修改外部變數

print(f"\n修改 multiplier 後：")
print(f"  partial_times3(2) = {partial_times3(2)} (仍使用原始綁定值 3)")
print(f"  lambda_times3(2)  = {lambda_times3(2)} (使用最新值 10，晚期綁定！)")
