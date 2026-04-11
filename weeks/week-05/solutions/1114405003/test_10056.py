import unittest


def winning_probability(player_count, success_probability, player_index):
    # 每一輪都會從第 1 位玩家重新開始，所以可用等比級數直接求解。
    failure_probability = 1.0 - success_probability
    denominator = 1.0 - (failure_probability ** player_count)
    return (failure_probability ** (player_index - 1) * success_probability) / denominator


class TestUVA10056(unittest.TestCase):
    def test_single_player(self):
        # 只有一名玩家時，只要成功事件真的發生，他就一定會贏。
        self.assertAlmostEqual(winning_probability(1, 0.37, 1), 1.0, places=4)

    def test_four_players_half_probability_first(self):
        # p = 0.5 時，機率分布可以手算，適合驗證公式是否正確。
        self.assertAlmostEqual(winning_probability(4, 0.5, 1), 8 / 15, places=4)

    def test_four_players_half_probability_last(self):
        # 同一組條件下，最後一位玩家的機率最小。
        self.assertAlmostEqual(winning_probability(4, 0.5, 4), 1 / 15, places=4)


if __name__ == "__main__":
    unittest.main()