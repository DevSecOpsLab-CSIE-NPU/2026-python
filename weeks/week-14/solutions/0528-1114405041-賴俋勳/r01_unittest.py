"""
R01 拆分版：unittest 基本技巧。

重點：
1. 測試 stdout 輸出
2. 測試 mock 物件呼叫
3. 測試例外與訊息
"""

from __future__ import annotations

from typing import Any


def url_print(host: str, domain: str) -> None:
    """印出網址字串，方便示範 stdout 測試。"""
    print(f"https://{host}.{domain}")


def parse_int(text: str) -> int:
    """空字串時主動拋出 ValueError，其餘交給 int 處理。"""
    if text == "":
        raise ValueError("空字串無法轉成整數")
    return int(text)


def fetch_user(api: Any, user_id: int) -> dict[str, Any]:
    """用注入的 api 物件抓使用者資料，利於 mock 測試。"""
    return api.get(f"/users/{user_id}")
