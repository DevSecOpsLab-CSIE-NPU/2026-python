"""10193 測試程式。"""

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
    sample_input = """3
1100
110
1010
101
1000
111
"""
    expected = """Pair #1: All you need is love!
Pair #2: All you need is love!
Pair #3: Love is not all you need!""".strip()

    for script in ["10193-easy.py", "10193.py"]:
        output = run_script(script, sample_input)
        assert output == expected, f"{script} 輸出不符合預期\n{output}"

    print("10193 tests passed")


if __name__ == "__main__":
    main()
