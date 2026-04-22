import sys

def simulate_robot(grid_width, grid_height, start_x, start_y, direction, instructions):
    directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    turns = {'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'},
             'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}}
    scents = set()

    x, y, dir = start_x, start_y, direction
    lost = False

    for instr in instructions:
        if instr in 'LR':
            dir = turns[instr][dir]
        elif instr == 'F':
            dx, dy = directions[dir]
            nx, ny = x + dx, y + dy
            if 0 <= nx <= grid_width and 0 <= ny <= grid_height:
                x, y = nx, ny
            else:
                if (x, y) not in scents:
                    scents.add((x, y))
                    lost = True
                    break
                # If scent, ignore

    return x, y, dir, lost

def main():
    input_lines = sys.stdin.readlines()
    idx = 0
    grid_width, grid_height = map(int, input_lines[idx].split())
    idx += 1

    while idx < len(input_lines):
        start_x, start_y, direction = input_lines[idx].strip().split()
        start_x, start_y = int(start_x), int(start_y)
        instructions = input_lines[idx + 1].strip()
        idx += 2

        x, y, dir, lost = simulate_robot(grid_width, grid_height, start_x, start_y, direction, instructions)
        print(f"{x} {y} {dir}", end="")
        if lost:
            print(" LOST")
        else:
            print()

if __name__ == "__main__":
    main()