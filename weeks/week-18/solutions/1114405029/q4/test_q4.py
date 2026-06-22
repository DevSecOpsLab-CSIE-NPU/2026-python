import os
import sys
import tempfile
import unittest
import importlib.util

MODULE_PATH = os.path.join(os.path.dirname(__file__), "q4.py")
SPEC = importlib.util.spec_from_file_location("q4_solution", MODULE_PATH)
q4_solution = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(q4_solution)

benchmark_searches = q4_solution.benchmark_searches
binary_search = q4_solution.binary_search
create_radar_chart = q4_solution.create_radar_chart
linear_search = q4_solution.linear_search
normalize_metrics = q4_solution.normalize_metrics
solve = q4_solution.solve


class TestQ4SearchPerformance(unittest.TestCase):
    def test_found_target(self):
        arr = list(range(1, 201))
        found, idx, cmp_count = linear_search(arr, 129)
        self.assertTrue(found)
        self.assertEqual(idx, 128)
        self.assertEqual(cmp_count, 129)

        found, idx, cmp_count = binary_search(arr, 129)
        self.assertTrue(found)
        self.assertEqual(idx, 128)
        self.assertLessEqual(cmp_count, 8)

    def test_not_found_target(self):
        arr = [2, 4, 6, 8]
        self.assertEqual(linear_search(arr, 5), (False, -1, 4))
        found, idx, cmp_count = binary_search(arr, 5)
        self.assertFalse(found)
        self.assertEqual(idx, -1)
        self.assertLessEqual(cmp_count, 3)

    def test_empty_array(self):
        self.assertEqual(linear_search([], 129), (False, -1, 0))
        self.assertEqual(binary_search([], 129), (False, -1, 0))

    def test_single_element(self):
        self.assertEqual(linear_search([129], 129), (True, 0, 1))
        self.assertEqual(binary_search([129], 129), (True, 0, 1))

    def test_edge_first_and_last_positions(self):
        arr = list(range(10, 20))
        self.assertEqual(linear_search(arr, 10), (True, 0, 1))
        self.assertEqual(linear_search(arr, 19), (True, 9, 10))
        self.assertTrue(binary_search(arr, 10)[0])
        self.assertTrue(binary_search(arr, 19)[0])

    def test_benchmark_and_normalized_metrics(self):
        arr = list(range(1, 201))
        result = benchmark_searches(arr, 129)
        self.assertIn("linear_time", result)
        self.assertIn("binary_time", result)
        self.assertEqual(result["linear"][1], 128)
        self.assertEqual(result["binary"][1], 128)

        metrics = normalize_metrics(129, 8)
        self.assertEqual(set(metrics), {"linear", "binary"})
        self.assertEqual(len(metrics["linear"]), 5)
        self.assertTrue(all(0 <= value <= 1 for values in metrics.values() for value in values))

    def test_create_radar_chart_file(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = os.path.join(tmp_dir, "radar.png")
            create_radar_chart(output_path)
            self.assertTrue(os.path.exists(output_path))
            self.assertGreater(os.path.getsize(output_path), 0)

    def test_solve_output_mentions_faster_strategy(self):
        output = solve("1 2 3 129 300", target=129)
        self.assertIn("linear: FOUND 3 cmp=4", output)
        self.assertIn("binary: FOUND 3 cmp=2", output)
        self.assertIn("binary:", output)
        self.assertRegex(output, r"=> (linear|binary) faster")


if __name__ == "__main__":
    unittest.main()
