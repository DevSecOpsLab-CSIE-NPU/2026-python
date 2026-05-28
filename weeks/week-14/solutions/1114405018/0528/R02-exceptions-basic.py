"""
R02：例外處理基本用法（記憶層）

本檔案示範三件在實務上很常見的事情：
1) 同一段程式可能拋出不同型別錯誤，如何一次處理
2) 如何用「安全執行器」包住任意函式，避免程式整體中斷
3) 如何建立自定義例外階層，讓上層可以用「類別」做分類處理

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
    """同一個 except 用 tuple 列出多種例外類別。"""
    # int(s) 常見失敗情境：
    # - s 為無法轉整數的字串 -> ValueError
    # - s 型別不支援轉整數（例如 None）-> TypeError
    # 這裡用一個 except 同時接住兩種錯誤，避免重複程式碼。
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # type(e).__name__ 可印出實際錯誤類別名稱，方便除錯與教學。
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        # 解析失敗時回傳 None，讓呼叫端可用 if result is None 判斷。
        return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """except Exception，而不是裸 except:（裸 except 會抓到 KeyboardInterrupt）。"""
    # 這個工具函式可包住任何「可能失敗」的操作。
    # 優點：把錯誤集中記錄，不讓主流程因單一任務失敗而停止。
    try:
        return func(*args)
    except Exception as e:
        # 捕捉一般程式錯誤（大多數業務錯誤都屬於 Exception 子類）。
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        # 印出完整 traceback（含呼叫堆疊），比只印錯誤訊息更容易定位問題。
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
    """所有網路錯誤的基底類別；繼承 Exception 而不是 BaseException。"""
    # 建立領域基底例外（domain base exception）的目的：
    # 上層只要 except NetworkError，就能一次處理所有網路相關錯誤。


class HostnameError(NetworkError):
    """找不到主機"""


class ConnectionTimeout(NetworkError):
    """連線逾時，附帶 host / seconds 屬性，方便上層判斷"""
    def __init__(self, host, seconds):
        # super().__init__ 設定可讀的錯誤訊息，方便直接印出。
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        # 額外保留結構化欄位，讓呼叫端可依 host 或 timeout 值做後續決策。
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    # 示範：用明確的例外類別表達不同錯誤語意。
    # 這比回傳 False 或錯誤碼更清楚，也更利於上層分類處理。
    if host == "":
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"


if __name__ == "__main__":
    # 1) 多例外同時處理：可觀察 ValueError 與 TypeError 都進入同一分支。
    print("--- 14.6 ---")
    parse_value("abc")
    parse_value(None)

    # 2) 安全執行：即便 lambda 內發生除以零，主程式仍可繼續跑後續區塊。
    print("\n--- 14.7 ---")
    safe_run(lambda: 1 / 0)

    # 3) 自定義例外：上層統一 except NetworkError，
    #    不需逐一列出 HostnameError/ConnectionTimeout。
    print("\n--- 14.8 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:
            # 仍可透過 type(e).__name__ 分辨實際子類別。
            print(f"接到 {type(e).__name__}: {e}")
