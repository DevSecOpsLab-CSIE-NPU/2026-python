"""
Unit tests for UVA 12019 — Doom's Day Algorithm

這個檔案包含：
- `weekday_name(m, d)`：把 2012 年的月份與日期轉成星期英文全名。
- `solve_from_string(s)`：模擬題目的輸入輸出，方便做 I/O 測試。

因為題目限定在 2012 年，所以可以直接用標準庫 datetime 當參考答案。
"""

import datetime
import unittest


WEEKDAY_NAMES = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def weekday_name(m: int, d: int) -> str:
    """回傳 2012 年 m/d 對應的星期幾。"""
    date = datetime.date(2012, m, d)
    return WEEKDAY_NAMES[date.weekday()]


def solve_from_string(s: str) -> str:
    """把完整輸入字串轉成題目輸出格式。"""
    lines = [line.strip() for line in s.strip().splitlines() if line.strip()]
    if not lines:
        return ""

    t = int(lines[0])
    outputs = []
    for i in range(1, t + 1):
        m, d = map(int, lines[i].split())
        outputs.append(weekday_name(m, d))
    return "\n".join(outputs) + ("\n" if outputs else "")


class TestDoomsDay12019(unittest.TestCase):
    """針對 12019 的範例與代表性日期做測試。"""

    def test_sample_like_cases(self):
        """題目敘述中的典型日期組合。"""
        inp = """
        5
        1 10
        2 21
        3 7
        12 12
        12 31
        """
        expected = "Tuesday\nTuesday\nWednesday\nWednesday\nMonday\n"
        self.assertEqual(solve_from_string(inp), expected)

    def test_january_first(self):
        """2012/1/1 是 Sunday。"""
        self.assertEqual(weekday_name(1, 1), "Sunday")

    def test_leap_day(self):
        """2012 是閏年，2/29 必須能正確處理。"""
        self.assertEqual(weekday_name(2, 29), "Wednesday")

    def test_year_end(self):
        """年末日期的檢查。"""
        self.assertEqual(weekday_name(12, 31), "Monday")

    def test_empty_input(self):
        """空輸入時回傳空字串。"""
        self.assertEqual(solve_from_string(""), "")


if __name__ == "__main__":
    # 直接執行此檔時，會跑所有 unittest。
    unittest.main()
