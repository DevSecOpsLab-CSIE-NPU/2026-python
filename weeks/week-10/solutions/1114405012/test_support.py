from __future__ import annotations

import subprocess
import sys
from pathlib import Path


# 以這個檔案所在目錄作為測試執行根目錄。
BASE_DIR = Path(__file__).resolve().parent


def run_script(script_name: str, input_data: str) -> str:
    # 用與目前測試相同的 Python 解譯器執行指定腳本。
    result = subprocess.run(
        [sys.executable, str(BASE_DIR / script_name)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    # 去掉頭尾空白，方便直接與 expected 比對。
    return result.stdout.strip()