import math
import os
import subprocess
import sys
import unittest
from pathlib import Path


def _find_solution_script() -> Path:
    """尋找 10221 解答程式位置；可由環境變數覆寫。"""
    custom = os.environ.get("TARGET_10221")
    if custom:
        p = Path(custom)
        if p.exists():
            return p

    base = Path(__file__).resolve().parent
    candidates = [
        "QUESTION-10221-手打.py",
        "QUESTION-10221.py",
        "question_10221.py",
        "uva10221.py",
        "10221.py",
        "solution_10221.py",
    ]
    for name in candidates:
        p = base / name
        if p.exists():
            return p

    raise unittest.SkipTest("找不到 10221 解答程式，請先放入同資料夾或設定 TARGET_10221")


def _run_solution(input_data: str):
    script = _find_solution_script()
    proc = subprocess.run(
        [sys.executable, str(script)],
        input=input_data,
        text=True,
        capture_output=True,
        check=True,
    )
    lines = [line.strip() for line in proc.stdout.strip().splitlines() if line.strip()]
    result = []
    for line in lines:
        a_str, c_str = line.split()
        result.append((float(a_str), float(c_str)))
    return result


def _reference(s: int, a: int, unit: str):
    # 題目要求取較小圓心角，避免走超過半圈的弧。
    if unit == "min":
        angle_deg = a / 60.0
    else:
        angle_deg = float(a)
    if angle_deg > 180.0:
        angle_deg = 360.0 - angle_deg

    r = 6440.0 + s
    rad = math.radians(angle_deg)
    arc = r * rad
    chord = 2.0 * r * math.sin(rad / 2.0)
    return arc, chord


class TestQuestion10221(unittest.TestCase):
    """UVA 10221 Satellites 測試。"""

    def test_sample_like_cases(self):
        input_data = (
            "500 30 deg\n"
            "700 60 min\n"
            "200 45 deg\n"
        )
        actual = _run_solution(input_data)
        expected = [
            _reference(500, 30, "deg"),
            _reference(700, 60, "min"),
            _reference(200, 45, "deg"),
        ]
        self.assertEqual(len(actual), len(expected))
        for (a1, c1), (a2, c2) in zip(actual, expected):
            self.assertAlmostEqual(a1, a2, places=6)
            self.assertAlmostEqual(c1, c2, places=6)

    def test_angle_over_180_should_flip(self):
        input_data = "0 270 deg\n"
        actual = _run_solution(input_data)
        self.assertEqual(len(actual), 1)
        arc, chord = actual[0]
        exp_arc, exp_chord = _reference(0, 270, "deg")
        self.assertAlmostEqual(arc, exp_arc, places=6)
        self.assertAlmostEqual(chord, exp_chord, places=6)

    def test_zero_angle(self):
        input_data = "1000 0 deg\n"
        actual = _run_solution(input_data)
        self.assertEqual(len(actual), 1)
        arc, chord = actual[0]
        self.assertAlmostEqual(arc, 0.0, places=6)
        self.assertAlmostEqual(chord, 0.0, places=6)


if __name__ == "__main__":
    unittest.main()
