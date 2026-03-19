# R16. 過濾：推導式 / generator / filter / compress（1.16）

# 範例資料
mylist = [1, 4, -5, 10]

# 串列推導式：直接得到結果清單（會立即計算）
positive_list = [n for n in mylist if n > 0]

# 生成器表達式：惰性計算，適合大資料量
positive_gen = (n for n in mylist if n > 0)

values = ['1', '2', '-3', '-', 'N/A']


def is_int(val):
    # 嘗試把字串轉成整數，可轉成功才回傳 True
    try:
        int(val)
        return True
    except ValueError:
        return False


# filter + 自訂判斷函式：保留可轉整數的字串
int_like_values = list(filter(is_int, values))

from itertools import compress

addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]

# 先做布林遮罩（True 的位置會被保留）
more_than_5 = [n > 5 for n in counts]

# compress：依遮罩過濾對應位置元素
filtered_addresses = list(compress(addresses, more_than_5))
