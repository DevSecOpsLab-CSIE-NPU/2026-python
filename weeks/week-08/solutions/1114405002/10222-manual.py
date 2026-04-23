# 手打版優質學生判斷程式
# 手動實現質數檢查

import sys

def main():
    id = int(sys.stdin.readline().strip())
    if id < 2:
        print("no")
        return
    is_prime = True
    i = 2
    while i * i <= id:
        if id % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()