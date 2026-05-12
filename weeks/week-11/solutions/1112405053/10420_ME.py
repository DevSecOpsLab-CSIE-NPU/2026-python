def solve():
    n, m, W = map(int, input().split())
    weights = list(map(int, input().split()))
    
    rounds = 0
    item_idx = 0  
    
    while item_idx < n:
        rounds += 1
        
        for truck in range(m):
            if item_idx >= n:
                break
            
            current_load = 0
            
            while item_idx < n and current_load + weights[item_idx] <= W:
                current_load += weights[item_idx]
                item_idx += 1
    
    print(rounds)


if __name__ == "__main__":
    solve()
