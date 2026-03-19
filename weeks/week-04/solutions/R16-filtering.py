# R16. 過濾：推導式 / generator / filter / compress（1.16）
# 此程式示範 Python 中多種過濾資料的方法，包括列表推導式、生成器表達式、filter 函數和 itertools.compress。
# 過濾是指從一個序列中選取滿足特定條件的元素，這是資料處理中的常見操作。

# 建立一個包含正數、負數和零的列表 mylist
# 這個列表將用來演示不同的過濾技術
mylist = [1, 4, -5, 10]

# 使用列表推導式過濾出大於 0 的元素
# 列表推導式是 Python 中創建新列表的簡潔方式
# 語法：[表達式 for 變數 in 可迭代物件 if 條件]
# 這裡的表達式是 n，條件是 n > 0
# 結果是一個新的列表，包含所有大於 0 的元素
[n for n in mylist if n > 0]

# 使用生成器表達式過濾出大於 0 的元素
# 生成器表達式類似於列表推導式，但使用圓括號 () 而不是方括號 []
# 它返回一個生成器物件，而不是立即創建列表
# 生成器是惰性求值的，只在需要時才計算值，節省記憶體
# 這裡的 pos 是一個生成器，可以用來迭代大於 0 的元素
pos = (n for n in mylist if n > 0)

# 建立一個包含字串的列表 values
# 這些字串代表可能包含數字或無效值的資料
values = ['1', '2', '-3', '-', 'N/A']

# 定義一個函數 is_int，用來檢查一個值是否可以轉換為整數
# 這個函數使用 try-except 來處理轉換失敗的情況
# 如果 int(val) 成功執行，返回 True；否則捕獲 ValueError 並返回 False
def is_int(val):
    try:
        int(val)  # 嘗試將 val 轉換為整數
        return True  # 如果成功，返回 True
    except ValueError:  # 如果發生 ValueError，表示無法轉換
        return False  # 返回 False

# 使用 filter 函數過濾 values 列表
# filter 函數接受兩個參數：一個函數和一個可迭代物件
# 它返回一個過濾器物件，包含使函數返回 True 的元素
# 這裡使用 is_int 函數來檢查每個值是否為有效整數
# list() 用來將過濾器轉換為列表，以便查看結果
list(filter(is_int, values))

# 從 itertools 模組導入 compress 函數
# itertools 提供高效能的迭代工具
# compress 用於根據另一個可迭代物件的布林值來過濾序列
from itertools import compress

# 建立兩個列表：addresses 和 counts
# addresses 包含地址，counts 包含對應的計數值
addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]

# 創建一個布林列表 more5，表示 counts 中哪些元素大於 5
# 列表推導式 [n > 5 for n in counts] 為每個計數生成 True 或 False
# 結果：[False, False, True]，因為只有 10 > 5
more5 = [n > 5 for n in counts]

# 使用 compress 函數根據 more5 的布林值過濾 addresses
# compress(addresses, more5) 返回一個迭代器，包含 addresses 中對應 more5 為 True 的元素
# 這裡只有 'a3' 對應 True，所以結果是 ['a3']
# list() 用來將壓縮結果轉換為列表
list(compress(addresses, more5))
