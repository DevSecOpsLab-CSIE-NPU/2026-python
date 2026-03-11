"""
UVA 118 — 乖乖的機器人（Mutant Flatworld Explorers）單元測試

測試目標：
1. turn_left / turn_right：方向轉換邏輯
2. move_forward：前進一格的座標計算
3. simulate_robot：完整模擬單一機器人的指令執行
4. 邊界掉落與 scent 標記機制
"""

import unittest


# ===== 方向與位移定義 =====

# 四個方向：北、東、南、西（順時針排列）
DIRS = ['N', 'E', 'S', 'W']

# 各方向對應的 x, y 位移量
DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]


def turn_left(direction_index):
    """左轉 90 度：方向索引逆時針移動一格"""
    return (direction_index + 3) % 4


def turn_right(direction_index):
    """右轉 90 度：方向索引順時針移動一格"""
    return (direction_index + 1) % 4


def move_forward(x, y, direction_index):
    """根據目前方向前進一格，回傳新座標 (nx, ny)"""
    return x + DX[direction_index], y + DY[direction_index]


def simulate_robot(mx, my, x, y, direction, commands, scents):
    """
    模擬一個機器人在 (0,0)~(mx,my) 的矩形世界上執行指令。

    參數：
        mx, my: 世界右上角座標
        x, y: 機器人初始座標
        direction: 初始方向字元 ('N','E','S','W')
        commands: 指令字串（由 'L','R','F' 組成）
        scents: 已有的 scent 標記集合（會被原地修改）

    回傳：
        (x, y, direction_char, lost) — 最終座標、方向、是否掉落
    """
    di = DIRS.index(direction)
    lost = False

    for c in commands:
        if c == 'L':
            di = turn_left(di)
        elif c == 'R':
            di = turn_right(di)
        elif c == 'F':
            nx, ny = move_forward(x, y, di)
            # 判斷是否超出邊界
            if nx < 0 or nx > mx or ny < 0 or ny > my:
                # 若當前位置+方向已有 scent，忽略此指令
                if (x, y, di) in scents:
                    continue
                # 否則標記 scent 並宣告掉落
                scents.add((x, y, di))
                lost = True
                break
            x, y = nx, ny

    return x, y, DIRS[di], lost


# ===== 測試類別 =====


class TestTurnLeft(unittest.TestCase):
    """測試左轉邏輯"""

    def test_north_to_west(self):
        """面北左轉後應面西"""
        self.assertEqual(turn_left(0), 3)  # N → W

    def test_east_to_north(self):
        """面東左轉後應面北"""
        self.assertEqual(turn_left(1), 0)  # E → N

    def test_south_to_east(self):
        """面南左轉後應面東"""
        self.assertEqual(turn_left(2), 1)  # S → E

    def test_west_to_south(self):
        """面西左轉後應面南"""
        self.assertEqual(turn_left(3), 2)  # W → S


class TestTurnRight(unittest.TestCase):
    """測試右轉邏輯"""

    def test_north_to_east(self):
        """面北右轉後應面東"""
        self.assertEqual(turn_right(0), 1)  # N → E

    def test_east_to_south(self):
        """面東右轉後應面南"""
        self.assertEqual(turn_right(1), 2)  # E → S

    def test_south_to_west(self):
        """面南右轉後應面西"""
        self.assertEqual(turn_right(2), 3)  # S → W

    def test_west_to_north(self):
        """面西右轉後應面北"""
        self.assertEqual(turn_right(3), 0)  # W → N


class TestMoveForward(unittest.TestCase):
    """測試前進一格的座標計算"""

    def test_move_north(self):
        """面北前進：y + 1"""
        self.assertEqual(move_forward(2, 3, 0), (2, 4))

    def test_move_east(self):
        """面東前進：x + 1"""
        self.assertEqual(move_forward(2, 3, 1), (3, 3))

    def test_move_south(self):
        """面南前進：y - 1"""
        self.assertEqual(move_forward(2, 3, 2), (2, 2))

    def test_move_west(self):
        """面西前進：x - 1"""
        self.assertEqual(move_forward(2, 3, 3), (1, 3))


