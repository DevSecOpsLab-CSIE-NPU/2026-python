import sys
def solve():
    kb = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    table = str.maketrans(kb[3:], kb[:-3])
    for line in sys.stdin:
        print(line.lower().translate(table), end="")
if __name__ == "__main__":
    solve()