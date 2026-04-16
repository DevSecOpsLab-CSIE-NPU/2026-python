import importlib.util
import unittest
from pathlib import Path

# 以絕對路徑動態載入教材檔，避免受到套件結構影響
ROOT_DIR = Path(__file__).resolve().parents[4]
SOURCE_PATH = ROOT_DIR / "weeks" / "week-05" / "in-class" / "R_02_enumerate_zip.py"


def load_module():
    spec = importlib.util.spec_from_file_location("r_02_enumerate_zip_module", SOURCE_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"無法載入模組: {SOURCE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestEnumerateZipExamples(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module()

    def test_enumerate_default_start(self):
        # 驗證 enumerate 預設從 0 開始
        result = list(enumerate(self.mod.colors))
        self.assertEqual(result, [(0, "red"), (1, "green"), (2, "blue")])

    def test_enumerate_with_start_1(self):
        # 驗證自訂起始值的行為
        result = list(enumerate(self.mod.colors, 1))
        self.assertEqual(result, [(1, "red"), (2, "green"), (3, "blue")])

    def test_zip_stops_at_shortest_sequence(self):
        # zip 會以最短序列長度為準
        result = list(zip(self.mod.x, self.mod.y))
        self.assertEqual(result, [(1, "a"), (2, "b")])

    def test_zip_longest_with_fillvalue(self):
        # zip_longest 會補齊較短序列
        result = list(self.mod.zip_longest(self.mod.x, self.mod.y, fillvalue=0))
        self.assertEqual(result, [(1, "a"), (2, "b"), (0, "c")])

    def test_dict_created_from_zip(self):
        # 驗證由 keys/values 配對建立字典的結果
        self.assertEqual(self.mod.d, {"name": "John", "age": "30", "city": "NYC"})


if __name__ == "__main__":
    unittest.main()
