import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def run_case(script_name: str, input_text: str, expected_output: str) -> None:
    script_path = BASE / script_name
    proc = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"{script_name} failed:\n{proc.stderr}")

    actual = proc.stdout.strip()
    expected = expected_output.strip()
    if actual != expected:
        raise AssertionError(
            f"{script_name} output mismatch\n"
            f"--- expected ---\n{expected}\n"
            f"--- actual ---\n{actual}"
        )


def main() -> None:
    input_text = "2\n40 20\n20 40\n"
    expected_output = "30 10\nimpossible"

    run_case("10812_main.py", input_text, expected_output)
    print("[PASS] 10812_main.py")

    print("All tests passed: 1 case")


if __name__ == "__main__":
    main()
