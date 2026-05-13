import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def run_case(input_text: str, expected_output: str) -> None:
    script_path = BASE / "10908_easy.py"
    proc = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"10908_easy.py failed:\n{proc.stderr}")

    actual = proc.stdout.strip()
    expected = expected_output.strip()
    if actual != expected:
        raise AssertionError(
            f"10908_easy.py output mismatch\n"
            f"--- expected ---\n{expected}\n"
            f"--- actual ---\n{actual}"
        )


def main() -> None:
    input_text = (
        "1\n"
        "7 10 4\n"
        "abbbaaaaaa\n"
        "abbbaaaaaa\n"
        "abbbaaaaaa\n"
        "aaaaaaaaaa\n"
        "aaaaaaaaaa\n"
        "aaccaaaaaa\n"
        "aaccaaaaaa\n"
        "1 2\n"
        "2 4\n"
        "4 6\n"
        "5 2\n"
    )
    run_case(input_text, "7 10 4\n3\n1\n5\n1")
    print("[PASS] 10908_easy.py")
    print("All tests passed: 1 case")


if __name__ == "__main__":
    main()
