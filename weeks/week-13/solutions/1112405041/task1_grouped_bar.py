import csv
import os
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import matplotlib

matplotlib.rcParams['font.family'] = ['Microsoft JhengHei', 'sans-serif']

def load_year(year: int, data_dir: Path) -> dict[str, int]:
    p = data_dir / f"{year}年新生資料庫.csv"
    c = {}
    with open(p, 'r', encoding='utf-8-sig') as f:
        r = csv.DictReader(f)
        for row in r:
            d = row['系所名稱']
            c[d] = c.get(d, 0) + 1
    return c

def get_top_depts(year_data: dict, top_n: int = 8) -> list[str]:
    top = set()
    for y in year_data:
        sorted_d = sorted(year_data[y].items(), key=lambda x: x[1], reverse=True)
        for i in range(min(top_n, len(sorted_d))):
            top.add(sorted_d[i][0])
    return list(top)

def solve():
    data_dir = Path(__file__).parent.parent.parent.parent / "assets" / "stu-data"
    years = [112, 113, 114]
    y_data = {y: load_year(y, data_dir) for y in years}
    depts = get_top_depts(y_data)
    
    # Plotting logic...
    plt.figure(figsize=(10, 8))
    # ... seaborn grouped bar plot code ...
    plt.savefig(Path(__file__).parent / "output/task1.png")

if __name__ == '__main__': solve()
