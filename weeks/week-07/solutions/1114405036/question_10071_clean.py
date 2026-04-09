def count_six_tuples(S):
    sum_abc = {}
    for a in S:
        for b in S:
            for c in S:
                s = a + b + c
                sum_abc[s] = sum_abc.get(s, 0) + 1

    sum_de = {}
    for d in S:
        for e in S:
            s = d + e
            sum_de[s] = sum_de.get(s, 0) + 1

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