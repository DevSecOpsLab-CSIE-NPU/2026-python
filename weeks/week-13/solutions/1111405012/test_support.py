"""
動態模組加載工具
支援 unittest 動態載入外部解決方案模組
"""

import importlib.util
import sys
from pathlib import Path


def load_module(filename):
    """
    動態載入 Python 模組

    Args:
        filename: 模組檔案名稱 (相對路徑或絕對路徑)

    Returns:
        已載入的模組物件

    Example:
        >>> module = load_module('QUESTION_11005.py')
        >>> result = module.solve()
    """
    filepath = Path(filename)

    if not filepath.exists():
        raise FileNotFoundError(f"模組檔案未找到: {filename}")

    spec = importlib.util.spec_from_file_location(
        filepath.stem,
        filepath
    )

    if spec is None or spec.loader is None:
        raise ImportError(f"無法載入模組: {filename}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[filepath.stem] = module
    spec.loader.exec_module(module)

    return module
