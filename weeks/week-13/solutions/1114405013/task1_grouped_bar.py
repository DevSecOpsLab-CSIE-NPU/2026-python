from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import Iterable, Optional

import matplotlib.pyplot as plt

YEARS = (112, 113, 114)
DEPT_COLUMN_CANDIDATES = ("系所名稱", "科系名稱", "系名", "系所")
YEAR_COLUMN_CANDIDATES = ("學年度", "年度", "入學學年度", "招生年度", "year", "Year")

# 作業指定的資料路徑。若實際資料夾不在此處，resolve_data_dir() 會自動找其他常見位置。
DATA_DIR = Path(__file__).parent.parent.parent.parent / "assets" / "stu-data"


def setup_chinese_font() -> None:
    """設定常見中文字型，避免圖表中文字變成方框。"""
    plt.rcParams["font.sans-serif"] = [
        "PingFang TC",
        "Heiti TC",
        "Arial Unicode MS",
        "Noto Sans CJK TC",
        "Microsoft JhengHei",
        "DejaVu Sans",
    ]
    plt.rcParams["axes.unicode_minus"] = False


def resolve_data_dir(data_dir: Optional[Path] = None) -> Path:
    """找出實際存在的 stu-data 資料夾。"""
    candidates: list[Path] = []
    if data_dir is not None:
        candidates.append(Path(data_dir))

    here = Path(__file__).resolve()
    for base in [here.parent, *here.parents]:
        candidates.append(base / "assets" / "stu-data")
        candidates.append(base / "week-13" / "assets" / "stu-data")
        candidates.append(base / "weeks" / "week-13" / "assets" / "stu-data")
        candidates.append(base / "weeks" / "assets" / "stu-data")

    seen: set[Path] = set()
    for candidate in candidates:
        candidate = candidate.resolve()
        if candidate in seen:
            continue
        seen.add(candidate)
        if candidate.exists() and any(candidate.rglob("*.csv")):
            return candidate

    checked = "\n".join(str(p) for p in list(seen)[:12])
    raise FileNotFoundError(
        "找不到 assets/stu-data 或其中沒有 CSV。請確認資料夾位置。\n"
        f"已檢查部分路徑：\n{checked}"
    )


def find_csv_files(data_dir: Path) -> list[Path]:
    """回傳資料夾下所有 CSV，去除重複並排序。"""
    data_dir = resolve_data_dir(data_dir)
    files = sorted(set(data_dir.rglob("*.csv")))
    if not files:
        raise FileNotFoundError(f"{data_dir} 底下找不到 CSV 檔。")
    return files


def get_column(row: dict[str, str], candidates: Iterable[str]) -> Optional[str]:
    """以欄位候選名稱取值，處理欄名多空白或 BOM 的情況。"""
    normalized = {str(k).strip().replace("\ufeff", ""): v for k, v in row.items()}
    for name in candidates:
        if name in normalized:
            return normalized[name]
    return None


def row_matches_year(row: dict[str, str], year: int) -> Optional[bool]:
    """
    若資料列有年度欄位，回傳是否符合指定學年度。
    若沒有年度欄位，回傳 None，表示需要靠檔名判斷。
    """
    raw_year = get_column(row, YEAR_COLUMN_CANDIDATES)
    if raw_year is None:
        return None
    digits = "".join(ch for ch in str(raw_year) if ch.isdigit())
    if not digits:
        return False
    return digits == str(year)


def iter_rows_for_year(year: int, data_dir: Path) -> Iterable[dict[str, str]]:
    """讀取指定學年度的資料列，支援分年 CSV 或單一總表 CSV。"""
    files = find_csv_files(data_dir)
    year_text = str(year)
    filename_matched_files = [p for p in files if year_text in p.name]
    target_files = filename_matched_files if filename_matched_files else files

    yielded = False
    saw_year_column = False

    for csv_path in target_files:
        with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                match = row_matches_year(row, year)
                if match is None:
                    if filename_matched_files:
                        yielded = True
                        yield row
                else:
                    saw_year_column = True
                    if match:
                        yielded = True
                        yield row

    if not yielded and not filename_matched_files and not saw_year_column:
        raise FileNotFoundError(
            f"找不到 {year} 學年度資料。請確認 CSV 檔名包含 {year}，或 CSV 內有學年度欄位。"
        )


