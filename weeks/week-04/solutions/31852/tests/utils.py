"""測試輔助工具。"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def run_script(script_name: str, input_data: str) -> str:
    """用子行程執行腳本，回傳標準輸出。"""
    completed = subprocess.run(
        [sys.executable, str(BASE_DIR / script_name)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
        cwd=BASE_DIR,
    )
    return completed.stdout.rstrip("\n")