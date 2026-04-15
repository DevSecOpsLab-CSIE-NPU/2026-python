import math
import os
import subprocess
import sys
import unittest
from pathlib import Path


# ============================================================
# 10221 好記版口訣：
# 1) 半徑 r = 6440 + s
# 2) 角度先轉成度，再轉弧度
# 3) 若角度 > 180，改用 360 - 角度
# 4) 弧長 = r * rad
# 5) 弦長 = 2 * r * sin(rad/2)
# ============================================================


def find_target_script() -> Path:
    """找 10221 解答檔，找不到就跳過。"""
    custom_path = os.environ.get("TARGET_10221")
    if custom_path:
        p = Path(custom_path)
        if p.exists():
            return p

    folder = Path(__file__).resolve().parent
    names = [
        "QUESTION-10221-手打.py",
        "QUESTION-10221.py",
        "question_10221.py",
        "uva10221.py",
        "10221.py",
        "solution_10221.py",
    ]
    for name in names:
        p = folder / name
        if p.exists():
            return p

    raise unittest.SkipTest("找不到 10221 解答檔，請放同資料夾或設定 TARGET_10221")


def run_program(input_text: str):
    """執行程式並解析每行的弧長、弦長。"""
    script = find_target_script()
    result = subprocess.run(
        [sys.executable, str(script)],
        input=input_text,
        text=True,
        capture_output=True,
        check=True,
    )

    pairs = []
    for line in result.stdout.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        arc_str, chord_str = line.split()
        pairs.append((float(arc_str), float(chord_str)))
    return pairs


def expected_values(s: int, a: int, unit: str):
    """用題目公式算預期答案。"""
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


class Test10221Easy(unittest.TestCase):
    """UVA 10221（Satellites）好記版測試。"""

    def test_three_common_cases(self):
        input_text = (
            "500 30 deg\n"
            "700 60 min\n"
            "200 45 deg\n"
        )
        actual = run_program(input_text)
        expected = [
            expected_values(500, 30, "deg"),
            expected_values(700, 60, "min"),
            expected_values(200, 45, "deg"),
        ]

        self.assertEqual(len(actual), len(expected))
        for (a1, c1), (a2, c2) in zip(actual, expected):
            self.assertAlmostEqual(a1, a2, places=6)
            self.assertAlmostEqual(c1, c2, places=6)

    def test_angle_larger_than_180(self):
        # 270 度應該視為較短路徑的 90 度。
        actual = run_program("0 270 deg\n")
        exp_arc, exp_chord = expected_values(0, 270, "deg")
        self.assertEqual(len(actual), 1)
        self.assertAlmostEqual(actual[0][0], exp_arc, places=6)
        self.assertAlmostEqual(actual[0][1], exp_chord, places=6)

    def test_zero_angle(self):
        # 角度 0 時，弧長與弦長都應該是 0。
        actual = run_program("1000 0 deg\n")
        self.assertEqual(len(actual), 1)
        self.assertAlmostEqual(actual[0][0], 0.0, places=6)
        self.assertAlmostEqual(actual[0][1], 0.0, places=6)


if __name__ == "__main__":
    unittest.main()
