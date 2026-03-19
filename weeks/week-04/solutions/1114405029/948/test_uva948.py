import unittest
from uva948 import solve


class TestUVA948(unittest.TestCase):
    """
    UVA 948 單元測試

    測試重點：
    1. 可以唯一找出假幣
    2. 無法唯一判定時要輸出 0
    3. 多組測資輸出時，中間要有空白行
    """

    def test_unique_fake_coin(self):
        """
        測試情境：
        第一次秤重：1 與 2 比，結果左輕，代表：
        - 1 可能偏輕
        - 2 可能偏重

        第二次秤重：2 與 3 比，結果相等，
        代表 2 和 3 都是真幣。

        因此唯一假幣只能是 1。
        """
        data = """1

4 2
1 1 2
<
1 2 3
=
"""
        expected = "1"
        self.assertEqual(solve(data), expected)

    def test_no_unique_answer(self):
        """
        測試情境：
        只有一次秤重，1 與 2 平衡，
        表示 1、2 都是真幣，但 3、4 都沒上秤，
        因此無法唯一判定哪顆是假幣，答案應為 0。
        """
        data = """1

4 1
1 1 2
=
"""
        expected = "0"
        self.assertEqual(solve(data), expected)

    def test_multiple_cases_with_blank_line_output(self):
        """
        測試多組測資：
        第一組答案為 1
        第二組答案為 0

        題目要求不同測資輸出之間需空一行，
        所以預期輸出要是：
        1

        0
        """
        data = """2

4 2
1 1 2
<
1 2 3
=

4 1
1 1 2
=
"""
        expected = "1\n\n0"
        self.assertEqual(solve(data), expected)


if __name__ == "__main__":
    unittest.main()