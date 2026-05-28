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
    """示範如何在同一個 except 區塊處理多種例外。

    如果輸入無法轉為整數，可能會發生 ValueError（格式錯誤）或 TypeError（傳入 None 等不可轉型態），
    可以在 except 後方以 tuple 同時列出多個例外類別來一次處理。
    回傳 None 表示解析失敗（示範用途，不一定是最佳實務）。
    """
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # 印出例外類型與訊息，方便除錯或紀錄
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """示範如何安全地捕獲例外：使用 `except Exception` 而非裸 `except:`。

    裸 `except:` 會捕捉到包括 SystemExit、KeyboardInterrupt 等特殊基底例外，通常不想捕捉。
    這裡捕捉 Exception 並印出堆疊追蹤以協助除錯。
    """
    try:
        return func(*args)
    except Exception as e:
        # 顯示發生的例外類型與訊息
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        # 印出完整 traceback，有助於定位錯誤來源
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
    """網路相關錯誤的基底類別。

    自定義例外應繼承自 Exception（而非 BaseException），以便正常被 except Exception 捕捉。
    """


class HostnameError(NetworkError):
    """代表找不到主機的錯誤，繼承自 NetworkError。"""


class ConnectionTimeout(NetworkError):
    """連線逾時錯誤，會攜帶 host 與 seconds 屬性以供上層使用。"""
    def __init__(self, host, seconds):
        # 將具體訊息傳給 Exception 的建構子，方便直接列印或日誌紀錄
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """模擬簡單的連線檢查，會在特定錯誤情況拋出自定義例外。

    - 若 host 為空字串，拋出 HostnameError
    - 若 timeout 小於 1，拋出 ConnectionTimeout
    否則回傳連線成功的字串（模擬用途）。
    """
    if host == "":
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"


if __name__ == "__main__":
    print("--- 14.6 ---")
    # 範例：嘗試解析無效的輸入，觀察錯誤處理行為
    parse_value("abc")
    parse_value(None)

    print("\n--- 14.7 ---")
    # safe_run 會捕捉 Exception 並印出 traceback，而不會讓程式中斷
    safe_run(lambda: 1 / 0)

    print("\n--- 14.8 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            # connect 可能拋出定義好的 NetworkError 子類，這裡示範如何捕捉並處理
            print(connect(host, t))
        except NetworkError as e:
            print(f"接到 {type(e).__name__}: {e}")
