import unittest
from question_11321 import simulate_trap_sequence


class TestQuestion11321(unittest.TestCase):
    def test_single_center(self):
        # 3x3，放置中心格 (1,1) 不會封死
        N, M = 3, 3
        proposals = [(1, 1)]
        res = simulate_trap_sequence(N, M, proposals)
        self.assertEqual(res, ['<(_ _)>'])

    def test_block_middle_column_sequential(self):
        # 3x3，依序封鎖中間列三格，最後一格會被拒絕
        N, M = 3, 3
        proposals = [(0, 1), (1, 1), (2, 1)]
        res = simulate_trap_sequence(N, M, proposals)
        self.assertEqual(res, ['<(_ _)>', '<(_ _)>', '>_<'])

    def test_single_cell_reject(self):
        # 1x1，若放陷阱會封死（因為起點即終點被封）
        N, M = 1, 1
        proposals = [(0, 0)]
        res = simulate_trap_sequence(N, M, proposals)
        self.assertEqual(res, ['>_<'])

    def test_no_blocking_when_path_exists(self):
        # 2x2，放角落陷阱不封路
        N, M = 2, 2
        proposals = [(0, 0), (1, 0)]  # 左邊兩個格子若被封也可能仍有其他路
        res = simulate_trap_sequence(N, M, proposals)
        # 第一個放在 (0,0) 會被接受 (還有其他起點)，第二個放 (1,0) 會被拒絕
        self.assertEqual(res, ['<(_ _)>', '>_<'])


if __name__ == '__main__':
    unittest.main()
