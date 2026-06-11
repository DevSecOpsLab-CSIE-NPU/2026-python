import sys
DOOMSDAYS = [0, 10, 21, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
def main():
    t = int(sys.stdin.readline())
    doomsday = 3
    for _ in range(t):
        m, d = map(int, sys.stdin.readline().split())
        w = (doomsday + (d - DOOMSDAYS[m])) % 7
        print(WEEK[w])
if __name__ == '__main__':
    main()