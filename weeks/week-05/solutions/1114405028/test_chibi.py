import unittest
from chibi_battle_easy import Warrior, battle

class TestWarrior(unittest.TestCase):
    def test_warrior_creation(self):
        w = Warrior("Test", 100, 20)
        self.assertEqual(w.name, "Test")
        self.assertEqual(w.hp, 100)
        self.assertEqual(w.attack, 20)

    def test_is_alive(self):
        w = Warrior("Test", 100, 20)
        self.assertTrue(w.is_alive())
        w.take_damage(100)
        self.assertFalse(w.is_alive())

    def test_take_damage(self):
        w = Warrior("Test", 100, 20)
        w.take_damage(30)
        self.assertEqual(w.hp, 70)

    def test_attack_enemy(self):
        w1 = Warrior("A", 100, 20)
        w2 = Warrior("B", 100, 10)
        w1.attack_enemy(w2)
        self.assertEqual(w2.hp, 80)

    def test_battle(self):
        w1 = Warrior("A", 100, 50)
        w2 = Warrior("B", 100, 20)
        winner = battle(w1, w2)
        self.assertEqual(winner, "A")

if __name__ == '__main__':
    unittest.main()