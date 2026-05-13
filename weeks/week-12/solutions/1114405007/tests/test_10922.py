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
    input_text = "9\n999\n7\n0\n"
    expected_output = (
        "9 is a multiple of 9 and has 9-degree 1.\n"
        "999 is a multiple of 9 and has 9-degree 2.\n"
        "7 is not a multiple of 9."
    )

    run_case("10922_main.py", input_text, expected_output)
    print("[PASS] 10922_main.py")

    print("All tests passed: 1 case")


if __name__ == "__main__":
    main()
