"""
R02：例外處理基本用法（記憶層）

對應 Cookbook：
- 14.6 處理多個例外
- 14.7 捕獲所有例外
- 14.8 建立自定義例外

執行：
    python R02-exceptions-basic.py
"""
import traceback  # 用來列印完整的錯誤堆疊追蹤（呼叫鏈），幫助我們找到問題的根源


# ---------- 14.6 多個例外（一個 except 可以處理多種錯誤） ----------
def parse_value(s):
    """試著把字串轉成整數，如果失敗就返回 None（而不是直接當機）

    同一個 except 用 tuple 列出多種例外類別，這樣可以用同一段程式碼
    處理多種相關的錯誤，例如：非數字字串會拋 ValueError，
    無法轉型會拋 TypeError，我們想一視同仁地捕捉這兩種。
    """
    try:  # 嘗試執行可能失敗的程式碼
        return int(s)  # 把字串轉成整數
    except (ValueError, TypeError) as e:  # 同時捕捉兩種錯誤
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")  # 印出是哪一種錯誤，以及錯誤訊息
        return None  # 回傳 None，表示「轉換失敗」


# ---------- 14.7 捕獲所有例外（但不要用裸 except）----------
def safe_run(func, *args):
    """安全地執行一個函式，如果出錯了就把錯誤訊息印出來，程式繼續運行

    重要：用 except Exception 而不是裸 except:（意思是 except:）
    因為裸 except 會連 KeyboardInterrupt（使用者按 Ctrl+C）都抓到，
    導致使用者無法中斷程式。
    """
    try:  # 嘗試執行函式
        return func(*args)  # 用傳進來的參數呼叫函式，並回傳結果
    except Exception as e:  # 只捕捉程式執行時的錯誤，不捕捉系統訊號
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")  # 印出錯誤類型和訊息
        traceback.print_exc()  # 印出完整的錯誤堆疊追蹤（告訴你從哪裡開始出問題）


# ---------- 14.8 自定義例外（建立你自己的錯誤類型） ----------
# 當內建的例外類型不夠用時，我們可以定義自己的，讓程式碼更清楚
class NetworkError(Exception):
    """所有網路相關錯誤的基底類別（父類）

    繼承 Exception 而不是 BaseException，這樣做的好處是：
    1. 上層程式碼可以統一捕捉所有網路相關的错誤
    2. 能區分「正常的程式邏輯錯誤」和「系統等級的中斷" （如 KeyboardInterrupt）
    """
    pass  # 暫時不需要添加額外的行為，只是建立一個分類


class HostnameError(NetworkError):
    """主機名稱無效時拋出的錯誤（例如：空字串、格式不符）"""
    pass  # 繼承 NetworkError，所以可以被更上層的 except NetworkError 捕捉


class ConnectionTimeout(NetworkError):
    """連線超過時限時拋出的錯誤

    這個類別不只拋出錯誤，還保存了「哪個主機" 和 "超過多久" 的細節，
    這樣上層程式碼可以根據這些資訊做不同的處理（例如重試、通知使用者等）
    """

    def __init__(self, host, seconds):
        # 先呼叫父類別的初始化，傳入人類看得懂的錯誤訊息
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        # 額外保存技術細節，供上層程式碼程式查詢
        self.host = host  # 記住是連線到哪個主機失敗的
        self.seconds = seconds  # 記住超過了多久


def connect(host, timeout):
    """嘗試連線到指定的主機

    如果主機名稱為空或逾時設定無效，就拋出適當的自定義例外
    """
    if host == "":  # 檢查主機名稱是否為空
        raise HostnameError("主機名稱為空")  # 拋出我們自己定義的錯誤類型
    if timeout < 1:  # 檢查逾時設定是否合理（少於 1 秒不合理）
        raise ConnectionTimeout(host, timeout)  # 拋出包含細節的錯誤
    return f"connected to {host}"  # 如果沒有問題，回傳成功訊息


if __name__ == "__main__":  # 這個檔案被直接執行（而不是被當成模組匯入）時，執行以下程式碼
    print("--- 14.6 ---")  # 演示：多種例外處理
    parse_value("abc")  # 非數字字符 → ValueError
    parse_value(None)  # None → TypeError

    print("\n--- 14.7 ---")  # 演示：安全執行函式
    safe_run(lambda: 1 / 0)  # 除以零 → ZeroDivisionError（會被 safe_run 捕捉）

    print("\n--- 14.8 ---")  # 演示：自定義例外
    # 測試三種情況：正常連線、空主機名稱、逾時設定無效
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            print(connect(host, t))  # 嘗試連線
        except NetworkError as e:  # 捕捉所有網路相關的錯誤
            # 因為我們的自定義例外都繼承 NetworkError，所以這裡能捕捉所有情況
            print(f"接到 {type(e).__name__}: {e}")
