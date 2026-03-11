"""
UVA 118 - 機器人移動問題的單元測試程式

這個程式測試機器人在矩形網格上的移動行為，包括：
1. 機器人的旋轉（左轉、右轉）
2. 機器人的前進（受邊界限制）
3. 掉出邊界時留下香氣(scent)標記
4. 機器人在有香氣的地方忽略會導致掉下去的指令
"""

import unittest
from enum import Enum
from typing import Set, Tuple, Optional


# ============================================================================
# 機器人類別定義
# ============================================================================

class Direction(Enum):
    """定義機器人的四個方向"""
    NORTH = 'N'
    SOUTH = 'S'
    EAST = 'E'
    WEST = 'W'


class Robot:
    """
    機器人類別
    
    屬性：
        x (int): 機器人的 x 座標
        y (int): 機器人的 y 座標
        direction (Direction): 機器人面向的方向
        grid_width (int): 網格的寬度（右上角 x 座標）
        grid_height (int): 網格的高度（右上角 y 座標）
        is_lost (bool): 機器人是否掉出邊界
        scent_positions (Set): 有香氣標記的所有坐標
    """
    
    def __init__(self, x: int, y: int, direction: str, 
                 grid_width: int, grid_height: int,
                 scent_positions: Optional[Set[Tuple[int, int]]] = None):
        """
        初始化機器人
        
        參數：
            x: 初始 x 座標
            y: 初始 y 座標
            direction: 初始方向 ('N', 'S', 'E', 'W')
            grid_width: 網格寬度（右上角 x 座標）
            grid_height: 網格高度（右上角 y 座標）
            scent_positions: 已有香氣的坐標集合
        """
        self.x = x
        self.y = y
        self.direction = Direction(direction)
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.is_lost = False
        
        # 如果沒有提供香氣位置集合，則建立空集合
        self.scent_positions = scent_positions if scent_positions is not None else set()
    
    def turn_left(self):
        """機器人左轉 90 度"""
        if self.is_lost:
            return
        
        # 定義左轉的順序：N -> W -> S -> E -> N
        turns = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH
        }
        self.direction = turns[self.direction]
    
    def turn_right(self):
        """機器人右轉 90 度"""
        if self.is_lost:
            return
        
        # 定義右轉的順序：N -> E -> S -> W -> N
        turns = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH
        }
        self.direction = turns[self.direction]
    
    def move_forward(self):
        """機器人向前行進一步"""
        if self.is_lost:
            return
        
        # 計算前進一步後的新座標
        new_x, new_y = self.x, self.y
        
        if self.direction == Direction.NORTH:
            new_y += 1
        elif self.direction == Direction.SOUTH:
            new_y -= 1
        elif self.direction == Direction.EAST:
            new_x += 1
        elif self.direction == Direction.WEST:
            new_x -= 1
        
        # 檢查新座標是否超出邊界
        if new_x < 0 or new_x > self.grid_width or \
           new_y < 0 or new_y > self.grid_height:
            # 機器人要掉出去了，檢查目前位置是否有香氣標記
            if (self.x, self.y) in self.scent_positions:
                # 有香氣標記，忽略這個「前進」指令
                return
            else:
                # 沒有香氣標記，機器人掉出去，留下香氣標記
                self.scent_positions.add((self.x, self.y))
                self.is_lost = True
                return
        
        # 座標有效，移動機器人
        self.x = new_x
        self.y = new_y
    
    def execute_instructions(self, instructions: str):
        """
        執行一段指令序列
        
        參數：
            instructions: 由 'L', 'R', 'F' 組成的字串
                L: 左轉 (Left)
                R: 右轉 (Right)
                F: 前進 (Forward)
        """
        for instruction in instructions:
            if instruction == 'L':
                self.turn_left()
            elif instruction == 'R':
                self.turn_right()
            elif instruction == 'F':
                self.move_forward()
    
    def get_status(self) -> str:
        """
        獲取機器人的狀態字串
        
        返回：
            格式為 "x y direction" 或 "x y direction LOST" 的字串
        """
        status = f"{self.x} {self.y} {self.direction.value}"
        if self.is_lost:
            status += " LOST"
        return status


# ============================================================================
# 單元測試類別
# ============================================================================

