# 【Bloom 階段：U - 理解與進階應用】
# U07. 隨機數 vs 密碼級安全性
# August 的惡意提醒：在資工專業中，
# random 模組是用來做「模擬」與「數據生成」的，絕對不准用來產密碼。
# 識破這點，是你在資安（Week 15）及格的門檻。

import random
import secrets

# 1. Random: 可預測性 (適合科學模擬與遊戲)
random.seed(42)
print(f"Reproducible Random: {random.random()}")

# 2. Secrets: 不可預測性 (密碼級，OS 特權訪問)
# 適合產 token, session keys
print(f"Secure Token: {secrets.token_hex(16)}")
print(f"Secure Choice: {secrets.choice(['A', 'B', 'C'])}")

# August 指紋筆記：雖然 secrets 比較慢，但在安全性場景它是唯一的合規解。
