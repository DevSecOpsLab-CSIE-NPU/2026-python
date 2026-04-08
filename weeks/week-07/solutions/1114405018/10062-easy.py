import sys


def solve_counts(counts):
    """根據題目給的 counts，重建最終排列。

    參數:
        counts: 長度為 n-1 的整數串列。
                counts[i] 代表「第 i+2 個位置」前面有多少個編號比它小。

    回傳:
        長度為 n 的排列（元素為 1..n）。

    這個版本刻意選擇「好記」而不是「最快」：
    1. 先把 1 放進答案。
    2. 依序處理 2, 3, ..., n。
    3. 每次依公式算出插入位置，直接 insert。
    """

    # 一開始只有編號 1，因為 n = len(counts) + 1。
    # 若 counts 為空，表示 n=1，答案自然是 [1]。
    ans = [1]

    # value 代表「目前要插入的牛編號」。
    # len(counts) + 2 的原因：
    # - len(counts) = n-1
    # - range(2, n+1) == range(2, len(counts)+2)
    for value in range(2, len(counts) + 2):
        # value 對應的資訊在 counts[value - 2]
        # 例如 value=2 -> counts[0]、value=3 -> counts[1]
        c = counts[value - 2]

        # 目前 ans 的長度是 value-1，且內容恰好是 1..value-1（某種順序）。
        # 由題意：在 value 前面、比 value 小的元素要有 c 個。
        # 由於目前 ans 裡全部都比 value 小，所以：
        # - value 前面元素數 = c
        # - 從左邊數第 c 個後面插入
        # - 等價成 Python 插入索引：value - 1 - c
        insert_index = value - 1 - c
        ans.insert(insert_index, value)

    return ans


def solve_text(text):
    """處理整段輸入文字，回傳題目要求的輸出字串。"""

    # split() 可以同時處理空白與換行，適合競賽輸入。
    nums = [int(x) for x in text.split()]
    if not nums:
        return ""

    # 輸入格式：
    # 第 1 個數字是 n
    # 後面 n-1 個數字是 counts
    n = nums[0]
    counts = nums[1:1 + (n - 1)]

    # 若輸入行數不足，切片會自動截斷；這裡維持簡潔寫法。
    result = solve_counts(counts)

    # 題目要求每行一個編號，因此以換行串接。
    return "\n".join(map(str, result))


def main():
    """標準競賽入口：讀 stdin，計算後輸出到 stdout。"""

    data = sys.stdin.read()
    output = solve_text(data)

    # 空輸入時不輸出任何內容，避免多印空行。
    if output:
        sys.stdout.write(output)


if __name__ == "__main__":
    main()
