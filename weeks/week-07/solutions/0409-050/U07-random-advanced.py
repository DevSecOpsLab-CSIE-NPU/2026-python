# U07. 隨機種子與安全亂數（3.11）
# random 模組為偽隨機，相同種子產生相同序列；密碼學請用 secrets

# 導入 random 模組：用於生成「偽亂數」(pseudo-random numbers)，運算速度較快，適合一般模擬、抽樣或遊戲。
import random
# 導入 secrets 模組：用於生成「密碼學安全的真亂數」，不可預測，適合生成密碼、安全憑證 (tokens) 或金鑰。
import secrets

# 相同種子 → 相同序列（可重現）
# 說明：random 模組底層使用數學演算法來產生看似隨機的數字。
# 如果給定相同的「種子」(seed)，演算法的起始狀態就會相同，進而產生完全一樣的亂數序列。
# 這在單元測試或需要結果可重現的科學模擬中非常有用。
random.seed(42)
# 產生 5 個 1 到 100 之間的隨機整數 
seq1 = [random.randint(1, 100) for _ in range(5)]

# 重新設定與剛剛相同的種子 42
random.seed(42)
# 再次產生 5 個隨機整數
seq2 = [random.randint(1, 100) for _ in range(5)]

# 輸出比較結果，必定為 True，因為兩次產生的序列一模一樣
print(f"seq1 == seq2: {seq1 == seq2}")  # True

# 不同 Random 實例各自獨立
# 說明：直接使用 random.randint() 等同於使用一個全域共用的產生器。
# 在多執行緒或複雜程式中，為了避免全域狀態互相干擾，可以實例化獨立的 Random 物件。
rng1 = random.Random(1)
rng2 = random.Random(2)
# 兩個獨立的產生器各自維護自己的亂數狀態 (隨機流)
print(f"rng1: {rng1.random():.4f}, rng2: {rng2.random():.4f}")

# 密碼學安全亂數（不可預測，不能設種子）
# 說明：secrets 模組使用作業系統提供的亂數來源 (例如 Linux 的 /dev/urandom)，無法藉由設定種子來預測。
print(secrets.randbelow(100))  # 產生一個 0 到 99 之間的密碼學安全隨機整數
print(secrets.token_hex(16))  # 產生 16 bytes 的隨機資料，並轉換為 32 個字元的十六進位字串 (非常適合做 API 金鑰或 Session ID)
print(secrets.token_bytes(16))  # 產生 16 bytes 的原始隨機位元組字串 (bytes)

# 重要：random 模組不適合密碼、token、session key 等安全場景
# 只適合遊戲、模擬、測試等非安全用途
# 再次強調危險性：只要駭客猜出或窮舉出 random 的種子（例如這通常會預設為系統當前時間），就能預測出接下來系統會產生的所有亂數！
