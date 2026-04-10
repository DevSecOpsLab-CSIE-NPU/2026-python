"""
U07. 隨機種子與安全亂數。

重點：
1. `random` 是偽隨機，給相同種子會得到相同結果。
2. 若要可重現的測試或模擬，固定 seed 很有用。
3. 若牽涉密碼、token、session key，應改用 `secrets`。
"""

import random
import secrets


# ── 1. 固定種子後，序列可以完全重現 ────────────────────────
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]

random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]

print(seq1 == seq2)  # True


# ── 2. 不同 Random 物件有各自獨立的亂數流 ──────────────────
rng1 = random.Random(1)
rng2 = random.Random(2)
print(rng1.random(), rng2.random())


# ── 3. 安全用途應改用 secrets ─────────────────────────────
# `secrets` 的目標是不可預測，而不是可重現。
print(secrets.randbelow(100))
print(secrets.token_hex(16))
print(secrets.token_bytes(16))


# `random` 適合：
# - 遊戲
# - 模擬
# - 測試資料
#
# `secrets` 適合：
# - 密碼學相關
# - 驗證碼 / token
# - session key
