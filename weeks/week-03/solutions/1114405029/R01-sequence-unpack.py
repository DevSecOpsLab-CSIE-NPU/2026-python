# R1. 序列解包（1.1）
#
# 什麼是「序列解包（sequence unpacking）」？
# - 把一個序列（例如 tuple、list）中的多個元素，一次指派到多個變數。
# - 左邊有幾個「接收位置」，右邊就必須有對應數量的元素（除非使用 * 擴充解包，這題尚未使用）。

# 1) 最基本的解包：tuple -> 兩個變數
p = (4, 5)
# 右邊 p 內有 2 個值，所以左邊也要剛好 2 個變數。
# 指派後：x = 4, y = 5
x, y = p

# 2) list 內含不同型別資料（字串、整數、浮點數、tuple）
data = ['ACME', 50, 91.1, (2012, 12, 21)]

# 直接解包第一層：
# - name   <- 'ACME'
# - shares <- 50
# - price  <- 91.1
# - date   <- (2012, 12, 21)
name, shares, price, date = data

# 巢狀解包（nested unpacking）：
# 第 4 個元素本身是 tuple，所以可在左邊再放一組括號繼續拆。
# 拆完後：
# - year = 2012, mon = 12, day = 21
name, shares, price, (year, mon, day) = data

# 3) 丟棄不需要的值（慣例用底線 _ 當占位符）
# 這行只關心 shares 和 price：
# - 第 1 個值（'ACME'）丟到 _（表示不用）
# - 第 2、3 個值分別給 shares、price
# - 第 4 個值（日期 tuple）也丟到 _
_, shares, price, _ = data

# 讀懂這段程式的重點檢查清單：
# 1. 先看右邊序列有幾層（是否有巢狀 tuple/list）。
# 2. 左邊結構要和右邊形狀對得起來（元素數量、巢狀層次）。
# 3. 只要部分資料時，用 _ 接住不需要的欄位。
# 4. 變數名稱盡量語意化（name/shares/price/year...）可讀性更高。
