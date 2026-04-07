import sys

def calculate_difference_simple(a, b):
    """
    簡易版本：計算絕對差
    """
    if a > b:
        return a - b
    else:
        return b - a

def main():
    for line in sys.stdin:
        if line.strip():
            soldiers = list(map(int, line.split()))
            if len(soldiers) == 2:
                hashmat, enemy = soldiers
                diff = calculate_difference_simple(hashmat, enemy)
                print(diff)

if __name__ == "__main__":
    main()