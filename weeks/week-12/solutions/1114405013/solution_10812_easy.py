"""UVA 10812 - Beat the Spread!

easy 版：把題目記成一個固定公式。
已知兩隊分數和為 S、差的絕對值為 D，
就可以直接反推：
    大分 = (S + D) / 2
    小分 = S - 大分

只要記住三個檢查點就好：
1. S + D 必須是偶數，否則大分不是整數。
2. 小分不能是負數，否則不符合題意。
3. 較大的分數要先輸出。
"""


def solve(in_stream, out_stream):
    # 第一行是測資數量 n。
    n = int(in_stream.readline())

    for _ in range(n):
        # 每一筆輸入都有兩個非負整數：總和 S 和差值 D。
        s, d = map(int, in_stream.readline().split())

        # 如果 S + D 是奇數，(S + D) / 2 會不是整數，直接無解。
        if (s + d) % 2:
            out_stream.write("impossible\n")
            continue

        # 先算出較大的那一隊分數。
        big = (s + d) // 2

        # 再用總和反推較小的分數。
        small = s - big

        # 若小分小於 0，代表分數不可能成立。
        if small < 0:
            out_stream.write("impossible\n")
            continue

        # 題目要求較大的分數先印，再印較小的分數。
        out_stream.write(f"{big} {small}\n")


if __name__ == "__main__":
    import sys

    solve(sys.stdin, sys.stdout)
