# R16. 過濾：推導式 / generator / filter / compress（1.16）

mylist = [1, 4, -5, 10]
[n for n in mylist if n > 0]
pos = (n for n in mylist if n > 0)

values = ['1', '2', '-3', '-', 'N/A']

def is_int(val):
    """R16. 過濾：推導式 / generator / filter / compress（1.16）

    範例說明：示範 list comprehension、generator expression、filter 與
    itertools.compress 的用法與差異。註解說明了每個步驟的目的。
    """

    mylist = [1, 4, -5, 10]

    # list comprehension：立即建立一個新列表，包含 mylist 中大於 0 的元素
    [n for n in mylist if n > 0]

    # generator expression（小括號）：懶惰求值，不會一次建立整個列表
    pos = (n for n in mylist if n > 0)

    values = ['1', '2', '-3', '-', 'N/A']

    def is_int(val):
        """嘗試將 val 轉為 int；成功回傳 True，否則（ValueError）回傳 False。

        常用於與 filter 搭配，過濾出能被視為整數的字串。
        """
        try:
            int(val)
            return True
        except ValueError:
            return False

    # 將 values 中能夠轉為整數的項目過濾出來，結果為 list
    list(filter(is_int, values))

    from itertools import compress

    addresses = ['a1', 'a2', 'a3']
    counts = [0, 3, 10]

    # more5 為布林列表，表示 counts 中每個元素是否大於 5
    more5 = [n > 5 for n in counts]

    # compress 根據 more5 的布林值選取對應的 addresses（True 表示保留）
    list(compress(addresses, more5))
