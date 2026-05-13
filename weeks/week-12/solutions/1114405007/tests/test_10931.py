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
    input_text = "1\n2\n10\n21\n0\n"
    expected_output = (
        "The parity of 1 is 1 (mod 2).\n"
        "The parity of 10 is 1 (mod 2).\n"
        "The parity of 1010 is 2 (mod 2).\n"
        "The parity of 10101 is 3 (mod 2)."
    )

    run_case("10931_main.py", input_text, expected_output)
    print("[PASS] 10931_main.py")

    print("All tests passed: 1 case")


if __name__ == "__main__":
    main()
