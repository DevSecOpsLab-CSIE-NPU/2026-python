# U07. 隨機種子與安全亂數（3.11）
# random 模組為偽隨機，相同種子產生相同序列；密碼學請用 secrets

import random
import secrets

# 相同種子 → 相同序列（可重現）
# random 模組是「偽隨機」：只要種子相同，產生出的數列就會完全一致。
# 這對測試、模擬、示範很有用，因為結果可以重現。
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]
random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]
print("相同種子產生的兩組序列是否相同：", seq1 == seq2)  # True
print("第一次序列：", seq1)
print("第二次序列：", seq2)

# 不同 Random 實例各自獨立
# 如果不想影響全域 random 狀態，可以自己建立 Random 物件。
# 每個實例都有自己的獨立亂數流，彼此不會互相干擾。
rng1 = random.Random(1)
rng2 = random.Random(2)
print("rng1 第一個亂數：", rng1.random())
print("rng2 第一個亂數：", rng2.random())

# 密碼學安全亂數（不可預測，不能設種子）
# secrets 是給安全用途用的，像是 token、驗證碼、session key。
# 它的輸出設計成不可預測，不應該拿來做需要可重現的測試資料。
secure_number = secrets.randbelow(100)
secure_hex = secrets.token_hex(16)
secure_bytes = secrets.token_bytes(16)

print("密碼學安全整數（0~99）：", secure_number)
print("密碼學安全十六進位字串：", secure_hex)
print("密碼學安全位元組：", secure_bytes)

# 重要：random 模組不適合密碼、token、session key 等安全場景
# 只適合遊戲、模擬、測試等非安全用途
# 如果用途是登入憑證、API token、一次性密碼，請改用 secrets。
