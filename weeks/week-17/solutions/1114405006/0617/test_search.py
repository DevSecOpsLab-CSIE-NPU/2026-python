"""0617 任务二 — search 搜索评估

规格:search.py 包含
  1. linear_search(data: list, target) -> int
     - 逐一比对,回传 index,找不到回 -1
     - 不可修改传入的 data
  2. binary_search(data: list, target) -> int
     - 前提:data 已排序;回传 index 或 -1
     - 收到未排序 data 时自行排序
     - 不可修改传入的 data
  3. 使用 timeit 进行性能评估
  4. 将评估结果写入 README.md

评估重点:
  - 比较线性搜索和二分搜索的执行时间
  - 评估不同大小的数据集（100、1000、10000个元素）
  - 评估排序是否值得（比较排序后二分搜索的时间）
"""

import time
import bisect
from unittest import TestCase

from timing import timeit
from search import linear_search, binary_search, SearchError


class TestSearch(TestCase):
    """search.py 的测试套件"""
    
    def test_linear_search_basic(self):
        """测试线性搜索基本功能"""
        result = linear_search([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, 2)

    def test_linear_search_not_found(self):
        """测试线性搜索未找到的情况"""
        result = linear_search([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, -1)

    def test_binary_search_basic(self):
        """测试二分搜索基本功能（已排序 data）"""
        result = binary_search([1, 2, 3, 4, 5], 4)
        self.assertEqual(result, 3)

    def test_binary_search_not_found(self):
        """测试二分搜索未找到的情况"""
        result = binary_search([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, -1)

    def test_linear_search_duplicate_elements_first_match(self):
        """测试线性搜索重复元素时返回第一个匹配项"""
        result = linear_search([1, 2, 2, 3, 4], 2)
        self.assertEqual(result, 1)

    def test_binary_search_duplicate_elements_first_match(self):
        """测试二分搜索重复元素时返回第一个匹配项"""
        result = binary_search([1, 2, 2, 3, 4], 2)
        self.assertEqual(result, 1)

    def test_binary_search_unsorted_data_auto_sort(self):
        """测试二分搜索收到未排序 data 时自动排序"""
        result = binary_search([5, 2, 8, 1, 9], 8)
        self.assertEqual(result, 3)

    def test_search_empty_data_linear(self):
        """测试线性搜索空 data 时抛出 SearchError 异常"""
        with self.assertRaises(SearchError):
            linear_search([], 1)

    def test_search_empty_data_binary(self):
        """测试二分搜索空 data 时抛出 SearchError 异常"""
        with self.assertRaises(SearchError):
            binary_search([], 1)

    def test_search_data_not_modified_linear(self):
        """测试线性搜索不会修改原始 data"""
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        linear_search(data, 4)
        self.assertEqual(data, [3, 1, 4, 1, 5, 9, 2, 6])

    def test_search_data_not_modified_binary(self):
        """测试二分搜索不会修改原始 data"""
        data = [3, 1, 4, 1, 5, 9, 2, 6]
        binary_search(data, 4)
        self.assertEqual(data, [3, 1, 4, 1, 5, 9, 2, 6])

    def test_search_large_data_set(self):
        """测试大数据集搜索性能"""
        data = list(range(10000))
        target = 5000
        result = linear_search(data, target)
        self.assertEqual(result, 5000)

    def test_search_performance_comparison(self):
        """性能比较测试"""
        # 测试不同大小的数据集
        test_data_100 = list(range(100))
        test_data_1000 = list(range(1000))
        test_data_10000 = list(range(10000))
        target = 50

        # 测试线性搜索
        linear_result_100 = linear_search(test_data_100, target)
        linear_result_1000 = linear_search(test_data_1000, target)
        linear_result_10000 = linear_search(test_data_10000, target)

        self.assertEqual(linear_result_100, 50)
        self.assertEqual(linear_result_1000, 50)
        self.assertEqual(linear_result_10000, 50)

        # 测试二分搜索
        binary_result_100 = binary_search(test_data_100, target)
        binary_result_1000 = binary_search(test_data_1000, target)
        binary_result_10000 = binary_search(test_data_10000, target)

        self.assertEqual(binary_result_100, 50)
        self.assertEqual(binary_result_1000, 50)
        self.assertEqual(binary_result_10000, 50)

    def test_binary_search_with_unsorted_target(self):
        """测试二分搜索搜索未排序列表中的目标"""
        data = [5, 3, 1, 4, 2]
        target = 4
        result = binary_search(data, target)
        self.assertEqual(result, 3)

    def test_linear_search_edge_cases(self):
        """测试线性搜索边界情况"""
        # 单个元素列表
        self.assertEqual(linear_search([42], 42), 0)
        self.assertEqual(linear_search([42], 43), -1)

        # 目标在列表开头
        self.assertEqual(linear_search([1, 2, 3], 1), 0)

        # 目标在列表结尾
        self.assertEqual(linear_search([1, 2, 3], 3), 2)

        # 目标不在列表中
        self.assertEqual(linear_search([1, 2, 3], 5), -1)

    def test_binary_search_edge_cases(self):
        """测试二分搜索边界情况"""
        # 单个元素列表
        self.assertEqual(binary_search([42], 42), 0)
        self.assertEqual(binary_search([42], 43), -1)

        # 目标在列表开头
        self.assertEqual(binary_search([1, 2, 3], 1), 0)

        # 目标在列表结尾
        self.assertEqual(binary_search([1, 2, 3], 3), 2)

        # 目标不在列表中
        self.assertEqual(binary_search([1, 2, 3], 5), -1)

    def test_search_timeit_integration(self):
        """测试 timeit 装饰器集成"""
        # 测试 linear_search
        result = linear_search([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, 2)
        self.assertIsNotNone(linear_search.f)
        self.assertIsInstance(linear_search.f.records, list)
        self.assertIsInstance(linear_search.f.last_elapsed, float)

        # 测试 binary_search
        result = binary_search([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, 2)
        self.assertIsNotNone(binary_search.f)
        self.assertIsInstance(binary_search.f.records, list)
        self.assertIsInstance(binary_search.f.last_elapsed, float)


if __name__ == "__main__":
    import unittest
    unittest.main()