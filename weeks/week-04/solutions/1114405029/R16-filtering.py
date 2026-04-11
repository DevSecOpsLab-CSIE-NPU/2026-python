# R16. 過濾：推導式 / generator / filter / compress（1.16）

mylist = [1, 4, -5, 10]

# ── 列表推導式 (List Comprehension) ────────────────────
# 直接建立一個新的列表，包含所有符合條件 (n > 0) 的元素
# 優點：語法簡潔、執行速度快
[n for n in mylist if n > 0]  # 結果：[1, 4, 10]

# ── 產生器表達式 (Generator Expression) ────────────────
# 使用小括號 () 而非方括號 []
# 它不會立即產生整個列表，而是在需要時才逐一計算，非常節省記憶體
pos = (n for n in mylist if n > 0)

# ── 處理複雜過濾條件 ──────────────────────────────────
values = ['1', '2', '-3', '-', 'N/A']

def is_int(val):
    """檢查字串是否能成功轉換為整數"""
    try:
        int(val)
        return True
    except ValueError:
        return False

# filter(函數, 序列)：
# 當過濾邏輯較複雜（例如需要 try-except）時，使用 filter 配合自定義函數。
# filter 會回傳一個迭代器，因此通常會用 list() 將其轉回列表顯示。
list(filter(is_int, values))  # 結果：['1', '2', '-3']

# ── 使用 itertools.compress 進行過濾 ──────────────────
from itertools import compress

addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]

# 建立一個布林值列表 (True/False)，作為「篩選遮罩 (Mask)」
# 在此例中，只有當 counts 中的數值 > 5 時，對應位置才會是 True
more5 = [n > 5 for n in counts]  # 結果：[False, False, True]

# compress(資料序列, 布林序列)：
# 它會根據布林序列的 True/False 來決定是否保留資料序列中對應位置的元素
# 這裡只有第三個位置是 True，所以只會留下 'a3'
list(compress(addresses, more5))  # 結果：['a3']