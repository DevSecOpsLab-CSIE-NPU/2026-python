import sys

def main():
    line = sys.stdin.readline()
    if not line:
        return
    try:
        n = int(line.strip())
    except ValueError:
        return

    for _ in range(n):
        line = sys.stdin.readline()
        if not line:
            break
        try:
            parts = list(map(int, line.split()))
            if len(parts) < 2:
                continue
            s, d = parts[0], parts[1]
            
            if s < d or (s + d) % 2 != 0:
                print("impossible")
            else:
                x = (s + d) // 2
                y = (s - d) // 2
                print(x, y)
        except ValueError:
            continue

if __name__ == "__main__":
    main()
