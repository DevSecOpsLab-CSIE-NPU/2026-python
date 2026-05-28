"""
R02：例外處理基本用法（記憶層）

這個範例示範三件事：
- 用同一個 except 一次處理多種可能發生的例外
- 用 Exception 限縮攔截範圍，避免裸 except 把系統中斷訊號也吃掉
- 自己定義例外類別，讓上層可以用型別判斷錯誤來源

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
    """示範在同一個 except 內同時攔截 ValueError 與 TypeError。"""
    try:
        # int() 遇到非數字字串會丟 ValueError，遇到 None 之類的型別會丟 TypeError。
        # 這裡故意保留這個轉換動作，方便展示如何用 tuple 一次處理多種錯誤。
        return int(s)
    except (ValueError, TypeError) as e:
        # 印出錯誤型別與訊息，方便在教學或除錯時看出到底是哪一種失敗。
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        # 回傳 None 表示這次解析失敗，但程式沒有直接中斷。
        return None


# ---------- 14.7 捕獲所有例外 ----------
def safe_run(func, *args):
    """示範只捕獲 Exception，避免裸 except 把中斷訊號也一起攔下。"""
    try:
        # 這裡不關心 func 是什麼，只要是可呼叫物件，就直接執行並傳入參數。
        return func(*args)
    except Exception as e:
        # 只攔截一般執行錯誤，像 KeyboardInterrupt 這類系統層中斷不會被吃掉。
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        # 印出完整 traceback，讓除錯資訊比單純錯誤訊息更完整。
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
class NetworkError(Exception):
    """所有網路錯誤的基底類別；繼承 Exception，而不是 BaseException。"""


class HostnameError(NetworkError):
    """主機名稱不合法或缺失時使用。"""


class ConnectionTimeout(NetworkError):
    """連線逾時，附帶 host / seconds 屬性，方便上層判斷。"""
    def __init__(self, host, seconds):
        # 先把可讀的錯誤訊息交給 Exception，這樣直接印出例外時就會有文字內容。
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        # 再保留結構化資訊，讓上層除了看訊息，還能直接讀取欄位做判斷。
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    # 空字串代表連線目標根本不存在，直接視為主機名稱錯誤。
    if host == "":
        raise HostnameError("主機名稱為空")
    # timeout 太小時模擬連線逾時，展示如何丟出帶參數的自定義例外。
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    # 成功時回傳描述字串，方便下方主程式直接印出結果。
    return f"connected to {host}"


if __name__ == "__main__":
    # 14.6：故意丟入字串與 None，分別觸發 ValueError 與 TypeError。
    print("--- 14.6 ---")
    parse_value("abc")
    parse_value(None)

    # 14.7：用一個會除以零的 lambda，示範 safe_run 會攔下例外並印 traceback。
    print("\n--- 14.7 ---")
    safe_run(lambda: 1 / 0)

    # 14.8：依序測試正常、主機名稱錯誤、逾時錯誤三種情況。
    print("\n--- 14.8 ---")
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:
        try:
            # 正常情況直接印出連線成功文字。
            print(connect(host, t))
        except NetworkError as e:
            # 只攔截我們自己定義的網路錯誤，其他未預期例外仍會往外冒。
            print(f"接到 {type(e).__name__}: {e}")
