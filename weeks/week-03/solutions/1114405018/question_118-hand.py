import sys

L = {"N": "W", "W": "S", "S": "E", "E": "N"}
R = {"N": "E", "E": "S", "S": "W", "W": "N"}
M = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}

def main():
    a = [s.strip() for s in sys.stdin if s.strip()]
    if not a:
        return
    X, Y = map(int, a[0].split())
    scent, out, i = set(), [], 1
    while i + 1 < len(a):
        x, y, d = a[i].split()
        x, y = int(x), int(y)
        lost = False
        for c in a[i + 1]:
            if c == "L":
                d = L[d]
            elif c == "R":
                d = R[d]
            else:
                dx, dy = M[d]
                nx, ny = x + dx, y + dy
                if 0 <= nx <= X and 0 <= ny <= Y:
                    x, y = nx, ny
                elif (x, y) not in scent:
                    scent.add((x, y))
                    lost = True
                    break
        out.append(f"{x} {y} {d}" + (" LOST" if lost else ""))
        i += 2
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
    