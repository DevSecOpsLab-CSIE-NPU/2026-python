# R02. 例外處理基本示範
# 這個檔案示範 Python 例外的三種常見寫法：
# - 14.6 多例外 tuple
# - 14.7 捕捉所有例外但避免裸 except
# - 14.8 自定義例外類別

import traceback


def parse_value(s):
    """把輸入字串轉成整數，若無法轉換則回傳 None。"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")
        return None


def safe_run(func, *args):
    """執行指定函式，若發生例外則印出例外資訊與 traceback。"""
    try:
        return func(*args)
    except Exception as e:
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")
        traceback.print_exc()


class NetworkError(Exception):
    """所有網路相關例外的共同基底類別。"""


class HostnameError(NetworkError):
    """代表主機名稱無效或為空。"""


class ConnectionTimeout(NetworkError):
    """代表連線逾時，包含主機與逾時秒數資訊。"""

    def __init__(self, host, seconds):
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


def connect(host, timeout):
    """模擬連線邏輯，若 host 或 timeout 不合法則丟出自定義例外。"""
    if host == "":
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
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
