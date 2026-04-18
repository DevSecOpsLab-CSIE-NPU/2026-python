import random
import secrets

# ── random.seed：讓隨機序列可重現 ────────────────────────
# 設定相同的種子值，之後產生的「隨機」序列會完全相同
# 適合用於測試、除錯、實驗可重現性
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]

random.seed(42)  # 重設相同種子
seq2 = [random.randint(1, 100) for _ in range(5)]

print(seq1 == seq2)  # True：兩次產生的序列完全相同

# ── random.Random：獨立的隨機數生成器實例 ────────────────
# 每個 random.Random 物件擁有獨立狀態，互不影響
# 適合在多執行緒或需要多個獨立亂數串流的場景
rng1 = random.Random(1)   # 種子為 1
rng2 = random.Random(2)   # 種子為 2，與 rng1 互相獨立
print(rng1.random(), rng2.random())  # 各自產生 [0.0, 1.0) 的浮點數

# ── secrets：密碼學安全的隨機數 ──────────────────────────
# random 模組使用 Mersenne Twister 演算法，不適合安全用途
# secrets 使用作業系統提供的加密安全亂數源（如 /dev/urandom）
# 應用場景：產生密碼、API 金鑰、CSRF token、重設密碼連結等

# 產生 [0, 100) 的加密安全隨機整數
print(secrets.randbelow(100))

# 產生 16 bytes 的隨機資料並以十六進位字串表示（共 32 個字元）
print(secrets.token_hex(16))    # 例：'a3f1c87b2e94d056...'

# 產生 16 bytes 的原始隨機位元組
print(secrets.token_bytes(16))  # 例：b'\x9d\x4a...'
