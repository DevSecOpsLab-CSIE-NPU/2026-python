"""Phase 5：遊戲流程單元測試

本測試檔對應 week-05/game_design/p5-test.md，
使用 Python 內建 unittest 驗證 BigTwoGame 的核心流程控制。
"""

import importlib
import unittest


# 動態載入，避免尚未建立模組時出現靜態匯入警告
_models_module = importlib.import_module("game.models")
_game_module = importlib.import_module("game.game")

Card = _models_module.Card
Hand = _models_module.Hand
Player = _models_module.Player
BigTwoGame = _game_module.BigTwoGame


class TestGameSetup(unittest.TestCase):
    """遊戲初始化測試。"""

    def test_game_has_4_players(self):
        # setup 後應有 4 位玩家
        game = BigTwoGame()
        game.setup()
        self.assertEqual(len(game.players), 4)

    def test_each_player_13_cards(self):
        # setup 後每位玩家應拿到 13 張牌
        game = BigTwoGame()
        game.setup()
        self.assertTrue(all(len(player.hand) == 13 for player in game.players))

    def test_total_cards_distributed(self):
        # 四位玩家手牌總數應為 52 張
        game = BigTwoGame()
        game.setup()
        total_cards = sum(len(player.hand) for player in game.players)
        self.assertEqual(total_cards, 52)

    def test_first_player_has_3_clubs(self):
        # current_player 應是持有 3♣ 的玩家
        game = BigTwoGame()
        game.setup()
        starter = game.players[game.current_player]
        self.assertTrue(any(card.rank == 3 and card.suit == 0 for card in starter.hand))

    def test_one_human_three_ai(self):
        # 預期配置為 1 位人類 + 3 位 AI
        game = BigTwoGame()
        game.setup()
        human_count = sum(1 for player in game.players if not player.is_ai)
        ai_count = sum(1 for player in game.players if player.is_ai)
        self.assertEqual(human_count, 1)
        self.assertEqual(ai_count, 3)


class TestPlayFlow(unittest.TestCase):
    """出牌流程測試。"""

    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()
        self.player = self.game.players[self.game.current_player]

    def test_play_removes_cards(self):
        # 合法出牌後，玩家手牌數應減少
        card_to_play = [self.player.hand[0]]
        before = len(self.player.hand)
        ok = self.game.play(self.player, card_to_play)
        self.assertTrue(ok)
        self.assertEqual(len(self.player.hand), before - 1)

    def test_play_sets_last_play(self):
        # 合法出牌後應設定 last_play
        card_to_play = [self.player.hand[0]]
        ok = self.game.play(self.player, card_to_play)
        self.assertTrue(ok)
        self.assertIsNotNone(self.game.last_play)

    def test_invalid_play(self):
        # 玩家手上沒有的牌，應視為非法出牌
        invalid_cards = [Card(15, 3)]
        ok = self.game.play(self.player, invalid_cards)
        self.assertFalse(ok)

    def test_pass_increments(self):
        # 過牌後 pass_count 應加 1
        before = self.game.pass_count
        ok = self.game.pass_(self.player)
        self.assertTrue(ok)
        self.assertEqual(self.game.pass_count, before + 1)


class TestTurnRules(unittest.TestCase):
    """回合判定測試。"""

    def test_three_passes_resets(self):
        # 連續 3 次過牌後，應重置 last_play 與 pass_count
        game = BigTwoGame()
        game.setup()

        player = game.players[game.current_player]
        game.play(player, [player.hand[0]])

        game.pass_count = 3
        game.check_round_reset()

        self.assertIsNone(game.last_play)
        self.assertEqual(game.pass_count, 0)

    def test_turn_rotates(self):
        # next_turn 後應輪到下一位玩家
        game = BigTwoGame()
        game.setup()
        before = game.current_player
        game.next_turn()
        self.assertEqual(game.current_player, (before + 1) % 4)


class TestWinnerRules(unittest.TestCase):
    """獲勝判定測試。"""

    def test_detect_winner(self):
        # 手牌為空者應被偵測為贏家
        game = BigTwoGame()
        game.setup()

        candidate = game.players[0]
        candidate.hand = Hand()

        winner = game.check_winner()
        self.assertIs(winner, candidate)

    def test_no_winner_yet(self):
        # 若所有玩家仍有牌，應回傳 None
        game = BigTwoGame()
        game.setup()
        winner = game.check_winner()
        self.assertIsNone(winner)

    def test_game_ends(self):
        # 有贏家後，is_game_over() 應為 True
        game = BigTwoGame()
        game.setup()

        game.players[1].hand = Hand()
        game.check_winner()

        self.assertTrue(game.is_game_over())


if __name__ == "__main__":
    unittest.main(verbosity=2)
