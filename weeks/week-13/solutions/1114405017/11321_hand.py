import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    N, M, T = map(int, input_data[:3])
    if N == 1:
        print('\n'.join([">_<"] * T))
        return
    parent = list(range(N * M))
    def find(i):
        """ 尋找集團的老大（含路徑壓縮，縮短以後找人的時間） """
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path: 
            parent[node] = i
        return i
    def union(i, j):
        """ 讓兩個格子認同一個老大 """
        root_i, root_j = find(i), find(j)
        if root_i != root_j:
            parent[root_i] = root_j
    has_trap = [[False] * M for _ in range(N)]
    output = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    idx = 3
    for _ in range(T):
        x, y = int(input_data[idx]), int(input_data[idx+1])
        idx += 2
        current_id = x * M + y
        all_roots = {find(current_id)}
        if x == 0:     all_roots.add(find(0 * M + y))   
        if x == N - 1: all_roots.add(find((N-1) * M + y))  
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and has_trap[nx][ny]:
                all_roots.add(find(nx * M + ny))
        has_bottom = any(find(i) in all_roots for i in range(M))         
        has_top = any(find((N - 1) * M + i) in all_roots for i in range(M))
        if has_bottom and has_top:
            output.append(">_<")
        else:
            output.append("<(_ _)>")
            has_trap[x][y] = True 
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and has_trap[nx][ny]:
                    union(current_id, nx * M + ny)
    print('\n'.join(output))
if __name__ == '__main__':
    solve()