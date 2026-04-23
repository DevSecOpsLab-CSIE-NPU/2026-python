import unittest

# 假設您的解答將會寫在同一個資料夾下的 solution_118.py 中
# 並且提供一個 solve_robots(world_size, robots) 函式：
# world_size: tuple (最大 X, 最大 Y)
# robots: list of tuple (初始X, 初始Y, 初始方向, 指令集字串)
# 回傳值預期為 list of strings，包含所有機器人的最後狀態。
from solution_118 import solve_robots

class TestUVA118(unittest.TestCase):
    
    def test_sample_case(self):
        """
        測試 UVA 118 題目提供的標準測資
        確保基本的 L, R, F 指令與 LOST/scent 規則能通過範例驗證
        """
        world_size = (5, 3)
        robots = [
            (1, 1, 'E', 'RFRFRFRF'),
            (3, 2, 'N', 'FRRFLLFFRRFLL'),
            (0, 3, 'W', 'LLFFFLFLFL')
        ]
        expected = [
            "1 1 E",
            "3 3 N LOST",
            "2 3 S"
        ]
        self.assertEqual(solve_robots(world_size, robots), expected)

    def test_rotation_and_movement(self):
        """
        基礎功能測試：驗證機器人的轉向 (L/R) 與前進 (F) 邏輯是否正確
        不會觸發越界
        """
        world_size = (10, 10)
        robots = [
            (5, 5, 'N', 'FF'),    # 往北走兩步
            (5, 5, 'E', 'LFF'),   # 左轉朝北，走兩步
            (5, 5, 'S', 'RRFF'),  # 右轉兩次朝北，走兩步
        ]
        expected = [
            "5 7 N",
            "5 7 N",
            "5 7 N"
        ]
        self.assertEqual(solve_robots(world_size, robots), expected)

    def test_scent_rule_same_direction(self):
        """
        進階規則測試： scent (標記) 規則
        如果有一台機器人因為 F 掉落留下標記，下一台同座標且「同方向」的機器人
        遇到致命的 F 指令時應該要忽略它，並繼續執行剩下的指令。
        """
        world_size = (2, 2)
        robots = [
            (2, 2, 'N', 'F'),    # 第一台：往北衝出邊界，於 (2,2,N) 留下 scent 並 LOST
            (2, 2, 'N', 'F'),    # 第二台：同方向前進，受 scent 保護忽略該 F 存活在 (2,2)
            (2, 2, 'N', 'FRF')   # 第三台：忽略會掉落的 F 後，繼續執行 R(轉向東) 與 F(往東前進) 
        ]
        expected = [
            "2 2 N LOST",
            "2 2 N",
            "2 1 E LOST"         # 因為轉向東後前進，(2,2,E) 沒有 scent 保護，所以 LOST
        ]
        self.assertEqual(solve_robots(world_size, robots), expected)

    def test_scent_rule_different_direction(self):
        """
        邊界陷阱測試：同座標但「不同方向」不該共用 scent
        """
        world_size = (2, 2)
        robots = [
            (2, 2, 'N', 'F'),    # 於 (2,2,N) 留下 scent
            (2, 2, 'E', 'F')     # 往東掉落，(2,2,N) 的標記「不能」保護往東掉落的機器人
        ]
        expected = [
            "2 2 N LOST",
            "2 2 E LOST"
        ]
        self.assertEqual(solve_robots(world_size, robots), expected)

if __name__ == '__main__':
    unittest.main()