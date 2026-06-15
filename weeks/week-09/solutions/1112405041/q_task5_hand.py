# q_task5_hand.py
# 題目五：用 pickle 建立年度招生統計快取＋入學方式分佈圖
# 關鍵：對象序列化與 Counter 整合應用

import csv
import os
import pickle
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = ['Microsoft JhengHei', 'Taipei Sans TC Beta', 'sans-serif']

def get_stats(year):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, f"../../../../assets/stu-data/{year}年新生資料庫.csv")
    cache_file = os.path.join(base_dir, f"output/{year}_stats.pkl")

    # 1. 檢查快取
    if os.path.exists(cache_file):
        print(f"「從快取載入」：{year}")
        with open(cache_file, 'rb') as f:
            return pickle.load(f)

    # 2. 重新計算
    print(f"「重新計算並快取」：{year}")
    stats = {'total': 0, 'by_admission': Counter(), 'by_dept': Counter(), 'top_school': ""}
    schools = Counter()

    with open(input_file, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stats['total'] += 1
            stats['by_admission'][row['入學方式']] += 1
            stats['by_dept'][row['系所名稱']] += 1
            schools[row['畢業學校']] += 1

    stats['top_school'] = schools.most_common(1)[0][0] if schools else "N/A"

    # 存檔
    with open(cache_file, 'wb') as f:
        pickle.dump(stats, f)

    return stats

def solve():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "output")

    # 測試快取邏輯
    for year in [112, 113, 112, 113]:
        stats = get_stats(year)
        top = max(stats['by_admission'], key=stats['by_admission'].get)
        print(f"{year} 年｜總人數：{stats['total']}｜最多入學方式：{top}")

    # 視覺化 113 年
    stats_113 = get_stats(113)
    by_adm = stats_113['by_admission'].most_common()

    labels = [x[0] for x in by_adm]
    counts = [x[1] for x in by_adm]

    plt.figure(figsize=(12, 8))
    sns.barplot(x=counts, y=labels, hue=labels, palette="viridis", legend=False)
    plt.title("113 學年度入學方式分佈", fontsize=16)
    plt.xlabel("人數", fontsize=12)
    plt.tight_layout()

    plt.savefig(os.path.join(output_dir, "113_admission.png"), dpi=150)
    print("圖表已儲存：output/113_admission.png")

if __name__ == "__main__":
    solve()
