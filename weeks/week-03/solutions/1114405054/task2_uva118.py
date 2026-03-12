import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    
    max_x, max_y = int(input_data[0]), int(input_data[1])
    idx = 2
    scents = set()
    dirs = ['N', 'E', 'S', 'W']
    move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    
    while idx < len(input_data):
        x, y = int(input_data[idx]), int(input_data[idx+1])
        d = input_data[idx+2]
        commands = input_data[idx+3]
        idx += 4
        lost = False
        
        for cmd in commands:
            if cmd == 'L':
                d = dirs[(dirs.index(d) - 1) % 4]
            elif cmd == 'R':
                d = dirs[(dirs.index(d) + 1) % 4]
            elif cmd == 'F':
                dx, dy = move[d]
                nx, ny = x + dx, y + dy
                if 0 <= nx <= max_x and 0 <= ny <= max_y:
                    x, y = nx, ny
                else:
                    if (x, y) not in scents:
                        scents.add((x, y))
                        lost = True
                        break
        print(f"{x} {y} {d}{' LOST' if lost else ''}")

if __name__ == "__main__":
    solve()