"""
R02：例外處理基本用法（記憶層）

對應 Cookbook：
- 14.6 處理多個例外
- 14.7 捕獲所有例外
- 14.8 建立自定義例外

本檔模組重點：
1) 用 tuple 一次捕獲多種例外型別
2) 用 except Exception 而非裸 except，避免誤抓 KeyboardInterrupt
3) 自訂例外層次、附加屬性，方便上層判斷

執行：
    python R02-exceptions-basic.py
"""
import traceback


# ---------- 14.6 多個例外 ----------
def parse_value(s):
    """同一個 except 用 tuple 列出多種例外類別"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # (ValueError, TypeError) 表示「其中任一個例外發生就進入此區塊」
        # 這比寫兩個分開的 except 更簡潔
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """except Exception，而不是裸 except:（裸 except 會抓到 KeyboardInterrupt）"""
    try:
        return func(*args)
    except Exception as e:
        # Exception 是所有一般程式錯誤的基底類別，不包含 KeyboardInterrupt、SystemExit
        # traceback.print_exc() 會印出完整的錯誤堆疊追蹤，方便除錯
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
    """所有網路錯誤的基底類別；繼承 Exception 而不是 BaseException"""
    # 繼承 Exception 而非 BaseException，這樣 except Exception 就能抓到此類錯誤
    # 所有自訂例外应都繼承 Exception，如此才能被 safe_run 這類通用捕獲工具抓到


class HostnameError(NetworkError):
    """找不到主機"""
    # 繼承 NetworkError，需要捕獲所有網路錯誤時只要 except NetworkError 即可


class ConnectionTimeout(NetworkError):
    """連線逾時，附帶 host / seconds 屬性，方便上層判斷"""
    def __init__(self, host, seconds):
        # 呼叫父類別的 __init__，设定標準的錯誤訊息
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        # 對於上層處理程式而言，有結構化屬性比只有字串訊息更方便取用
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    # 驗證順序：先檢查主機名稱，再檢查逾時限制
    if host == "":
        raise HostnameError("主機名稱為空")    # 丟出子類別例外
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)  # 附帶結構化屬性
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
            print(f"接到 {type(e).__name__}: {e}")
