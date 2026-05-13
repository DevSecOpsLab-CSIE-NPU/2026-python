import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def run_case(input_text: str, expected_output: str) -> None:
    script_path = BASE / "10812_easy.py"
    proc = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"10812_easy.py failed:\n{proc.stderr}")

    actual = proc.stdout.strip()
    expected = expected_output.strip()
    if actual != expected:
        raise AssertionError(
            f"10812_easy.py output mismatch\n"
            f"--- expected ---\n{expected}\n"
            f"--- actual ---\n{actual}"
        )


def main() -> None:
    run_case("2\n40 20\n20 40\n", "30 10\nimpossible")
    print("[PASS] 10812_easy.py")
    print("All tests passed: 1 case")


if __name__ == "__main__":
    main()
