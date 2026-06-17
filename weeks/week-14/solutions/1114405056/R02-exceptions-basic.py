"""R02: exception handling basics examples.

Run:
    python R02-exceptions-basic.py
"""

import traceback
from typing import Any, Callable, Optional


def parse_value(text: Any) -> Optional[int]:
    """Handle multiple parse exceptions in one block."""
    try:
        return int(text)
    except (ValueError, TypeError) as exc:
        print(f"[multi-except] parse failed: {type(exc).__name__}: {exc}")
        return None


def safe_run(func: Callable, *args):
    """Catch regular application errors without swallowing KeyboardInterrupt."""
    try:
        return func(*args)
    except Exception as exc:  # intentionally not using bare except
        print(f"[safe-run] error: {type(exc).__name__}: {exc}")
        traceback.print_exc()
        return None


class NetworkError(Exception):
    """Base class for network-related failures."""


class HostnameError(NetworkError):
    """Raised when host is invalid."""


class ConnectionTimeout(NetworkError):
    """Raised on timeout with structured context."""

    def __init__(self, host: str, seconds: int) -> None:
        super().__init__(f"connection to {host} exceeded {seconds} second(s)")
        self.host = host
        self.seconds = seconds


def connect(host: str, timeout: int) -> str:
    """Fake connection function used for exception examples."""
    if host == "":
        raise HostnameError("host cannot be empty")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    return f"connected to {host}"


if __name__ == "__main__":
    print("--- multiple except ---")
    parse_value("abc")
    parse_value(None)

    print("\n--- catch Exception only ---")
    safe_run(lambda: 1 / 0)

    print("\n--- custom exceptions ---")
    for host, timeout in [("example.com", 5), ("", 5), ("slow.example", 0)]:
        try:
            print(connect(host, timeout))
        except NetworkError as exc:
            print(f"caught {type(exc).__name__}: {exc}")
