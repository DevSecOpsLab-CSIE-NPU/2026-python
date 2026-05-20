# 11332 最簡單版本 - 鏡子可見性

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def visible(i, mirrors):
    s, e = mirrors[i]
    for t in [0, 0.25, 0.5, 0.75, 1]:
        p = (s[0] + t*(e[0]-s[0]), s[1] + t*(e[1]-s[1]))
        dp = p[0]*p[0] + p[1]*p[1]
        ok = True
        
        for j in range(len(mirrors)):
            if i == j: continue
            s2, e2 = mirrors[j]
            c1, c2 = cross((0,0), p, s2), cross((0,0), p, e2)
            
            if c1*c2 <= 0 and (c1 or c2):
                d2 = min(s2[0]*s2[0]+s2[1]*s2[1], e2[0]*e2[0]+e2[1]*e2[1])
                if d2 < dp: ok = False; break
        
        if ok: return True
    return False

while True:
    n = int(input())
    if n == 0: break
    mirrors = [((int(x) for x in input().split())[0:4])]
    # Fix: proper parsing
    mirrors = []
    for _ in range(n):
        parts = list(map(int, input().split()))
        mirrors.append(((parts[0], parts[1]), (parts[2], parts[3])))
    
    print(''.join('1' if visible(i, mirrors) else '0' for i in range(n)))
