"""
第四題測試：二分搜尋效能

本題參數：
- 陣列大小至少 10^5
- 搜尋目標 K = 123
- 比較 linear search 與 binary search 的比較次數與搜尋時間
"""

import unittest

from p4_binary_search_perf import (
    DATA_SIZE,
    K,
    make_test_data,
    linear_search_with_count,
    binary_search_with_count,
    benchmark_search,
)


class TestBinarySearchPerformance(unittest.TestCase):
    def test_data_size_should_be_at_least_100000(self):
        """效能測試陣列長度至少要 10^5。"""
        self.assertGreaterEqual(DATA_SIZE, 100000)

    def test_make_test_data_should_be_sorted_and_contain_target(self):
        """測試資料要已排序，且包含 K = 123。"""
        data = make_test_data()

        self.assertGreaterEqual(len(data), 100000)
        self.assertIn(K, data)
        self.assertEqual(data, sorted(data))

    def test_linear_search_found_should_return_index_and_comparisons(self):
        """linear search 找到目標時，要回傳 index 與比較次數。"""
        data = [0, 0, 123]

        index, comparisons = linear_search_with_count(data, K)

        self.assertEqual(index, 2)
        self.assertEqual(comparisons, 3)

    def test_linear_search_not_found_should_return_minus_one(self):
        """linear search 找不到目標時，要回傳 -1 與比較次數。"""
        data = [0, 0, 0]

        index, comparisons = linear_search_with_count(data, K)

        self.assertEqual(index, -1)
        self.assertEqual(comparisons, 3)

    def test_binary_search_found_should_return_index_and_comparisons(self):
        """binary search 找到目標時，要回傳 index 與比較次數。"""
        data = [0, 0, 0, 123]

        index, comparisons = binary_search_with_count(data, K)

        self.assertEqual(index, 3)
        self.assertGreaterEqual(comparisons, 1)

    def test_binary_search_not_found_should_return_minus_one(self):
        """binary search 找不到目標時，要回傳 -1 與比較次數。"""
        data = [0, 0, 0, 0]

        index, comparisons = binary_search_with_count(data, K)

        self.assertEqual(index, -1)
        self.assertGreaterEqual(comparisons, 1)

    def test_binary_search_empty_list_should_return_minus_one(self):
        """空 list 搜尋不到資料，應回傳 -1。"""
        index, comparisons = binary_search_with_count([], K)

        self.assertEqual(index, -1)
        self.assertEqual(comparisons, 0)

    def test_binary_search_unsorted_data_should_return_minus_one(self):
        """未排序資料不 raise error，依本次規格回傳 -1。"""
        data = [123, 0, 5]

        index, comparisons = binary_search_with_count(data, K)

        self.assertEqual(index, -1)
        self.assertGreaterEqual(comparisons, 0)

    def test_binary_search_duplicate_target_can_return_any_matching_index(self):
        """如果有兩個相同的目標值，找到任一個正確 index 即可。"""
        data = [0, 0, 123, 123, 200]

        index, comparisons = binary_search_with_count(data, K)

        self.assertIn(index, [2, 3])
        self.assertEqual(data[index], K)
        self.assertGreaterEqual(comparisons, 1)

    def test_search_functions_should_not_modify_original_data(self):
        """兩種搜尋都不可以修改原始資料。"""
        data = [0, 0, 123]
        original = data.copy()

        linear_search_with_count(data, K)
        binary_search_with_count(data, K)

        self.assertEqual(data, original)

    def test_benchmark_should_return_times_and_comparisons(self):
        """benchmark 要回傳兩種搜尋法的時間與比較次數。"""
        data = make_test_data()

        result = benchmark_search(data, K, repeat=3)

        self.assertIn("linear_index", result)
        self.assertIn("linear_comparisons", result)
        self.assertIn("linear_time", result)
        self.assertIn("binary_index", result)
        self.assertIn("binary_comparisons", result)
        self.assertIn("binary_time", result)

        self.assertIsInstance(result["linear_time"], float)
        self.assertIsInstance(result["binary_time"], float)
        self.assertGreaterEqual(result["linear_time"], 0)
        self.assertGreaterEqual(result["binary_time"], 0)

        self.assertGreaterEqual(result["linear_comparisons"], 1)
        self.assertGreaterEqual(result["binary_comparisons"], 1)


if __name__ == "__main__":
    unittest.main()