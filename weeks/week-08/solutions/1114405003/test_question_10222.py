import os
import subprocess
import sys
import unittest
from pathlib import Path


def _find_solution_script() -> Path:
    """尋找 10222 解答程式位置；可由環境變數覆寫。"""
    custom = os.environ.get("TARGET_10222")
    if custom:
        p = Path(custom)
        if p.exists():
            return p

    base = Path(__file__).resolve().parent
    candidates = [
        "QUESTION-10222-手打.py",
        "QUESTION-10222.py",
        "question_10222.py",
        "uva10222.py",
        "10222.py",
        "solution_10222.py",
    ]
    for name in candidates:
        p = base / name
        if p.exists():
            return p

    raise unittest.SkipTest("找不到 10222 解答程式，請先放入同資料夾或設定 TARGET_10222")


def _run_solution(input_data: str) -> str:
    script = _find_solution_script()
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return proc.stdout


def _reference_decode(text: str) -> str:
    # 依 UVA 10222 慣例，將每個字元映射到鍵盤上往左兩格的位置。
    keyboard = "`1234567890-=WERTYUIOP[]\\SDFGHJKL;'XCVBNM,./"
    table = {keyboard[i]: keyboard[i - 2] for i in range(2, len(keyboard))}
    out = []
    for ch in text:
        up = ch.upper()
        if up in table:
            out.append(table[up])
        else:
            out.append(ch)
    return "".join(out)


class TestQuestion10222(unittest.TestCase):
    """UVA 10222 Decode the Mad man 測試。"""

    def test_known_phrase(self):
        input_data = "O S, GOMR YPFSU/\n"
        expected = "I AM FINE TODAY.\n"
        actual = _run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_generic_line(self):
        input_data = "YHOO\n"
        expected = _reference_decode(input_data)
        actual = _run_solution(input_data)
        self.assertEqual(actual, expected)

    def test_with_spaces_and_symbols(self):
        input_data = "Jr;;p Ept;f\n"
        expected = _reference_decode(input_data)
        actual = _run_solution(input_data)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
