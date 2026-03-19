# R16. 過濾：推導式 / generator / filter / compress（1.16）
# 此示例演示四種不同的數據過濾方法，用於從集合中選取符合條件的元素

# ===== 方法 1：列表推導式 (List Comprehension) =====
# 建立包含正負數的列表
mylist = [1, 4, -5, 10]

# 使用列表推導式過濾出所有正數
# [表達式 for 元素 in 迭代器 if 條件]
# 特點：返回一個完整的列表，立即計算所有結果，內存使用較多
[n for n in mylist if n > 0]  # 結果：[1, 4, 10]

# ===== 方法 2：生成器表達式 (Generator Expression) =====
# 使用生成器表達式過濾出所有正數
# (表達式 for 元素 in 迭代器 if 條件)
# 特點：返回一個生成器對象，延遲計算，按需生成元素，內存使用更高效
pos = (n for n in mylist if n > 0)  # 返回生成器，未立即計算結果

# ===== 方法 3：filter() 函數 =====
# 建立包含混合類型的列表（字符串和數字）
values = ['1', '2', '-3', '-', 'N/A']

# 定義過濾函數：檢查字符串是否可以轉換為整數
def is_int(val):
    """
    檢查給定的值是否能被轉換為整數
    - 如果轉換成功，返回 True
    - 如果轉換失敗（ValueError 異常），返回 False
    """
    try:
        int(val)  # 嘗試將值轉換為整數
        return True  # 轉換成功，返回 True
    except ValueError:  # 捕捉轉換失敗的異常
        return False  # 轉換失敗，返回 False

# 使用 filter() 函數過濾列表
# filter(函數, 迭代器)：返回一個過濾器對象
# filter() 將函數應用於迭代器的每個元素，只保留函數返回 True 的元素
# 需使用 list() 將過濾器對象轉換為列表以查看結果
list(filter(is_int, values))  # 結果：['1', '2', '-3']
[n for n in values if is_int(n)]

# ===== 方法 4：compress() 函數 =====
# 导入 compress 函数，用於根據布爾掩碼選取元素
from itertools import compress

# 建立地址列表
addresses = ['a1', 'a2', 'a3']

# 建立計數列表
counts = [0, 3, 10]

# 建立布爾掩碼：標記計數值是否大於 5 的每個對應位置
# 此列表的每個元素表示 counts 中對應位置的值是否大於 5
more5 = [n > 5 for n in counts]  # 結果：[False, False, True]

# 使用 compress() 根據布爾掩碼過濾地址
# compress(數據, 掩碼)：只選取掩碼為 True 的對應數據元素
# 特點：在需要基於另一個列表的條件進行過濾時特別有用
list(compress(addresses, more5))  # 結果：['a3']，因為只有 counts[2]=10 > 5
