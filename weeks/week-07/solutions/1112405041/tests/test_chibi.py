import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import os
from chibi_battle import ChibiBattle

class TestChibiBattle(unittest.TestCase):
    def setUp(self):
        # ç¢ºä?æ¸¬è©¦?°å???generals.txt
        # ?™æ˜¯?ºä?è§?±ºè·¯å??°é›·ï¼Œæ??•æ?å®šç?å°è·¯å¾?
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.test_file = os.path.join(current_dir, "..", "..", "generals.txt")

        self.game = ChibiBattle()
        self.game.load_generals(self.test_file)

    def test_load_count(self):
        """æ¸¬è©¦ 1: ?¯å¦è®€??9 ä½æ­¦å°?""
        self.assertEqual(len(self.game.generals), 9)

    def test_specific_general(self):
        """æ¸¬è©¦ 2: é©—è??œç¾½å±¬æ€?""
        if '?œç¾½' in self.game.generals:
            guanyu = self.game.generals['?œç¾½']
            self.assertEqual(guanyu.faction, '?€')
            self.assertEqual(guanyu.atk, 28)
        else:
            self.fail("?œç¾½ä¸åœ¨æ­¦å??å–®ä¸?)

    def test_battle_order(self):
        """æ¸¬è©¦ 3: é©—è??Ÿåº¦?’å?"""
        order = self.game.get_battle_order()
        if order:
            self.assertGreaterEqual(order[0].spd, order[-1].spd)
        else:
            self.fail("?’å?çµæ??ºç©º")

    def test_damage_calc(self):
        """æ¸¬è©¦ 4: ?·å®³è¨ˆç??è¼¯"""
        # ?¹æ?(28) vs ?‰å?(16) => 12 ?·å®³
        if '?¹æ?' in self.game.generals and '?‰å?' in self.game.generals:
            dmg = self.game.calculate_damage('?¹æ?', '?‰å?')
            self.assertEqual(dmg, 12)

    def test_counter_stat(self):
        """æ¸¬è©¦ 5: Counter ?·å®³ç´¯å?"""
        if '?œç¾½' in self.game.generals and '?¹æ?' in self.game.generals:
            self.game.calculate_damage('?œç¾½', '?¹æ?')
            self.game.calculate_damage('?œç¾½', '?¹æ?')
            # ?œç¾½(28) - ?¹æ?(16) = 12; 12 * 2 = 24
            self.assertEqual(self.game.stats['damage']['?œç¾½'], 24)

    def test_faction_stats(self):
        """æ¸¬è©¦ 6: ?¢å?çµ±è?"""
        self.game.simulate_battle()
        stats = self.game.get_faction_stats()
        self.assertTrue('?€' in stats or '?? in stats or 'é­? in stats)

    def test_ranking_length(self):
        """æ¸¬è©¦ 7: ?’å??·åº¦"""
        self.game.simulate_battle()
        ranking = self.game.get_damage_ranking()
        self.assertLessEqual(len(ranking), 5)

    def test_eof_handling(self):
        """æ¸¬è©¦ 8: EOF ?•ç?"""
        self.assertEqual(len(self.game.generals), 9)

if __name__ == "__main__":
    unittest.main()

