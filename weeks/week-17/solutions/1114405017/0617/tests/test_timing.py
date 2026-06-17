import unittest
from timing import timeit  # Ensure to import the timeit decorator from timing.py


class TestTimeit(unittest.TestCase):
    def test_returns_original_result(self):
        @timeit(repeat=3)
        def sample_function():
            return 42
        
        result = sample_function()
        self.assertEqual(result, 42)

    def test_preserves_function_metadata(self):
        @timeit(repeat=3)
        def sample_function():
            """This is a sample function."""
            return 42
        
        self.assertEqual(sample_function.__name__, 'sample_function')
        self.assertEqual(sample_function.__doc__, "This is a sample function.")

    def test_records_each_repeat_and_average(self):
        @timeit(repeat=5)
        def sample_function():
            return sum(range(1000))
        
        self.assertEqual(len(sample_function.records), 5)
        self.assertIsInstance(sample_function.last_elapsed, float)

    def test_rejects_invalid_repeat(self):
        with self.assertRaises(ValueError):
            @timeit(repeat=0)
            def sample_function():
                return 42
            
            sample_function()  # This should raise ValueError


if __name__ == "__main__":
    unittest.main()