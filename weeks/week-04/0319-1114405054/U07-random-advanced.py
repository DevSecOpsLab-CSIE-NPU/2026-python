# U07. 隨機種子與安全亂數（3.11）
# random 模組為偽隨機，相同種子產生相同序列；密碼學請用 secrets

import random
import secrets

# 相同種子 → 相同序列（可重現）
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]
random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]
print(seq1 == seq2)  # True

# 不同 Random 實例各自獨立
rng1 = random.Random(1)
rng2 = random.Random(2)
print(rng1.random(), rng2.random())  # 各自的隨機流

# 密碼學安全亂數（不可預測，不能設種子）
print(secrets.randbelow(100))  # 密碼學安全整數
print(secrets.token_hex(16))  # 密碼學安全 hex 字串
print(secrets.token_bytes(16))  # 密碼學安全 bytes

# 重要：random 模組不適合密碼、token、session key 等安全場景
# 只適合遊戲、模擬、測試等非安全用途
