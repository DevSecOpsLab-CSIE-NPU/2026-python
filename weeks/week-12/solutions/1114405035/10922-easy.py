import sys

# 10922 - Easy Version
# 使用遞迴概念與精簡寫法

def get_degree(s):
    # 計算位數和
    n_sum = sum(int(d) for d in str(s))
    if n_sum == 9: return 1
    if n_sum % 9 != 0: return 0
    return 1 + get_degree(n_sum)

def solve():
    for line in sys.stdin:
        n = line.strip()
        if n == '0': break
        
        degree = get_degree(n)
        if degree > 0:
            print(f"{n} is a multiple of 9 and has 9-degree {degree}.")
        else:
            print(f"{n} is not a multiple of 9.")

if __name__ == "__main__":
    solve()