class TestSimulateRobot(unittest.TestCase):
    """測試完整機器人模擬"""

    def test_sample_robot_1(self):
        """題目範例第一個機器人：(1,1,E) RFRFRFRF → 原地繞圈回到 (1,1,E)"""
        scents = set()
        x, y, d, lost = simulate_robot(5, 3, 1, 1, 'E', 'RFRFRFRF', scents)
        self.assertEqual((x, y, d), (1, 1, 'E'))
        self.assertFalse(lost)

    def test_sample_robot_2(self):
        """題目範例第二個機器人：(3,2,N) FRRFLLFFRRFLL → 掉落，最終 (3,3,N) LOST"""
        scents = set()
        x, y, d, lost = simulate_robot(5, 3, 3, 2, 'N', 'FRRFLLFFRRFLL', scents)
        self.assertEqual((x, y, d), (3, 3, 'N'))
        self.assertTrue(lost)

    def test_sample_robot_3(self):
        """題目範例第三個機器人：前面機器人留下 scent，(0,3,W) LLFFFLFLFL → (2,3,S)"""
        scents = set()
        # 先執行第二個機器人，產生 scent
        simulate_robot(5, 3, 3, 2, 'N', 'FRRFLLFFRRFLL', scents)
        # 再執行第三個機器人
        x, y, d, lost = simulate_robot(5, 3, 0, 3, 'W', 'LLFFFLFLFL', scents)
        self.assertEqual((x, y, d), (2, 3, 'S'))
        self.assertFalse(lost)

    def test_no_commands(self):
        """空指令：機器人原地不動"""
        scents = set()
        x, y, d, lost = simulate_robot(5, 5, 2, 2, 'N', '', scents)
        self.assertEqual((x, y, d), (2, 2, 'N'))
        self.assertFalse(lost)

    def test_only_turns(self):
        """只有轉向指令：座標不變，方向改變"""
        scents = set()
        # LLL 等於右轉一次：N → E
        x, y, d, lost = simulate_robot(5, 5, 0, 0, 'N', 'LLL', scents)
        self.assertEqual((x, y, d), (0, 0, 'E'))
        self.assertFalse(lost)

    def test_fall_off_south(self):
        """從南方邊界掉落：(0,0,S) F → (0,0,S) LOST"""
        scents = set()
        x, y, d, lost = simulate_robot(5, 5, 0, 0, 'S', 'F', scents)
        self.assertEqual((x, y, d), (0, 0, 'S'))
        self.assertTrue(lost)

    def test_fall_off_west(self):
        """從西方邊界掉落：(0,0,W) F → (0,0,W) LOST"""
        scents = set()
        x, y, d, lost = simulate_robot(5, 5, 0, 0, 'W', 'F', scents)
        self.assertEqual((x, y, d), (0, 0, 'W'))
        self.assertTrue(lost)

    def test_fall_off_north(self):
        """從北方邊界掉落：(0,5,N) F → (0,5,N) LOST（世界 5x5）"""
        scents = set()
        x, y, d, lost = simulate_robot(5, 5, 0, 5, 'N', 'F', scents)
        self.assertEqual((x, y, d), (0, 5, 'N'))
        self.assertTrue(lost)

    def test_fall_off_east(self):
        """從東方邊界掉落：(5,0,E) F → (5,0,E) LOST（世界 5x5）"""
        scents = set()
        x, y, d, lost = simulate_robot(5, 5, 5, 0, 'E', 'F', scents)
        self.assertEqual((x, y, d), (5, 0, 'E'))
        self.assertTrue(lost)


class TestScentMechanism(unittest.TestCase):
    """測試 scent 標記機制"""

    def test_scent_prevents_fall(self):
        """有 scent 標記的位置+方向，後續機器人不會掉落"""
        scents = set()
        # 第一個機器人掉落，留下 scent
        simulate_robot(3, 3, 3, 3, 'N', 'F', scents)
        self.assertIn((3, 3, 0), scents)  # 0 = N
        # 第二個機器人在同位置同方向，不會掉落
        x, y, d, lost = simulate_robot(3, 3, 3, 3, 'N', 'F', scents)
        self.assertEqual((x, y, d), (3, 3, 'N'))
        self.assertFalse(lost)

    def test_scent_direction_specific(self):
        """scent 只對同一方向有效，不同方向仍會掉落"""
        scents = set()
        # 面北掉落留下 scent
        simulate_robot(3, 3, 3, 3, 'N', 'F', scents)
        # 面東在同位置仍會掉落
        x, y, d, lost = simulate_robot(3, 3, 3, 3, 'E', 'F', scents)
        self.assertTrue(lost)

    def test_multiple_scents(self):
        """多個 scent 可以同時存在"""
        scents = set()
        simulate_robot(3, 3, 3, 3, 'N', 'F', scents)
        simulate_robot(3, 3, 3, 3, 'E', 'F', scents)
        self.assertEqual(len(scents), 2)


if __name__ == "__main__":
    unittest.main()
