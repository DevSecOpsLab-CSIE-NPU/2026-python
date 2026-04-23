# 118.py
# UVA 118：機器人移動
# 功能：模擬機器人移動

from typing import Tuple, Set

class RobotSimulator:
    DIRECTIONS = ['N', 'E', 'S', 'W']
    MOVES = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.scents: Set[Tuple[int, int]] = set()
    
    def simulate_robot(self, start_x: int, start_y: int, start_dir: str, instructions: str) -> Tuple[int, int, str, bool]:
        x, y = start_x, start_y
        dir_index = self.DIRECTIONS.index(start_dir)
        lost = False
        
        for cmd in instructions:
            if cmd == 'L':
                dir_index = (dir_index - 1) % 4
            elif cmd == 'R':
                dir_index = (dir_index + 1) % 4
            elif cmd == 'F':
                dx, dy = self.MOVES[self.DIRECTIONS[dir_index]]
                new_x = x + dx
                new_y = y + dy
                
                if new_x < 0 or new_x > self.width or new_y < 0 or new_y > self.height:
                    if (x, y) in self.scents:
                        continue
                    else:
                        self.scents.add((x, y))
                        lost = True
                        break
                else:
                    x, y = new_x, new_y
        
        final_dir = self.DIRECTIONS[dir_index]
        return x, y, final_dir, lost

def process_robot_input(lines: list) -> list:
    if not lines: return []
    grid_line = lines[0].split()
    if not grid_line: return []
    width = int(grid_line[0])
    height = int(grid_line[1])
    
    simulator = RobotSimulator(width, height)
    results = []
    
    i = 1
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        robot_line = line.split()
        if len(robot_line) < 3:
            i += 1
            continue
        start_x = int(robot_line[0])
        start_y = int(robot_line[1])
        start_dir = robot_line[2]

        instructions = ""
        if i + 1 < len(lines):
            instructions = lines[i+1].strip()
            i += 2
        else:
            i += 1
        
        result = simulator.simulate_robot(start_x, start_y, start_dir, instructions)
        results.append(result)

    return results

def format_output(results: list) -> list:
    outputs = []
    for x, y, dir, lost in results:
        output = f"{x} {y} {dir}"
        if lost:
            output += " LOST"
        outputs.append(output)
    return outputs

def main():
    import sys
    lines = sys.stdin.read().splitlines()
    if not lines: return
    results = process_robot_input(lines)
    outputs = format_output(results)
    for output in outputs:
        print(output)

if __name__ == "__main__":
    main()
