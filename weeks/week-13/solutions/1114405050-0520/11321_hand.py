import sys
sys.setrecursionlimit(20000)

def main():
    data = iter(sys.stdin.read().split())
    for n_str in data:
        N, M, T = int(n_str), int(next(data)), int(next(data))
        parent, top, bottom, grid = {}, {}, {}, set()
        
        def find(p):
            if parent[p] != p:
                parent[p] = find(parent[p])
            return parent[p]
            
        for _ in range(T):
            x, y = int(next(data)), int(next(data))
            is_top, is_bot = (x == N - 1), (x == 0)
            neighbors = []
            
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0: continue
                    if (x + dx, y + dy) in grid:
                        neighbors.append(find((x + dx, y + dy)))
                        
            will_top = is_top or any(top[r] for r in neighbors)
            will_bot = is_bot or any(bottom[r] for r in neighbors)
            
            if will_top and will_bot:
                print(">_<")
            else:
                print("<(_ _)>")
                grid.add((x, y))
                parent[(x, y)] = (x, y)
                top[(x, y)], bottom[(x, y)] = is_top, is_bot
                for r in neighbors:
                    root = find(r)
                    if root != (x, y):
                        parent[root] = (x, y)
                        top[(x, y)], bottom[(x, y)] = top[(x, y)] or top[root], bottom[(x, y)] or bottom[root]
if __name__ == '__main__': main()