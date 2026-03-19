"""R16: 多種過濾技巧 (list comp / generator / filter / compress)。"""

from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print('正數(list comprehension):', [n for n in mylist if n > 0])
print('負數(generator):', list(n for n in mylist if n < 0))

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


print('可轉 int 的字串:', list(filter(is_int, values)))

addresses = ['A 棟', 'B 棟', 'C 棟', 'D 棟']
counts = [0, 3, 10, 2]
more_than_2 = [n > 2 for n in counts]
print('符合條件地址(compress):', list(compress(addresses, more_than_2)))
