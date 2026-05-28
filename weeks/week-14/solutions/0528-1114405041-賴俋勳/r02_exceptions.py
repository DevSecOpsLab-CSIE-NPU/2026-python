"""
R02 拆分版：例外處理基本用法。

重點：
1. 多重例外處理
2. 安全執行封裝
3. 自定義例外階層
"""

from __future__ import annotations

from typing import Any, Callable


def parse_value(value: Any) -> int | None:
    """示範同時處理 ValueError 與 TypeError。"""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def safe_run(func: Callable[..., Any], *args: Any) -> tuple[bool, Any]:
    """統一回傳格式：成功(True, result)；失敗(False, 例外名稱)。"""
    try:
        return True, func(*args)
    except Exception as exc:  # noqa: BLE001
        return False, type(exc).__name__


class NetworkError(Exception):
    """網路錯誤基底。"""


class HostnameError(NetworkError):
    """主機名稱錯誤。"""


class ConnectionTimeout(NetworkError):
    """逾時錯誤，保留 host 與 seconds 屬性。"""

    def __init__(self, host: str, seconds: int):
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


def connect(host: str, timeout: int) -> str:
    """模擬連線：空 host 與過小 timeout 都視為錯誤。"""
    if host == "":
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"
