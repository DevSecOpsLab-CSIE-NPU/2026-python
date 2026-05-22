import csv
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Provide font support for traditional Chinese in matplotlib
plt.rcParams['font.sans-serif'] = ['PingFang HK', 'Heiti TC', 'Microsoft JhengHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict"""
    file_path = data_dir / f"{year}年新生資料庫.csv"
    counts = {}
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row.get("系所名稱", "").strip()
            if dept:
                counts[dept] = counts.get(dept, 0) + 1
    return counts

def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所清單"""
    top_depts = set()
    for year, counts in year_data.items():
        sorted_depts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        for dept, _ in sorted_depts[:top_n]:
            top_depts.add(dept)
    
    dept_totals = {d: sum(year_data[y].get(d, 0) for y in year_data) for d in top_depts}
    sorted_top = sorted(list(top_depts), key=lambda d: dept_totals[d], reverse=True)
    return sorted_top

def plot_grouped_bar(year_data: dict[int, dict], depts: list[str], output_path: Path):
    years = sorted(list(year_data.keys()))
    
    y_labels = list(reversed(depts))
    y = np.arange(len(y_labels))
    height = 0.25
    multiplier = 0
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    for year in years:
        offset = height * multiplier
        counts = [year_data[year].get(dept, 0) for dept in y_labels]
        rects = ax.barh(y + offset, counts, height, label=str(year))
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_xlabel('人數')
    ax.set_ylabel('系所名稱')
    ax.set_title('各系招生人數比較 (任一年曾進前 8 名)')
    ax.set_yticks(y + height, y_labels)
    ax.legend(title='學年度')

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

if __name__ == "__main__":
    DATA_DIR = Path(__file__).parent.parent.parent.parent.parent / "assets" / "stu-data"
    OUTPUT_DIR = Path(__file__).parent / "output"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    years = [112, 113, 114]
    year_data = {y: load_year(y, DATA_DIR) for y in years}
    depts = get_top_depts(year_data, top_n=8)
    
    plot_grouped_bar(year_data, depts, OUTPUT_DIR / "task1.png")
    print(f"Task 1 completed. Saved to {OUTPUT_DIR / 'task1.png'}")
