import sys

def solve():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    out = []
    total_y = 0.0
    for line in data[1:1 + n]:
        nums = list(map(int, line.split()))
        for i in range(0, len(nums), 3):
            r, g, b = nums[i], nums[i+1], nums[i+2]
            x = 0.5149*r + 0.3244*g + 0.1607*b
            y = 0.2654*r + 0.6704*g + 0.0642*b
            z = 0.0248*r + 0.1248*g + 0.8504*b
            out.append(f"{x:.4f} {y:.4f} {z:.4f}")
            total_y += y
    avg = total_y / (n * n)
    out.append(f"The average of Y is {avg:.4f}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
