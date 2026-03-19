"""
題目 118 - 罐頭工廠機器人 單元測試

完整的 unit-test 套件，涵蓋所有功能和邊界情況。
"""

import unittest
from solution_question_118 import RobotWorld, parse_and_simulate, format_output


class TestRobotWorldBasics(unittest.TestCase):
    """測試 RobotWorld 基礎功能"""
    
    def setUp(self):
        """每個測試前初始化一個 5x3 的世界"""
        self.world = RobotWorld(5, 3)
    
    def test_world_initialization(self):
        """測試世界初始化"""
        self.assertEqual(self.world.width, 5)
        self.assertEqual(self.world.height, 3)
        self.assertEqual(len(self.world.scents), 0)
    
    def test_is_within_bounds_valid(self):
        """測試有效座標判定"""
        self.assertTrue(self.world.is_within_bounds(0, 0))
        self.assertTrue(self.world.is_within_bounds(5, 3))
        self.assertTrue(self.world.is_within_bounds(2, 1))
    
    def test_is_within_bounds_invalid(self):
        """測試無效座標判定"""
        self.assertFalse(self.world.is_within_bounds(-1, 0))
        self.assertFalse(self.world.is_within_bounds(0, -1))
        self.assertFalse(self.world.is_within_bounds(6, 3))
        self.assertFalse(self.world.is_within_bounds(5, 4))
    
    def test_is_within_bounds_edges(self):
        """測試边界邊界"""
        # 邊界上的點應該有效
        self.assertTrue(self.world.is_within_bounds(0, 3))
        self.assertTrue(self.world.is_within_bounds(5, 0))
        # 邊界外的點應該無效
        self.assertFalse(self.world.is_within_bounds(6, 3))
        self.assertFalse(self.world.is_within_bounds(5, 4))


class TestRobotRotation(unittest.TestCase):
    """測試機器人旋轉"""
    
    def setUp(self):
        self.world = RobotWorld(5, 3)
    
    def test_rotate_right_from_north(self):
        """北向右轉_to_東"""
        result = self.world.rotate('N', 'R')
        self.assertEqual(result, 'E')
    
    def test_rotate_right_from_east(self):
        """東向右轉_to_南"""
        result = self.world.rotate('E', 'R')
        self.assertEqual(result, 'S')
    
    def test_rotate_right_from_south(self):
        """南向右轉_to_西"""
        result = self.world.rotate('S', 'R')
        self.assertEqual(result, 'W')
    
    def test_rotate_right_from_west(self):
        """西向右轉_to_北"""
        result = self.world.rotate('W', 'R')
        self.assertEqual(result, 'N')
    
    def test_rotate_left_from_north(self):
        """北向左轉_to_西"""
        result = self.world.rotate('N', 'L')
        self.assertEqual(result, 'W')
    
    def test_rotate_left_from_east(self):
        """東向左轉_to_北"""
        result = self.world.rotate('E', 'L')
        self.assertEqual(result, 'N')
    
    def test_rotate_left_from_south(self):
        """南向左轉_to_東"""
        result = self.world.rotate('S', 'L')
        self.assertEqual(result, 'E')
    
    def test_rotate_left_from_west(self):
        """西向左轉_to_南"""
        result = self.world.rotate('W', 'L')
        self.assertEqual(result, 'S')
    
    def test_double_rotation_right(self):
        """右轉兩次應轉 180°"""
        result = self.world.rotate('N', 'R')
        result = self.world.rotate(result, 'R')
        self.assertEqual(result, 'S')
    
    def test_quad_rotation_full_circle(self):
        """右轉四次應回到原方向"""
        result = 'N'
        for _ in range(4):
            result = self.world.rotate(result, 'R')
        self.assertEqual(result, 'N')


class TestRobotMovement(unittest.TestCase):
    """測試機器人前進"""
    
    def setUp(self):
        self.world = RobotWorld(5, 3)
    
    def test_move_north(self):
        """北方前進：y 增加"""
        x, y, direction, lost = self.world.execute_instructions(1, 1, 'N', 'F')
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)
        self.assertEqual(direction, 'N')
        self.assertFalse(lost)
    
    def test_move_south(self):
        """南方前進：y 減少"""
        x, y, direction, lost = self.world.execute_instructions(1, 2, 'S', 'F')
        self.assertEqual(x, 1)
        self.assertEqual(y, 1)
        self.assertEqual(direction, 'S')
        self.assertFalse(lost)
    
    def test_move_east(self):
        """東方前進：x 增加"""
        x, y, direction, lost = self.world.execute_instructions(2, 2, 'E', 'F')
        self.assertEqual(x, 3)
        self.assertEqual(y, 2)
        self.assertEqual(direction, 'E')
        self.assertFalse(lost)
    
    def test_move_west(self):
        """西方前進：x 減少"""
        x, y, direction, lost = self.world.execute_instructions(2, 2, 'W', 'F')
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)
        self.assertEqual(direction, 'W')
        self.assertFalse(lost)
    
    def test_multiple_forward_moves(self):
        """多次前進"""
        x, y, direction, lost = self.world.execute_instructions(0, 0, 'N', 'FFF')
        self.assertEqual(x, 0)
        self.assertEqual(y, 3)
        self.assertEqual(direction, 'N')
        self.assertFalse(lost)


