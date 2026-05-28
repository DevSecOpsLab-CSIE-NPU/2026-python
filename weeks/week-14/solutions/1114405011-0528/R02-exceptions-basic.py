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
    """同一個 except 用 tuple 列出多種例外類別"""
    try:
        # int() 可能因為內容不合法拋 ValueError，或因型別不對拋 TypeError。
        return int(s)
    except (ValueError, TypeError) as e:
        # 將錯誤型別與訊息一起印出，方便除錯與教學觀察。
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """except Exception，而不是裸 except:（裸 except 會抓到 KeyboardInterrupt）"""
    try:
        # 讓呼叫端傳入任何函式與參數，統一在此處包裝錯誤處理。
        return func(*args)
    except Exception as e:
        # 這裡示範「集中處理」：先印簡短錯誤摘要。
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        # 再印完整 traceback，包含呼叫堆疊，便於定位問題來源。
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
    """所有網路錯誤的基底類別；繼承 Exception 而不是 BaseException"""


class HostnameError(NetworkError):
    """找不到主機"""


class ConnectionTimeout(NetworkError):
    """連線逾時，附帶 host / seconds 屬性，方便上層判斷"""
    def __init__(self, host, seconds):
        # 先把可讀訊息交給父類別，讓 str(e) 可直接顯示友善文字。
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        # 額外保存結構化欄位，供上層程式做邏輯判斷或記錄。
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """模擬連線流程：示範拋出自定義例外與正常回傳。"""
    if host == "":
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"


if __name__ == "__main__":
    # 14.6：示範多例外共用一個 except 的處理方式。
    print("--- 14.6 ---")
    parse_value("abc")
    parse_value(None)

    # 14.7：示範集中捕捉 Exception 並輸出 traceback。
    print("\n--- 14.7 ---")
    safe_run(lambda: 1 / 0)

    # 14.8：示範如何以共同父類別 NetworkError 進行統一攔截。
    print("\n--- 14.8 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:
            # 不同子類別都能在這裡被捕捉，並可用 type(e) 區分。
            print(f"接到 {type(e).__name__}: {e}")
