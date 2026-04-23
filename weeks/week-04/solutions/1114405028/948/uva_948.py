import sys

input = sys.stdin.read
data = input().splitlines()
idx = 0
M = int(data[idx])
idx += 1

for case in range(M):
    while idx < len(data) and data[idx].strip() == '':
        idx += 1
    N, K = map(int, data[idx].split())
    idx += 1
    weighings = []
    for _ in range(K):
        while idx < len(data) and data[idx].strip() == '':
            idx += 1
        parts = list(map(int, data[idx].split()))
        Pi = parts[0]
        left = parts[1:1+Pi]
        right = parts[1+Pi:1+2*Pi]
        idx += 1
        result = data[idx].strip()
        idx += 1
        weighings.append((left, right, result))
    
    possible = []
    for coin in range(1, N+1):
        for is_light in [True, False]:  # True: light, False: heavy
            consistent = True
            for left, right, res in weighings:
                left_has_fake = coin in left
                right_has_fake = coin in right
                if left_has_fake and right_has_fake:
                    consistent = False
                    break
                if not left_has_fake and not right_has_fake:
                    if res != '=':
                        consistent = False
                        break
                elif left_has_fake:
                    if is_light:
                        if res != '<':
                            consistent = False
                            break
                    else:  # heavy
                        if res != '>':
                            consistent = False
                            break
                elif right_has_fake:
                    if is_light:
                        if res != '>':
                            consistent = False
                            break
                    else:  # heavy
                        if res != '<':
                            consistent = False
                            break
            if consistent:
                possible.append(coin)
    
    if len(possible) == 1:
        print(possible[0])
    else:
        print(0)
    if case < M-1:
        print()