"""
U07. 隨機種子與安全亂數 - 單元測試
=================================
測試重點：
1. 相同種子產生相同序列（可重現）
2. 不同 Random 實例各自獨立
3. secrets 模組用於密碼學安全亂數
"""

import unittest
import random
import secrets


class TestRandomAdvanced(unittest.TestCase):
    """隨機種子與安全亂數的單元測試"""

    def test_same_seed_produces_same_sequence(self):
        """測試：相同種子產生相同序列"""
        # 第一次
        random.seed(42)
        seq1 = [random.randint(1, 100) for _ in range(5)]
        
        # 第二次
        random.seed(42)
        seq2 = [random.randint(1, 100) for _ in range(5)]
        
        # 序列應該完全相同
        self.assertEqual(seq1, seq2)

    def test_different_seeds_produce_different_sequences(self):
        """測試：不同種子產生不同序列"""
        random.seed(42)
        seq1 = [random.randint(1, 100) for _ in range(5)]
        
        random.seed(43)
        seq2 = [random.randint(1, 100) for _ in range(5)]
        
        # 序列應該不同（機率非常高）
        self.assertNotEqual(seq1, seq2)

    def test_separate_random_instances_independent(self):
        """測試：不同 Random 實例各自獨立"""
        rng1 = random.Random(1)
        rng2 = random.Random(2)
        
        # 各自產生不同的序列
        seq1 = [rng1.randint(1, 100) for _ in range(5)]
        seq2 = [rng2.randint(1, 100) for _ in range(5)]
        
        # 序列不同
        self.assertNotEqual(seq1, seq2)

    def test_same_seed_different_instances_same_sequence(self):
        """測試：相同種子的不同實例產生相同序列"""
        rng1 = random.Random(42)
        rng2 = random.Random(42)
        
        seq1 = [rng1.randint(1, 100) for _ in range(5)]
        seq2 = [rng2.randint(1, 100) for _ in range(5)]
        
        # 應該相同
        self.assertEqual(seq1, seq2)

    def test_secrets_randbelow_produces_value_in_range(self):
        """測試：secrets.randbelow 產生指定範圍內的密碼學安全整數"""
        # 產生 100 個值，確保都在 0-99 範圍內
        for _ in range(100):
            value = secrets.randbelow(100)
            self.assertGreaterEqual(value, 0)
            self.assertLess(value, 100)

    def test_secrets_token_hex_length(self):
        """測試：secrets.token_hex 產生指定字節數的十六進位字串"""
        # token_hex(16) 產生 32 個十六進位字符（每個字節2個字符）
        token = secrets.token_hex(16)
        
        self.assertEqual(len(token), 32)
        # 檢查是否全是十六進位字符
        self.assertTrue(all(c in "0123456789abcdef" for c in token))

    def test_secrets_token_bytes_length(self):
        """測試：secrets.token_bytes 產生指定字節數的安全 bytes"""
        token = secrets.token_bytes(16)
        
        self.assertEqual(len(token), 16)
        self.assertIsInstance(token, bytes)

    def test_random_vs_secrets_for_different_purposes(self):
        """測試：random vs secrets 的用途差異"""
        # random 模組可重現，適合遊戲、模擬、測試
        random.seed(42)
        game_value1 = random.randint(1, 100)
        random.seed(42)
        game_value2 = random.randint(1, 100)
        
        self.assertEqual(game_value1, game_value2)
        
        # secrets 不可預測，適合密碼、token、session key
        token1 = secrets.token_hex(16)
        token2 = secrets.token_hex(16)
        
        # 極度不可能相同
        self.assertNotEqual(token1, token2)

    def test_secrets_choices_secure_random(self):
        """測試：secrets.choice 選擇密碼學安全隨機選項"""
        choices = ["apple", "banana", "cherry", "date"]
        
        # 產生 10 個選擇，確保都在列表中
        selected = [secrets.choice(choices) for _ in range(10)]
        
        for item in selected:
            self.assertIn(item, choices)


if __name__ == "__main__":
    unittest.main()
