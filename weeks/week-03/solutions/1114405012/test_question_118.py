import importlib.util
import unittest
from pathlib import Path


# 由於受測檔名含有連字號，不能直接使用一般 import，
# 因此這裡透過檔案路徑動態載入 QUESTION-118.py。
def load_solution_module():
    solution_path = Path(__file__).with_name("QUESTION-118.py")
    spec = importlib.util.spec_from_file_location("question_118_solution", solution_path)

    if spec is None or spec.loader is None:
        raise ImportError("無法載入 QUESTION-118.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestQuestion118(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 只在整個測試類別開始時載入一次模組即可。
        cls.solution = load_solution_module()

    def test_turn_left_from_north(self):
        # 北方左轉後應該面向西方。
        self.assertEqual(self.solution.turn_left("N"), "W")

    def test_turn_right_from_west(self):
        # 西方右轉後應該回到北方。
        self.assertEqual(self.solution.turn_right("W"), "N")

    def test_sample_input_output(self):
        # 題目官方範例必須完整對應到預期輸出。
        self.assertEqual(
            self.solution.solve(self.solution.SAMPLE_INPUT),
            self.solution.SAMPLE_OUTPUT,
        )

    def test_robot_can_be_lost_and_leave_scent(self):
        # 第二台機器人的範例會從地圖邊界掉落，並留下標記。
        scents = set()
        x, y, direction, lost = self.solution.simulate_robot(
            3,
            2,
            "N",
            "FRRFLLFFRRFLL",
            5,
            3,
            scents,
        )

        self.assertEqual((x, y, direction, lost), (3, 3, "N", True))
        self.assertIn((3, 3, "N"), scents)

    def test_scent_prevents_repeated_loss(self):
        # 若相同位置與方向已留下標記，之後的危險前進指令應被忽略。
        scents = {(3, 3, "N")}
        x, y, direction, lost = self.solution.simulate_robot(
            3,
            3,
            "N",
            "F",
            5,
            3,
            scents,
        )

        self.assertEqual((x, y, direction, lost), (3, 3, "N", False))

    def test_solve_ignores_blank_lines(self):
        # 輸入中即使夾雜空白行，也應能正確解析。
        text = """
5 3

1 1 E
RFRFRFRF

3 2 N
FRRFLLFFRRFLL
"""
        expected = "1 1 E\n3 3 N LOST"
        self.assertEqual(self.solution.solve(text), expected)


if __name__ == "__main__":
    # 直接執行本檔時，啟動 Python 內建單元測試。
    unittest.main()
