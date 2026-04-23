import sys

input_data = sys.stdin.read().split()

if input_data:
    M = int(input_data[0])
    idx = 1
    
    for t in range(M):
        N = int(input_data[idx])
        K = int(input_data[idx+1])
        idx += 2
        
        can_be_heavy = [True] * (N + 1)
        can_be_light = [True] * (N + 1)
        
        for _ in range(K):
            P = int(input_data[idx])
            idx += 1
            
            left = [int(x) for x in input_data[idx : idx + P]]
            idx += P
            right = [int(x) for x in input_data[idx : idx + P]]
            idx += P
            
            result = input_data[idx]
            idx += 1
            
            on_scale = set(left + right)
            
            if result == '=':
                for x in on_scale:
                    can_be_heavy[x] = False
                    can_be_light[x] = False
            elif result == '<':
                for x in range(1, N + 1):
                    if x not in on_scale:
                        can_be_heavy[x] = False
                        can_be_light[x] = False
                for x in left:
                    can_be_heavy[x] = False
                for x in right:
                    can_be_light[x] = False
            elif result == '>':
                for x in range(1, N + 1):
                    if x not in on_scale:
                        can_be_heavy[x] = False
                        can_be_light[x] = False
                for x in left:
                    can_be_light[x] = False
                for x in right:
                    can_be_heavy[x] = False
                    
        suspects = []
        for i in range(1, N + 1):
            if can_be_heavy[i] or can_be_light[i]:
                suspects.append(i)
                
        if t > 0:
            print()
            
        if len(suspects) == 1:
            print(suspects[0])
        else:
            print(0)