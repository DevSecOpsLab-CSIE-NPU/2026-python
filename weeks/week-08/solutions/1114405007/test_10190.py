"""10190 測試程式。"""

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
    sample_input = """3 2
12 3
9 3
3 3
1 5
999 1
"""
    expected = """Boring!
Boring!
9 3 1
3 1
Boring!
Boring!""".strip()

    for script in ["10190-easy.py", "10190.py"]:
        output = run_script(script, sample_input)
        assert output == expected, f"{script} 輸出不符合預期\n{output}"

    print("10190 tests passed")


if __name__ == "__main__":
    main()
