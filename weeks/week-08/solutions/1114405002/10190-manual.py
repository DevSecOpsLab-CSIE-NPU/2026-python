# 手打版雨水體積計算程式
# 手動實現合併區間

import sys

def main():
    lines = sys.stdin.readlines()
    data = []
    for line in lines:
        data.extend(line.split())
    index = 0
    N = int(data[index])
    index += 1
    W = int(data[index])
    index += 1
    T = int(data[index])
    index += 1
    V = float(data[index])
    index += 1
    umbrellas = []
    for _ in range(N):
        x = int(data[index])
        index += 1
        l = int(data[index])
        index += 1
        v = int(data[index])
        index += 1
        umbrellas.append((x, x + l))
    
    # 手動合併區間
    if umbrellas:
        umbrellas.sort()
        merged = [umbrellas[0]]
        for start, end in umbrellas[1:]:
            if start <= merged[-1][1]:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
            else:
                merged.append((start, end))
        covered = sum(end - start for start, end in merged)
    else:
        covered = 0
    
    uncovered = W - covered
    volume = V * uncovered * T
    print(f"{volume:.2f}")

if __name__ == "__main__":
    main()