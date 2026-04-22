# R16. 過濾：推導式 / generator / filter / compress（1.16）
# 本檔示範四種常見過濾方式，並比較它們各自適用時機。

from itertools import compress

mylist = [1, 4, -5, 10, -7, 3]

# 1) 串列推導式：立即產生結果，最直覺。
positives = [n for n in mylist if n > 0]
print("推導式過濾正數:", positives)

# 2) 生成器表達式：延遲計算，適合大資料流。
pos_gen = (n for n in mylist if n > 0)
print("生成器第一次取值:", next(pos_gen))
print("生成器剩餘值:", list(pos_gen))

values = ["1", "2", "-3", "-", "N/A", "5"]


def is_int(val):
    """回傳字串是否可安全轉成 int。"""
    try:
        int(val)
        return True
    except ValueError:
        return False


# 3) filter + 驗證函式：當規則適合抽成函式時可讀性高。
ints_only = list(filter(is_int, values))
print("可轉 int 的字串:", ints_only)

addresses = ["a1", "a2", "a3"]
counts = [0, 3, 10]

# 4) compress：用布林選擇器（mask）選資料，常見於平行陣列。
more_than_5 = [n > 5 for n in counts]
selected = list(compress(addresses, more_than_5))
print("布林遮罩:", more_than_5)
print("compress 選出的地址:", selected)
