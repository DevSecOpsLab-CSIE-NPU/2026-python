# U07. 隨機種子與安全亂數（3.11）
# 本程式示範隨機數生成器的特性與安全考量：
# - random 模組為偽隨機，相同種子產生相同序列
# - 密碼學應用必須使用 secrets 模組，不可預測

import random
import secrets

# ── 偽隨機與種子 ───────────────────────────────────
# random 模組產生的是「偽隨機」數，不是真正的隨機
# 給定相同種子，會產生完全相同的序列

# 設定種子為 42
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]
print(f"第一次序列: {seq1}")

# 再次設定相同種子，得到相同序列
random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]
print(f"第二次序列: {seq2}")
print(f"序列相同: {seq1 == seq2}")  # True

# ── 獨立隨機實例 ───────────────────────────────────
# 不同 Random 實例有各自的狀態，互不影響
# 適合需要多個獨立亂數流的場合

rng1 = random.Random(1)  # 種子 1
rng2 = random.Random(2)  # 種子 2

print(f"rng1 隨機數: {rng1.random()}")
print(f"rng2 隨機數: {rng2.random()}")

# ── 密碼學安全亂數 ─────────────────────────────────
# secrets 模組提供真正的隨機數，適用於安全敏感場景
# 無法設定種子，不可預測

# 隨機整數（0 到指定值之間）
print(f"安全隨機整數: {secrets.randbelow(100)}")

# 隨機 16 字元十六進位字串（32 個字元）
print(f"安全 hex 字串: {secrets.token_hex(16)}")

# 隨機 16 位元組
print(f"安全 bytes: {secrets.token_bytes(16)}")

# ── 重要安全提醒 ───────────────────────────────────
# random 模組適用場景：
# ✓ 遊戲隨機事件
# ✓ 測試資料生成
# ✓ 模擬和統計
# ✓ 非安全性的隨機需求

# secrets 模組適用場景：
# ✓ 密碼生成
# ✓ 安全 token
# ✓ session key
# ✓ 任何需要不可預測性的場合

# 千萬不要用 random 產生密碼或安全相關的隨機值！
