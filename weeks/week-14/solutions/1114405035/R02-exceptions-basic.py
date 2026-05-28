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


# ---------- 14.6 多個例外 (Handling Multiple Exceptions) ----------
def parse_value(s):
    """
    示範如何在同一個 except 區塊中，使用 tuple 列出多種例外類別。
    這在多種錯誤的處理邏輯相同時非常有用。
    """
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # 當 s 不是字串/數字 (TypeError) 或內容無法轉為整數 (ValueError) 時觸發
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


# ---------- 14.7 捕獲所有例外 (Catching All Exceptions) ----------
def safe_run(func, *args):
    """
    示範如何安全地捕獲所有「程式錯誤」產生的例外。
    注意：應使用 `except Exception` 而非「裸 except:」。
    「裸 except:」會捕獲 SystemExit 和 KeyboardInterrupt (Ctrl+C)，這通常不是我們想要的。
    """
    try:
        return func(*args)
    except Exception as e:
        # 捕獲所有繼承自 Exception 的例外
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        # 印出詳細的堆疊追蹤 (Stack Trace)，方便除錯
        traceback.print_exc()


# ---------- 14.8 自定義例外 (Custom Exceptions) ----------
class NetworkError(Exception):
    """
    自定義例外類別的基底類別。
    建議繼承 Exception 而不是更底層的 BaseException。
    """


class HostnameError(NetworkError):
    """當主機名稱解析錯誤時拋出，繼承自 NetworkError"""


class ConnectionTimeout(NetworkError):
    """
    當連線逾時時拋出。
    可以自定義 __init__ 來儲存額外的錯誤資訊（如 host 和 seconds）。
    """
    def __init__(self, host, seconds):
        # 呼叫父類別的初始化，設定錯誤訊息
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """模擬連線過程並拋出特定的自定義例外"""
    if host == "":
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"


if __name__ == "__main__":
    print("--- 14.6 多個例外測試 ---")
    parse_value("abc")   # 觸發 ValueError
    parse_value(None)    # 觸發 TypeError

    print("\n--- 14.7 捕獲所有例外測試 (除以零) ---")
    safe_run(lambda: 1 / 0)

    print("\n--- 14.8 自定義例外測試 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(f"嘗試連線到 {host if host else '(空)'}...")
            print(connect(host, t))
        except NetworkError as e:
            # 捕獲所有類型的網路錯誤（包含子類別）
            print(f"接到 {type(e).__name__}: {e}")
