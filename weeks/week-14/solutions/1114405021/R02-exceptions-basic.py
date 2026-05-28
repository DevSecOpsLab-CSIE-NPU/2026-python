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
    """
    同一個 except 用 tuple 列出多種例外類別。

    範例說明：當傳入的 `s` 無法轉為整數時，可能拋出 `ValueError`（字串格式不正確），
    或者傳入 None 等非字串/非數值類型會導致 `TypeError`。

    我們使用 `except (ValueError, TypeError) as e` 將兩種例外合併處理，
    在例外發生時印出錯誤類別與訊息，並回傳 `None` 表示解析失敗。
    """
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # 範例：輸入 'abc' -> ValueError；輸入 None -> TypeError
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """
    安全執行傳入的 callable：捕捉 `Exception` 及其子類別的例外。

    為什麼不用裸 `except:`？因為裸 except 會捕捉到 `BaseException` 的所有子類別，
    包括 `KeyboardInterrupt` 或 `SystemExit` 等特殊例外，會阻礙程式正常中斷。

    此函式在發生例外時會印出例外類別與訊息，並印出完整的 traceback 方便除錯。
    """
    try:
        return func(*args)
    except Exception as e:
        # 印出簡短錯誤資訊，並顯示堆疊追蹤供開發時檢查
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
    """
    所有網路錯誤的基底類別。

    設計說明：自定義例外應繼承自 `Exception`（而非 `BaseException`），
    以便能被常見的 `except Exception:` 捕捉，同時保留系統層級例外的行為。
    """


class HostnameError(NetworkError):
    """找不到主機（例如傳入空字串或無效主機名稱）"""


class ConnectionTimeout(NetworkError):
    """
    連線逾時例外；此例外會攜帶 `host` 與 `seconds` 屬性，方便呼叫端依據來源做特定處理。
    """
    def __init__(self, host, seconds):
        # 將描述性的訊息傳給 Exception 的建構子，方便直接列印或記錄
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        # 儲存額外屬性供上層程式使用或判斷
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    # 範例：簡單模擬連線檢查並視情況拋出自定義例外
    if host == "":
        # 無效主機名稱 -> 拋出 HostnameError
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        # 設定的 timeout 太小 -> 拋出 ConnectionTimeout，攜帶 host 與 timeout
        raise ConnectionTimeout(host, timeout)
    # 若一切正常，回傳連線成功的字串（此處為模擬）
    return f"connected to {host}"


if __name__ == "__main__":
    print("--- 14.6 ---")
    parse_value("abc")
    parse_value(None)

    print("\n--- 14.7 ---")
    safe_run(lambda: 1 / 0)

    print("\n--- 14.8 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            # 嘗試連線並印出結果；對於自定義的 NetworkError 進行處理
            print(connect(host, t))
        except NetworkError as e:
            # 這裡會捕捉 HostnameError、ConnectionTimeout 等 NetworkError 子類別
            # 可以根據例外型別或屬性做不同處理，例如記錄、重試或回報使用者
            print(f"接到 {type(e).__name__}: {e}")
