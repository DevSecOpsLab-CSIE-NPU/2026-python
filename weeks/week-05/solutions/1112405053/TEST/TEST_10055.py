from __future__ import annotations

import subprocess
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGET_SCRIPT = BASE_DIR.parent / "10055_AI.py"
RESULT_FILE = BASE_DIR / "RESULT_10055.txt"


TEST_CASES = [
    {
        "name": "case-1: simple range query",
        "input": "2 1\n2 1 2\n",
    },
    {
        "name": "case-2: toggle and query",
        "input": "3 3\n1 1\n1 2\n2 1 3\n",
    },
    {
        "name": "case-3: multiple queries",
        "input": "4 4\n1 2\n2 1 2\n2 2 4\n1 2\n",
    },
    {
        "name": "case-4: single element",
        "input": "1 2\n1 1\n2 1 1\n",
    },
    {
        "name": "case-5: complex operations",
        "input": "5 5\n1 1\n1 2\n2 1 3\n1 3\n2 1 5\n",
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
    lines.append(f"10055 測試時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
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
