"""
單元測試（-easy 版本）：測試 `question_11063-easy.py` 的簡易實作。

說明：由於檔名含 '-'，無法直接用 import 語句載入，因此使用 importlib 動態載入模組。
"""

import unittest
import importlib.util
import os


def load_easy_module():
    """動態載入 question_11063-easy.py，並回傳模組物件。"""
    path = os.path.join(os.path.dirname(__file__), "question_11063-easy.py")
    spec = importlib.util.spec_from_file_location("q11063_easy", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class TestQuestion11063Easy(unittest.TestCase):
    def test_single_pixel_easy(self):
        mod = load_easy_module()
        pixels = [(255, 3, 192)]
        out = mod.convert_rgb_to_xyz(pixels)
        self.assertEqual(out[0], "163.1271 82.0146 169.9752")
        self.assertEqual(out[1], "The average of Y is 82.0146")

    def test_two_pixels_easy(self):
        mod = load_easy_module()
        pixels = [(255, 3, 192), (0, 0, 0)]
        out = mod.convert_rgb_to_xyz(pixels)
        self.assertEqual(out[1], "0.0000 0.0000 0.0000")
        expected_avg = (82.0146 + 0.0) / 2
        self.assertEqual(out[-1], f"The average of Y is {expected_avg:.4f}")


if __name__ == "__main__":
    unittest.main()
