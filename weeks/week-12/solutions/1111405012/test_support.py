"""Week 12 測試共用工具。

提供動態載入解題模組的方法，讓測試可以直接驗證單一檔案。
"""

from __future__ import annotations

import importlib.util
from pathlib import Path


def load_module(filename: str):
    """依檔名從同資料夾載入 Python 模組。"""

    module_path = Path(__file__).with_name(filename)
    module_name = module_path.stem.replace("-", "_")
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"無法載入模組：{filename}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
