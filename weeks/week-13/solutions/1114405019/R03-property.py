"""
R03-property.py - Property 與 Setter 資料驗證

進階觀念：
  @property 讓我們用「屬性存取語法」（obj.attr）隱藏背後的計算或驗證邏輯，
  同時保持介面的一致性（不需要改為 get_attr() 這種方法呼叫形式）。

  三個相關裝飾器：
    @property           → getter（唯讀或讀寫的第一步）
    @<name>.setter      → setter（帶驗證的寫入）
    @<name>.deleter     → deleter（控制刪除行為）

常見陷阱：
  1. 子類別覆寫 setter 時，必須重新宣告完整的 @property，
     否則只宣告 @setter 會導致 AttributeError 或覆寫失敗（最常見的坑！）。
  2. 在 setter 中呼叫 self._value = ... 時若名稱與 property 同名（無底線前綴），
     會觸發無限遞迴（setter 呼叫自身）。正確做法是用底線命名私有變數。
  3. @property 若沒有 setter，賦值時會拋出 AttributeError，
     這正是「唯讀屬性」的實作方式。

標準寫法：
  - 私有實例變數以 _name 命名，公開屬性以 property 暴露。
  - Setter 的驗證邏輯應拋出有意義的例外（TypeError / ValueError），而非靜默轉換。
  - 子類別覆寫時，用 super() 呼叫父類別的 setter 保留原有邏輯，再加上額外約束。
"""


# ─────────────────────────────────────────────
# 基礎類別：網路埠設定（Port Configuration）
# ─────────────────────────────────────────────

