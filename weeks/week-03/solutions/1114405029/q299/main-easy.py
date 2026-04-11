import sys

# 詳細繁體中文註解說明：
# 這題問的是「最少交換幾次相鄰車廂」才能排好。
# 其實這就是「泡沫排序法」的工作原理：
# 每次看到左邊比右邊大，就交換它們，直到全部排好。
# 總共交換了幾次，就是答案。

def solve():
    # 第一行是告訴我們總共有幾組題目要算
    first_line = sys.stdin.readline()
    if not first_line:
        return
    n = int(first_line)

    for _ in range(n):
        # 讀取火車長度 L
        l_line = sys.stdin.readline()
        if not l_line:
            break
        length = int(l_line)
        
        # 讀取現在火車車廂的編號清單
        # 因為輸入可能會有空格或換行，我們用 split() 切開後轉成數字列表
        cars = []
        while len(cars) < length:
            cars.extend(map(int, sys.stdin.readline().split()))
        
        swaps = 0
        # 開始跑兩層迴圈進行「泡沫排序」
        for i in range(length):
            for j in range(0, length - i - 1):
                # 如果左邊的車廂編號比右邊的大，就交換
                if cars[j] > cars[j+1]:
                    # 交換兩個變數的值
                    cars[j], cars[j+1] = cars[j+1], cars[j]
                    # 紀錄交換了一次
                    swaps += 1
        
        # 最後印出題目規定的句子，其中 {swaps} 會被換成數字
        print(f"Optimal train swapping takes {swaps} swaps.")

if __name__ == "__main__":
    solve()