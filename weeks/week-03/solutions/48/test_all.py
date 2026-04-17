import subprocess
from pathlib import Path


BASE = Path(__file__).resolve().parent
PY = "C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe"


TESTS = [
    (
        "10041.py",
        "2\n2 2 4\n3 2 4 6\n",
        "2\n4\n",
    ),
    (
        "10050.py",
        "1\n14\n3\n3\n4\n8\n",
        "5\n",
    ),
    (
        "10055.py",
        "5 6\n2 1 5\n1 2\n2 1 3\n1 4\n2 1 5\n2 4 4\n",
        "0\n1\n0\n1\n",
    ),
    (
        "10056.py",
        "2\n3 0.1666666667 1\n3 0.1666666667 2\n",
        "0.3956\n0.3297\n",
    ),
    (
        "10057.py",
        "4\n1\n2\n2\n4\n2\n10\n20\n",
        "2 2 1\n10 2 11\n",
    ),
    (
        "10041-easy.py",
        "2\n2 2 4\n3 2 4 6\n",
        "2\n4\n",
    ),
    (
        "10050-easy.py",
        "1\n14\n3\n3\n4\n8\n",
        "5\n",
    ),
    (
        "10055-easy.py",
        "5 6\n2 1 5\n1 2\n2 1 3\n1 4\n2 1 5\n2 4 4\n",
        "0\n1\n0\n1\n",
    ),
    (
        "10056-easy.py",
        "2\n3 0.1666666667 1\n3 0.1666666667 2\n",
        "0.3956\n0.3297\n",
    ),
    (
        "10057-easy.py",
        "4\n1\n2\n2\n4\n2\n10\n20\n",
        "2 2 1\n10 2 11\n",
    ),
]


def run_case(file_name: str, given_input: str, expected: str) -> tuple[bool, str]:
    target = BASE / file_name
    proc = subprocess.run(
        [PY, str(target)],
        input=given_input,
        text=True,
        capture_output=True,
        check=False,
    )

    got = proc.stdout
    ok = proc.returncode == 0 and got.rstrip("\n") == expected.rstrip("\n")
    if ok:
        return True, f"[PASS] {file_name}"

    details = [f"[FAIL] {file_name}"]
    details.append(f"  returncode: {proc.returncode}")
    details.append(f"  expected : {expected!r}")
    details.append(f"  got      : {got!r}")
    if proc.stderr:
        details.append(f"  stderr   : {proc.stderr!r}")
    return False, "\n".join(details)


def main() -> None:
    lines = []
    passed = 0

    for file_name, given_input, expected in TESTS:
        ok, message = run_case(file_name, given_input, expected)
        lines.append(message)
        if ok:
            passed += 1

    total = len(TESTS)
    lines.append(f"\nSummary: {passed}/{total} passed")
    text = "\n".join(lines)

    print(text)
    (BASE / "TEST_LOG.txt").write_text(text + "\n", encoding="utf-8")

    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
