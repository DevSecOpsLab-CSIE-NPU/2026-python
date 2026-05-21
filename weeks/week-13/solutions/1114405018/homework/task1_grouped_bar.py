from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Microsoft JhengHei'
from typing import Dict


def load_year(year: int, data_dir: Path) -> Dict[str, int]:
    path = data_dir / f"{year}年新生資料庫.csv"
    cnt: Counter[str] = Counter()
    with path.open('r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for r in reader:
            dept = r.get('系所名稱') or r.get('系別') or ''
            if dept:
                cnt[dept] += 1
    return dict(cnt)


def find_data_dir() -> Path:
    p = Path(__file__).resolve()
    # 向上搜尋最多 10 層，尋找 assets/stu-data
    for _ in range(10):
        candidate = p.parent
        if (candidate / 'assets' / 'stu-data').exists():
            return (candidate / 'assets' / 'stu-data')
        p = candidate
    return Path(r"c:/Users/nina9/OneDrive/桌面/python/python2/2026-python/assets/stu-data")


def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    # 找出任一年曾進前 top_n 的系
    selected = set()
    for y, d in year_data.items():
        top = sorted(d.items(), key=lambda kv: kv[1], reverse=True)[:top_n]
        selected.update(name for name, _ in top)
    return list(selected)


def plot_grouped_bar(all_years: dict[int, dict], years: list[int], out_path: Path):
    depts = get_top_depts(all_years)
    depts = sorted(depts)
    data = [[all_years.get(y, {}).get(d, 0) for d in depts] for y in years]

    import numpy as np
    x = np.arange(len(depts))
    width = 0.2

    fig, ax = plt.subplots(figsize=(10, max(4, len(depts)*0.5)))
    for i, y in enumerate(years):
        y_pos = x + (i - len(years)/2)*width
        bars = ax.barh(y_pos, data[i], height=width, label=str(y))
        # annotate values
        for bar, val in zip(bars, data[i]):
            ax.text(val + max(1, max(data[i]) * 0.01), bar.get_y() + bar.get_height()/2,
                    str(val), va='center', fontsize=8)

    ax.set_yticks(x)
    ax.set_yticklabels(depts)
    ax.set_xlabel('人數')
    ax.set_title('三年並排長條圖')
    ax.legend(title='年份')
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path)


if __name__ == '__main__':
    from pathlib import Path
    BASE = find_data_dir()
    years = [112, 113, 114]
    all_years = {y: load_year(y, BASE) for y in years}
    out = Path(__file__).parent / 'output' / 'task1.png'
    plot_grouped_bar(all_years, years, out)
