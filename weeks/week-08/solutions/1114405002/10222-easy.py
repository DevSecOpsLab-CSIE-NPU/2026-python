# 簡單版優質學生判斷程式
# 使用繁體中文註解說明

import sys

def is_prime(n):
    # 判斷是否為質數
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    id = int(sys.stdin.readline().strip())  # 讀取學生編號
    if is_prime(id):  # 如果是質數
        print("yes")  # 優質學生
    else:
        print("no")  # 不是

if __name__ == "__main__":
    main()