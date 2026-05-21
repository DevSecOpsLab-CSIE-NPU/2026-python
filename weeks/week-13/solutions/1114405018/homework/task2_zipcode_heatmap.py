from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from typing import Dict
plt.rcParams['font.family'] = 'Microsoft JhengHei'

ZIPCODE_TO_COUNTY = {
    "880": "澎湖縣", "881": "澎湖縣", "882": "澎湖縣", "884": "澎湖縣",
    "100": "台北市", "103": "台北市", "104": "台北市", "106": "台北市",
    "110": "台北市", "111": "台北市", "114": "台北市", "115": "台北市",
    "116": "台北市",
    # （簡化：未列全表，實作使用前 3 碼比對）
}


def zip_to_county(zipcode: str) -> str:
    return ZIPCODE_TO_COUNTY.get(zipcode[:3], '其他')


def load_county_counts(year: int, data_dir: Path) -> Dict[str, int]:
    path = data_dir / f"{year}年新生資料庫.csv"
    cnt: Counter[str] = Counter()
    with path.open('r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for r in reader:
            z = (r.get('郵遞區號') or '').strip()
            if not z:
                continue
            county = zip_to_county(z)
            cnt[county] += 1
    return dict(cnt)


def find_data_dir() -> Path:
    p = Path(__file__).resolve()
    for _ in range(10):
        candidate = p.parent
        if (candidate / 'assets' / 'stu-data').exists():
            return (candidate / 'assets' / 'stu-data')
        p = candidate
    return Path(r"c:/Users/nina9/OneDrive/桌面/python/python2/2026-python/assets/stu-data")


def get_top_counties(all_years: dict[int, dict], top_n: int = 10) -> list[str]:
    total = Counter()
    for d in all_years.values():
        total.update(d)
    return [c for c, _ in total.most_common(top_n)]


def plot_heatmap(all_years: dict[int, dict], years: list[int], out_path: Path):
    counties = get_top_counties(all_years)
    data = [[all_years.get(y, {}).get(c, 0) for c in counties] for y in years]

    import numpy as np
    arr = np.array(data)
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(arr.T, aspect='auto')
    ax.set_yticks(range(len(counties)))
    ax.set_yticklabels(counties)
    ax.set_xticks(range(len(years)))
    ax.set_xticklabels([str(y) for y in years])
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label('人數')
    ax.set_title('縣市 × 年份 熱力圖')
    ax.set_xlabel('年份')
    ax.set_ylabel('縣市')
    # annotate cells
    for i in range(arr.T.shape[0]):
        for j in range(arr.T.shape[1]):
            val = int(arr.T[i, j])
            ax.text(j, i, str(val), ha='center', va='center', color='white' if val>max(arr.T.flatten())*0.6 else 'black', fontsize=8)
    fig.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path)


if __name__ == '__main__':
    from pathlib import Path
    BASE = find_data_dir()
    years = [109,110,111,112,113,114]
    all_years = {y: load_county_counts(y, BASE) for y in years}
    out = Path(__file__).parent / 'output' / 'task2.png'
    plot_heatmap(all_years, years, out)
