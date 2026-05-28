"""
R02 easy 版：例外處理記憶模板。
"""


def safe_int(value):
    # int 失敗最常見是 ValueError/TypeError。
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def run_guard(func, *args):
    # 成功回 True，失敗回 False + 例外名稱。
    try:
        return True, func(*args)
    except Exception as exc:
        return False, type(exc).__name__


class NetErr(Exception):
    # 網路例外基底。
    pass


class HostErr(NetErr):
    # 主機名稱錯誤。
    pass


class TimeoutErr(NetErr):
    # 逾時錯誤。
    def __init__(self, host, seconds):
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


def simple_connect(host, timeout):
    # 固定順序：先檢查 host，再檢查 timeout。
    if host == "":
        raise HostErr("主機名稱為空")
    if timeout < 1:
        raise TimeoutErr(host, timeout)
    return f"connected to {host}"
