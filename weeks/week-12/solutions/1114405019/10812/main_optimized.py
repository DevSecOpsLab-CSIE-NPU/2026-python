import sys

# 優化版：簡化輸入處理與邏輯判斷
def solve():
    # 使用 generator 讀取輸入，減少記憶體佔用
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield int(word)

    input_gen = get_input()
    try:
        n = next(input_gen)
    except StopIteration:
        return

    for _ in range(n):
        s = next(input_gen)
        d = next(input_gen)
        
        # 合併判斷條件：s >= d 且 (s+d) 為偶數
        if s >= d and (s + d) % 2 == 0:
            print((s + d) // 2, (s - d) // 2)
        else:
            print("impossible")

if __name__ == "__main__":
    solve()
