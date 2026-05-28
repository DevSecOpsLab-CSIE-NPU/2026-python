"""
R02：例外處理基本用法（記憶層）

對應 Cookbook：
- 14.6 處理多個例外
- 14.7 捕獲所有例外
- 14.8 建立自定義例外

執行：
    python R02-exceptions-basic.py
"""
import traceback


# ---------- 14.6 多個例外 ----------
def parse_value(s):
        """嘗試將輸入轉成整數，示範在同一個 except 中以 tuple 列出多種可捕獲的例外類別。

        說明：
            - 當輸入為無效的數字字串時，`int(s)` 會丟出 ValueError。
            - 當輸入為 None 等非字串/數字類型時，`int(s)` 可能丟出 TypeError。
            - 此函式用 `except (ValueError, TypeError) as e` 一次捕捉兩種例外，並回傳 None 表示解析失敗。

        參數：
            s: 欲解析的值（通常為字串）

        回傳：
            int 或 None（解析失敗時為 None）
        """
        try:
                return int(s)
        except (ValueError, TypeError) as e:
                # 在真實應用中，這裡通常會記錄 log 或採取其他錯誤處理策略
                print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
                return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
        """執行傳入的 callable，捕獲 Exception 類的例外並印出追蹤資訊。

        說明：
            - 建議使用 `except Exception` 而不是裸 `except:`，以避免捕捉到像 KeyboardInterrupt 或 SystemExit 這類不應被吞掉的特殊例外。
            - 捕捉到例外後，會印出簡短訊息並用 `traceback.print_exc()` 列印完整堆疊追蹤，方便除錯。

        參數：
            func: 可呼叫物件（callable），例如 function 或 lambda
            *args: 傳遞給 func 的位置參數

        回傳：
            回傳 func 的執行結果（若無例外），否則回傳 None 並印出例外資訊
        """
        try:
                return func(*args)
        except Exception as e:
                # 顯示簡短的錯誤類型與訊息
                print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
                # 印出完整的例外堆疊，利於偵錯
                traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
        """網路相關錯誤的基底例外類別。

        說明：
            - 繼承自 `Exception`，代表這類錯誤可被一般的 except Exception 捕捉。
            - 未包含額外屬性，作為其他網路例外的共用父類別。
        """


class HostnameError(NetworkError):
    """表示主機名稱無效或找不到對應主機的例外。"""


class ConnectionTimeout(NetworkError):
    """連線逾時例外，會帶有 `host` 與 `seconds` 屬性以供上層使用者或處理器判斷。

    例如上層可依據 `e.seconds` 做重試或回退策略。
    """
    def __init__(self, host, seconds):
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """模擬連線行為，根據輸入參數決定是否拋出自定義例外。

    規則：
      - 若 host 為空字串，拋出 `HostnameError`。
      - 若 timeout 小於 1，拋出 `ConnectionTimeout` 並攜帶 host 與 seconds 資訊。
      - 正常情況下回傳成功連線的字串。
    """
    if host == "":
        # 主機名稱不合法，明確拋出定義好的例外供上層處理
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        # 逾時情境，攜帶相關資訊
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"


if __name__ == "__main__":
    # 範例示範：14.6 多種例外捕捉
    print("--- 14.6 ---")
    # 會印出解析失敗的訊息並回傳 None
    parse_value("abc")
    parse_value(None)

    # 範例示範：14.7 捕獲 Exception 並印出追蹤資訊
    print("\n--- 14.7 ---")
    # safe_run 會捕捉除零錯誤並列印 traceback
    safe_run(lambda: 1 / 0)

    # 範例示範：14.8 自定義例外與處理方式
    print("\n--- 14.8 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            # 嘗試連線，成功時印出結果
            print(connect(host, t))
        except NetworkError as e:
            # 捕捉 NetworkError（包含 HostnameError、ConnectionTimeout）並印出簡短說明
            print(f"接到 {type(e).__name__}: {e}")
