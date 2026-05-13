import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def run_case(script_name: str, input_text: str) -> str:
    script_path = BASE / script_name
    proc = subprocess.run(
        [sys.executable, str(script_path)],
        input=input_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"{script_name} failed with code {proc.returncode}:\n{proc.stderr}"
        )
    return proc.stdout.strip()


def assert_case(script_name: str, input_text: str, expected_output: str) -> None:
    actual = run_case(script_name, input_text)
    expected = expected_output.strip()
    if actual != expected:
        raise AssertionError(
            f"{script_name} output mismatch\n"
            f"--- expected ---\n{expected}\n"
            f"--- actual ---\n{actual}\n"
        )


def main() -> None:
    tests = [
        (
            ["10812_easy.py", "10812_main.py"],
            "2\n40 20\n20 40\n",
            "30 10\nimpossible",
        ),
        (
            ["10908_easy.py", "10908_main.py"],
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
            "5 2\n",
            "7 10 4\n3\n1\n5\n1",
        ),
        (
            ["10922_easy.py", "10922_main.py"],
            "9\n999\n7\n0\n",
            "9 is a multiple of 9 and has 9-degree 1.\n"
            "999 is a multiple of 9 and has 9-degree 2.\n"
            "7 is not a multiple of 9.",
        ),
        (
            ["10929_easy.py", "10929_main.py"],
            "112233\n123456\n0\n",
            "112233 is a multiple of 11.\n123456 is not a multiple of 11.",
        ),
        (
            ["10931_easy.py", "10931_main.py"],
            "1\n2\n10\n21\n0\n",
            "The parity of 1 is 1 (mod 2).\n"
            "The parity of 10 is 1 (mod 2).\n"
            "The parity of 1010 is 2 (mod 2).\n"
            "The parity of 10101 is 3 (mod 2).",
        ),
    ]

    total = 0
    for scripts, input_text, expected in tests:
        for script in scripts:
            assert_case(script, input_text, expected)
            total += 1
            print(f"[PASS] {script}")

    print(f"All tests passed: {total} cases")


if __name__ == "__main__":
    main()
