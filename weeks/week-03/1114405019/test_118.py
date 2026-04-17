import unittest

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

class Test118(unittest.TestCase):

    def test_simulate_robot(self):
        # Test case 1: Robot moves and stays
        x, y, d, lost = simulate_robot(5, 3, 1, 1, 'E', 'RFRFRFRF')
        self.assertEqual((x, y, d, lost), (1, 1, 'E', False))

        # Test case 2: Robot falls off
        x, y, d, lost = simulate_robot(5, 3, 3, 2, 'N', 'FRRFLLFFRRFLL')
        self.assertEqual((x, y, d, lost), (3, 3, 'N', True))

if __name__ == '__main__':
    unittest.main()