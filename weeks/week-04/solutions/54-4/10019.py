import sys

def calculate_difference(a, b):
    """
    計算兩個數字的絕對差
    參數：a, b - 兩個整數
    返回：絕對差值
    """
    return abs(a - b)

def main():
    for line in sys.stdin:
        if line.strip():
            soldiers = list(map(int, line.split()))
            if len(soldiers) == 2:
                hashmat, enemy = soldiers
                diff = calculate_difference(hashmat, enemy)
                print(diff)

if __name__ == "__main__":
    main()