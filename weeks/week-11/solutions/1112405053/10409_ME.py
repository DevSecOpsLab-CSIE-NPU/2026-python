def solve():
    n, W = map(int, input().split())
    weights = list(map(int, input().split()))
    
    weights.sort()
    
    trips = 0
    left = 0
    right = n - 1
    
    while left <= right:
        if left == right:
            trips += 1
            break
        
        if weights[left] + weights[right] <= W:
            left += 1
            right -= 1
            trips += 1
        else:
            right -= 1
            trips += 1
    
    print(trips)


if __name__ == "__main__":
    solve()
