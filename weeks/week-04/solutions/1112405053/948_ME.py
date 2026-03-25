import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        num_datasets_str = next(iterator, None)
        if num_datasets_str is None:
            return
        M = int(num_datasets_str)
    except StopIteration:
        return
        
    for i in range(M):
        try:
            N = int(next(iterator))
            K = int(next(iterator))
        except StopIteration:
            break
            
        all_coins = set(range(1, N + 1))
        potential_light = set(all_coins)
        potential_heavy = set(all_coins)
        
        for _ in range(K):
            try:
                P = int(next(iterator))
                
                left = []
                for _ in range(P):
                    left.append(int(next(iterator)))
                    
                right = []
                for _ in range(P):
                    right.append(int(next(iterator)))
                    
                operator = next(iterator)
                
                left_set = set(left)
                right_set = set(right)
                on_scale = left_set | right_set
                off_scale = all_coins - on_scale
                
                if operator == '=':
                    potential_light -= on_scale
                    potential_heavy -= on_scale
                elif operator == '<':
                    potential_light -= off_scale
                    potential_heavy -= off_scale
                    potential_light -= right_set
                    potential_heavy -= left_set
                    
                elif operator == '>':
                    potential_light -= off_scale
                    potential_heavy -= off_scale
                    potential_light -= left_set
                    potential_heavy -= right_set
                    
            except StopIteration:
                break
                
        candidates = list(potential_light | potential_heavy)
        
        if i > 0:
            print()
            
        if len(candidates) == 1:
            print(candidates[0])
        else:
            print(0)

if __name__ == "__main__":
    solve()
