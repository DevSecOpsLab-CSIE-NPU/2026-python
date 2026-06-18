import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib

matplotlib.rcParams['font.family'] = ['Microsoft JhengHei', 'sans-serif']

ZIP_MAP = {"880": "澎湖縣", "100": "台北市"} # Simplified for brevity

def zip_to_county(zipcode: str) -> str:
    return ZIP_MAP.get(zipcode[:3], "其他")

def load_county_counts(year: int, data_dir: Path) -> dict[str, int]:
    p = data_dir / f"{year}年新生資料庫.csv"
    c = {}
    with open(p, 'r', encoding='utf-8-sig') as f:
        r = csv.DictReader(f)
        for row in r:
            co = zip_to_county(row['郵遞區號'])
            c[co] = c.get(co, 0) + 1
    return c

def solve():
    # Heatmap logic...
    plt.savefig(Path(__file__).parent / "output/task2.png")

if __name__ == '__main__': solve()
