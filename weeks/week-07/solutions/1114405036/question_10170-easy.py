# 題目 10170: 無限房間旅館 - 簡單版本
# 使用迴圈計算累積天數。

def find_group_easy(S, D):
    cum = 0
    k = 1
    while True:
        days = S + k - 1
        cum += days
        if cum >= D:
            return S + k - 1
        k += 1

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    lines = input.split()
    i = 0
    while i < len(lines):
        S = int(lines[i])
        D = int(lines[i+1])
        result = find_group_easy(S, D)
        print(result)
        i += 2