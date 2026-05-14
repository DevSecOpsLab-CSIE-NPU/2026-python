"""測試輔助工具。"""

from __future__ import annotations

import importlib.util
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


def load_module(filename: str):
    """用檔案路徑載入帶有連字號的 Python 腳本。"""
    file_path = BASE_DIR / filename
    module_name = filename.replace("-", "_").replace(".py", "")
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"無法載入模組：{file_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
