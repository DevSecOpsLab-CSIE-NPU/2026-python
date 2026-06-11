import sys


# 精簡版的 Doomsday 解法（針對 2012 年），與完整版本相同但程式更短
DOOMSDAYS = [0, 10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


def main():
    # 讀一個整數 t，之後每行 m d
    t = int(sys.stdin.readline())
    # 2012 doomsday = Wednesday -> index 3
    doomsday = 3
    for _ in range(t):
        m, d = map(int, sys.stdin.readline().split())
        w = (doomsday + (d - DOOMSDAYS[m])) % 7
        print(WEEK[w])


if __name__ == '__main__':
    main()
