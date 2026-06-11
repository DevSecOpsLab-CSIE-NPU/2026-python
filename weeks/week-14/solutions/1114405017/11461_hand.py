import sys, math
def main():
    for line in sys.stdin:
        a,b = map(int, line.split())
        if a==0 and b==0:
            break
        print(math.isqrt(b)-math.isqrt(a-1))
if __name__ == '__main__':
    main()