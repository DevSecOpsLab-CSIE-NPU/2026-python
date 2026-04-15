from __future__ import annotations

import importlib.util
import pathlib
import subprocess
import sys
from types import ModuleType


BASE_DIR = pathlib.Path(__file__).resolve().parent


def load_module(file_name: str) -> ModuleType:
    """依照檔案路徑載入模組，讓檔名包含 -easy 也能測試。"""
    file_path = BASE_DIR / file_name
    module_name = file_name.replace("-", "_").replace(".", "_")
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"無法載入模組: {file_name}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_script(file_name: str, input_data: str) -> str:
    """以 subprocess 模擬評測系統，確認 stdin/stdout 流程正確。"""
    completed = subprocess.run(
        [sys.executable, str(BASE_DIR / file_name)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()