class TestRobotFallOff(unittest.TestCase):
    """測試機器人掉落"""
    
    def setUp(self):
        self.world = RobotWorld(5, 3)
    
    def test_fall_off_north(self):
        """向北掉落"""
        x, y, direction, lost = self.world.execute_instructions(0, 3, 'N', 'F')
        self.assertEqual(x, 0)
        self.assertEqual(y, 3)
        self.assertEqual(direction, 'N')
        self.assertTrue(lost)
        self.assertIn((0, 3), self.world.scents)
    
    def test_fall_off_south(self):
        """向南掉落"""
        x, y, direction, lost = self.world.execute_instructions(0, 0, 'S', 'F')
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual(direction, 'S')
        self.assertTrue(lost)
        self.assertIn((0, 0), self.world.scents)
    
    def test_fall_off_east(self):
        """向東掉落"""
        x, y, direction, lost = self.world.execute_instructions(5, 0, 'E', 'F')
        self.assertEqual(x, 5)
        self.assertEqual(y, 0)
        self.assertEqual(direction, 'E')
        self.assertTrue(lost)
        self.assertIn((5, 0), self.world.scents)
    
    def test_fall_off_west(self):
        """向西掉落"""
        x, y, direction, lost = self.world.execute_instructions(0, 0, 'W', 'F')
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
        self.assertEqual(direction, 'W')
        self.assertTrue(lost)
        self.assertIn((0, 0), self.world.scents)
    
    def test_scent_marker_left_at_edge(self):
        """確認 scent 標記留在邊界"""
        # 第一個機器人掉落
        self.world.execute_instructions(5, 0, 'E', 'F')
        # 驗證 scent 在 (5,0)
        self.assertIn((5, 0), self.world.scents)
        self.assertEqual(len(self.world.scents), 1)


class TestScentMechanism(unittest.TestCase):
    """測試 scent 臭跡機制"""
    
    def setUp(self):
        self.world = RobotWorld(5, 3)
    
    def test_scent_prevents_falloff(self):
        """臭跡應防止後續機器人掉落"""
        # 第一個機器人掉落，留下 scent 在 (1,3)
        self.world.execute_instructions(1, 3, 'N', 'F')
        self.assertIn((1, 3), self.world.scents)
        
        # 第二個機器人應在相同位置停止
        x, y, direction, lost = self.world.execute_instructions(1, 1, 'N', 'FFF')
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)  # 停在 scent 下方
        self.assertEqual(direction, 'N')
        self.assertFalse(lost)
    
    def test_scent_only_at_edge(self):
        """臭跡只對邊界有效"""
        # 在內部掉落的指令不會被阻止（不可能掉落）
        x, y, direction, lost = self.world.execute_instructions(2, 2, 'N', 'F')
        self.assertEqual(x, 2)
        self.assertEqual(y, 3)
        self.assertFalse(lost)
    
    def test_multiple_scents(self):
        """測試多個 scent 標記"""
        # 第一個機器人
        self.world.execute_instructions(1, 3, 'N', 'F')
        # 第二個機器人
        self.world.execute_instructions(0, 0, 'W', 'F')
        
        self.assertEqual(len(self.world.scents), 2)
        self.assertIn((1, 3), self.world.scents)
        self.assertIn((0, 0), self.world.scents)


class TestComplexInstructions(unittest.TestCase):
    """測試複雜指令序列"""
    
    def setUp(self):
        self.world = RobotWorld(5, 3)
    
    def test_square_path(self):
        """繞正方形一圈（回到起點）"""
        x, y, direction, lost = self.world.execute_instructions(1, 1, 'E', 'FRFRFRFR')
        self.assertEqual(x, 1)
        self.assertEqual(y, 1)
        self.assertEqual(direction, 'E')
        self.assertFalse(lost)
    
    def test_turn_in_place(self):
        """原地旋轉"""
        x, y, direction, lost = self.world.execute_instructions(2, 2, 'N', 'LLLL')
        self.assertEqual(x, 2)
        self.assertEqual(y, 2)
        self.assertEqual(direction, 'N')
        self.assertFalse(lost)
    
    def test_example1_from_problem(self):
        """題目範例 1：(1,1,E) RFRFRFRF 應回到起點未掉落"""
        x, y, direction, lost = self.world.execute_instructions(1, 1, 'E', 'RFRFRFRF')
        self.assertFalse(lost)
        self.assertEqual((x, y, direction), (1, 1, 'E'))
    
    def test_complex_path(self):
        """複雜指令序列"""
        x, y, direction, lost = self.world.execute_instructions(3, 2, 'N', 'FRRFLLFFRRFLL')
        # 手動驗證: F:(3,3,N), RR:(3,3,S), F:(3,2,S), L:(3,2,E), L:(3,2,N), FF:(3,3,N)+(3,4,N掉落)
        self.assertTrue(lost)
        self.assertEqual((x, y, direction), (3, 3, 'N'))


