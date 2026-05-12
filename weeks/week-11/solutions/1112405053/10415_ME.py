def solve():
    n, W = map(int, input().split())
    
    categories = {}
    for _ in range(n):
        w, c = map(int, input().split())
        if c not in categories:
            categories[c] = []
        categories[c].append(w)
    
    total_trips = 0
    
    for category, weights in categories.items():
        weights.sort()
        
        left = 0
        right = len(weights) - 1
        
        while left <= right:
            if left == right:
                total_trips += 1
                break
            
            if weights[left] + weights[right] <= W:
                left += 1
                right -= 1
                total_trips += 1
            else:
                right -= 1
                total_trips += 1
    
    print(total_trips)


if __name__ == "__main__":
    solve()
