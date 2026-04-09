# U07. 隨機種子與安全亂數（3.11）
#
# 這個檔案要區分兩種「隨機」概念：
# 1. random 模組是偽隨機，適合模擬、抽樣、測試與遊戲。
# 2. secrets 模組提供更適合安全用途的亂數，適合 token、密碼、session id。
# 如果牽涉安全性，不要用 random。

import random
import secrets

# 相同種子會產生相同序列，因此很適合重現測試結果。
# 這也是為什麼在模擬、教學、單元測試中常會固定 seed。
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]
random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]
print(seq1 == seq2)  # True

# 如果建立不同的 Random 實例，它們的亂數流彼此獨立。
# 這在需要多組可重現但互不干擾的隨機資料時很有用。
rng1 = random.Random(1)
rng2 = random.Random(2)
print(rng1.random(), rng2.random())  # 各自的隨機流

# secrets 模組的結果不可預測，不應該也不需要手動設 seed。
# 這類亂數用於安全場景，目標是降低被猜測或重播的風險。
print(secrets.randbelow(100))  # 密碼學安全整數
print(secrets.token_hex(16))  # 密碼學安全 hex 字串
print(secrets.token_bytes(16))  # 密碼學安全 bytes

# 重要提醒：random 模組的輸出可被推測，不適合拿來產生密碼、驗證碼、
# token 或 session key。這些安全敏感的值應該改用 secrets。
