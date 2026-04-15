import os
import re
import subprocess
import sys
import unittest
from pathlib import Path


# ============================================================
# 10190 好記版：
# - 這題原始敘述較複雜，先用「一定成立的邊界條件」做測試
# - 例如 T=0 或 V=0，答案一定是 0
# ============================================================


def find_target_script() -> Path:
    """找 10190 解答檔，找不到就跳過。"""
    custom_path = os.environ.get("TARGET_10190")
    if custom_path:
        p = Path(custom_path)
        if p.exists():
            return p

    folder = Path(__file__).resolve().parent
    names = [
        "QUESTION-10190-手打.py",
        "QUESTION-10190.py",
        "question_10190.py",
        "uva10190.py",
        "10190.py",
        "solution_10190.py",
    ]
    for name in names:
        p = folder / name
        if p.exists():
            return p

    raise unittest.SkipTest("找不到 10190 解答檔，請放同資料夾或設定 TARGET_10190")


def run_program(input_text: str) -> str:
    """執行程式並回傳輸出字串。"""
    script = find_target_script()
    result = subprocess.run(
        [sys.executable, str(script)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout.strip()


def pick_first_number(text: str) -> float:
    """從輸出抓第一個數字（整數或小數）。"""
    m = re.search(r"[-+]?\d+(?:\.\d+)?", text)
    if not m:
        raise AssertionError(f"輸出沒有可解析數字: {text!r}")
    return float(m.group(0))


class Test10190Easy(unittest.TestCase):
    """UVA 10190（自動傘）好記版測試。"""

    def test_when_time_is_zero(self):
        # 規則：T=0 代表沒有經過時間，累積雨量必為 0。
        input_text = (
            "2 10 0 7\n"
            "0 5 1\n"
            "2 3 -1\n"
        )
        output = run_program(input_text)
        value = pick_first_number(output)
        self.assertAlmostEqual(value, 0.0, places=2)

    def test_when_rain_rate_is_zero(self):
        # 規則：V=0 代表根本沒下雨，結果也一定是 0。
        input_text = (
            "1 8 100 0\n"
            "1 4 2\n"
        )
        output = run_program(input_text)
        value = pick_first_number(output)
        self.assertAlmostEqual(value, 0.0, places=2)

    def test_output_format_contains_two_decimals(self):
        # 題目要求輸出到小數點後兩位，因此至少應含有 x.xx 形式。
        input_text = "0 10 10 3\n"
        output = run_program(input_text)
        _ = pick_first_number(output)
        self.assertRegex(output, r"\d+\.\d{2}")


if __name__ == "__main__":
    unittest.main()
