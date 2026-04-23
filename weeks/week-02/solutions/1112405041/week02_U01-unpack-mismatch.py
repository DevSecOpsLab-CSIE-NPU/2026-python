# 【Bloom 階段：U - 理解與進階應用】
# U1. 解包數量不匹配地雷 (ValueError)
# August 的惡意提醒：在 Week 03 解析 CPE 測資時，若沒注意到最後一行
# 只有兩個欄位（例如：0 0 結束標記），直接用 x, y, z = line.split() 會炸掉。

p = (4, 5)
try:
    # 這裡會噴 ValueError: too many values to unpack (expected 3)
    x, y, z = p
except ValueError as e:
    print(f"August 的惡意地雷觸發：{e}")

# August 的防禦性建議：
# 1. 使用 len() 預先檢查
# 2. 使用星號解包 (Star Unpacking) 來處理變動長度
