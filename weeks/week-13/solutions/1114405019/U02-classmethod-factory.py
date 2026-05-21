"""
U02-classmethod-factory.py - Classmethod 工廠方法

進階觀念：
  @classmethod 裝飾器讓方法的第一個參數接收「類別本身」（習慣命名為 cls）
  而非實例（self）。這使得 classmethod 可以作為「替代建構子（Alternative Constructor）」，
  從各種資料來源初始化物件，同時正確支援繼承。

  為何用 cls 而非硬編碼類別名稱？
    若工廠方法寫 return MyClass(...)，子類別繼承後呼叫工廠方法，
    建立的仍是父類別 MyClass 的實例，而非子類別的實例。
    改用 return cls(...)，子類別繼承後呼叫，cls 就是子類別，
    確保多型（polymorphism）正確運作。

  相關方法比較：
    instance method  : 第一個參數 self → 操作實例狀態
    @classmethod     : 第一個參數 cls  → 操作類別狀態，或作為替代建構子
    @staticmethod    : 無隱含第一個參數 → 邏輯上屬於類別但不依賴類別或實例狀態

常見陷阱：
  1. 在 classmethod 中硬編碼父類別名稱，導致繼承後建立錯誤型別。
  2. 工廠方法中解析資料後忘記驗證，直接傳入可能導致 __init__ 拋出難以追蹤的錯誤。
  3. 混淆 @classmethod 與 @staticmethod 的使用時機。

標準寫法：
  - 工廠方法命名慣例：from_<source>（如 from_json, from_dict, from_csv_row）。
  - 永遠使用 cls(...)，不要用 ClassName(...)。
  - 在工廠方法中加入資料解析錯誤的明確提示（用 raise ... from err）。
"""

import json
from datetime import datetime, timezone
from typing import Optional


# ─────────────────────────────────────────────
# CPE（Customer Premises Equipment）裝置記錄
# ─────────────────────────────────────────────

class CPERecord:
    """
    代表一筆 CPE 裝置的管理記錄，包含設備識別資訊與最後上線時間。

    設計背景：
      ACS（Auto Configuration Server，如 TR-069）在管理 CPE 時，
      裝置資訊可能來自不同來源：
        - 資料庫查詢結果（tuple）
        - REST API 回應（JSON 字串）
        - CSV 匯出檔（字串列表）
        - 另一個 CPERecord 物件（複製）
      每種來源都可用工廠方法提供友善的初始化介面。
    """

    def __init__(
        self,
        mac_address: str,
        hostname: str,
        firmware_version: str,
        last_seen: Optional[datetime] = None,
        is_online: bool = False,
    ):
        self.mac_address = mac_address.upper().strip()
        self.hostname = hostname.strip()
        self.firmware_version = firmware_version.strip()
        self.last_seen = last_seen or datetime.now(timezone.utc)
        self.is_online = is_online

    # ── 工廠方法 1：從 JSON 字串初始化 ──
    @classmethod
    def from_json(cls, json_str: str) -> "CPERecord":
        """
        從 ACS 的 REST API 回應（JSON 字串）建立 CPERecord。

        使用 cls(...)：
          若子類別（如 ManagedCPERecord）繼承並呼叫 from_json，
          cls 就是 ManagedCPERecord，建立的是子類別實例而非父類別。

        錯誤處理：
          使用 raise ValueError(...) from err 保留原始錯誤堆疊，
          方便追蹤是 JSON 格式問題還是欄位缺失問題。
        """
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as err:
            raise ValueError(f"from_json: 無效的 JSON 字串: {json_str!r}") from err

        # 解析 last_seen（ISO 8601 格式）
        last_seen = None
        if raw_ts := data.get("last_seen"):
            try:
                last_seen = datetime.fromisoformat(raw_ts)
            except ValueError as err:
                raise ValueError(f"from_json: last_seen 格式錯誤: {raw_ts!r}") from err

        try:
            return cls(
                mac_address=data["mac_address"],
                hostname=data["hostname"],
                firmware_version=data["firmware_version"],
                last_seen=last_seen,
                is_online=data.get("is_online", False),
            )
        except KeyError as err:
            raise ValueError(f"from_json: JSON 缺少必要欄位 {err}") from err

    # ── 工廠方法 2：從 Tuple 初始化（例如資料庫查詢結果）──
    @classmethod
    def from_tuple(cls, record: tuple) -> "CPERecord":
        """
        從資料庫查詢結果（tuple）建立 CPERecord。

        欄位順序約定：(mac_address, hostname, firmware_version, last_seen_iso, is_online)
        使用 cls 確保子類別繼承時能建立正確的型別。
        """
        if len(record) < 3:
            raise ValueError(
                f"from_tuple: 至少需要 3 個欄位（mac, hostname, firmware），"
                f"收到 {len(record)} 個: {record!r}"
            )

        mac, hostname, fw = record[0], record[1], record[2]
        last_seen_str = record[3] if len(record) > 3 else None
        is_online = bool(record[4]) if len(record) > 4 else False

        last_seen = None
        if last_seen_str:
            try:
                last_seen = datetime.fromisoformat(last_seen_str)
            except (ValueError, TypeError) as err:
                raise ValueError(f"from_tuple: last_seen 格式錯誤: {last_seen_str!r}") from err

        return cls(mac, hostname, fw, last_seen, is_online)

    # ── 工廠方法 3：從 CSV 行字串初始化 ──
    @classmethod
    def from_csv_row(cls, csv_line: str, delimiter: str = ",") -> "CPERecord":
        """
        從 CSV 匯出的一行文字建立 CPERecord。
        示範工廠方法也可以接受額外的設定參數（delimiter）。
        """
        parts = [p.strip() for p in csv_line.split(delimiter)]
        return cls.from_tuple(tuple(parts))

    # ── 工廠方法 4：建立「離線佔位」記錄 ──
    @classmethod
    def create_placeholder(cls, mac_address: str) -> "CPERecord":
        """
        當裝置 MAC 已知但詳細資訊尚未取得時，建立一個佔位記錄。
        語義比 CPERecord("aa:bb:...", "unknown", "unknown") 更清晰。
        """
        return cls(
            mac_address=mac_address,
            hostname="(未知主機名稱)",
            firmware_version="(未知版本)",
            is_online=False,
        )

    def __repr__(self) -> str:
        ts = self.last_seen.strftime("%Y-%m-%d %H:%M") if self.last_seen else "N/A"
        status = "●" if self.is_online else "○"
        return (
            f"{self.__class__.__name__}("
            f"mac={self.mac_address}, "
            f"host={self.hostname!r}, "
            f"fw={self.firmware_version!r}, "
            f"last_seen={ts}, "
            f"online={status})"
        )


