import sys
import math

def cross(ax, ay, bx, by):
    return ax*by - ay*bx

def on_seg(px, py, qx, qy, rx, ry):
    return min(px,qx) <= rx <= max(px,qx) and min(py,qy) <= ry <= max(py,qy)

def seg_intersect(a,b,c,d):
    """檢查線段 AB 與 CD 是否相交（含端點）"""
    ax, ay = a; bx, by = b; cx, cy = c; dx, dy = d
    o1 = cross(bx-ax, by-ay, cx-ax, cy-ay)
    o2 = cross(bx-ax, by-ay, dx-ax, dy-ay)
    o3 = cross(dx-cx, dy-cy, ax-cx, ay-cy)
    o4 = cross(dx-cx, dy-cy, bx-cx, by-cy)
    if o1 == 0 and on_seg(ax,ay,bx,by,cx,cy): return True
    if o2 == 0 and on_seg(ax,ay,bx,by,dx,dy): return True
    if o3 == 0 and on_seg(cx,cy,dx,dy,ax,ay): return True
    if o4 == 0 and on_seg(cx,cy,dx,dy,bx,by): return True
    return (o1>0) != (o2>0) and (o3>0) != (o4>0)

def dist2(x,y):
    return x*x + y*y

def solve():
    data = sys.stdin.read().strip().splitlines()
    idx = 0
    out = []
    while idx < len(data):
        if not data[idx].strip():
            idx += 1
            continue
        n = int(data[idx]); idx += 1
        mirrors = []
        for _ in range(n):
            sx,sy,ex,ey = map(int, data[idx].split()); idx += 1
            mirrors.append(((sx,sy),(ex,ey)))
        visible = [1]*n
        for i in range(n):
            p, q = mirrors[i]
            # 多取幾個取樣點檢查
            for t in [0, 0.3, 0.5, 0.7, 1]:
                mx = p[0] + t*(q[0]-p[0])
                my = p[1] + t*(q[1]-p[1])
                blocked = False
                for j in range(n):
                    if i == j: continue
                    a, b = mirrors[j]
                    if seg_intersect((0,0),(mx,my), a, b):
                        # 檢查遮擋物是否更靠近原點
                        # 粗略判斷：遮擋物端點到原點距離最小值
                        d_block = min(dist2(*a), dist2(*b))
                        d_mirror = min(dist2(*p), dist2(*q))
                        if d_block < d_mirror:
                            blocked = True
                            break
                if not blocked:
                    break
            else:
                visible[i] = 0
        out.append(' '.join(map(str,visible)))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()