"""
R02：例外處理基本用法（加強繁中註解版）

本檔聚焦三個例外處理重點：
1. 同一個 except 同時處理多種例外
2. 安全執行包裝（safe_run）
3. 自訂例外階層（方便上層依類型處理）

執行方式：
    python R02-exceptions-basic.py
"""

import traceback


# ============================================================
# 14.6 多個例外：except (A, B)
# ============================================================
def parse_value(s):
    """
    將輸入嘗試轉成 int。

    可能出錯情境：
    - ValueError：例如 "abc"
    - TypeError：例如 None

    這裡使用同一個 except 處理多種例外，
    讓錯誤處理集中、程式更簡潔。
    """
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


# ============================================================
# 14.7 捕獲所有「一般」例外：except Exception
# ============================================================
def safe_run(func, *args):
    """
    安全執行任意函式。

    寫法重點：
    - 用 except Exception，而不是裸 except:
      這樣不會吃掉 KeyboardInterrupt / SystemExit 等系統訊號。
    - traceback.print_exc() 可印出完整堆疊，便於除錯。
    """
    try:
        return func(*args)
    except Exception as e:
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        traceback.print_exc()


# ============================================================
# 14.8 自定義例外
# ============================================================
class NetworkError(Exception):
    """
    網路錯誤的基底類別。

    為什麼要有基底類別：
    - 上層只要 except NetworkError，就能一次處理所有網路相關錯誤。
    """


class HostnameError(NetworkError):
    """主機名稱無效（例如空字串）。"""


class ConnectionTimeout(NetworkError):
    """
    連線逾時錯誤。

    額外保留 host / seconds 屬性，
    讓呼叫端可讀取結構化資訊做後續處理。
    """

    def __init__(self, host, seconds):
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """
    模擬連線邏輯。

    規則：
    - host 為空字串 -> HostnameError
    - timeout < 1 -> ConnectionTimeout
    - 其餘視為成功
    """
    if host == "":
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"


if __name__ == "__main__":
    print("--- 14.6 ---")
    parse_value("abc")
    parse_value(None)

    print("\n--- 14.7 ---")
    safe_run(lambda: 1 / 0)

    print("\n--- 14.8 ---")
    # 透過多組測資示範「成功」與「不同失敗型別」的處理。
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:
            print(f"接到 {type(e).__name__}: {e}")