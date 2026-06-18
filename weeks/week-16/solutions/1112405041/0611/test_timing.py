import unittest
import time
from timing import timeit

class TestTiming(unittest.TestCase):
    def test_metadata_preservation(self):
        @timeit
        def my_func():
            """This is a docstring."""
            pass
        self.assertEqual(my_func.__name__, "my_func")
        self.assertEqual(my_func.__doc__, "This is a docstring.")

    def test_return_value_unchanged(self):
        @timeit
        def add(a, b):
            return a + b
        self.assertEqual(add(1, 2), 3)

    def test_elapsed_recording(self):
        @timeit
        def slow_func():
            time.sleep(0.1)
            return True
        
        slow_func()
        self.assertTrue(hasattr(slow_func, "last_elapsed"))
        self.assertTrue(hasattr(slow_func, "records"))
        self.assertGreaterEqual(slow_func.last_elapsed, 0.1)
        self.assertEqual(len(slow_func.records), 1)
        
        slow_func()
        self.assertEqual(len(slow_func.records), 2)

if __name__ == "__main__":
    unittest.main()

