import sys

def solve():
    first_line = sys.stdin.readline().split()
    if not first_line: return
    max_x, max_y = int(first_line[0]), int(first_line[1])
    
    scents = []
    
    while True:
        pos_data = sys.stdin.readline().split()
        if not pos_data: break
        
        curr_x = int(pos_data[0])
        curr_y = int(pos_data[1])
        facing = pos_data[2]
        actions = sys.stdin.readline().strip()
        
        dir_list = ['N', 'E', 'S', 'W']
        lost = False
        
        for act in actions:
            if act == 'R':
                idx = dir_list.index(facing)
                facing = dir_list[(idx + 1) % 4]
            elif act == 'L':
                idx = dir_list.index(facing)
                facing = dir_list[(idx - 1) % 4]
            elif act == 'F':
                next_x, next_y = curr_x, curr_y
                if facing == 'N': next_y += 1
                elif facing == 'E': next_x += 1
                elif facing == 'S': next_y -= 1
                elif facing == 'W': next_x -= 1
                
                if next_x < 0 or next_x > max_x or next_y < 0 or next_y > max_y:
                    if (curr_x, curr_y) in scents:
                        continue
                    else:
                        scents.append((curr_x, curr_y))
                        lost = True
                        break
                else:
                    curr_x, curr_y = next_x, next_y
        
        output = f"{curr_x} {curr_y} {facing}"
        if lost: output += " LOST"
        print(output)

if __name__ == "__main__":
    solve()