"""
測試程式：UVA 12019 — Doom's Day Algorithm
用 subprocess 直接執行手打版 12019.py，驗證標準輸出是否正確

2012 年 Doomsday 日期（全為星期三）：
  Jan:4  Feb:29  Mar:7  Apr:4  May:9  Jun:6
  Jul:11 Aug:8   Sep:5  Oct:10 Nov:7  Dec:12
"""
import unittest
import subprocess
import sys
import os

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '12019.py')

# 2012 年各月 Doomsday 日期
DOOMSDAY = [4, 29, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]


def run(input_text):
    """執行手打版程式，傳入模擬標準輸入，回傳標準輸出（已去除首尾空白）"""
    result = subprocess.run(
        [sys.executable, SCRIPT],
        input=input_text,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


class TestDoomsDay(unittest.TestCase):

    def test_all_doomsday_dates_are_wednesday(self):
        """12 個月的 Doomsday 日期都應輸出 Wednesday"""
        inp = "12\n" + "\n".join(f"{m} {DOOMSDAY[m-1]}" for m in range(1, 13)) + "\n"
        expected = "\n".join(["Wednesday"] * 12)
        self.assertEqual(run(inp), expected)

    def test_jan1_sunday(self):
        """2012/1/1 = 星期日"""
        self.assertEqual(run("1\n1 1\n"), "Sunday")

    def test_jan4_wednesday(self):
        """2012/1/4 是 Doomsday → 星期三"""
        self.assertEqual(run("1\n1 4\n"), "Wednesday")

    def test_feb29_wednesday(self):
        """2012/2/29（閏年）是 Doomsday → 星期三"""
        self.assertEqual(run("1\n2 29\n"), "Wednesday")

    def test_mar7_wednesday(self):
        """2012/3/7 是 Doomsday → 星期三"""
        self.assertEqual(run("1\n3 7\n"), "Wednesday")

    def test_dec25_tuesday(self):
        """2012/12/25 = 星期二（Dec 12 是週三，+13 天）"""
        self.assertEqual(run("1\n12 25\n"), "Tuesday")

    def test_oct1_monday(self):
        """2012/10/1 = 星期一（Oct 10 是週三，-9 天）"""
        self.assertEqual(run("1\n10 1\n"), "Monday")

    def test_consecutive_seven_days(self):
        """3/5 到 3/11 連續七天應涵蓋完整一週"""
        inp = "7\n3 5\n3 6\n3 7\n3 8\n3 9\n3 10\n3 11\n"
        expected = "Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday"
        self.assertEqual(run(inp), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
