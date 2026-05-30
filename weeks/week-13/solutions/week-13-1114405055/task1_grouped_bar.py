import csv
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Font configuration
mpl.rcParams['font.sans-serif'] = ['Noto Sans CJK JP', 'Noto Sans CJK TC', 'WenQuanYi Micro Hei', 'Taipei Sans TC Beta', 'sans-serif']
mpl.rcParams['axes.unicode_minus'] = False # for minus sign

DATA_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / "assets" / "stu-data"

def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict"""
    file_path = data_dir / f"{year}年新生資料庫.csv"
    if not file_path.exists():
        return {}
    
    counts = {}
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row.get('系所名稱')
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
    
    return sorted(list(top_depts))

if __name__ == "__main__":
    years = [112, 113, 114]
    year_data = {year: load_year(year, DATA_DIR) for year in years}
    
    top_depts = get_top_depts(year_data, top_n=8)
    
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    
    # Plot grouped bar
    fig, ax = plt.subplots(figsize=(12, 8))
    
    y = np.arange(len(top_depts))  
    height = 0.25  
    multiplier = 0
    
    for year in years:
        values = [year_data[year].get(dept, 0) for dept in top_depts]
        offset = height * multiplier
        rects = ax.barh(y + offset, values, height, label=f"{year}")
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_ylabel('系所名稱')
    ax.set_xlabel('人數')
    ax.set_title('比較 112、113、114 學年度各系招生人數')
    # Center y-ticks in middle of group
    ax.set_yticks(y + height, top_depts)
    ax.legend(loc='lower right')
    
    plt.tight_layout()
    plt.savefig(output_dir / "task1.png", dpi=300)
    plt.close()
