import unittest
from task2_student_ranking import student_ranking

class TestTask2StudentRanking(unittest.TestCase):
    def test_normal_sorting(self):
        data = [
            '6 3',
            'amy 88 20',
            'bob 88 19',
            'zoe 92 21',
            'ian 88 19',
            'leo 75 20',
            'eva 92 20',
        ]
        out = student_ranking(data)
        self.assertEqual(out, ['eva 92 20', 'zoe 92 21', 'bob 88 19'])

    def test_tie_break_age_name(self):
        data = [
            '4 4',
            'x 90 20',
            'a 90 19',
            'b 90 19',
            'c 90 20',
        ]
        out = student_ranking(data)
        self.assertEqual(out, ['a 90 19', 'b 90 19', 'c 90 20', 'x 90 20'])

    def test_empty_students(self):
        self.assertEqual(student_ranking([]), [])
