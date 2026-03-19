# R16. 過濾：推導式 / generator / filter / compress（1.16）
# 展示多種 Python 過濾資料的方法

# 原始數列
mylist = [1, 4, -5, 10]

# 方法 1：列表推導式（list comprehension）- 建立新列表
print("方法 1 - 列表推導式:", [n for n in mylist if n > 0])  # 結果：[1, 4, 10] 類型為 list

# 方法 2：生成器表達式（generator expression）- 惰性求值，節省記憶體
pos = (n for n in mylist if n > 0)  # 回傳生成器物件，直到被迭代時才計算
print("方法 2 - 生成器表達式:", list(pos))

# 建立包含各種類型值的列表
values = ['1', '2', '-3', '-', 'N/A']

# 定義函數：檢查字串是否能轉換為整數
def is_int(val):
    try:
        int(val)  # 嘗試轉換
        return True
    except ValueError:  # 無法轉換時拋出異常
        return False

# 方法 3：filter() 函數 - 使用謂詞函數過濾
print("方法 3 - filter 函數:", list(filter(is_int, values)))  # 結果：['1', '2', '-3']，非整數字串被過濾

# 導入 compress 函數
from itertools import compress

# 準備資料：地址列表和計數列表
addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]

# 方法 4：compress() - 根據布林值選擇器過濾
# 建立布林值選擇器：檢查每個計數是否大於 5
more5 = [n > 5 for n in counts]  # [False, False, True]
# compress 只保留對應位置為 True 的元素
print("方法 4 - compress:", list(compress(addresses, more5)))  # 結果：['a3']
