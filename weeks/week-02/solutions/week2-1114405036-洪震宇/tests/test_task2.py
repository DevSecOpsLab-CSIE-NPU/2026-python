import unittest

from task2_student_ranking import format_ranking, rank_students


class TestTask2StudentRanking(unittest.TestCase):
    def test_example_ranking(self):
        lines = [
            "amy 88 20",
            "bob 88 19",
            "zoe 92 21",
            "ian 88 19",
            "leo 75 20",
            "eva 92 20",
        ]
        ranking = rank_students(lines, k=3)
        self.assertEqual(ranking, [("eva", 92, 20), ("zoe", 92, 21), ("bob", 88, 19)])

    def test_tie_breaking_age_and_name(self):
        lines = [
            "alice 90 18",
            "aaron 90 17",
            "bob 90 17",
            "carol 90 18",
        ]
        ranking = rank_students(lines, k=4)
        # aaron and bob have same score and age, but aaron < bob
        self.assertEqual(ranking[0], ("aaron", 90, 17))
        self.assertEqual(ranking[1], ("bob", 90, 17))

    def test_k_out_of_range(self):
        lines = ["x 50 20"]
        ranking = rank_students(lines, k=0)
        self.assertEqual(ranking, [])
        ranking = rank_students(lines, k=10)
        self.assertEqual(ranking, [("x", 50, 20)])

    def test_format_ranking(self):
        out = format_ranking([("a", 1, 2), ("b", 2, 3)])
        expected = "a 1 2\nb 2 3"
        self.assertEqual(out, expected)


if __name__ == "__main__":
    unittest.main()
