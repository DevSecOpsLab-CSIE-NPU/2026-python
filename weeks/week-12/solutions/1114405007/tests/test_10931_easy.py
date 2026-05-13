import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def run_case(input_text: str, expected_output: str) -> None:
    script_path = BASE / "10931_easy.py"
    proc = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"10931_easy.py failed:\n{proc.stderr}")

    actual = proc.stdout.strip()
    expected = expected_output.strip()
    if actual != expected:
        raise AssertionError(
            f"10931_easy.py output mismatch\n"
            f"--- expected ---\n{expected}\n"
            f"--- actual ---\n{actual}"
        )


def main() -> None:
    run_case(
        "1\n2\n10\n21\n0\n",
        "The parity of 1 is 1 (mod 2).\n"
        "The parity of 10 is 1 (mod 2).\n"
        "The parity of 1010 is 2 (mod 2).\n"
        "The parity of 10101 is 3 (mod 2).",
    )
    print("[PASS] 10931_easy.py")
    print("All tests passed: 1 case")


if __name__ == "__main__":
    main()
