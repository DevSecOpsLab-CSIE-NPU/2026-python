"""
UVA 10908 — Largest Square 簡易版

這一版只保留最容易記憶的做法：

1. 先把查詢點本身的字元當成「目標字元」。
2. 正方形邊長從 1 開始，之後每次都只增加 2。
   原因是中心點固定在正中間，所以邊長只能是奇數。
3. 每次都檢查目前這個正方形範圍內的所有字元。
4. 只要有任何一格不是目標字元，或正方形超出網格邊界，就停止。
5. 前一次成功擴張的邊長，就是這一題的答案。

這種寫法不追求技巧，而是追求「好記、好懂、好手寫」。
因為題目的資料範圍不大，所以直接逐層檢查也足夠快速。
"""


def largest_square(grid, row, col):
    """
    回傳以 (row, col) 為中心，所有字元相同的最大奇數邊長。

    這個函式的思考方式很單純：
    - 先假設最小答案一定是 1，也就是只有中心點自己。
    - 然後嘗試把正方形一圈一圈往外擴大。
    - 每次擴大時，檢查新增的範圍是不是還全部都等於中心點字元。
    - 如果可以擴大，就繼續；如果不行，就回傳上一個成功的邊長。
    """
    rows = len(grid)
    cols = len(grid[0])
    target = grid[row][col]

    # answer 代表目前已經確認可以成立的最大邊長。
    # 一開始只看中心點自己，所以答案先設為 1。
    answer = 1

    # half 代表從中心點往上下左右各延伸幾格。
    # 例如：
    # half = 0 -> 邊長 1
    # half = 1 -> 邊長 3
    # half = 2 -> 邊長 5
    # 一般化公式就是：邊長 = 2 * half + 1
    half = 1

    while True:
        # 根據目前的 half 算出這個正方形的四個邊界。
        # top    : 最上面那一列
        # bottom : 最下面那一列
        # left   : 最左邊那一行
        # right  : 最右邊那一行
        top = row - half
        bottom = row + half
        left = col - half
        right = col + half

        # 只要任一邊超出網格範圍，就代表下一圈不能成立。
        # 因為正方形再擴下去就會碰到不存在的位置。
        if top < 0 or bottom >= rows or left < 0 or right >= cols:
            break

        # 先假設這一圈可以通過。
        # 如果檢查過程中發現不同字元，就把 ok 改成 False。
        ok = True

        # 直接把目前這個正方形範圍內的每一格都檢查一次。
        # 這是最直觀、最好記的寫法：不用特別拆成四條邊，
        # 直接看整個區域是不是全部都一樣。
        for current_row in range(top, bottom + 1):
            for current_col in range(left, right + 1):
                # 只要發現有一格不是中心點的字元，
                # 就表示這個更大的正方形不成立。
                if grid[current_row][current_col] != target:
                    ok = False
                    break
            if not ok:
                break

        # 如果這一圈失敗，就代表前一圈才是最大答案。
        if not ok:
            break

        # 如果這一圈成功，就把答案往外擴 2。
        # 因為正方形邊長只會是奇數，所以每次只加 2。
        answer += 2
        half += 1

    return answer


def main():
    """
    讀取所有測資並輸出答案。

    輸入格式：
    - 第一行：測資組數 T
    - 每組測資：
      1. M N Q
      2. M 行字元網格
      3. Q 行查詢座標 (r, c)

    輸出格式：
    - 每組測資先輸出 M N Q
    - 再依序輸出每個查詢的最大正方形邊長
    """
    test_cases = int(input())

    for _ in range(test_cases):
        # 讀取這組測資的網格大小與查詢數量。
        rows, cols, queries = map(int, input().split())

        # 讀入 M 行字元網格。
        # 每一行都是一整串字元，所以先用 strip() 去掉換行，再轉成 list。
        grid = []
        for _ in range(rows):
            grid.append(list(input().strip()))

        # 題目要求：每組測資要先印出原本的 M N Q。
        print(f"{rows} {cols} {queries}")

        # 逐一處理每個查詢座標。
        for _ in range(queries):
            row, col = map(int, input().split())
            print(largest_square(grid, row, col))


if __name__ == "__main__":
    main()