class TestRobotDirection(unittest.TestCase):
    """測試機器人的方向轉換功能"""
    
    def setUp(self):
        """每個測試前的準備工作"""
        self.robot = Robot(1, 1, 'N', 5, 5)
    
    def test_turn_left_from_north(self):
        """測試從北方左轉應該面向西方"""
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, Direction.WEST)
    
    def test_turn_left_from_west(self):
        """測試從西方左轉應該面向南方"""
        self.robot.direction = Direction.WEST
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, Direction.SOUTH)
    
    def test_turn_left_from_south(self):
        """測試從南方左轉應該面向東方"""
        self.robot.direction = Direction.SOUTH
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, Direction.EAST)
    
    def test_turn_left_from_east(self):
        """測試從東方左轉應該面向北方"""
        self.robot.direction = Direction.EAST
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, Direction.NORTH)
    
    def test_turn_right_from_north(self):
        """測試從北方右轉應該面向東方"""
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, Direction.EAST)
    
    def test_turn_right_from_east(self):
        """測試從東方右轉應該面向南方"""
        self.robot.direction = Direction.EAST
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, Direction.SOUTH)
    
    def test_turn_right_from_south(self):
        """測試從南方右轉應該面向西方"""
        self.robot.direction = Direction.SOUTH
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, Direction.WEST)
    
    def test_turn_right_from_west(self):
        """測試從西方右轉應該面向北方"""
        self.robot.direction = Direction.WEST
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, Direction.NORTH)
    
    def test_four_left_turns_return_to_original(self):
        """測試四次左轉應該回到原始方向"""
        original_direction = self.robot.direction
        self.robot.turn_left()
        self.robot.turn_left()
        self.robot.turn_left()
        self.robot.turn_left()
        self.assertEqual(self.robot.direction, original_direction)
    
    def test_four_right_turns_return_to_original(self):
        """測試四次右轉應該回到原始方向"""
        original_direction = self.robot.direction
        self.robot.turn_right()
        self.robot.turn_right()
        self.robot.turn_right()
        self.robot.turn_right()
        self.assertEqual(self.robot.direction, original_direction)


class TestRobotMovement(unittest.TestCase):
    """測試機器人的移動功能"""
    
    def setUp(self):
        """每個測試前的準備工作"""
        self.robot = Robot(1, 1, 'N', 5, 5)
    
    def test_move_forward_north(self):
        """測試向北方前進應該增加 y 座標"""
        self.robot.move_forward()
        self.assertEqual((self.robot.x, self.robot.y), (1, 2))
    
    def test_move_forward_south(self):
        """測試向南方前進應該減少 y 座標"""
        self.robot.direction = Direction.SOUTH
        self.robot.move_forward()
        self.assertEqual((self.robot.x, self.robot.y), (1, 0))
    
    def test_move_forward_east(self):
        """測試向東方前進應該增加 x 座標"""
        self.robot.direction = Direction.EAST
        self.robot.move_forward()
        self.assertEqual((self.robot.x, self.robot.y), (2, 1))
    
    def test_move_forward_west(self):
        """測試向西方前進應該減少 x 座標"""
        self.robot.direction = Direction.WEST
        self.robot.move_forward()
        self.assertEqual((self.robot.x, self.robot.y), (0, 1))
    
    def test_multiple_moves_north(self):
        """測試多次向北方前進"""
        for _ in range(4):
            self.robot.move_forward()
        self.assertEqual((self.robot.x, self.robot.y), (1, 5))
    
    def test_move_to_boundary(self):
        """測試移動到邊界"""
        self.robot.x = 5
        self.robot.direction = Direction.EAST
        self.robot.move_forward()
        # 移動到 x=6 會超出邊界，掉出去
        self.assertTrue(self.robot.is_lost)
        self.assertEqual((self.robot.x, self.robot.y), (5, 1))


class TestRobotBoundary(unittest.TestCase):
    """測試機器人的邊界和掉出去的行為"""
    
    def test_move_out_of_boundary_north(self):
        """測試向北方掉出邊界"""
        robot = Robot(2, 5, 'N', 5, 5)
        robot.move_forward()
        self.assertTrue(robot.is_lost)
        self.assertEqual((robot.x, robot.y), (2, 5))
    
    def test_move_out_of_boundary_south(self):
        """測試向南方掉出邊界"""
        robot = Robot(2, 0, 'S', 5, 5)
        robot.move_forward()
        self.assertTrue(robot.is_lost)
        self.assertEqual((robot.x, robot.y), (2, 0))
    
    def test_move_out_of_boundary_east(self):
        """測試向東方掉出邊界"""
        robot = Robot(5, 2, 'E', 5, 5)
        robot.move_forward()
        self.assertTrue(robot.is_lost)
        self.assertEqual((robot.x, robot.y), (5, 2))
    
    def test_move_out_of_boundary_west(self):
        """測試向西方掉出邊界"""
        robot = Robot(0, 2, 'W', 5, 5)
        robot.move_forward()
        self.assertTrue(robot.is_lost)
        self.assertEqual((robot.x, robot.y), (0, 2))
    
    def test_scent_mark_left_when_lost(self):
        """測試機器人掉出去時會留下香氣標記"""
        scent_set: Set[Tuple[int, int]] = set()
        robot = Robot(5, 2, 'E', 5, 5, scent_set)
        robot.move_forward()
        self.assertTrue(robot.is_lost)
        self.assertIn((5, 2), scent_set)


