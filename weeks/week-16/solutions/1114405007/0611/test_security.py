import os
import unittest

from benchmark import make_data, run_benchmark


class TestSecurity(unittest.TestCase):
    def test_make_data_rejects_negative_n(self):
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_run_benchmark_rejects_invalid_repeats(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(10,), repeats=0)

    def test_run_benchmark_rejects_non_positive_sizes_edge_case(self):
        with self.assertRaises(ValueError):
            run_benchmark(sizes=(10, 0, -3), repeats=1)

    def test_source_has_no_eval_or_exec(self):
        for filename in ["timing.py", "sorts.py", "benchmark.py", "plot.py"]:
            with self.subTest(file=filename):
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                self.assertNotIn("eval(", content)
                self.assertNotIn("exec(", content)


if __name__ == "__main__":
    unittest.main()
