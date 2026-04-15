"""10189 測試程式。"""

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
    sample_input = """4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0
"""
    expected = """Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100""".strip()

    for script in ["10189-easy.py", "10189.py"]:
        output = run_script(script, sample_input)
        assert output == expected, f"{script} 輸出不符合預期\n{output}"

    print("10189 tests passed")


if __name__ == "__main__":
    main()
