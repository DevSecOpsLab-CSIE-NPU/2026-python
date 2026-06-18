# -*- coding: utf-8 -*-
import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    N, M, T = int(data[0]), int(data[1]), int(data[2])
    num = N * M
    TOP, BOTTOM = num, num + 1
    parent = list(range(num + 2))
    
    def find(i):
        curr = i
        while parent[curr] != curr:
            curr = parent[curr]
        # 路徑壓縮
        temp = i
        while temp != curr:
            nxt = parent[temp]
            parent[temp] = curr
            temp = nxt
        return curr

    is_trap = [False] * num
    idx = 3
    for _ in range(T):
        r, c = int(data[idx]), int(data[idx+1])
        idx += 2
        cell = r * M + c
        
        union_roots = {find(cell)}
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if is_trap[nr * M + nc]:
                        union_roots.add(find(nr * M + nc))
                        
        if r == N - 1:
            union_roots.add(find(TOP))
        if r == 0:
            union_roots.add(find(BOTTOM))
            
        if find(TOP) in union_roots and find(BOTTOM) in union_roots:
            print(">_<")
        else:
            print("<(_ _)>")
            is_trap[cell] = True
            root_cell = find(cell)
            for rt in union_roots:
                parent[rt] = root_cell

if __name__ == "__main__":
    solve()
