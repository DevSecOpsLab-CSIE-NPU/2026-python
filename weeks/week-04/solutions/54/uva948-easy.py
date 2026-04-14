def is_valid_coin(n, weighings):
    for coin in range(1, n + 1):
        valid = True
        for left, right, result in weighings:
            left_sum = sum(1 for c in left if c == coin)
            right_sum = sum(1 for c in right if c == coin)
            
            if left_sum > right_sum:
                if result != '>':
                    valid = False
                    break
            elif left_sum < right_sum:
                if result != '<':
                    valid = False
                    break
            else:
                if result != '=':
                    valid = False
                    break
        if valid:
            return coin
    return 0

m = int(input())
for _ in range(m):
    input()
    n, k = map(int, input().split())
    weighings = []
    for _ in range(k):
        data = list(map(int, input().split()))
        p = data[0]
        left = data[1:p+1]
        right = data[p+1:2*p+1]
        result = input().strip()
        weighings.append((left, right, result))
    
    print(is_valid_coin(n, weighings))
    if _ < m - 1:
        print()
