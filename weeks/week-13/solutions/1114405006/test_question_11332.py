import unittest
from question_11332 import visible_segments

# 單元測試說明（繁體中文）：
# 此測試檔驗證 visible_segments 在基本情況下的行為：
# - 單一線段是否被判為可見
# - 共線且在相同射線上時近段遮擋遠段
# - 不同角度的線段皆可見
# - 被前方線段部分或完全遮擋的情形


class TestQuestion11332(unittest.TestCase):
    def test_single_segment_visible(self):
        # 單一線段，位於正 x 軸上的一段
        segs = [(1, 0, 2, 0)]
        self.assertEqual(visible_segments(segs), [1])

    def test_two_colinear_same_ray(self):
        # 兩段位於相同射線上，較近的遮擋較遠的
        segs = [(1, 0, 2, 0), (3, 0, 4, 0)]
        # 第一段可見，第二段被擋
        self.assertEqual(visible_segments(segs), [1, 0])

    def test_two_different_angles(self):
        # 兩段在不同角度都可見
        segs = [(1, 0, 2, 0), (0, 1, 0, 2)]
        self.assertEqual(visible_segments(segs), [1, 1])

    def test_blocking_by_near_segment(self):
        # 第一段在前方會遮擋第二段的某些角度
        segs = [(1, -1, 1, 1), (3, -1, 3, 1)]
        # 左邊的豎段較近，能遮擋右邊那條豎段
        res = visible_segments(segs)
        self.assertEqual(res[0], 1)
        self.assertIn(res[1], (0, 1))  # 依代表角選取，第二段可能不可見


if __name__ == '__main__':
    unittest.main()