class PortConfig:
    """
    代表一個網路服務的埠設定，包含埠號與描述。

    唯讀屬性：protocol（建構後不可更改）
    可寫屬性：port_number（含驗證）、description
    計算屬性：service_endpoint（唯讀，動態計算）
    """

    # 合法的 TCP/UDP 埠範圍
    MIN_PORT = 1
    MAX_PORT = 65535

    def __init__(self, protocol: str, port_number: int, description: str = ""):
        self._protocol = protocol.upper()  # 唯讀，儲存後不允許修改
        self.port_number = port_number     # 透過 setter 驗證
        self.description = description     # 透過 setter 驗證

    # ── 唯讀屬性：只有 getter，沒有 setter ──
    @property
    def protocol(self) -> str:
        """通訊協定（建構後不可修改，唯讀）。"""
        return self._protocol

    # ── 帶驗證的 setter：port_number ──
    @property
    def port_number(self) -> int:
        """埠號（1 ~ 65535 的整數）。"""
        return self._port_number

    @port_number.setter
    def port_number(self, value: int) -> None:
        """
        驗證規則：
          1. 必須是整數（拒絕浮點數、字串等）。
          2. 必須在 1 ~ 65535 範圍內。
        注意：使用 self._port_number 儲存，避免觸發 setter 遞迴。
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"port_number 必須是整數，收到 {type(value).__name__}")
        if not (self.MIN_PORT <= value <= self.MAX_PORT):
            raise ValueError(
                f"port_number 必須介於 {self.MIN_PORT} ~ {self.MAX_PORT}，收到 {value}"
            )
        self._port_number = value

    # ── 帶驗證的 setter：description ──
    @property
    def description(self) -> str:
        """服務描述（純字串，長度不超過 128 字元）。"""
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f"description 必須是字串，收到 {type(value).__name__}")
        if len(value) > 128:
            raise ValueError(f"description 長度不得超過 128 字元（收到 {len(value)} 字元）")
        self._description = value

    # ── 計算屬性：唯讀，動態計算 ──
    @property
    def service_endpoint(self) -> str:
        """回傳服務端點字串，例如 'tcp/443'。"""
        return f"{self._protocol.lower()}/{self._port_number}"

    def __repr__(self) -> str:
        return (
            f"PortConfig(protocol={self._protocol!r}, "
            f"port_number={self._port_number}, "
            f"description={self._description!r})"
        )

    def __str__(self) -> str:
        desc = f"  # {self._description}" if self._description else ""
        return f"{self.service_endpoint}{desc}"


print("=== PortConfig 示範 ===")

http  = PortConfig("TCP", 80,  "HTTP 明文")
https = PortConfig("TCP", 443, "HTTPS 加密")
ssh   = PortConfig("TCP", 22)

print(repr(http))
print(str(https))
print(f"SSH endpoint: {ssh.service_endpoint}")

# 修改 description（透過 setter 驗證）
ssh.description = "Secure Shell 管理埠"
print(f"SSH: {ssh}")

# 嘗試設定唯讀屬性
try:
    http.protocol = "UDP"
except AttributeError as e:
    print(f"[唯讀保護] {e}")

# 驗證失敗範例
for bad_port, label in [(0, "埠號=0"), (65536, "埠號=65536"), ("80", "字串'80'"), (3.14, "浮點數")]:
    try:
        PortConfig("TCP", bad_port)
    except (TypeError, ValueError) as e:
        print(f"[驗證拒絕] {label}: {e}")


# ─────────────────────────────────────────────
# 子類別：特權埠設定（Privileged Port Config）
# ─────────────────────────────────────────────

class PrivilegedPortConfig(PortConfig):
    """
    特權埠設定：僅允許 1 ~ 1023 的系統埠（well-known ports）。

    覆寫 port_number setter 的正確方式：
      1. 先定義新的 @property（必須重新宣告，即使 getter 邏輯相同）。
      2. 在新的 @setter 中呼叫 super() 的 setter 以保留父類驗證，
         再疊加子類的額外限制。

    注意這個常見的坑：
      若只寫 @PortConfig.port_number.setter 而不重新宣告 @property，
      Python 會找不到對應的 getter，拋出 AttributeError 或行為異常。
    """

    MAX_PRIVILEGED_PORT = 1023

    # 必須重新宣告完整的 @property（getter 邏輯與父類相同，但需重新綁定）
    @property
    def port_number(self) -> int:
        """特權埠號（1 ~ 1023）。"""
        return self._port_number   # 直接讀取私有變數（與父類 getter 邏輯相同）

    @port_number.setter
    def port_number(self, value: int) -> None:
        """
        先呼叫父類 setter 進行基本驗證（型別、1~65535 範圍），
        再加上子類的額外限制（必須 <= 1023）。
        這樣不會破壞父類邏輯，也能擴充限制。
        """
        # 透過父類的 setter property 物件呼叫其 fset 方法
        PortConfig.port_number.fset(self, value)   # 呼叫父類 setter
        # 疊加子類額外限制
        if value > self.MAX_PRIVILEGED_PORT:
            raise ValueError(
                f"PrivilegedPortConfig 只允許 1~{self.MAX_PRIVILEGED_PORT}，收到 {value}"
            )


print("\n=== PrivilegedPortConfig（子類覆寫 setter）===")

well_known = PrivilegedPortConfig("TCP", 443, "HTTPS（特權埠）")
print(repr(well_known))

# 父類驗證仍有效
try:
    PrivilegedPortConfig("TCP", 0)
except ValueError as e:
    print(f"[父類驗證] {e}")

# 子類額外限制
try:
    PrivilegedPortConfig("TCP", 8080)
except ValueError as e:
    print(f"[子類限制] {e}")

# 可以正常修改到合法的特權埠
well_known.port_number = 80
print(f"改埠後: {well_known}")


# ─────────────────────────────────────────────
# 進階：使用 __set_name__ 的通用驗證描述器
# （展示 property 背後的 Descriptor Protocol）
# ─────────────────────────────────────────────

class ValidatedInt:
    """
    通用整數範圍驗證描述器（Descriptor），作為 property 的更可重用替代。
    展示 property 本質上是描述器的語法糖。
    """

    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val
        self.attr_name = None

    def __set_name__(self, owner, name: str) -> None:
        self.attr_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.attr_name, None)

    def __set__(self, obj, value: int) -> None:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{self.attr_name} 必須是整數")
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(f"{self.attr_name} 必須介於 {self.min_val}~{self.max_val}")
        setattr(obj, self.attr_name, value)


class VLANConfig:
    """使用描述器的 VLAN 設定類別。"""
    vlan_id   = ValidatedInt(1, 4094)
    priority  = ValidatedInt(0, 7)

    def __init__(self, vlan_id: int, name: str, priority: int = 0):
        self.vlan_id  = vlan_id
        self.name     = name
        self.priority = priority

    def __repr__(self) -> str:
        return f"VLANConfig(vlan_id={self.vlan_id}, name={self.name!r}, priority={self.priority})"


print("\n=== 描述器示範（ValidatedInt）===")
mgmt_vlan = VLANConfig(100, "MGMT", priority=6)
print(repr(mgmt_vlan))

try:
    VLANConfig(5000, "INVALID")
except ValueError as e:
    print(f"[描述器驗證] {e}")
