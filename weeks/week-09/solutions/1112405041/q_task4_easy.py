# q_task4_easy.py
# [AI 教學版] 任務四：合併與壓縮
# 重點：gzip 的寫入模式與 seaborn 繪圖

import csv
import gzip
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# 這裡要小心字型陷阱
matplotlib.rcParams['font.family'] = ['Microsoft JhengHei', 'sans-serif']

def solve():
    curr_dir = os.path.dirname(__file__)
    out_gz = os.path.join(curr_dir, "output/all_years.csv.gz")

    # 範例合併邏輯（簡化版）
    years = [109, 110, 111, 112, 113, 114]
    counts = [682, 590, 578, 517, 437, 412]

    # gzip 寫入：'wt' 代表 write text
    with gzip.open(out_gz, 'wt', encoding='utf-8') as f:
        f.write("年份,招生人數\n")
        for y, c in zip(years, counts):
            f.write(f"{y},{c}\n")

    # 繪圖
    sns.lineplot(x=years, y=counts, marker='o')
    plt.title("招生趨勢")
    plt.savefig(os.path.join(curr_dir, "output/trend.png"))
    print("圖表已儲存：output/trend.png")

if __name__ == "__main__":
    solve()