class TestRobotScent(unittest.TestCase):
    """測試香氣標記的功能"""
    
    def test_ignore_forward_instruction_with_scent(self):
        """測試有香氣標記時忽略會掉下去的前進指令"""
        scent_set: Set[Tuple[int, int]] = {(5, 2)}
        robot = Robot(5, 2, 'E', 5, 5, scent_set)
        robot.move_forward()
        
        # 由於有香氣標記，機器人應該忽略這個前進指令
        self.assertFalse(robot.is_lost)
        self.assertEqual((robot.x, robot.y), (5, 2))
    
    def test_scent_does_not_affect_other_directions(self):
        """測試香氣標記只影響會掉下去的方向"""
        scent_set: Set[Tuple[int, int]] = {(5, 2)}
        robot = Robot(5, 2, 'N', 5, 5, scent_set)
        
        # 向北方前進不會掉下去，應該正常移動
        robot.move_forward()
        self.assertFalse(robot.is_lost)
        self.assertEqual((robot.x, robot.y), (5, 3))
    
    def test_multiple_scent_locations(self):
        """測試多個香氣標記位置"""
        scent_set: Set[Tuple[int, int]] = {(5, 2), (0, 3), (1, 0)}
        robot = Robot(5, 2, 'E', 5, 5, scent_set)
        
        robot.move_forward()
        self.assertFalse(robot.is_lost)


class TestRobotInstructions(unittest.TestCase):
    """測試機器人執行指令序列"""
    
    def test_execute_simple_instructions(self):
        """測試執行簡單的指令序列"""
        robot = Robot(1, 1, 'N', 5, 5)
        robot.execute_instructions("RFF")
        
        # R: 右轉（面向E），F: 前進到(2,1)，F: 前進到(3,1)
        self.assertEqual((robot.x, robot.y), (3, 1))
        self.assertEqual(robot.direction, Direction.EAST)
    
    def test_execute_complex_instructions(self):
        """測試執行複雜的指令序列"""
        robot = Robot(0, 0, 'N', 5, 5)
        robot.execute_instructions("FRFL")
        
        # F: 前進到(0,1)，R: 右轉(E)，F: 前進到(1,1)，L: 左轉(N)
        self.assertEqual((robot.x, robot.y), (1, 1))
        self.assertEqual(robot.direction, Direction.NORTH)
    
    def test_execute_instructions_with_boundary(self):
        """測試執行導致掉出邊界的指令"""
        robot = Robot(5, 5, 'N', 5, 5)
        robot.execute_instructions("F")
        
        self.assertTrue(robot.is_lost)
        self.assertEqual((robot.x, robot.y), (5, 5))
    
    def test_robot_does_not_move_after_lost(self):
        """測試機器人掉出去後不再執行指令"""
        robot = Robot(5, 5, 'N', 5, 5)
        robot.execute_instructions("FFF")
        
        # 第一個F後機器人就掉出去了，後續指令應該被忽略
        self.assertTrue(robot.is_lost)
        self.assertEqual((robot.x, robot.y), (5, 5))


class TestRobotStatus(unittest.TestCase):
    """測試機器人狀態輸出"""
    
    def test_status_format_normal(self):
        """測試正常機器人的狀態字串格式"""
        robot = Robot(1, 2, 'N', 5, 5)
        self.assertEqual(robot.get_status(), "1 2 N")
    
    def test_status_format_lost(self):
        """測試掉出去的機器人的狀態字串格式"""
        robot = Robot(5, 5, 'N', 5, 5)
        robot.move_forward()
        self.assertEqual(robot.get_status(), "5 5 N LOST")
    
    def test_status_with_different_directions(self):
        """測試不同方向的狀態字串"""
        for direction in ['N', 'S', 'E', 'W']:
            robot = Robot(3, 4, direction, 5, 5)
            expected = f"3 4 {direction}"
            self.assertEqual(robot.get_status(), expected)


class TestUVA118Examples(unittest.TestCase):
    """測試 UVA 118 的官方範例"""
    
    def test_example_1(self):
        """測試第一個官方範例"""
        scent_set: Set[Tuple[int, int]] = set()
        
        # 第一個機器人：初始位置 (1, 1, E)，指令 "RFRFRFRF"
        robot1 = Robot(1, 1, 'E', 5, 3, scent_set)
        robot1.execute_instructions("RFRFRFRF")
        self.assertEqual(robot1.get_status(), "1 1 E")
        
        # 第二個機器人：初始位置 (3, 2, N)，指令 "FRRFLLFFRRFLL"
        robot2 = Robot(3, 2, 'N', 5, 3, scent_set)
        robot2.execute_instructions("FRRFLLFFRRFLL")
        self.assertEqual(robot2.get_status(), "3 3 N LOST")
        
        # 驗證香氣標記是否被留下
        self.assertIn((3, 3), scent_set)
        
        # 第三個機器人：初始位置 (0, 3, W)，指令 "LLFFFLFLFL"
        robot3 = Robot(0, 3, 'W', 5, 3, scent_set)
        robot3.execute_instructions("LLFFFLFLFL")
        self.assertEqual(robot3.get_status(), "2 3 S")


# ============================================================================
# 主程式入口
# ============================================================================

if __name__ == '__main__':
    # 執行所有單元測試
    unittest.main(verbosity=2)
