import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    s = int(input_data[0])
    curr = 1
    for _ in range(s):
        n = int(input_data[curr])
        p = float(input_data[curr+1])
        i = int(input_data[curr+2])
        curr += 3

        if p == 0:
            print(f"{0.0000:.4f}")
            continue

        q = 1 - p
        # Win probability = p * q^(i-1) / (1 - q^n)
        # 加入一個極小的數避免浮點數誤差導致的四捨五入問題
        ans = (p * (q**(i-1))) / (1 - (q**n))
        # 四捨五入到四位小數
        print(f"{ans + 1e-9:.4f}")

if __name__ == "__main__":
    solve()
