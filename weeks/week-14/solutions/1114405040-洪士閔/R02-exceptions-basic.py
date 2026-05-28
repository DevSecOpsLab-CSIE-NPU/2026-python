"""
R02 - 例外處理基礎練習

本檔案示範：
1. except 可以一次捕捉多種例外
2. 如何捕捉一般 Exception 並印出 traceback
3. 如何建立自訂例外類別

執行方式：
    python R02-exceptions-basic.py
"""
import traceback


# ---------- 14.6 一次捕捉多種例外 ----------
def parse_value(s):
    """嘗試把輸入轉成整數；失敗時回傳 None。"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # ValueError：例如 int("abc")
        # TypeError：例如 int(None)
        print(f"[14.6] 轉換失敗 {type(e).__name__}: {e}")
        return None


# ---------- 14.7 捕捉一般例外 ----------
def safe_run(func, *args):
    """安全執行函式；若發生一般例外，印出錯誤資訊與 traceback。"""
    try:
        return func(*args)
    except Exception as e:
        # except Exception 通常比單純 except: 好，因為不會攔截 KeyboardInterrupt 等系統層級例外。
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        traceback.print_exc()


# ---------- 14.8 自訂例外類別 ----------
class NetworkError(Exception):
    """網路相關錯誤的父類別；自訂例外通常繼承 Exception。"""


class HostnameError(NetworkError):
    """主機名稱錯誤，例如空字串或格式不正確。"""


class ConnectionTimeout(NetworkError):
    """連線逾時錯誤，額外保存 host 和 seconds 兩個資訊。"""

    def __init__(self, host, seconds):
        super().__init__(f"連線到 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """模擬連線流程，依照輸入狀況拋出不同的自訂例外。"""
    if host == "":
        raise HostnameError("主機名稱不可為空")
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
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:
            # 因為 HostnameError 和 ConnectionTimeout 都繼承 NetworkError，所以可以一起處理。
            print(f"捕捉到 {type(e).__name__}: {e}")
