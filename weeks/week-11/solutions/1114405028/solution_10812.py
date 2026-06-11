"""
UVA 10812 — Beat the Spread! 解決方案
給定和 S 與差 D，求兩隊各自得分（較大分數先輸出）

公式：
  a + b = S
  a - b = D
  a = (S + D) / 2
  b = (S - D) / 2
"""

def get_scores(s, d):
    """計算兩隊得分，回傳結果字串。"""
    if s < d or (s + d) % 2 != 0:
        return "impossible"

    larger_score = (s + d) // 2
    smaller_score = (s - d) // 2
    if smaller_score < 0:
        return "impossible"

    return f"{larger_score} {smaller_score}"


def main():
    n = int(input())
    for _ in range(n):
        s, d = map(int, input().split())
        print(get_scores(s, d))


if __name__ == "__main__":
    main()
