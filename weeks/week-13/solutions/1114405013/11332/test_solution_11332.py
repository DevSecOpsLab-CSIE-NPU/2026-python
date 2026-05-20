import unittest

from solution_11332 import solve, visible_mirrors
from solution_11332_easy import solve as solve_easy


class TestUVA11332(unittest.TestCase):
    # 基本案例：只有一面鏡子時，必定可見。
    def test_single_mirror_visible(self):
        segments = [(1, 0, 2, 0)]
        self.assertEqual(visible_mirrors(segments), [1])

    # 同一條視線上的前後兩面鏡子，近的可見、遠的被完全遮住。
    def test_collinear_far_mirror_hidden(self):
        segments = [
            (1, 1, 2, 2),
            (3, 3, 4, 4),
        ]
        self.assertEqual(visible_mirrors(segments), [1, 0])

    # 角度區間互不重疊時，所有鏡子都應可見。
    def test_non_overlapping_angles_all_visible(self):
        segments = [
            (2, 1, 2, 2),
            (-2, 1, -2, 2),
        ]
        self.assertEqual(visible_mirrors(segments), [1, 1])

    # 近鏡子只遮掉遠鏡子的一部分時，兩者都仍可見。
    def test_partial_occlusion_both_visible(self):
        segments = [
            (2, -1, 2, 1),
            (5, -3, 5, 3),
        ]
        self.assertEqual(visible_mirrors(segments), [1, 1])

    # 多組測資（EOF）輸入應逐行輸出答案。
    def test_solve_multiple_cases(self):
        data = "1\n1 0 2 0\n2\n1 1 2 2\n3 3 4 4\n"
        expected = "1\n1 0"
        self.assertEqual(solve(data), expected)

    # easy 版本輸出必須與主版本完全一致。
    def test_easy_matches_main(self):
        data = "3\n2 -1 2 1\n5 -3 5 3\n-4 -1 -4 1\n"
        self.assertEqual(solve_easy(data), solve(data))


if __name__ == "__main__":
    unittest.main()