class TestParsingAndFormatting(unittest.TestCase):
    """測試輸入解析和輸出格式化"""
    
    def test_parse_simple_input(self):
        """解析簡單輸入"""
        input_str = """5 3
1 1 E
RF"""
        results = parse_and_simulate(input_str)
        self.assertEqual(len(results), 1)
        x, y, direction, lost = results[0]
        # R: 右轉 (E->S), F: 前進，結果應是 (1,0,S)
        self.assertEqual((x, y, direction), (1, 0, 'S'))
        self.assertFalse(lost)
    
    def test_parse_multiple_robots(self):
        """解析多個機器人"""
        input_str = """5 3
1 1 E
RF
3 2 N
FRF"""
        results = parse_and_simulate(input_str)
        self.assertEqual(len(results), 2)
    
    def test_format_output_not_lost(self):
        """格式化未掉落的機器人"""
        results = [(1, 1, 'E', False)]
        output = format_output(results)
        self.assertEqual(output, "1 1 E")
    
    def test_format_output_lost(self):
        """格式化已掉落的機器人"""
        results = [(1, 1, 'E', True)]
        output = format_output(results)
        self.assertEqual(output, "1 1 E LOST")
    
    def test_format_output_mixed(self):
        """格式化混合狀態"""
        results = [(1, 1, 'E', True), (3, 3, 'N', False)]
        output = format_output(results)
        lines = output.split('\n')
        self.assertEqual(lines[0], "1 1 E LOST")
        self.assertEqual(lines[1], "3 3 N")


class TestIntegration(unittest.TestCase):
    """整合測試：驗證完整的題目範例"""
    
    def test_full_problem_example(self):
        """測試題目提供的完整例子"""
        input_str = """5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLLL"""
        
        results = parse_and_simulate(input_str)
        
        # 驗證結果數量
        self.assertEqual(len(results), 3)
        
        # 機器人 1: (1,1,E) RFRFRFRF 回到原點未掉落
        self.assertEqual(results[0][3], False)  # 未掉落
        self.assertEqual((results[0][0], results[0][1], results[0][2]), (1, 1, 'E'))
        
        # 機器人 2: (3,2,N) FRRFLLFFRRFLL 應掉落
        self.assertEqual(results[1][3], True)  # 已掉落
        self.assertEqual((results[1][0], results[1][1], results[1][2]), (3, 3, 'N'))
        
        # 機器人 3
        self.assertEqual(results[2][3], False)  # 未掉落
        self.assertEqual((results[2][0], results[2][1], results[2][2]), (0, 3, 'W'))
    
    def test_output_format_matches_expected(self):
        """驗證輸出格式匹配預期"""
        input_str = """5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLLL"""
        
        results = parse_and_simulate(input_str)
        output = format_output(results)
        
        expected = """1 1 E
3 3 N LOST
0 3 W"""
        
        self.assertEqual(output, expected)


class TestEdgeCases(unittest.TestCase):
    """測試邊界情況"""
    
    def test_empty_instructions(self):
        """空指令集"""
        world = RobotWorld(5, 3)
        x, y, direction, lost = world.execute_instructions(2, 2, 'N', '')
        self.assertEqual(x, 2)
        self.assertEqual(y, 2)
        self.assertEqual(direction, 'N')
        self.assertFalse(lost)
    
    def test_robot_at_origin(self):
        """機器人在原點"""
        world = RobotWorld(5, 3)
        x, y, direction, lost = world.execute_instructions(0, 0, 'N', 'FFF')
        self.assertEqual((x, y, direction, lost), (0, 3, 'N', False))
    
    def test_robot_at_corner(self):
        """機器人在角落"""
        world = RobotWorld(5, 3)
        x, y, direction, lost = world.execute_instructions(5, 3, 'N', 'F')
        self.assertTrue(lost)


if __name__ == '__main__':
    # 以詳細模式運行所有測試
    unittest.main(verbosity=2)
