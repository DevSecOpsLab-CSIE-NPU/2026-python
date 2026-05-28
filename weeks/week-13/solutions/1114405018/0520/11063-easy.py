"""UVA 11063 - 簡化版：RGB -> XYZ

這個版本的重點是把輸入資料一次讀進來，再用比較直觀的方式處理：
1. 先取出矩陣大小 n
2. 再把後面的 RGB 數值每 3 個當成一組
3. 依照題目公式轉成 XYZ
4. 最後輸出每組結果，並計算 Y 的平均值

這樣寫的好處是結構清楚，適合拿來學習與比對題目公式。
"""

import sys


def solve():
    # 一次把標準輸入全部讀進來，避免逐行處理時的額外樣板程式。
    data = list(map(int, sys.stdin.read().split()))
    # 若沒有任何輸入，直接結束，避免後續索引錯誤。
    if not data:
        return

    # 第一個數字是 n，代表 n x n 張色塊資料。
    n = data[0]
    # 其餘數字才是 RGB 資料。
    vals = data[1:]
    # 理論上需要 3 * n * n 個數值，每 3 個是一組 RGB。
    expect = 3 * n * n
    # 若輸入多帶了資料，這裡只取前面題目需要的部分。
    vals = vals[:expect]

    # out_lines 用來收集每一列輸出，最後一次寫出。
    out_lines = []
    # ys 用來蒐集每組轉換後的 Y 值，以便計算平均值。
    ys = []

    # 每 3 個數字是一組 RGB，依序轉成 XYZ。
    for i in range(0, len(vals), 3):
        r, g, b = vals[i], vals[i+1], vals[i+2]
        # 依照題目給定的線性轉換公式計算 X、Y、Z。
        x = 0.5149 * r + 0.3244 * g + 0.1607 * b
        y = 0.2654 * r + 0.6704 * g + 0.0642 * b
        z = 0.0248 * r + 0.1248 * g + 0.8504 * b

        # 保存 Y 值，供最後計算平均值使用。
        ys.append(y)
        # 題目要求四位小數格式輸出。
        out_lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    # 若有資料就計算平均 Y；沒有資料時避免除以零，回傳 0.0。
    avg_y = sum(ys) / len(ys) if ys else 0.0
    out_lines.append(f"The average of Y is {avg_y:.4f}")
    # 一次輸出所有結果，避免逐行 print 造成額外開銷。
    sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
    # 直接執行此檔案時，進入解題流程。
    solve()
