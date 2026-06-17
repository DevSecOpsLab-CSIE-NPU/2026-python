"""0617 任務一 — timeit 裝飾器測試"""

import unittest
from timing import timeit


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit
        def add(a, b):
            return a + b

        result = add(3, 4)
        self.assertEqual(result, 7)

    def test_preserves_function_metadata(self):
        @timeit
        def hello():
            """Say hello"""
            return "hi"

        self.assertEqual(hello.__name__, "hello")
        self.assertEqual(hello.__doc__, "Say hello")

    def test_records_each_repeat_and_average(self):
        @timeit
        def f():
            return 42

        f()
        self.assertTrue(hasattr(f, "records"))
        self.assertEqual(len(f.records), 3)
        self.assertTrue(hasattr(f, "last_elapsed"))
        self.assertIsInstance(f.last_elapsed, float)

    def test_rejects_invalid_repeat(self):
        def dummy():
            pass

        for invalid in (0, -1, -5):
            with self.subTest(repeat=invalid):
                with self.assertRaises(ValueError):
                    timeit(dummy, repeat=invalid)

    def test_preserves_exception(self):
        class CustomError(Exception):
            pass

        @timeit
        def crash():
            raise CustomError("boom")

        with self.assertRaises(CustomError):
            crash()


if __name__ == "__main__":
    unittest.main()
