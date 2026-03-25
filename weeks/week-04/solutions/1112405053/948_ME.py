import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        M_str = next(iterator)
        M = int(M_str)
    except StopIteration:
        return

    first_case = True
    for _ in range(M):
        try:
            N = int(next(iterator))
            K = int(next(iterator))
        except StopIteration:
            break

        can_be_light = [True] * (N + 1)
        can_be_heavy = [True] * (N + 1)
        
        for _ in range(K):
            Pi = int(next(iterator))
            left_coins = []
            for _ in range(Pi):
                left_coins.append(int(next(iterator)))
            right_coins = []
            for _ in range(Pi):
                right_coins.append(int(next(iterator)))
            
            result = next(iterator)
            
            left_set = set(left_coins)
            right_set = set(right_coins)
            weighed_set = left_set | right_set
            
            if result == '=':
                for coin in weighed_set:
                    can_be_light[coin] = False
                    can_be_heavy[coin] = False
            elif result == '<':
                for i in range(1, N + 1):
                    if i not in weighed_set:
                        can_be_light[i] = False
                        can_be_heavy[i] = False
                for coin in left_set:
                    can_be_heavy[coin] = False
                for coin in right_set:
                    can_be_light[coin] = False
            elif result == '>':
                for i in range(1, N + 1):
                    if i not in weighed_set:
                        can_be_light[i] = False
                        can_be_heavy[i] = False
                for coin in left_set:
                    can_be_light[coin] = False
                for coin in right_set:
                    can_be_heavy[coin] = False
        candidates = []
        for i in range(1, N + 1):
            if can_be_light[i] or can_be_heavy[i]:
                candidates.append(i)
        if not first_case:
            print()
        first_case = False
        
        if len(candidates) == 1:
            print(candidates[0])
        else: 
            print(0)

if __name__ == '__main__':
    solve()
