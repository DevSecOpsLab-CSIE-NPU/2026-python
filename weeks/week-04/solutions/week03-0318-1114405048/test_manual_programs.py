import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent


def normalize(s: str) -> str:
    lines = [line.rstrip() for line in s.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    return "\n".join(lines).strip()


def run_case(py_name: str, test_input: str):
    proc = subprocess.run(
        [sys.executable, str(BASE / py_name)],
        input=test_input,
        text=True,
        capture_output=True,
        cwd=str(BASE),
    )
    return proc.returncode, proc.stdout, proc.stderr


def main():
    tests = [
        {
            "name": "manual_QUESTION-948.py",
            "input": """2

3 2
1 1 2
<
1 1 3
=

3 1
1 1 2
=
""",
            "expected": """2

3
""",
        },
        {
            "name": "manual_QUESTION-10008.py",
            "input": """3
This is a test.
Count me 123!
Aaa BBB ccc
""",
            "expected": """A 4
C 4
T 4
B 3
S 3
E 2
I 2
H 1
M 1
N 1
O 1
U 1
""",
        },
        {
            "name": "manual_QUESTION-10019.py",
            "input": """10 12
10 14
100 200
""",
            "expected": """2
4
100
""",
        },
        {
            "name": "manual_QUESTION-10035.py",
            "input": """123 456
555 555
123 594
0 0
""",
            "expected": """No carry operation.
3 carry operations.
1 carry operation.
""",
        },
        {
            "name": "manual_QUESTION-10038.py",
            "input": """4 1 4 2 3
5 1 4 2 -1 6
1 10
""",
            "expected": """Jolly
Not jolly
Jolly
""",
        },
    ]

    result_rows = []
    all_pass = True

    for t in tests:
        rc, out, err = run_case(t["name"], t["input"])
        passed = (rc == 0) and (normalize(out) == normalize(t["expected"]))
        all_pass = all_pass and passed

        result_rows.append(
            {
                "name": t["name"],
                "rc": rc,
                "pass": passed,
                "input": t["input"],
                "expected": t["expected"],
                "actual": out,
                "stderr": err,
            }
        )

    lines = []
    lines.append("# 手打程式測試 LOG")
    lines.append("")
    lines.append("總結: " + ("全部通過" if all_pass else "有失敗項目"))
    lines.append("")

    for row in result_rows:
        lines.append(f"## {row['name']}")
        lines.append(f"- Return code: {row['rc']}")
        lines.append(f"- 結果: {'PASS' if row['pass'] else 'FAIL'}")
        lines.append("")
        lines.append("### Input")
        lines.append("```text")
        lines.append(row["input"].rstrip("\n"))
        lines.append("```")
        lines.append("")
        lines.append("### Expected")
        lines.append("```text")
        lines.append(row["expected"].rstrip("\n"))
        lines.append("```")
        lines.append("")
        lines.append("### Actual")
        lines.append("```text")
        lines.append(row["actual"].rstrip("\n"))
        lines.append("```")
        lines.append("")

        if row["stderr"].strip():
            lines.append("### STDERR")
            lines.append("```text")
            lines.append(row["stderr"].rstrip("\n"))
            lines.append("```")
            lines.append("")

    log_path = BASE / "MANUAL_TEST_LOG.md"
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("ALL_PASS=" + str(all_pass))
    print("LOG=" + str(log_path))


if __name__ == "__main__":
    main()
