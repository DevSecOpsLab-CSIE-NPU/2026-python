# 題目 10062: 乳牛排序問題 - 簡單版本
# 使用 sorted list 來處理，雖然效率較低但容易理解。

def reconstruct_cow_order_easy(N, counts):
    # 使用 sorted list 來維護可用編號
    available = sorted(list(range(1, N+1)))
    order = [0] * N

    # 從最後位置開始
    for i in range(N-1, 0, -1):  # i from N-1 down to 1
        count = counts[i-1]
        k = count + 1
        if k > len(available):
            raise ValueError("無效的count")
        num = available[k-1]
        order[i] = num
        available.remove(num)

    # 位置1 是剩下的
    order[0] = available[0]

    return order

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    counts = list(map(int, data[1:]))
    order = reconstruct_cow_order_easy(N, counts)
    for num in order:
        print(num)