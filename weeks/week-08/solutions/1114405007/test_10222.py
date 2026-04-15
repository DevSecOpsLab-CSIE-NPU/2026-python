"""10222 測試程式。"""

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
    return completed.stdout


def main() -> None:
    sample_input = "o s, gomr ypfsu/\n"
    expected = "i am fine today.\n"

    for script in ["10222-easy.py", "10222.py"]:
        output = run_script(script, sample_input)
        assert output == expected, f"{script} 輸出不符合預期\n{output}"

    print("10222 tests passed")


if __name__ == "__main__":
    main()
