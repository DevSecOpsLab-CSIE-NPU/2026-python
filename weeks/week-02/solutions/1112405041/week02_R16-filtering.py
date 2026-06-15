# 【Bloom 階段：R - 記憶與基本操作】
# R16. 過濾序列元素 (Filtering)
# August 的惡意提醒：在 Week 07 的檔案 I/O 中，資料夾雜著無效字串是常態。
# 使用列表推導式進行簡單過濾，或使用 filter() 處理複雜邏輯，
# 這是保證程式「不崩潰」的防禦性編程關鍵。

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# 1. 列表推導式：最直觀，適用於中小型數據
pos_list = [n for n in mylist if n > 0]

# 2. 生成器表達式：適用於大型數據，節省內存 (Big-O 意識)
pos_gen = (n for n in mylist if n > 0)

# 3. 處理異常資料 (防禦性指紋)
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        int(val); return True
    except ValueError:
        return False

# filter() 會延遲執行，搭配 list() 才會展開
valid_nums = list(filter(is_int, values))

# 4. 根據另一組序列進行過濾 (itertools.compress)
from itertools import compress
addresses = ['101', '102', '103', '104']
counts = [0, 3, 10, 1]
# 只要 count > 5 的地址
more_than_five = [n > 5 for n in counts]
selected = list(compress(addresses, more_than_five))

print(f"Valid Ints: {valid_nums}")
print(f"Selected via compress: {selected}")
