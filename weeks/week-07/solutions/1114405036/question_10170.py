# 題目 10170: 無限房間旅館
# 給定起始團人數 S 和天數 D，找出第 D 天住宿的旅行團人數。

def find_group(S, D):
    # 二分查找 k
    left, right = 1, 10**8  # sufficient
    while left < right:
        mid = (left + right) // 2
        cum = mid * (2 * S + mid - 1) // 2
        if cum >= D:
            right = mid
        else:
            left = mid + 1
    k = left
    # 驗證
    cum = k * (2 * S + k - 1) // 2
    if cum < D:
        return -1  # error
    return S + k - 1

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    lines = input.split()
    i = 0
    while i < len(lines):
        S = int(lines[i])
        D = int(lines[i+1])
        result = find_group(S, D)
        print(result)
        i += 2