# q_task4_hand.py
# 題目四：合併六年資料並壓縮封存＋趨勢視覺化
# 關鍵：處理 Gzip 讀寫與 Seaborn 中文字型顯示

import csv
import gzip
import os
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from collections import Counter

# 設定中文字型 (依據 August Spec 可能需要手動指定路徑)
matplotlib.rcParams['font.family'] = ['Microsoft JhengHei', 'Taipei Sans TC Beta', 'sans-serif']
matplotlib.rcParams['axes.unicode_minus'] = False

def solve():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "../../../../assets/stu-data/")
    output_dir = os.path.join(base_dir, "output")
    gz_file = os.path.join(output_dir, "all_years.csv.gz")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    all_data = []
    years = [109, 110, 111, 112, 113, 114]

    # 1. 讀取並合併
    fieldnames = []
    for year in years:
        file_path = os.path.join(data_dir, f"{year}年新生資料庫.csv")
        with open(file_path, mode='r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            if not fieldnames:
                fieldnames = reader.fieldnames + ['年份']
            for row in reader:
                row['年份'] = year
                all_data.append(row)

    # 2. 寫入壓縮檔
    with gzip.open(gz_file, mode='wt', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)

    # 3. 讀取驗證與統計
    counts = []
    with gzip.open(gz_file, mode='rt', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data_list = list(reader)
        year_counter = Counter(row['年份'] for row in data_list)
        for year in years:
            c = year_counter[str(year)]
            counts.append(c)
            print(f"{year} 年：{c} 人")

    print(f"壓縮後大小：{os.path.getsize(gz_file)} bytes")

    # 4. 視覺化
    plt.figure(figsize=(10, 6))
    sns.set_theme(style="whitegrid")
    # 陷阱：Seaborn 的 lineplot 需要確保數據類型正確
    ax = sns.lineplot(x=years, y=counts, marker='o', linewidth=2.5, color='royalblue')

    for i, count in enumerate(counts):
        plt.text(years[i], count + 5, str(count), ha='center', fontweight='bold')

    plt.title("澎科大 109～114 學年度招生人數趨勢", fontsize=15)
    plt.xlabel("學年度", fontsize=12)
    plt.ylabel("招生人數", fontsize=12)

    plt.savefig(os.path.join(output_dir, "trend.png"), dpi=150, bbox_inches='tight')
    print(f"圖表已儲存：output/trend.png")

if __name__ == "__main__":
    solve()
