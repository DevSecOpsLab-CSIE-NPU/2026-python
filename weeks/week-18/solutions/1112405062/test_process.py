import unittest
from process import process


class TestProcess(unittest.TestCase):

    def test_basic_flow(self):
        self.assertEqual(process([1, 4, 4, 8, 3], 4), [4, 8])

    def test_all_filtered_out(self):
        self.assertEqual(process([1, 2, 3], 4), [])

    def test_all_duplicates(self):
        self.assertEqual(process([4, 4, 4, 4], 4), [4])

    def test_negative_numbers(self):
        self.assertEqual(process([-4, 4, -8, 8], 4), [-8, -4, 4, 8])

    def test_empty_input(self):
        self.assertEqual(process([], 4), [])

    def test_single_element(self):
        self.assertEqual(process([4], 4), [4])


if __name__ == '__main__':
    unittest.main()
