"""10221 測試程式。"""

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent


def run_script(script_name: str, input_data: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(BASE / script_name)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return completed.stdout.strip()


def main() -> None:
    sample_input = """500 30 deg
700 60 min
200 45 deg
"""
    expected = """3633.775503 3592.408346
124.616509 124.614927
5215.043805 5082.035982""".strip()

    for script in ["10221-easy.py", "10221.py"]:
        output = run_script(script, sample_input)
        assert output == expected, f"{script} 輸出不符合預期\n{output}"

    print("10221 tests passed")


if __name__ == "__main__":
    main()
