#!/usr/bin/env python3
import sys

def solve():
    parts = list(map(int, sys.stdin.read().split()))
    if not parts:
        return
    p = 0
    n = parts[p]; p+=1
    tot = 0.0
    for _ in range(n*n):
        r = parts[p]; g = parts[p+1]; b = parts[p+2]; p+=3
        X = 0.5149*r + 0.3244*g + 0.1607*b
        Y = 0.2654*r + 0.6704*g + 0.0642*b
        Z = 0.0248*r + 0.1248*g + 0.8504*b
        tot += Y
        print("{:.4f} {:.4f} {:.4f}".format(X,Y,Z))
    print("The average of Y is {:.4f}".format(tot/(n*n)))

if __name__ == '__main__':
    solve()
