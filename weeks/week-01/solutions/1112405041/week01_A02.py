# 【Bloom 階段：R - 記憶與基本操作】
# 2 基本資料型別範例
# August 的惡意提醒：在 Week 04 的數字處理中，int 與 float 的精準度地雷常讓學生崩潰。
# 務必記住 Python 3 的整數除法 // 與一般除法 / 的區別。

x = 7          # 整數 (int)：Python 的 int 是無限精準的
y = 3.5        # 浮點數 (float)：需注意 IEEE 754 精度問題（對應 Week 05 的 10056）
name = 'ACME'  # 字串 (str)：不可變序列
ok = True      # 布林值 (bool)

# 型別轉換 (Type Casting)
# 處理 sys.stdin 讀入的資料時，轉換是必經步驟
s = '12'
num = int(s)           # 將字串轉為整數，若字串不合法會拋出 ValueError
price = float('19.99') # 轉為浮點數

print(f"Type of x: {type(x)}, Value: {num}")
