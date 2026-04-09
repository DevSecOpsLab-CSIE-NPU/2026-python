# 題目 10071: 計算六元組數量 - 簡單版本
# 使用暴力枚舉所有組合，適合小 N。

def count_six_tuples_easy(S):
    count = 0
    for a in S:
        for b in S:
            for c in S:
                for d in S:
                    for e in S:
                        for f in S:
                            if a + b + c + d + e == f:
                                count += 1
    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    S = list(map(int, data[1:]))
    result = count_six_tuples_easy(S)
    print(result)