# ─────────────────────────────────────────────
# 子類別：受管 CPE（帶有 ACS 連線設定）
# ─────────────────────────────────────────────

class ManagedCPERecord(CPERecord):
    """
    繼承 CPERecord，額外記錄 ACS 管理資訊。

    驗證工廠方法繼承行為：
      from_json / from_tuple 都使用 cls(...)，
      所以 ManagedCPERecord.from_json(...) 建立的是 ManagedCPERecord 實例，
      而非 CPERecord 實例——即使工廠方法定義在父類別中。
    """

    def __init__(self, *args, acs_url: str = "", connection_key: str = "", **kwargs):
        super().__init__(*args, **kwargs)
        self.acs_url = acs_url
        self.connection_key = connection_key

    @classmethod
    def from_json(cls, json_str: str) -> "ManagedCPERecord":
        """
        覆寫 from_json，先呼叫父類邏輯，再設定子類欄位。
        """
        # 先取出子類專屬欄位（避免 __init__ 出現意外關鍵字引數）
        data = json.loads(json_str)
        acs_url = data.pop("acs_url", "")
        connection_key = data.pop("connection_key", "")

        # 把剩餘欄位重新序列化，呼叫父類的 from_json
        base = super().from_json(json.dumps(data))

        # 補充子類欄位
        base.acs_url = acs_url
        base.connection_key = connection_key
        return base  # cls 已由 super().from_json 決定（因為 super() 使用 cls）

    def __repr__(self) -> str:
        base = super().__repr__()
        return f"{base[:-1]}, acs={self.acs_url!r})"


# ─────────────────────────────────────────────
# 示範各工廠方法
# ─────────────────────────────────────────────

print("=== from_json 工廠方法 ===")
json_str = json.dumps({
    "mac_address": "aa:bb:cc:dd:ee:01",
    "hostname": "cpe-living-room",
    "firmware_version": "v3.2.1",
    "last_seen": "2026-05-21T10:30:00",
    "is_online": True,
})
cpe1 = CPERecord.from_json(json_str)
print(cpe1)

print("\n=== from_tuple 工廠方法（模擬資料庫查詢）===")
db_row = ("bb:cc:dd:ee:ff:02", "cpe-bedroom", "v3.1.0", "2026-05-21T08:15:00", 0)
cpe2 = CPERecord.from_tuple(db_row)
print(cpe2)

print("\n=== from_csv_row 工廠方法 ===")
csv_line = "CC:DD:EE:FF:00:03, cpe-kitchen, v3.2.1, 2026-05-20T22:00:00, 1"
cpe3 = CPERecord.from_csv_row(csv_line)
print(cpe3)

print("\n=== create_placeholder 工廠方法 ===")
placeholder = CPERecord.create_placeholder("DD:EE:FF:00:11:04")
print(placeholder)

print("\n=== 子類別繼承工廠方法（cls 的重要性）===")
managed_json = json.dumps({
    "mac_address": "EE:FF:00:11:22:05",
    "hostname": "managed-cpe-01",
    "firmware_version": "v4.0.0",
    "is_online": True,
    "acs_url": "http://acs.example.com:7547",
    "connection_key": "secret-key-abc",
})
managed_cpe = ManagedCPERecord.from_json(managed_json)
print(f"型別: {type(managed_cpe).__name__}")   # ManagedCPERecord（非 CPERecord）
print(managed_cpe)

# 驗證 from_tuple 也能正確建立子類別實例
managed_via_tuple = ManagedCPERecord.from_tuple(
    ("FF:00:11:22:33:06", "managed-cpe-02", "v4.0.0")
)
print(f"\nfrom_tuple 型別: {type(managed_via_tuple).__name__}")  # ManagedCPERecord

print("\n=== 錯誤處理示範 ===")
for bad_input, method_name in [
    ("{not valid json}", "from_json"),
    ('{"hostname": "missing-mac"}', "from_json"),
]:
    try:
        CPERecord.from_json(bad_input)
    except ValueError as e:
        print(f"[{method_name}] {e}")
