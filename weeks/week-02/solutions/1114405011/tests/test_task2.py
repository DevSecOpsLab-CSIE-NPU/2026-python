import pathlib
import sys
import unittest

p = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(p.parent.parent))

from task2_student_ranking import format_output, parse_input, rank_students


class MyTask2Test(unittest.TestCase):
    def test_case1_sample(self):
        lines = [
            "6 3",
            "amy 88 20",
            "bob 88 19",
            "zoe 92 21",
            "ian 88 19",
            "leo 75 20",
            "eva 92 20",
        ]
        arr, k = parse_input(lines)
        ans = rank_students(arr, k)
        self.assertEqual(ans, [("eva", 92, 20), ("zoe", 92, 21), ("bob", 88, 19)])

    def test_case2_tie(self):
        arr = [
            ("amy", 90, 20),
            ("zoe", 90, 19),
            ("bob", 90, 19),
            ("ian", 90, 21),
        ]
        ans = rank_students(arr, 4)
        self.assertEqual(ans, [("bob", 90, 19), ("zoe", 90, 19), ("amy", 90, 20), ("ian", 90, 21)])

    def test_case3_k_big(self):
        arr = [("amy", 80, 20), ("bob", 70, 21)]
        ans = rank_students(arr, 10)
        self.assertEqual(ans, [("amy", 80, 20), ("bob", 70, 21)])

    def test_case4_text(self):
        s = format_output([("eva", 92, 20), ("zoe", 92, 21)])
        self.assertTrue("eva 92 20" in s)


if __name__ == "__main__":
    unittest.main()
