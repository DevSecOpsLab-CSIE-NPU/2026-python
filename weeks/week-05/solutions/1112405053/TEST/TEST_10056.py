from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGET_SCRIPT = BASE_DIR.parent / "10056_AI.py"
RESULT_FILE = BASE_DIR / "RESULT_10056.txt"


TEST_CASES = [
    {
        "name": "case-1: 2x3 matrix",
        "input": "2 3\n1 2 3 4 5 6\n",
    },
    {
        "name": "case-2: 3x2 matrix",
        "input": "3 2\n1 2 3 4 5 6\n",
    },
    {
        "name": "case-3: 1x5 row vector",
        "input": "1 5\n10 20 30 40 50\n",
    },
    {
        "name": "case-4: 4x1 column vector",
        "input": "4 1\n7 8 9 10\n",
    },
    {
        "name": "case-5: 3x3 square matrix",
        "input": "3 3\n1 2 3 4 5 6 7 8 9\n",
    },
]


def run_one_case(case_input: str) -> tuple[str, int, str]:
    completed = subprocess.run(
        ["python", str(TARGET_SCRIPT)],
        input=case_input,
        text=True,
        capture_output=True,
        check=False,
    )
    return completed.stdout.strip(), completed.returncode, completed.stderr.strip()


def main() -> None:
    lines: list[str] = []
    lines.append("=" * 60)
    lines.append(f"10056 測試時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"目標程式: {TARGET_SCRIPT}")
    lines.append("=" * 60)

    success_count = 0
    for index, case in enumerate(TEST_CASES, start=1):
        actual, returncode, stderr_text = run_one_case(case["input"])
        status = "SUCCESS" if returncode == 0 else "ERROR"
        if returncode == 0:
            success_count += 1

        lines.append(f"[第 {index} 次] {case['name']}")
        lines.append(f"輸入:\n{case['input'].rstrip()}")
        lines.append(f"輸出: {actual}")
        lines.append(f"狀態: {status}")
        if returncode != 0:
            lines.append(f"return code: {returncode}")
        if stderr_text:
            lines.append(f"stderr: {stderr_text}")
        lines.append("-" * 60)

    lines.append(f"總結: {success_count}/{len(TEST_CASES)} 次執行成功")

    output = "\n".join(lines) + "\n"
    RESULT_FILE.write_text(output, encoding="utf-8")

    print(output)
    print(f"測試結果已寫入: {RESULT_FILE}")


if __name__ == "__main__":
    main()
