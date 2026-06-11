"""
R02：例外處理基本用法（記憶層）

```
"""
R02：例外處理基本用法（記憶層）

此範例展示三個主題：
- 同一個 except 捕捉多種例外類別
- 捕獲所有一般例外但避免使用裸 except
- 如何定義並使用自訂例外以表達應用層的錯誤語意

執行：
    python R02-exceptions-basic.py
"""
"""R02：例外處理基本用法（記憶層）

此範例展示三個主題：
- 同一個 except 捕捉多種例外類別
- 捕獲所有一般例外但避免使用裸 except
- 如何定義並使用自訂例外以表達應用層的錯誤語意

執行：
    python R02-exceptions-basic.py
"""
import traceback


# ---------- 14.6 多個例外 ----------
def parse_value(s):
    """嘗試把輸入轉為整數。

    如果輸入為 None、非數字字串或其他不可轉換的型態，int() 會拋出 ValueError 或 TypeError。
    這裡用 except (ValueError, TypeError) 把這兩種情況一起處理，示範如何在一個 except 中捕捉多種例外類別。
    回傳 None 表示解析失敗（此處僅示範，實務可選擇回傳 sentinel 或重新拋出）。
    """
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # 列印發生的例外類型與訊息，方便觀察
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """以 except Exception 捕捉大部分的例外，但不要使用裸 except:。

    - 使用裸 except 會捕捉到 BaseException 的子類（例如 KeyboardInterrupt、SystemExit），
      這些通常不應該被吞掉。
    - 使用 Exception 可以捕捉大多數程式執行期錯誤，同時仍允許系統中斷等特殊例外升到最上層。
    - 捕捉到例外後示範列印完整 traceback，以便除錯。
    """
    try:
        return func(*args)
    except Exception as e:
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        # 列印完整 traceback，對於除錯比只 print(e) 有用得多
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
    """所有網路錯誤的基底類別；繼承 Exception 而不是 BaseException。

    - 繼承自 Exception 表示這是可被捕捉的「錯誤情況」，而非系統級別的異常。
    """


class HostnameError(NetworkError):
    """表示找不到主機或主機名稱不合法的錯誤。"""


class ConnectionTimeout(NetworkError):
    """連線逾時的例外，帶有 host 及 seconds 屬性，方便上層邏輯使用。"""
    def __init__(self, host, seconds):
        # 以人類可讀的訊息初始化基底 Exception
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        # 保留原始屬性，呼叫端可根據 host/seconds 做更細緻處理
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """模擬簡單的連線函式，根據參數拋出對應自定義例外。

    - host 為空字串視為主機名稱錯誤，拋出 HostnameError。
    - timeout 小於 1 視為逾時條件，拋出 ConnectionTimeout。
    - 成功時回傳表示連線成功的字串。
    """
    if host == "":
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"


if __name__ == "__main__":
    print("--- 14.6 ---")
    # 演示解析失敗會印出錯誤並回傳 None
    parse_value("abc")
    parse_value(None)

    print("\n--- 14.7 ---")
    # safe_run 會捕捉 ZeroDivisionError 並印出 traceback
    safe_run(lambda: 1 / 0)

    print("\n--- 14.8 ---")
    # 逐一測試不同情況，捕捉 NetworkError 的通用錯誤類別並印出
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:
            print(f"接到 {type(e).__name__}: {e}")
