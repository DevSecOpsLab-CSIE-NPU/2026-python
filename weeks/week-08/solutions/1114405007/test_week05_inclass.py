"""Week 05 in-class 單元測試

測試目標：
1. 驗證標準版功能正確
2. 驗證 easy 版輸出符合預期
"""

import importlib.util
import pathlib
import unittest

BASE_DIR = pathlib.Path(__file__).resolve().parent


def load_module(filename, module_name):
    """因檔名含有連字號，使用動態載入避免 import 限制。"""
    file_path = BASE_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


r_std = load_module("R_02_enumerate_zip.py", "r_std")
r_easy = load_module("R_02_enumerate_zip-easy.py", "r_easy")
u_std = load_module("U_01_generator_basics.py", "u_std")
u_easy = load_module("U_01_generator_basics-easy.py", "u_easy")


class TestEnumerateZip(unittest.TestCase):
    def test_enumerate_and_lines(self):
        self.assertEqual(
            r_std.enumerate_colors(["red", "green"], 1),
            ["1: red", "2: green"],
        )
        self.assertEqual(
            r_std.number_lines(["a", "b"]),
            ["行 1: a", "行 2: b"],
        )

    def test_zip_and_dict(self):
        self.assertEqual(
            r_std.zip_shortest([1, 2], ["a", "b", "c"]),
            [(1, "a"), (2, "b")],
        )
        self.assertEqual(
            r_std.zip_longest_with_fill([1, 2], ["a", "b", "c"], 0),
            [(1, "a"), (2, "b"), (0, "c")],
        )
        self.assertEqual(
            r_std.build_dict(["x", "y"], [10, 20]),
            {"x": 10, "y": 20},
        )

    def test_easy_version(self):
        data = r_easy.run_enumerate_zip_examples()
        self.assertEqual(data["enumerate0"], ["0: red", "1: green", "2: blue"])
        self.assertEqual(data["sum_three"], [111, 222, 333])
        self.assertEqual(data["dict"], {"name": "John", "age": "30", "city": "NYC"})


class TestGenerators(unittest.TestCase):
    def test_frange_and_countdown(self):
        self.assertEqual(list(u_std.frange(0, 2, 0.5)), [0, 0.5, 1.0, 1.5])
        self.assertEqual(list(u_std.countdown(3)), [3, 2, 1])

    def test_fibonacci_chain_flatten(self):
        fib = u_std.fibonacci()
        first_seven = [next(fib) for _ in range(7)]
        self.assertEqual(first_seven, [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(list(u_std.chain_iter([1, 2], [3], [4, 5])), [1, 2, 3, 4, 5])
        self.assertEqual(list(u_std.flatten([1, [2, [3, 4]], 5])), [1, 2, 3, 4, 5])

    def test_depth_first(self):
        root = u_std.Node(0)
        root.add_child(u_std.Node(1))
        root.add_child(u_std.Node(2))
        root.children[0].add_child(u_std.Node(3))
        values = [node.value for node in root.depth_first()]
        self.assertEqual(values, [0, 1, 3, 2])

    def test_easy_version(self):
        self.assertEqual(list(u_easy.easy_frange(0, 2, 0.5)), [0, 0.5, 1.0, 1.5])
        self.assertEqual(list(u_easy.easy_countdown(3)), [3, 2, 1])
        self.assertEqual(u_easy.easy_fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(list(u_easy.easy_chain([1, 2], [3], [4, 5])), [1, 2, 3, 4, 5])
        self.assertEqual(list(u_easy.easy_flatten([1, [2, [3, 4]], 5])), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main(verbosity=2)
