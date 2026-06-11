import random
import unittest

from sorts import bubble_sort, quick_sort, merge_sort

# Stage 3: 試圖引入加速版排序函式
try:
    from sorts import bubble_sort_fast, quick_sort_fast
    _FAST_SORTS_AVAILABLE = True
except (ImportError, AttributeError):
    _FAST_SORTS_AVAILABLE = False


SORT_FUNCTIONS = [
    bubble_sort,
    quick_sort,
    merge_sort,
]

# Stage 3: 如果加速版可用，加入測試清單
if _FAST_SORTS_AVAILABLE:
    SORT_FUNCTIONS.extend([bubble_sort_fast, quick_sort_fast])


class TestSortFunctions(unittest.TestCase):
    def test_basic_cases(self):
        cases = [
            [],
            [1],
            [3, 1, 2],
            [3, 1, 3, 2],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [5, 5, 5, 5],
            [0, -1, 8, 3, -2],
        ]

        for sort_fn in SORT_FUNCTIONS:
            for data in cases:
                with self.subTest(sort=sort_fn.__name__, data=data):
                    self.assertEqual(sort_fn(data), sorted(data))

    def test_random_data_matches_builtin(self):
        random.seed(42)
        random_cases = [
            [random.randint(-100, 100) for _ in range(size)]
            for size in (5, 10, 20)
        ]

        for sort_fn in SORT_FUNCTIONS:
            for data in random_cases:
                with self.subTest(sort=sort_fn.__name__, data=data):
                    self.assertEqual(sort_fn(data), sorted(data))

    def test_input_not_mutated(self):
        original = [7, 3, 9, 1, 7, 2]

        for sort_fn in SORT_FUNCTIONS:
            with self.subTest(sort=sort_fn.__name__):
                data = list(original)
                result = sort_fn(data)
                self.assertEqual(data, original)
                self.assertIsNot(result, data)

    def test_non_list_input_raises_type_error(self):
        bad_inputs = (
            None,
            "123",
            (3, 2, 1),
            {"a": 1},
        )

        for sort_fn in SORT_FUNCTIONS:
            for bad in bad_inputs:
                with self.subTest(sort=sort_fn.__name__, bad=bad):
                    with self.assertRaises(TypeError):
                        sort_fn(bad)


class TestStage3AcceleratedSorts(unittest.TestCase):
    """Stage 3: 驗證加速版排序函式的存在與正確性"""

    def test_accelerated_sorts_available(self):
        """驗證加速版函式已被引入測試清單"""
        if not _FAST_SORTS_AVAILABLE:
            self.fail("尚未實作加速版排序 — bubble_sort_fast 與 quick_sort_fast")


if __name__ == "__main__":
    unittest.main()
