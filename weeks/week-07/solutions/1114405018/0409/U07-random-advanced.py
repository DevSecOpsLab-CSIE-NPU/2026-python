# U07. 隨機種子與安全亂數（3.11）
# 這份範例要說明兩件很重要的事：
# 1. random 模組產生的是「偽隨機」，可透過 seed() 重現相同結果，適合測試與模擬。
# 2. 如果是密碼、token、session key 這類安全用途，應該改用 secrets 模組。

import random
import secrets

# 相同種子 → 相同序列（可重現）
# random.seed() 會初始化全域亂數產生器。
# 只要種子相同，之後產生的亂數序列就會完全一致，這對除錯與測試很有用。
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]
random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]
# 因為兩次都使用相同種子，所以 seq1 和 seq2 會一模一樣。
print(seq1 == seq2)  # True

# 不同 Random 實例各自獨立
# random.Random() 可以建立獨立的亂數產生器實例。
# 每個實例都有自己的內部狀態，所以互不影響，適合需要多組獨立隨機流的情境。
rng1 = random.Random(1)
rng2 = random.Random(2)
# 雖然都屬於 random 模組，但因為種子不同，所以產生的第一個亂數也會不同。
print(rng1.random(), rng2.random())  # 各自的隨機流

# 密碼學安全亂數（不可預測，不能設種子）
# secrets 模組是為安全用途設計的，來源是系統層級的安全亂數來源。
# 它的特點是較難被預測，因此適合拿來產生密碼、驗證碼、token 等敏感資料。
print(secrets.randbelow(100))  # 密碼學安全整數
# token_hex() 會產生十六進位字串，常用於 API token、邀請碼或一次性識別值。
print(secrets.token_hex(16))  # 密碼學安全 hex 字串
# token_bytes() 直接回傳 bytes，適合需要原始位元組資料的安全場景。
print(secrets.token_bytes(16))  # 密碼學安全 bytes

# 重要：random 模組不適合密碼、token、session key 等安全場景
# 只適合遊戲、模擬、測試等非安全用途
# 簡單說：random 偏向可重現，secrets 偏向不可預測。
# 如果你的需求是「可驗證、可重播」就用 random；如果需求是「不能猜到」就用 secrets。
