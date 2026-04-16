import importlib.util
import unittest
from itertools import islice
from pathlib import Path

# 以檔案路徑載入教材程式，讓測試可直接重用原始定義
ROOT_DIR = Path(__file__).resolve().parents[4]
SOURCE_PATH = ROOT_DIR / "weeks" / "week-05" / "in-class" / "U_01_generator_basics.py"


def load_module():
    spec = importlib.util.spec_from_file_location("u_01_generator_basics_module", SOURCE_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"無法載入模組: {SOURCE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestGeneratorBasics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    def test_frange_basic(self):
        # frange 應逐步產生指定範圍的浮點值
        self.assertEqual(list(self.mod.frange(0, 2, 0.5)), [0, 0.5, 1.0, 1.5])

    def test_countdown_values(self):
        # countdown 需依序遞減直到 1
        self.assertEqual(list(self.mod.countdown(3)), [3, 2, 1])

    def test_fibonacci_first_ten(self):
        # 驗證 Fibonacci 前十項是否正確
        fib = self.mod.fibonacci()
        self.assertEqual(list(islice(fib, 10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_chain_iter(self):
        # chain_iter 透過 yield from 串接多個可迭代物件
        result = list(self.mod.chain_iter([1, 2], [3, 4], [5, 6]))
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_node_depth_first(self):
        # 建立小型樹並驗證深度優先走訪順序
        root = self.mod.Node(0)
        root.add_child(self.mod.Node(1))
        root.add_child(self.mod.Node(2))
        root.children[0].add_child(self.mod.Node(3))
        root.children[0].add_child(self.mod.Node(4))

        values = [node.value for node in root.depth_first()]
        self.assertEqual(values, [0, 1, 3, 4, 2])

    def test_flatten_nested(self):
        # flatten 會遞迴展開巢狀結構，但字串視為單一元素
        nested = [1, [2, [3, 4]], "ab", ["cd"]]
        self.assertEqual(list(self.mod.flatten(nested)), [1, 2, 3, 4, "ab", "cd"])


if __name__ == "__main__":
    unittest.main()
