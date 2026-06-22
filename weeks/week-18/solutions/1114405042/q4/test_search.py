#!/usr/bin/env python3
"""測試腳本，驗證第四題實現的功能

本腳本測試主要功能：
1. timeit 裝飾器的正確性
2. 三種搜索算法的正確性
3. 時間度量的一致性
4. binary_search 接收未排序數據的行為
"""

import unittest
from timing import timeit
from search import linear_search, binary_search, set_search


class TestTimeit(unittest.TestCase):
    """timeit 裝飾器的單元測試"""

    def test_timeit_basic(self):
        """測試 timeit 的基本功能"""
        @timeit
        def add(a, b):
            return a + b

        result = add(5, 3)
        self.assertEqual(result, 8)
        self.assertIsNotNone(add.last_elapsed)
        self.assertIsInstance(add.last_elapsed, (int, float))
        self.assertTrue(len(add.records) > 0)

    def test_timeit_repeat(self):
        """測試 timeit 的 repeat 參數"""
        @timeit(repeat=5)
        def slow_func(n):
            total = 0
            for i in range(n):
                total += i
            return total

        result = slow_func(1000)
        self.assertEqual(result, 499500)
        self.assertIsNotNone(slow_func.last_elapsed)
        self.assertEqual(len(slow_func.records), 5)

    def test_timeit_return_value(self):
        """測試 timeit 保留回傳值"""
        @timeit
        def func_with_side_effect():
            return {"key": "value"}

        result = func_with_side_effect()
        self.assertEqual(result, {"key": "value"})

    def test_timeit_records_preserved(self):
        """测试 records 在多次呼叫时更新"""
        @timeit
        def simple_func():
            return 42

        result1 = simple_func()
        self.assertEqual(result1, 42)
        records1 = simple_func.records.copy()
        result2 = simple_func()
        self.assertEqual(result2, 42)
        records2 = simple_func.records
        # 记录应该更新，而不是追加，所以长度应该相同
        self.assertEqual(len(records2), len(records1))

    def test_timeit_raise_error(self):
        """測試 repeat < 1 時 raise ValueError"""
        try:
            @timeit(repeat=0)
            def func():
                return 1
            func()
            self.fail("應該 raise ValueError")
        except ValueError:
            pass


class TestSearch(unittest.TestCase):
    """三種搜索算法的單元測試"""

    def setUp(self):
        """設定測試資料"""
        self.data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        self.target = 7
        self.non_existent = 10

    def test_linear_search_found(self):
        """測試 linear_search 找到目標"""
        result = linear_search(self.data, self.target)
        self.assertEqual(result, 3)

    def test_linear_search_not_found(self):
        """測試 linear_search 未找到目標"""
        result = linear_search(self.data, self.non_existent)
        self.assertEqual(result, -1)

    def test_binary_search_found(self):
        """測試 binary_search 找到目標（數據已排序）"""
        result = binary_search(self.data, self.target)
        self.assertEqual(result, 3)

    def test_binary_search_not_found(self):
        """測試 binary_search 未找到目標"""
        result = binary_search(self.data, self.non_existent)
        self.assertEqual(result, -1)

    def test_binary_search_unsorted(self):
        """測試 binary_search 收到未排序數據的行為"""
        unsorted_data = [19, 3, 15, 7, 1, 9, 5, 11, 13, 17]
        result = binary_search(unsorted_data, 7)
        self.assertEqual(result, -2)

    def test_set_search_found(self):
        """測試 set_search 找到目標"""
        result = set_search(self.data, self.target)
        self.assertTrue(result)

    def test_set_search_not_found(self):
        """測試 set_search 未找到目標"""
        result = set_search(self.data, self.non_existent)
        self.assertFalse(result)

    def test_search_return_types(self):
        """測試三種搜索的回傳型別不一致"""
        linear_result = linear_search(self.data, self.target)
        binary_result = binary_search(self.data, self.target)
        set_result = set_search(self.data, self.target)

        self.assertIsInstance(linear_result, int)
        self.assertIsInstance(binary_result, int)
        self.assertIsInstance(set_result, bool)

    def test_search_data_immutable(self):
        """測試三種搜索不可修改輸入的 data"""
        data_copy = self.data.copy()
        linear_search(self.data, self.target)
        binary_search(self.data, self.target)
        set_search(self.data, self.target)
        self.assertEqual(self.data, data_copy)

    def test_binary_search_edge_cases(self):
        """測試 binary_search 的邊界情況"""
        # 空列表
        result = binary_search([], 5)
        self.assertEqual(result, -1)

        # 單元素找到
        result = binary_search([5], 5)
        self.assertEqual(result, 0)

        # 單元素未找到
        result = binary_search([5], 3)
        self.assertEqual(result, -1)

        # 重複元素
        data = [1, 2, 2, 2, 3, 4, 5]
        result = binary_search(data, 2)
        self.assertIn(result, [1, 2, 3])


class TestBenchmark(unittest.TestCase):
    """benchmark.py 的單元測試"""

    def test_make_data(self):
        """測試 make_data 函式"""
        from benchmark import make_data

        data = make_data(100)
        self.assertEqual(len(data), 100)
        self.assertTrue(all(0 <= x < 100 for x in data))

        # 測試負數邊界
        with self.assertRaises(ValueError):
            make_data(-1)

    def test_make_data_seed(self):
        """測試 make_data 使用固定 seed"""
        from benchmark import make_data

        data1 = make_data(10, seed=42)
        data2 = make_data(10, seed=42)
        self.assertEqual(data1, data2)

    def test_benchmark_structure(self):
        """測試 benchmark 的結構"""
        from benchmark import run_benchmark

        result = run_benchmark(sizes=(10,), queries=5)
        self.assertIn("data", result)
        self.assertIn("results", result)
        self.assertEqual(len(result["results"]), 1)
        self.assertEqual(result["results"][0]["n"], 10)

        # 測試每種算法都有記錄
        for algo in ["linear", "binary", "set"]:
            algo_result = result["results"][0][algo]
            self.assertIn("total_time", algo_result)
            self.assertIn("avg_time", algo_result)
            self.assertIn("records", algo_result)
            self.assertTrue(len(algo_result["records"]) > 0)


if __name__ == "__main__":
    unittest.main()