# AI Easy 版: 10812 Beat the Spread!
import sys

def solve():
    """
    已知兩隊得分之和 S 與之差 D，求兩隊得分 a, b (a >= b)。
    方程：a + b = S, a - b = D
    解得：a = (S + D) / 2, b = (S - D) / 2
    條件：S >= D 且 (S + D) 必須為偶數。
    """
    input_data = sys.stdin.read().split()
    if not input_data: return

    t_cases = int(input_data[0])
    for i in range(1, t_cases + 1):
        s = int(input_data[1 + (i-1)*2])
        d = int(input_data[2 + (i-1)*2])

        # 檢查是否有整數解且非負
        if s < d or (s + d) % 2 != 0:
            print("impossible")
        else:
            a = (s + d) // 2
            b = s - a
            print(f"{a} {b}")

if __name__ == "__main__":
    solve()
