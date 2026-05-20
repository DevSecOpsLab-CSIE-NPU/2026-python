# 11063 最簡單版本 - RGB 轉 XYZ

n = int(input())
pixels = []
total_y = 0

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        r, g, b = row[j*3:j*3+3]
        
        x = 0.5149*r + 0.3244*g + 0.1607*b
        y = 0.2654*r + 0.6704*g + 0.0642*b
        z = 0.0248*r + 0.1248*g + 0.8504*b
        
        pixels.append((x, y, z))
        total_y += y

for x, y, z in pixels:
    print(f"{x:.4f} {y:.4f} {z:.4f}")

print(f"The average of Y is {total_y/(n*n):.4f}")
