def can_transport(weights, m, W):
    trucks_used = 1
    current_load = 0
    
    for weight in weights:
        if current_load + weight <= W:
            current_load += weight
        else:
            trucks_used += 1
            current_load = weight
            
            if trucks_used > m:
                return False
    
    return True


def solve():
    n, m = map(int, input().split())
    weights = list(map(int, input().split()))
    
    left = max(weights)  
    right = sum(weights)  
    
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_transport(weights, m, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(result)


if __name__ == "__main__":
    solve()
