import os
import re
import subprocess
import sys
import unittest
from pathlib import Path


def _find_solution_script() -> Path:
    """尋找 10190 解答程式位置；可由環境變數覆寫。"""
    custom = os.environ.get("TARGET_10190")
    if custom:
        p = Path(custom)
        if p.exists():
            return p

    base = Path(__file__).resolve().parent
    candidates = [
        "QUESTION-10190-手打.py",
        "QUESTION-10190.py",
        "question_10190.py",
        "uva10190.py",
        "10190.py",
        "solution_10190.py",
    ]
    for name in candidates:
        p = base / name
        if p.exists():
            return p

    raise unittest.SkipTest("找不到 10190 解答程式，請先放入同資料夾或設定 TARGET_10190")


def _run_solution(input_data: str) -> str:
    script = _find_solution_script()
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    return proc.stdout.strip()


def _parse_single_float(text: str) -> float:
    # 允許答案僅輸出一個數字（可含小數）。
    match = re.search(r"[-+]?\d+(?:\.\d+)?", text)
    if not match:
        raise AssertionError(f"輸出中找不到數值: {text!r}")
    return float(match.group(0))


class TestQuestion10190(unittest.TestCase):
    """10190（自動傘）基本邊界情境測試。"""

    def test_zero_time_should_be_zero_volume(self):
        # T=0 時不論其他參數為何，累積雨量都應為 0。
        input_data = (
            "2 10 0 7\n"
            "0 5 1\n"
            "2 3 -1\n"
        )
        actual = _parse_single_float(_run_solution(input_data))
        self.assertAlmostEqual(actual, 0.0, places=2)

    def test_zero_rain_rate_should_be_zero_volume(self):
        # V=0 時沒有降雨，最終體積必為 0。
        input_data = (
            "1 8 100 0\n"
            "1 4 2\n"
        )
        actual = _parse_single_float(_run_solution(input_data))
        self.assertAlmostEqual(actual, 0.0, places=2)

    def test_output_has_two_decimals_style(self):
        # 檢查常見格式：至少有可解析數值，且建議有兩位小數。
        input_data = "0 10 10 3\n"
        raw = _run_solution(input_data)
        _ = _parse_single_float(raw)
        self.assertRegex(raw, r"\d+\.\d{2}")


if __name__ == "__main__":
    unittest.main()
