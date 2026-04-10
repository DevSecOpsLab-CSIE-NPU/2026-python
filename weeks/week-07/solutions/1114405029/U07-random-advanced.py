# U07. 隨機種子與安全亂數（3.11）
# random 模組為偽隨機，相同種子產生相同序列；密碼學請用 secrets

import random
import secrets

# 相同種子 (Seed) 會產生「固定且可預測」的隨機序列（適用於科學實驗重現結果）
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]
random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]
print(seq1 == seq2)  # True

# 不同 Random 實例彼此獨立，擁有各自的狀態快照
rng1 = random.Random(1)
rng2 = random.Random(2)
print(rng1.random(), rng2.random())  # 兩者產生的隨機數互不干擾

# 密碼學安全亂數 (CSPRNG)：不可預測，作業系統提供的高強度隨機來源
# secrets 模組不允許設定 seed，因為它必須是不可預測的
print(secrets.randbelow(100))  # 產生 0-99 之間的隨機整數
print(secrets.token_hex(16))  # 產生隨機的 16 進位字串 (適合 Session ID)
print(secrets.token_bytes(16))  # 產生隨機的 bytes 物件

# 重要警告：
# random 模組僅適合：遊戲、蒙地卡羅模擬、一般的測試程式。
# secrets 模組必須用於：密碼、憑證 (Token)、Session Key、重設連結等涉及安全的場景。