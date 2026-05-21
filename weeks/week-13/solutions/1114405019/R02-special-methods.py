"""
R02-special-methods.py - OOP 魔術方法

進階觀念：
  Python 的特殊方法（dunder methods）讓自訂類別能無縫融入語言的內建操作。
  本例示範以下魔術方法的精確語義：

  __repr__  : 給「開發者」看，應能重建物件（eval(repr(obj)) == obj），
              出現在 REPL、日誌、容器的 repr() 中。
  __str__   : 給「使用者」看，出現在 print()、str()、f-string 中。
              若未定義，Python 回退到 __repr__。
  __eq__    : 定義 == 運算，預設比較 id（identity），覆寫後比較 value。
              注意：定義 __eq__ 後，預設的 __hash__ 會被設為 None，
              使物件不可 hash（無法作為 dict key / set 元素），
              若需要，必須明確定義 __hash__。
  __lt__    : 搭配 functools.total_ordering，只需定義 __eq__ 和 __lt__，
              其餘比較運算子（>, <=, >=）由裝飾器自動推導。
  __slots__ : 限制實例只能有預先宣告的屬性，
              避免意外新增屬性，並減少每個實例的記憶體開銷。

常見陷阱：
  1. 忘記在定義 __eq__ 後同步定義 __hash__，導致物件無法放入 set / dict。
  2. __repr__ 回傳的字串格式不能用 eval() 重建，違反慣例。
  3. 使用 total_ordering 時忘記同時實作 __eq__，會導致比較邏輯錯誤。
  4. __slots__ 在繼承時必須在每層子類別各自宣告，否則子類別仍會有 __dict__。

標準寫法：
  - 若物件可排序，同時定義 __hash__（通常用相同的排序欄位）。
  - 使用 @functools.total_ordering 減少重複程式碼。
  - __repr__ 格式建議：ClassName(field1=val, field2=val)
"""

from functools import total_ordering


# ─────────────────────────────────────────────
# 情境：CPE（Customer Premises Equipment）裝置記錄
# ─────────────────────────────────────────────

@total_ordering   # 自動補完 >, <=, >= 三個比較運算子
class CPEDevice:
    """
    代表一台 CPE 裝置（如家用路由器、ONT 等）的資料物件。

    __slots__ 說明：
      - 每個 Python 實例預設帶有 __dict__（一個 dict），用來儲存所有實例屬性。
        對於大量小物件，這個 dict 本身就佔用可觀記憶體（約 200-300 bytes/object）。
      - 宣告 __slots__ = (...) 後，Python 改用固定大小的陣列儲存屬性，
        省去 __dict__ 的開銷（實測通常可節省 40-60% 記憶體）。
      - 副作用：無法在執行時動態新增未宣告的屬性（TypeError），
        這在資料類別中反而是好事，可防止打字錯誤導致的靜默 bug。
      - 若子類別沒有宣告自己的 __slots__，子類別仍會有 __dict__，
        __slots__ 的節省效果就消失了。
    """
    __slots__ = ("mac_address", "hostname", "firmware_version", "signal_dbm")

    def __init__(
        self,
        mac_address: str,
        hostname: str,
        firmware_version: str,
        signal_dbm: float = 0.0,
    ):
        self.mac_address = mac_address.upper()
        self.hostname = hostname
        self.firmware_version = firmware_version
        self.signal_dbm = signal_dbm

    # ── __repr__：給開發者看，ideally eval-able ──
    def __repr__(self) -> str:
        """
        格式：CPEDevice(mac_address='...', hostname='...', ...)
        在 REPL、logging、容器的 repr 中出現，讓開發者一眼重建物件狀態。
        """
        return (
            f"CPEDevice("
            f"mac_address={self.mac_address!r}, "
            f"hostname={self.hostname!r}, "
            f"firmware_version={self.firmware_version!r}, "
            f"signal_dbm={self.signal_dbm!r})"
        )

    # ── __str__：給使用者看，著重可讀性 ──
    def __str__(self) -> str:
        """
        格式：[MAC] hostname  fw=...  signal=...dBm
        出現在 print()、str()、f-string 中，對終端使用者更友善。
        """
        signal_bar = "▓" * max(0, int((self.signal_dbm + 100) / 10))
        return (
            f"[{self.mac_address}] {self.hostname:<20s} "
            f"fw={self.firmware_version:<10s} "
            f"signal={self.signal_dbm:+.1f}dBm {signal_bar}"
        )

    # ── __eq__：比較實質內容（而非記憶體位址）──
    def __eq__(self, other: object) -> bool:
        """
        兩台裝置相等的條件：MAC address 相同（MAC 是唯一識別碼）。
        注意：定義 __eq__ 後必須同步定義 __hash__，否則物件不可 hash。
        """
        if not isinstance(other, CPEDevice):
            return NotImplemented   # 回傳 NotImplemented 讓 Python 嘗試反向運算
        return self.mac_address == other.mac_address

    # ── __hash__：與 __eq__ 保持一致 ──
    def __hash__(self) -> int:
        """
        若兩物件 __eq__ 為 True，其 __hash__ 必須相同。
        使用 mac_address 作為 hash 的依據。
        """
        return hash(self.mac_address)

    # ── __lt__：搭配 total_ordering，只需定義這一個 ──
    def __lt__(self, other: "CPEDevice") -> bool:
        """
        依信號強度排序（signal_dbm 越大表示信號越好）。
        @total_ordering 會用 __eq__ 和 __lt__ 推導 >, <=, >= 三個方法。
        """
        if not isinstance(other, CPEDevice):
            return NotImplemented
        return self.signal_dbm < other.signal_dbm


