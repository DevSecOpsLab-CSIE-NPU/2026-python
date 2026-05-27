"""UVA 10812 - Beat the Spread!

主版本：保留清楚的判斷流程，方便閱讀與除錯。
"""


def solve(in_stream, out_stream):
    # 讀入測試資料組數
    t_line = in_stream.readline().strip()
    if not t_line:
        return

    t = int(t_line)

    for _ in range(t):
        # 每筆資料包含總和 S 與差值 D
        s, d = map(int, in_stream.readline().split())

        # 若 S + D 是奇數，代表較大分數不是整數，直接無解
        if (s + d) % 2 != 0:
            out_stream.write("impossible\n")
            continue

        high = (s + d) // 2
        low = (s - d) // 2

        # 低分不能是負數，否則不符合題意
        if low < 0:
            out_stream.write("impossible\n")
            continue

        # 題目要求較大的分數先輸出
        out_stream.write(f"{high} {low}\n")


if __name__ == "__main__":
    import sys

    solve(sys.stdin, sys.stdout)
