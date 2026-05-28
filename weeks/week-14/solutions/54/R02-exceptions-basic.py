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
        return int(s)  # 嘗試將字串轉為整數
    except (ValueError, TypeError) as e:  # 捕獲多種例外
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None  # 失敗時返回 None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """except Exception，而不是裸 except:（裸 except 會抓到 KeyboardInterrupt）"""
    try:
        return func(*args)  # 執行傳入的函式
    except Exception as e:  # 捕獲所有例外（不包含 KeyboardInterrupt）
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        traceback.print_exc()  # 輸出完整的追蹤訊息


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
    """所有網路錯誤的基底類別；繼承 Exception 而不是 BaseException"""
    pass


class HostnameError(NetworkError):
    """找不到主機"""
    pass


class ConnectionTimeout(NetworkError):
    """連線逾時，附帶 host / seconds 屬性，方便上層判斷"""
    def __init__(self, host, seconds):
        # 呼叫父類別的建構子，設定例外的訊息
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        # 儲存主機名稱和逾時時間作為屬性
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """嘗試連線到指定主機，不同的錯誤條件會拋出不同的例外"""
    if host == "":  # 檢查主機名稱是否為空
        raise HostnameError("主機名稱為空")
    if timeout < 1:  # 檢查逾時時間是否合理
    # 展示 14.6 的多異常捕獲
    print("--- 14.6 ---")
    parse_value("abc")  # 拋出 ValueError
    parse_value(None)   # 拋出 TypeError

    # 展示 14.7 的通用例外捕獲
    print("\n--- 14.7 ---")
    safe_run(lambda: 1 / 0)  # 拋出 ZeroDivisionError

    # 展示 14.8 的自訂例外
    print("\n--- 14.8 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:  # 捕獲自訂的網路例外
    print("\n--- 14.8 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))
        except NetworkError as e:
            print(f"接到 {type(e).__name__}: {e}")
