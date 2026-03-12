# R1. 序列解包（Sequence Unpacking）—— Python Cookbook 1.1

# ── 基本解包 ──────────────────────────────────────────────
# 把 tuple/list 的元素「一次展開」指派給多個變數
# 左邊變數數量必須和右邊元素數量相同，否則 ValueError
p = (4, 5)
x, y = p          # x = 4, y = 5

# 巢狀結構也可以解包：date 本身是 tuple，可以再往下拆
data = ['ACME', 50, 91.1, (2012, 12, 21)]

# 第一種：date 整體當一個變數
name, shares, price, date = data

# 第二種：同時把 date tuple 也展開成 year/mon/day
name, shares, price, (year, mon, day) = data

# ── 丟棄不需要的值 ─────────────────────────────────────────
# 慣例上用 _ 作為「我不在乎這個值」的佔位符
# 這裡只想要 shares 和 price，頭尾都不需要
_, shares, price, _ = data
