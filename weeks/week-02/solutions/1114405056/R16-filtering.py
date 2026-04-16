# R16. 過濾：推導式 / generator / filter / compress（1.16）

mylist = [1, 4, -5, 10]
[n for n in mylist if n > 0]
pos = (n for n in mylist if n > 0)

values = ['1', '2', '-3', '-', 'N/A']

def is_int(val):
    try:
        int(val); return True
    except ValueError:
        return False

list(filter(is_int, values))

from itertools import compress
addresses = ['a1', 'a2', 'a3']
counts = [0, 3, 10]
more5 = [n > 5 for n in counts]
list(compress(addresses, more5))
