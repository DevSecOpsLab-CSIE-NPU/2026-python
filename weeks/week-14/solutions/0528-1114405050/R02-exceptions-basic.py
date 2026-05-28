"""
R02：例外處理基本用法（記憶層）

對應 Cookbook：
- 14.6 處理多個例外
- 14.7 捕獲所有例外
- 14.8 建立自定義例外

執行：
    python R02-exceptions-basic.py
"""
import traceback  # 用於印出詳細的錯誤追蹤訊息 (traceback)，包含檔案、行號與呼叫鏈


# ---------- 14.6 多個例外 ----------
def parse_value(s):
    """同一個 except 用 tuple 列出多種例外類別"""
    try:
        return int(s)  # 嘗試將傳入的參數轉成整數
    except (ValueError, TypeError) as e:
        # 當 s 為字串如 "abc" 時，會拋出 ValueError
        # 當 s 為 None 或不支援轉 int 的型別時，會拋出 TypeError
        # 將這兩種例外放在 tuple 裡，可以同時捕捉並共用相同的錯誤處理邏輯
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """except Exception，而不是裸 except:（裸 except 會抓到 KeyboardInterrupt）"""
    try:
        return func(*args)  # 執行傳入的函式
    except Exception as e:
        # 捕捉所有繼承自 Exception 的錯誤 (也就是幾乎所有的常規程式錯誤)
        # 警告：絕對不要寫「裸 except:」，因為那樣會連 KeyboardInterrupt (Ctrl+C) 和 SystemExit (sys.exit) 都攔截掉，導致程式難以關閉
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        # 利用 traceback 模組印出完整的錯誤追蹤，方便除錯
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
# 自定義例外通常建立一個模組層級的基底例外 (Base Exception)，其他特定例外再繼承它
class NetworkError(Exception):
    """所有網路錯誤的基底類別；繼承 Exception 而不是 BaseException"""
    # 這裡通常不需要實作任何內容，用 pass 即可。
    # 外部的 try-except 區塊可以用 `except NetworkError:` 來捕捉所有與這個模組相關的錯誤
    pass


class HostnameError(NetworkError):
    """找不到主機"""
    pass


class ConnectionTimeout(NetworkError):
    """連線逾時，附帶 host / seconds 屬性，方便上層判斷"""
    def __init__(self, host, seconds):
        # 呼叫父類別 (Exception) 的 __init__，設定錯誤訊息字串
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        # 儲存客製化的屬性，讓捕獲這個例外的人可以更容易取用相關資訊進行後續處理
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """模擬網路連線的函式，會根據條件拋出不同的自定義例外"""
    if host == "":
        raise HostnameError("主機名稱為空")  # 主動拋出 HostnameError
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)  # 主動拋出 ConnectionTimeout，並傳遞自訂屬性
    return f"connected to {host}"


if __name__ == "__main__":
    # 以下為測試與示範程式碼
    print("--- 14.6 ---")
    parse_value("abc")  # 將觸發 ValueError
    parse_value(None)  # 將觸發 TypeError

    print("\n--- 14.7 ---")
    safe_run(lambda: 1 / 0)  # 會觸發 ZeroDivisionError，被 safe_run 裡面的 Exception 捕獲

    print("\n--- 14.8 ---")
    # 測試正常與兩種例外的狀況
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:
            # 這裡用 NetworkError 一次抓取 HostnameError 和 ConnectionTimeout 兩種錯誤
            print(f"接到 {type(e).__name__}: {e}")
