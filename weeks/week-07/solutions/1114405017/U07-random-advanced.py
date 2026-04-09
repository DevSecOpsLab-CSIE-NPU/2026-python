# U07. 隨機種子與安全亂數（Python 3.11+）
# 核心觀念：random 模組使用的是 Mersenne Twister 演算法，屬於「偽隨機」（Pseudo-random），
# 其序列是可預測的。若涉及安全性（如密碼、金鑰），務必使用 secrets 模組。

import random
import secrets

# --- 1. 隨機種子 (Seed) 的特性 ---
# 設定相同的種子（Seed），會產生完全相同的隨機序列。這在「科學實驗」或「除錯」時非常有用，因為結果可重現。
random.seed(42)
seq1 = [random.randint(1, 100) for _ in range(5)]

random.seed(42)
seq2 = [random.randint(1, 100) for _ in range(5)]

print(f"序列 1: {seq1}")
print(f"序列 2: {seq2}")
print(f"兩者是否相同: {seq1 == seq2}")  # True，因為種子相同

# --- 2. 獨立的隨機實例 (Random Instances) ---
# 使用 random.Random() 類別可以建立多個獨立的隨機產生器物件，
# 它們之間的狀態是隔離的，不會互相干擾。
rng1 = random.Random(1)  # 使用種子 1 的實例
rng2 = random.Random(2)  # 使用種子 2 的實例
print(f"實例 1 隨機數: {rng1.random()}")
print(f"實例 2 隨機數: {rng2.random()}")

# --- 3. 密碼學安全亂數 (Cryptographically Secure Random Numbers) ---
# secrets 模組調用作業系統提供的強隨機源（如 Linux 的 /dev/urandom），
# 無法透過設定「種子」來預測結果，適合處理敏感資訊。

# 生成一個 0 到 99 之間的隨機整數（不包含 100）
print(f"安全隨機整數: {secrets.randbelow(100)}")

# 生成一組 16 字節（Bytes）的隨機十六進位字串（常用於 API Token 或 Reset Token）
# 16 bytes 會轉成 32 個 hex 字元
print(f"安全 Hex 字串: {secrets.token_hex(16)}")

# 生成 16 字節的原始隨機二進位資料（常用於加密金鑰或 Salt 鹽值）
print(f"安全 Bytes 資料: {secrets.token_bytes(16)}")

# --- 總結建議 ---
# 1. random 模組：
#    - 用途：遊戲機制（爆擊率）、數據模擬、自動化測試。
#    - 優點：速度快、可透過 seed 重現結果。
# 2. secrets 模組：
#    - 用途：密碼重設 Token、Session ID、密碼雜湊的鹽值 (Salt)、OAuth 狀態碼。
#    - 優點：具備密碼學強度，不可被惡意預測。