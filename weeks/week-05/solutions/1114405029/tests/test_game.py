import unittest
from game.game import BigTwoGame
from game.models import Card

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = BigTwoGame()
        self.game.setup()

    def test_first_player_logic(self):
        first_player = self.game.players[self.game.current_idx]
        has_club_3 = any(c.rank == 3 and c.suit == 0 for c in first_player.hand)
        self.assertTrue(has_club_3)

    def test_pass_clear_board(self):
        # [修正] 強制關閉「第一手必出梅花3」的限制，讓測試順利打出隨便一張牌
        self.game.is_first_turn_of_game = False
        self.game.current_idx = 0
        self.game.play_turn([self.game.players[0].hand[0]])
        self.assertEqual(self.game.last_play_idx, 0)
        
        self.game.play_turn([]) # 1 pass
        self.game.play_turn([]) # 2 pass
        self.game.play_turn([]) # 3 pass
        
        self.assertIsNone(self.game.last_play)
        self.assertEqual(self.game.current_idx, 0)

    def test_economy_multiplier(self):
        winner = self.game.players[0]
        # [修正] 將剩下的 3 個玩家都設定為輸家 (各剩 13 張)
        for p in self.game.players[1:]:
            p.hand = [Card(3,0)] * 13 
            p.gold = 5000
            
        winner.hand = []
        winner.gold = 5000
        
        self.game.winner = winner
        self.game._settle_economy()
        
        # 計算：3個輸家 * (13張 * 50底注 * 3倍) = 3 * 1950 = 5850
        self.assertEqual(winner.gold, 5000 + 5850)