def find_group(S, D):
    left, right = 1, 10**8
    while left < right:
        mid = (left + right) // 2
        cum = mid * (2 * S + mid - 1) // 2
        if cum >= D:
            right = mid
        else:
            left = mid + 1
    k = left
    cum = k * (2 * S + k - 1) // 2
    if cum < D:
        return -1
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