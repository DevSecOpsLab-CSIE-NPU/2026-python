import sys
import math

def process():
    data = sys.stdin.read().split()
    idx = 0
    while idx < len(data):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        if a == 0 and b == 0:
            break
        s = math.ceil(math.sqrt(a))
        e = math.floor(math.sqrt(b))
        if s <= e:
            print(e - s + 1)
        else:
            print(0)

if __name__ == '__main__':
    process()
