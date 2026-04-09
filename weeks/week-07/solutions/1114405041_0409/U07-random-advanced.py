# U07. 隨機種子與安全亂數（3.11）
# random 模組為偽隨機，相同種子產生相同序列；密碼學請用 secrets
# 核心觀念：
# - random：可重現、速度快，適合模擬/測試
# - secrets：不可預測，適合安全用途（密碼、token）
# 最大重點不是「怎麼產生亂數」，而是「你現在需要的是可重現，還是不可預測」。

import random
import secrets

# ── 相同種子 → 相同序列（可重現）─────────────────────
# random.seed() 會把偽隨機產生器初始化到固定狀態。
# 只要 seed 一樣，後面取出的亂數序列也會完全一樣。
# 這在除錯、教學、模擬實驗重現時非常好用。
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]

# 再次設回相同種子，序列就會從同一個起點重新開始。
random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]
print(seq1 == seq2)  # True

# ── 不同 Random 實例各自獨立 ─────────────────────────
# 若不想讓全域 random 狀態被不同函式互相影響，
# 可以自己建立獨立的 Random 物件。
# 這樣每個物件都有自己的亂數狀態，較容易控制。
rng1 = random.Random(1)
rng2 = random.Random(2)
print(rng1.random(), rng2.random())  # 各自走自己的亂數流

# ── 密碼學安全亂數（不可預測，不能設種子）─────────────
# random 的設計目標是統計上夠亂、速度快，
# 不是要抵抗猜測或攻擊，所以不適合安全用途。
# 例如密碼重設 token、驗證碼、session key，都不該用 random。

# secrets 會使用作業系統提供的安全亂數來源，
# 重點是不可預測，而不是可重現。
print(secrets.randbelow(100))  # 回傳 0~99 間的安全整數
print(secrets.token_hex(16))  # 產生 16 bytes，輸出為 32 個 hex 字元
print(secrets.token_bytes(16))  # 直接產生原始 bytes

# 重要結論：
# - 要重現結果：用 random
# - 要安全、不可預測：用 secrets
# - 不要把 random 用在密碼、token、session key 等安全場景
