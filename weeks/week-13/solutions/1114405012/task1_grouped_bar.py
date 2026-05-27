from collections import Counter
from csv import DictReader
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _find_repo_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "assets" / "stu-data").exists():
            return parent
    raise FileNotFoundError("找不到 assets/stu-data 目錄")


def _configure_chinese_font() -> None:
    available_fonts = {font.name for font in matplotlib.font_manager.fontManager.ttflist}
    for family in ("PingFang TC", "Heiti TC", "Arial Unicode MS", "Noto Sans CJK TC", "Microsoft JhengHei"):
        if family in available_fonts:
            plt.rcParams["font.sans-serif"] = [family]
            break
    plt.rcParams["axes.unicode_minus"] = False


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict"""
    file_path = data_dir / f"{year}年新生資料庫.csv"
    with file_path.open(encoding="utf-8-sig", newline="") as file_handle:
        rows = DictReader(file_handle)
        counts = Counter()
        for row in rows:
            dept_name = (row.get("系所名稱") or "").strip()
            if dept_name:
                counts[dept_name] += 1
    return dict(counts)


def get_top_depts(year_data: dict[int, dict], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所清單"""
    candidate_depts: set[str] = set()
    for dept_counts in year_data.values():
        ranked = Counter(dept_counts).most_common(top_n)
        candidate_depts.update(dept_name for dept_name, _ in ranked)

    combined_counts = Counter()
    for dept_counts in year_data.values():
        for dept_name in candidate_depts:
            combined_counts[dept_name] += dept_counts.get(dept_name, 0)

    ranked_candidates = sorted(
        candidate_depts,
        key=lambda dept_name: (-combined_counts[dept_name], dept_name),
    )
    return ranked_candidates[:top_n]


def build_grouped_bar(year_data: dict[int, dict[str, int]], output_path: Path) -> None:
    _configure_chinese_font()

    years = sorted(year_data)
    departments = get_top_depts(year_data)
    if not departments:
        raise ValueError("沒有可繪圖的系所資料")

    positions = list(range(len(departments)))
    group_height = 0.72
    bar_height = group_height / len(years)
    max_count = max(
        (count for dept_counts in year_data.values() for count in dept_counts.values()),
        default=0,
    )

    fig, ax = plt.subplots(figsize=(12, max(6, 0.55 * len(departments) + 1.5)))
    for index, year in enumerate(years):
        offset = (index - (len(years) - 1) / 2) * bar_height
        counts = [year_data[year].get(department, 0) for department in departments]
        bar_positions = [position + offset for position in positions]
        bars = ax.barh(
            bar_positions,
            counts,
            height=bar_height * 0.88,
            label=f"{year}",
        )
        ax.bar_label(bars, padding=3, fontsize=9)

    ax.set_yticks(positions)
    ax.set_yticklabels(departments)
    ax.invert_yaxis()
    ax.set_xlim(0, max_count * 1.18 if max_count else 1)
    ax.set_xlabel("人數")
    ax.set_ylabel("系所名稱")
    ax.set_title("112～114 學年度各系招生人數並排長條圖")
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    ax.legend(title="學年度", frameon=False)
    fig.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    repo_root = _find_repo_root()
    data_dir = repo_root / "assets" / "stu-data"
    output_path = Path(__file__).resolve().parent / "output" / "task1.png"

    year_data = {year: load_year(year, data_dir) for year in (112, 113, 114)}
    build_grouped_bar(year_data, output_path)


if __name__ == "__main__":
    main()