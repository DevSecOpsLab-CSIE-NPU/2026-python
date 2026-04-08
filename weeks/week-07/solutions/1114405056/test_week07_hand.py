import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Case:
    name: str
    input_text: str
    expected: str


def normalize(text: str) -> str:
    return text.replace("\r", "").strip()


def run_case(script_path: Path, case: Case) -> tuple[str, bool]:
    result = subprocess.run(
        [sys.executable, str(script_path)],
        input=case.input_text,
        text=True,
        capture_output=True,
        check=False,
    )

    if result.returncode != 0:
        output = (
            f"Runtime Error (code={result.returncode})\n"
            f"stderr:\n{result.stderr.strip()}"
        )
        return output, False

    actual = normalize(result.stdout)
    expected = normalize(case.expected)
    return actual, actual == expected


def write_problem_log(base_dir: Path, problem: str, cases: list[Case]) -> bool:
    script_path = base_dir / f"{problem}-hand.py"
    log_path = base_dir / f"week07-hand-{problem}-log.txt"

    lines: list[str] = []
    lines.append("Week 07 Hand Test Log")
    lines.append(f"Problem: {problem}")
    lines.append(f"Runner: {Path(sys.executable).name}")
    lines.append("")

    all_passed = True

    for case in cases:
        actual, ok = run_case(script_path, case)
        all_passed = all_passed and ok

        lines.append(f"[{case.name}]")
        lines.append("Input:")
        lines.append(case.input_text.strip())
        lines.append("Expected:")
        lines.append(normalize(case.expected))
        lines.append("Output:")
        lines.append(actual)
        lines.append(f"Result: {'PASS' if ok else 'FAIL'}")
        lines.append("")

    log_path.write_text("\n".join(lines), encoding="utf-8")
    return all_passed


def main() -> int:
    base_dir = Path(__file__).resolve().parent

    tests: dict[str, list[Case]] = {
        "uva10062": [
            Case("case1", "5\n0\n2\n2\n3\n", "2\n1\n5\n3\n4\n"),
            Case("case2", "3\n0\n1\n", "3\n1\n2\n"),
        ],
        "uva10071": [
            Case("case1", "1\n0\n", "1\n"),
            Case("case2", "2\n0\n1\n", "6\n"),
        ],
        "uva10093": [
            Case("case1", "1 1\nP\n", "1\n"),
            Case("case2", "2 2\nPP\nPP\n", "2\n"),
        ],
        "uva10101": [
            Case("case1", "1+1=3#", "1+1=2#\n"),
        ],
        "uva10170": [
            Case("case1", "4 10\n", "6\n"),
            Case("case2", "1 1\n", "1\n"),
        ],
    }

    all_passed = True
    for problem, cases in tests.items():
        if not write_problem_log(base_dir, problem, cases):
            all_passed = False

    if all_passed:
        print("All hand tests passed. Logs generated.")
        return 0

    print("Some hand tests failed. Check per-problem logs.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
