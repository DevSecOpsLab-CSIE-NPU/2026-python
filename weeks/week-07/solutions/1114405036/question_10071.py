# 題目 10071: 計算六元組數量
# 計算滿足 a + b + c + d + e = f 的六元組數量，其中 a,b,c,d,e,f 均來自集合 S，可重複使用。

def count_six_tuples(S):
    # 使用字典來存儲所有可能的 a+b+c 的和及其出現次數
    sum_abc = {}
    for a in S:
        for b in S:
            for c in S:
                s = a + b + c
                sum_abc[s] = sum_abc.get(s, 0) + 1

    # 存儲所有可能的 d+e 的和及其出現次數
    sum_de = {}
    for d in S:
        for e in S:
            s = d + e
            sum_de[s] = sum_de.get(s, 0) + 1

    # 計算總數
    total = 0
    for f in S:
        for de_s, cnt_de in sum_de.items():
            needed = f - de_s
            if needed in sum_abc:
                total += sum_abc[needed] * cnt_de

    return total

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    S = list(map(int, data[1:]))
    result = count_six_tuples(S)
    print(result)