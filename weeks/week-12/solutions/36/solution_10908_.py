def find_max_square(grid, r, c):

    m, n = len(grid), len(grid[0])
    
    ch = grid[r][c]
    
    size = 1
    
    for radius in range(1, max(m, n)):
        t = r - radius      
        b = r + radius      
        l = c - radius      
        right = c + radius  
        
        if t < 0 or b >= m or l < 0 or right >= n:
            break
        
        ok = True
        for j in range(l, right + 1):
            if grid[t][j] != ch or grid[b][j] != ch:
                ok = False

        for i in range(t, b + 1):
            if grid[i][l] != ch or grid[i][right] != ch:
                ok = False
        
        if ok:
            size = 2 * radius + 1
        else:
            break
    
    return size