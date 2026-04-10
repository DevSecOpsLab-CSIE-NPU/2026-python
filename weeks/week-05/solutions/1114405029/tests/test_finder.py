import unittest
from game.models import Card
from game.finder import HandFinder

class TestFinder(unittest.TestCase):
    def test_first_turn_restriction(self):
        """[規則測試] 遊戲第一手必須包含梅花 3"""
        hand = [Card(3,0), Card(3,1), Card(4,2), Card(4,3)] # ♣3, ♦3, ♥4, ♠4
        club_3 = Card(3, 0)
        
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play=None, must_include=club_3)
        # 所有找出來的合法組合，都必須含有 ♣3
        for play in valid_plays:
            self.assertIn(club_3, play)

    def test_find_better_combo(self):
        """[搜尋深度] 測試是否能找出壓過上家葫蘆的更大葫蘆或鐵支"""
        hand = [Card(4,0), Card(4,1), Card(4,2), Card(4,3), Card(5,0)] # 4鐵支+單張
        last_play = [Card(3,0), Card(3,1), Card(3,2), Card(8,0), Card(8,1)] # 3葫蘆
        
        valid_plays = HandFinder.get_all_valid_plays(hand, last_play=last_play)
        # 應該要能找出 4的鐵支 (帶5) 來壓過葫蘆
        self.assertTrue(len(valid_plays) > 0)