# ─────────────────────────────────────────────
# 驗證各魔術方法的行為
# ─────────────────────────────────────────────

dev1 = CPEDevice("aa:bb:cc:dd:ee:01", "cpe-living-room", "v3.2.1", signal_dbm=-55.0)
dev2 = CPEDevice("AA:BB:CC:DD:EE:01", "cpe-living-room", "v3.2.1", signal_dbm=-55.0)
dev3 = CPEDevice("aa:bb:cc:dd:ee:02", "cpe-bedroom",     "v3.1.0", signal_dbm=-72.5)
dev4 = CPEDevice("aa:bb:cc:dd:ee:03", "cpe-kitchen",     "v3.2.1", signal_dbm=-61.0)

print("=== __repr__ 與 __str__ ===")
print("repr(dev1) :", repr(dev1))
print("str(dev1)  :", str(dev1))
print("print(dev3):", dev3)          # print 自動呼叫 __str__

print("\n=== 容器中的表示（用 repr）===")
devices = [dev1, dev3, dev4]
print(devices)  # list 的 repr 對元素呼叫 __repr__

print("\n=== __eq__ 比較 ===")
print(f"dev1 == dev2 (同 MAC): {dev1 == dev2}")     # True（MAC 正規化為大寫後相同）
print(f"dev1 == dev3 (不同 MAC): {dev1 == dev3}")    # False
print(f"dev1 is dev2: {dev1 is dev2}")               # False（不同物件）

print("\n=== __hash__：放入 set / dict ===")
device_set = {dev1, dev2, dev3}
print(f"set 大小（dev1 和 dev2 視為同一台）: {len(device_set)}")  # 2

device_lookup = {dev1: "living_room_vlan", dev3: "bedroom_vlan"}
print(f"用 dev2 查 dict（與 dev1 同 MAC）: {device_lookup[dev2]}")  # living_room_vlan

print("\n=== __lt__ 與 total_ordering ===")
print(f"dev1.signal={dev1.signal_dbm} < dev3.signal={dev3.signal_dbm}: {dev1 < dev3}")  # False（-55 > -72.5）
print(f"dev3 < dev1: {dev3 < dev1}")     # True
print(f"dev1 > dev3: {dev1 > dev3}")     # True（由 total_ordering 推導）
print(f"dev1 >= dev2: {dev1 >= dev2}")   # True（相等時 >= 也為 True）

print("\n=== 依信號強度排序（最強在前）===")
for d in sorted(devices, reverse=True):
    print(f"  {d}")

print("\n=== __slots__ 保護 ===")
try:
    dev1.unknown_field = "oops"  # 嘗試新增未宣告的屬性
except AttributeError as e:
    print(f"[slots 保護] {e}")

# 驗證沒有 __dict__
print(f"dev1 有 __dict__: {hasattr(dev1, '__dict__')}")  # False
print(f"dev1 的 __slots__: {CPEDevice.__slots__}")
