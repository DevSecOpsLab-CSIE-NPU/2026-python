import sys

def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        m, n, q = map(int, sys.stdin.readline().split())

        grid = []

        for _ in range(m):
            grid.append(sys.stdin.readline().strip())

        print(m, n, q)

        for _ in range(q):
            r, c = map(int, sys.stdin.readline().split())

            target = grid[r][c]
            answer = 1
            radius = 1

            while True:
                top = r - radius
                bottom = r + radius
                left = c - radius
                right = c + radius

                if top < 0 or bottom >= m or left < 0 or right >= n:
                    break

                ok = True

                for i in range(top, bottom + 1):
                    for j in range(left, right + 1):
                        if grid[i][j] != target:
                            ok = False
                            break

                    if not ok:
                        break

                if ok:
                    answer = radius * 2 + 1
                    radius += 1
                else:
                    break

            print(answer)

if __name__ == "__main__":
    main()