def load_year(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份 CSV，回傳 {系所名稱: 人數} 的 dict。"""
    counter: Counter[str] = Counter()
    for row in iter_rows_for_year(year, data_dir):
        dept = get_column(row, DEPT_COLUMN_CANDIDATES)
        if dept is None:
            raise KeyError(f"CSV 缺少系所欄位，需有其中之一：{DEPT_COLUMN_CANDIDATES}")
        dept = str(dept).strip()
        if dept:
            counter[dept] += 1
    return dict(counter)


def get_top_depts(year_data: dict[int, dict[str, int]], top_n: int = 8) -> list[str]:
    """從多年資料中找出任一年曾進前 top_n 的系所，並依多年合計排序後最多回傳 top_n 個。"""
    candidates: set[str] = set()
    for counts in year_data.values():
        yearly_top = sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:top_n]
        candidates.update(dept for dept, _count in yearly_top)

    totals = {
        dept: sum(counts.get(dept, 0) for counts in year_data.values())
        for dept in candidates
    }
    return sorted(candidates, key=lambda dept: (-totals[dept], dept))[:top_n]


def find_largest_change(year_data: dict[int, dict[str, int]]) -> tuple[str, int, dict[int, int]]:
    """找出 112～114 年間最大差距的系所。"""
    all_depts = set().union(*(counts.keys() for counts in year_data.values()))
    best_dept = ""
    best_gap = -1
    best_values: dict[int, int] = {}

    for dept in all_depts:
        values = {year: year_data[year].get(dept, 0) for year in year_data}
        gap = max(values.values()) - min(values.values())
        if gap > best_gap:
            best_dept = dept
            best_gap = gap
            best_values = values

    return best_dept, best_gap, best_values


def plot_grouped_bar(years: tuple[int, ...] = YEARS, data_dir: Path = DATA_DIR) -> Path:
    """產生 Task 1 三年並排長條圖，輸出 output/task1.png。"""
    setup_chinese_font()
    data_dir = resolve_data_dir(data_dir)
    year_data = {year: load_year(year, data_dir) for year in years}
    depts = get_top_depts(year_data, top_n=8)

    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "task1.png"

    y_positions = list(range(len(depts)))
    bar_height = 0.22
    center_offset = (len(years) - 1) / 2

    fig, ax = plt.subplots(figsize=(12, max(6, len(depts) * 0.65)))
    for idx, year in enumerate(years):
        values = [year_data[year].get(dept, 0) for dept in depts]
        positions = [y + (idx - center_offset) * bar_height for y in y_positions]
        bars = ax.barh(positions, values, height=bar_height, label=f"{year} 學年度")
        ax.bar_label(bars, labels=[str(v) for v in values], padding=3, fontsize=8)

    ax.set_yticks(y_positions)
    ax.set_yticklabels(depts)
    ax.invert_yaxis()
    ax.set_xlabel("人數")
    ax.set_ylabel("系所名稱")
    ax.set_title("112～114 學年度各系招生人數比較")
    ax.legend(title="學年度")
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    plt.close(fig)
    return output_path


if __name__ == "__main__":
    actual_data_dir = resolve_data_dir(DATA_DIR)
    data = {year: load_year(year, actual_data_dir) for year in YEARS}
    path = plot_grouped_bar(YEARS, actual_data_dir)
    dept, gap, values = find_largest_change(data)
    print(f"Task 1 圖表已輸出：{path}")
    print(f"三年間人數變化最大系所：{dept}，最大差距：{gap} 人，年度資料：{values}")
