def solve_10268_easy():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    
    idx = 0
    out = []
    while idx < len(data):
        k = int(data[idx])
        if k == 0: break
        n = int(data[idx+1])
        idx += 2
        
        if n == 0:
            out.append("0")
            continue
            
        ans = "More than 63 trials needed."
        for t in range(1, 64):
            floors = 0
            c = 1
            for i in range(1, min(k, t) + 1):
                c = c * (t - i + 1) // i
                floors += c
                
            if floors >= n:
                ans = str(t)
                break
                
        out.append(ans)
        
    if out:
        sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    solve_10268_easy()