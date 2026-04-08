from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path


RUN_COUNT = 5

# Default input uses ZeroJudge a086 sample.
TEST_INPUT = """5 4
PHPP
PPHH
PPPP
PHPP
PHHP
"""


def main() -> None:
    test_dir = Path(__file__).resolve().parent
    solution_path = test_dir.parent / "10101_ME.py"
    log_path = test_dir / "TEST_10101_results.txt"

    if not solution_path.exists():
        raise FileNotFoundError(f"Solution file not found: {solution_path}")

    lines: list[str] = []
    lines.append(f"Target: {solution_path}")
    lines.append(f"Python: {sys.executable}")
    lines.append(f"Run count: {RUN_COUNT}")
    lines.append("Input:")
    lines.append(TEST_INPUT.rstrip("\n"))
    lines.append("=" * 60)

    for i in range(1, RUN_COUNT + 1):
        start = time.perf_counter()
        proc = subprocess.run(
            [sys.executable, str(solution_path)],
            input=TEST_INPUT,
            text=True,
            capture_output=True,
            check=False,
        )
        elapsed_ms = (time.perf_counter() - start) * 1000

        lines.append(f"Run {i}")
        lines.append(f"Return code: {proc.returncode}")
        lines.append(f"Elapsed: {elapsed_ms:.3f} ms")
        lines.append("Stdout:")
        lines.append(proc.stdout.rstrip("\n") or "<empty>")
        lines.append("Stderr:")
        lines.append(proc.stderr.rstrip("\n") or "<empty>")
        lines.append("-" * 60)

    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Done. Result log written to: {log_path}")


if __name__ == "__main__":
    main()
