import sys

# 【August 的惡意：身分置換】
# 此題在 QUESTION-948.md 中被魔改為「天平找假幣問題」(UVA 665)。
# 雖然題號是 948 (Fibonaccimal)，但聖經要求實作假幣偵測。

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    try:
        m_cases = int(input_data[0])
    except: return

    ptr = 1

    for case_idx in range(m_cases):
        if ptr >= len(input_data): break

        try:
            n = int(input_data[ptr])
            k = int(input_data[ptr+1])
            ptr += 2
        except: break

        # 候選人集合：True 表示可能是假的
        candidates = [True] * (n + 1)
        candidates[0] = False # 0 號不使用

        for _ in range(k):
            try:
                pi = int(input_data[ptr])
                ptr += 1
                left = [int(x) for x in input_data[ptr:ptr+pi]]
                ptr += pi
                right = [int(x) for x in input_data[ptr:ptr+pi]]
                ptr += pi
                result = input_data[ptr]
                ptr += 1
            except: break

            if result == '=':
                # 這些硬幣都是真的
                for x in left + right:
                    candidates[x] = False
            else:
                # 沒參與秤重的硬幣在不等號發生時必然是真的
                participated = set(left + right)
                for i in range(1, n + 1):
                    if i not in participated:
                        candidates[i] = False

        possible = [i for i, can in enumerate(candidates) if can]

        if case_idx > 0:
            print()

        if len(possible) == 1:
            print(possible[0])
        else:
            print(0)

if __name__ == "__main__":
    solve()
