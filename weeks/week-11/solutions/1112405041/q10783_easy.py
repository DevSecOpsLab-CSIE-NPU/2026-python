# AI Easy 版: 10783 Odd Sum
import sys

def solve():
    """
    計算給定範圍 [a, b] 內所有奇數的總和。
    """
    input_data = sys.stdin.read().split()
    if not input_data: return

    t_cases = int(input_data[0])
    for i in range(1, t_cases + 1):
        a = int(input_data[1 + (i-1)*2])
        b = int(input_data[2 + (i-1)*2])

        # 確保 a 是奇數，如果不是則往後找第一個奇數
        if a % 2 == 0: a += 1

        odd_sum = 0
        for num in range(a, b + 1, 2):
            odd_sum += num

        print(f"Case {i}: {odd_sum}")

if __name__ == "__main__":
    solve()
