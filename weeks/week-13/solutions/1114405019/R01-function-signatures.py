"""
R01-function-signatures.py - 彈性函數簽名

進階觀念：
  Python 函數的引數分為五種類型（依位置順序）：
    1. 位置引數 (positional)
    2. *args：收集多餘的位置引數為 tuple
    3. 關鍵字限定引數 (keyword-only)：放在 * 或 *args 之後，必須以關鍵字呼叫
    4. **kwargs：收集多餘的關鍵字引數為 dict
    5. 僅位置引數 (positional-only)：放在 / 之前（Python 3.8+）

常見陷阱：
  1. 位置引數不能出現在 *args 之後（語法錯誤）。
  2. **kwargs 必須排在最後。
  3. 若忘記加 * 隔開，原本想設計為關鍵字限定的參數仍可用位置呼叫，
     可能導致呼叫端傳錯順序而難以察覺。

標準寫法：
  - 對「語義上不宜隨意換順序」的引數，使用關鍵字限定（*, param）強制呼叫端明確說明。
  - 公開 API 建議多用關鍵字限定，減少因引數順序改變導致的 breaking change。
"""


# ─────────────────────────────────────────────
# 完整引數類型示範
# ─────────────────────────────────────────────

def full_demo(pos1, pos2, /, normal, *args, kw_only1, kw_only2="default", **kwargs):
    """
    pos1, pos2   : 僅位置引數（/ 之前），不能用關鍵字傳入
    normal       : 一般引數，可位置或關鍵字傳入
    *args        : 收集多餘位置引數
    kw_only1     : 關鍵字限定，必須寫 kw_only1=值
    kw_only2     : 關鍵字限定且有預設值
    **kwargs     : 收集多餘關鍵字引數
    """
    print(f"  pos1={pos1}, pos2={pos2}")
    print(f"  normal={normal}")
    print(f"  args={args}")
    print(f"  kw_only1={kw_only1}, kw_only2={kw_only2}")
    print(f"  kwargs={kwargs}")

print("=== 完整引數類型示範 ===")
full_demo(1, 2, "norm", "extra1", "extra2", kw_only1="必填", extra_kw="額外")


# ─────────────────────────────────────────────
# 實際應用：結構化日誌紀錄器（Logger）
# ─────────────────────────────────────────────

import datetime
import json
import sys
from typing import Any

# 日誌等級定義
LOG_LEVELS = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40, "CRITICAL": 50}


def log(
    *messages: Any,             # 可傳入多個訊息片段（自動 join）
    level: str = "INFO",        # 關鍵字限定：強制呼叫端明確指定等級
    source: str = "app",        # 關鍵字限定：訊息來源模組
    timestamp: bool = True,     # 關鍵字限定：是否附加時間戳記
    output_format: str = "text",# 關鍵字限定：輸出格式 "text" 或 "json"
    **extra_fields: Any,        # 接收任意附加欄位（如 request_id, device_ip 等）
):
    """
    彈性日誌函數。

    設計說明：
      - *messages 允許像 print() 一樣傳入多個片段，方便拼接動態訊息。
      - level/source 等參數使用關鍵字限定，確保呼叫端不會因位置順序搞混
        而靜默地傳入錯誤值（例如把 source 填入 level 的位置）。
      - **extra_fields 允許附加任意業務欄位，不需修改函數簽名即可擴充。

    API 安全性說明：
      - 若 level 不在已知等級中，以 WARNING 取代並提示，避免靜默失敗。
    """
    # 正規化等級，避免靜默失敗
    level = level.upper()
    if level not in LOG_LEVELS:
        extra_fields["original_level"] = level
        level = "WARNING"
        messages = (f"[未知等級] ",) + messages

    message_str = " ".join(str(m) for m in messages)

    if output_format == "json":
        record = {
            "level": level,
            "source": source,
            "message": message_str,
            **extra_fields,
        }
        if timestamp:
            record["timestamp"] = datetime.datetime.now().isoformat()
        print(json.dumps(record, ensure_ascii=False))
    else:
        ts = f"[{datetime.datetime.now().strftime('%H:%M:%S')}] " if timestamp else ""
        extras = "  ".join(f"{k}={v}" for k, v in extra_fields.items())
        extras_str = f"  | {extras}" if extras else ""
        print(f"{ts}[{level}] [{source}] {message_str}{extras_str}")


print("\n=== 結構化日誌紀錄器示範 ===")

# 基本用法
log("系統啟動完成")
log("使用者登入", level="INFO", source="auth")

# 傳入多個片段（類似 print）
log("裝置", "192.168.1.1", "離線", level="WARNING", source="monitor")

# 附加任意業務欄位
log("連線失敗", level="ERROR", source="cpe-agent",
    device_mac="00:11:22:33:44:55", retry_count=3, port=7547)

# JSON 格式輸出（適合送往 ELK / Loki）
log("韌體更新成功", level="INFO", source="acs",
    output_format="json", device_id="CPE-001", firmware="v2.3.1")


# ─────────────────────────────────────────────
# 實際應用：資料庫連線設定產生器
# ─────────────────────────────────────────────

def build_db_config(
    host: str,
    database: str,
    *,                          # * 之後全為關鍵字限定引數
    port: int = 5432,
    user: str = "postgres",
    password: str = "",
    ssl_mode: str = "prefer",
    connect_timeout: int = 10,
    **driver_options: Any,      # 允許傳入特定資料庫驅動的額外選項
) -> dict:
    """
    建立資料庫連線設定字典。

    使用關鍵字限定的好處：
      - host 和 database 是必填且有固定語義，適合用位置傳入。
      - port / user / ssl_mode 等參數語義不同，若允許位置傳入，
        一旦未來新增參數或調整順序，舊程式碼會靜默傳錯值。
      - 強制關鍵字可讓函數簽名改版時更安全（只要關鍵字名稱不變）。
    """
    config = {
        "host": host,
        "port": port,
        "database": database,
        "user": user,
        "password": password,
        "sslmode": ssl_mode,
        "connect_timeout": connect_timeout,
        **driver_options,
    }
    return config


print("\n=== 資料庫連線設定示範 ===")

# 正確用法：關鍵字引數讓意圖清晰
prod_db = build_db_config(
    "db.prod.example.com",
    "cpe_inventory",
    port=5432,
    user="cpe_svc",
    password="s3cr3t",
    ssl_mode="require",
    application_name="acs-server",  # 傳入 psycopg2 驅動選項
)
print("Production DB config:", json.dumps(prod_db, indent=2))

# 錯誤示範（被關鍵字限定保護）：
try:
    # 嘗試以位置引數傳入 port（會引發 TypeError，因為 port 是關鍵字限定）
    bad_config = build_db_config("localhost", "test_db", 3306)
except TypeError as e:
    print(f"\n[保護機制] 位置引數嘗試被攔截: {e}")
