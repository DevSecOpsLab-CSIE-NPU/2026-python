# -*- coding: utf-8 -*-
"""
針對 `solution_1114405006_12019.py` 的 unit tests（使用 unittest）

測試重點：
- 題目範例
- 2012 年 doomsday 日期是否皆為 Wednesday
- 不同月份的偏移是否正確
- main() 的輸入輸出格式

所有註解皆為繁體中文。
"""
import io
import sys
import unittest

from solution_1114405006_12019 import weekday_2012, main


class TestDoomsday2012(unittest.TestCase):
    def test_sample_io(self):
        # 題目範例：檢查輸入輸出是否符合預期
        sample_input = """
3
3 7
1 10
12 25
"""
        expected_output = "Wednesday\nTuesday\nTuesday\n"
        orig_stdin = sys.stdin
        orig_stdout = sys.stdout
        try:
            sys.stdin = io.StringIO(sample_input.strip() + "\n")
            sys.stdout = io.StringIO()
            main()
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output.strip())
        finally:
            sys.stdin = orig_stdin
            sys.stdout = orig_stdout

    def test_day_offsets(self):
        # 檢查幾個固定日期：前一天、當天、後一天
        self.assertEqual(weekday_2012(3, 6), "Tuesday")
        self.assertEqual(weekday_2012(3, 7), "Wednesday")
        self.assertEqual(weekday_2012(3, 8), "Thursday")

    def test_various_months(self):
        # 不同月份的代表性日期，避免只測到單一月份
        self.assertEqual(weekday_2012(1, 1), "Sunday")
        self.assertEqual(weekday_2012(4, 4), "Wednesday")
        self.assertEqual(weekday_2012(10, 31), "Wednesday")


if __name__ == '__main__':
    unittest.main()
