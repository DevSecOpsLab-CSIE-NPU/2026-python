import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def run_case(input_text: str, expected_output: str) -> None:
    script_path = BASE / "10922_easy.py"
    proc = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"10922_easy.py failed:\n{proc.stderr}")

    actual = proc.stdout.strip()
    expected = expected_output.strip()
    if actual != expected:
        raise AssertionError(
            f"10922_easy.py output mismatch\n"
            f"--- expected ---\n{expected}\n"
            f"--- actual ---\n{actual}"
        )


def main() -> None:
    run_case(
        "9\n999\n7\n0\n",
        "9 is a multiple of 9 and has 9-degree 1.\n"
        "999 is a multiple of 9 and has 9-degree 2.\n"
        "7 is not a multiple of 9.",
    )
    print("[PASS] 10922_easy.py")
    print("All tests passed: 1 case")


if __name__ == "__main__":
    main()
