import inspect
import unittest

import sorts


class TestSortsExtra(unittest.TestCase):
    def test_functions_exist_and_signature(self):
        for name in ('bubble_sort', 'quick_sort', 'merge_sort'):
            with self.subTest(name=name):
                func = getattr(sorts, name, None)
                self.assertIsNotNone(func)
                self.assertTrue(callable(func))
                # Expect single positional argument `data`
                self.assertEqual(func.__code__.co_argcount, 1)

    def test_input_not_modified_multiple_cases(self):
        cases = [[], [1], [2, 1], [3, 1, 2], [5, -1, 5, 0]]
        for name in ('bubble_sort', 'quick_sort', 'merge_sort'):
            f = getattr(sorts, name)
            for case in cases:
                with self.subTest(func=name, case=case):
                    original = list(case)
                    res = f(list(case))
                    self.assertEqual(case, original)  # input preserved
                    self.assertEqual(res, sorted(original))

    def test_no_sorted_or_list_sort_in_source(self):
        src = inspect.getsource(sorts)
        self.assertNotIn('sorted(', src)
        self.assertNotIn('.sort(', src)


if __name__ == '__main__':
    unittest.main()
