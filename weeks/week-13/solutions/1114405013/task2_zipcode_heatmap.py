from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from typing import Iterable, Optional

import matplotlib.pyplot as plt

YEARS = (109, 110, 111, 112, 113, 114)
ZIP_COLUMN_CANDIDATES = ("郵遞區號", "戶籍郵遞區號", "郵遞區碼", "zip", "zipcode", "Zipcode")
YEAR_COLUMN_CANDIDATES = ("學年度", "年度", "入學學年度", "招生年度", "year", "Year")
DATA_DIR = Path(__file__).parent.parent.parent.parent / "assets" / "stu-data"

ZIPCODE_TO_COUNTY = {
    "880": "澎湖縣", "881": "澎湖縣", "882": "澎湖縣", "884": "澎湖縣",
    "100": "台北市", "103": "台北市", "104": "台北市", "106": "台北市",
    "110": "台北市", "111": "台北市", "114": "台北市", "115": "台北市", "116": "台北市",
    "200": "基隆市", "201": "基隆市", "202": "基隆市", "203": "基隆市",
    "220": "新北市", "221": "新北市", "231": "新北市", "234": "新北市", "235": "新北市",
    "236": "新北市", "238": "新北市", "239": "新北市", "241": "新北市", "242": "新北市",
    "243": "新北市", "244": "新北市", "247": "新北市", "248": "新北市", "251": "新北市",
    "252": "新北市", "253": "新北市",
    "260": "宜蘭縣", "261": "宜蘭縣", "263": "宜蘭縣", "265": "宜蘭縣",
    "300": "新竹市", "302": "新竹縣", "303": "新竹縣", "304": "新竹縣", "305": "新竹縣",
    "306": "新竹縣", "307": "新竹縣", "308": "新竹縣",
    "310": "苗栗縣", "350": "苗栗縣", "351": "苗栗縣", "360": "苗栗縣",
    "400": "台中市", "401": "台中市", "402": "台中市", "403": "台中市", "404": "台中市",
    "406": "台中市", "407": "台中市", "408": "台中市", "411": "台中市", "412": "台中市",
    "413": "台中市", "420": "台中市", "421": "台中市", "422": "台中市", "423": "台中市",
    "424": "台中市", "426": "台中市", "427": "台中市", "428": "台中市", "429": "台中市",
    "430": "台中市", "431": "台中市", "432": "台中市", "433": "台中市", "434": "台中市",
    "435": "台中市", "436": "台中市", "437": "台中市", "438": "台中市", "439": "台中市",
    "500": "彰化縣", "502": "彰化縣", "503": "彰化縣", "504": "彰化縣", "505": "彰化縣",
    "506": "彰化縣", "507": "彰化縣", "508": "彰化縣", "509": "彰化縣", "510": "彰化縣",
    "511": "彰化縣", "512": "彰化縣", "513": "彰化縣", "514": "彰化縣", "515": "彰化縣",
    "516": "彰化縣",
    "520": "南投縣", "521": "南投縣", "522": "南投縣", "523": "南投縣", "545": "南投縣", "546": "南投縣",
    "600": "嘉義市", "602": "嘉義縣", "603": "嘉義縣", "604": "嘉義縣", "605": "嘉義縣",
    "630": "雲林縣", "631": "雲林縣", "632": "雲林縣", "633": "雲林縣", "640": "雲林縣", "641": "雲林縣",
    "700": "台南市", "701": "台南市", "702": "台南市", "703": "台南市", "704": "台南市",
    "708": "台南市", "709": "台南市", "710": "台南市", "711": "台南市", "712": "台南市",
    "713": "台南市", "714": "台南市", "715": "台南市", "716": "台南市", "717": "台南市",
    "718": "台南市", "719": "台南市", "720": "台南市", "721": "台南市", "722": "台南市",
    "723": "台南市", "724": "台南市", "725": "台南市", "726": "台南市", "730": "台南市",
    "731": "台南市", "732": "台南市", "733": "台南市", "734": "台南市", "735": "台南市", "736": "台南市",
    "800": "高雄市", "801": "高雄市", "802": "高雄市", "803": "高雄市", "804": "高雄市",
    "805": "高雄市", "806": "高雄市", "807": "高雄市", "811": "高雄市", "812": "高雄市",
    "813": "高雄市", "814": "高雄市", "815": "高雄市", "820": "高雄市", "821": "高雄市",
    "822": "高雄市", "823": "高雄市", "824": "高雄市", "825": "高雄市", "826": "高雄市",
    "827": "高雄市", "828": "高雄市", "829": "高雄市", "830": "高雄市", "831": "高雄市",
    "832": "高雄市", "833": "高雄市", "840": "高雄市", "842": "高雄市", "843": "高雄市",
    "844": "高雄市", "845": "高雄市", "846": "高雄市", "847": "高雄市",
    "900": "屏東縣", "901": "屏東縣", "902": "屏東縣", "903": "屏東縣", "904": "屏東縣",
    "905": "屏東縣", "906": "屏東縣", "907": "屏東縣", "908": "屏東縣", "909": "屏東縣",
    "911": "屏東縣", "912": "屏東縣", "913": "屏東縣", "920": "屏東縣", "921": "屏東縣",
    "922": "屏東縣", "923": "屏東縣", "924": "屏東縣", "925": "屏東縣", "926": "屏東縣",
    "927": "屏東縣", "928": "屏東縣", "929": "屏東縣", "931": "屏東縣", "932": "屏東縣",
    "940": "屏東縣", "941": "屏東縣", "942": "屏東縣", "943": "屏東縣", "944": "屏東縣",
    "945": "屏東縣", "946": "屏東縣", "947": "屏東縣", "954": "屏東縣", "955": "屏東縣",
    "956": "屏東縣", "957": "屏東縣", "958": "屏東縣", "966": "屏東縣",
    "950": "台東縣", "951": "台東縣", "952": "台東縣", "953": "台東縣",
    "970": "花蓮縣", "971": "花蓮縣", "972": "花蓮縣", "973": "花蓮縣", "974": "花蓮縣",
    "975": "花蓮縣", "976": "花蓮縣", "977": "花蓮縣", "978": "花蓮縣", "981": "花蓮縣", "983": "花蓮縣",
}


def setup_chinese_font() -> None:
    plt.rcParams["font.sans-serif"] = [
        "PingFang TC",
        "Heiti TC",
        "Arial Unicode MS",
        "Noto Sans CJK TC",
        "Microsoft JhengHei",
        "DejaVu Sans",
    ]
    plt.rcParams["axes.unicode_minus"] = False


def zip_to_county(zipcode: str) -> str:
    """郵遞區號前 3 碼 → 縣市名稱，找不到回傳 '其他'。"""
    digits = "".join(ch for ch in str(zipcode).strip() if ch.isdigit())
    return ZIPCODE_TO_COUNTY.get(digits[:3], "其他")


def resolve_data_dir(data_dir: Optional[Path] = None) -> Path:
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
    data_dir = resolve_data_dir(data_dir)
    files = sorted(set(data_dir.rglob("*.csv")))
    if not files:
        raise FileNotFoundError(f"{data_dir} 底下找不到 CSV 檔。")
    return files


def get_column(row: dict[str, str], candidates: Iterable[str]) -> Optional[str]:
    normalized = {str(k).strip().replace("\ufeff", ""): v for k, v in row.items()}
    for name in candidates:
        if name in normalized:
            return normalized[name]
    return None


def row_matches_year(row: dict[str, str], year: int) -> Optional[bool]:
    raw_year = get_column(row, YEAR_COLUMN_CANDIDATES)
    if raw_year is None:
        return None
    digits = "".join(ch for ch in str(raw_year) if ch.isdigit())
    if not digits:
        return False
    return digits == str(year)


def iter_rows_for_year(year: int, data_dir: Path) -> Iterable[dict[str, str]]:
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


def load_county_counts(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份，回傳 {縣市: 人數} 的 dict。"""
    counter: Counter[str] = Counter()
    for row in iter_rows_for_year(year, data_dir):
        zipcode = get_column(row, ZIP_COLUMN_CANDIDATES)
        if zipcode is None:
            raise KeyError(f"CSV 缺少郵遞區號欄位，需有其中之一：{ZIP_COLUMN_CANDIDATES}")
        counter[zip_to_county(str(zipcode))] += 1
    return dict(counter)


def get_top_counties(all_years: dict[int, dict[str, int]], top_n: int = 10) -> list[str]:
    """6 年合計，回傳人數前 top_n 的縣市清單。"""
    totals: Counter[str] = Counter()
    for counts in all_years.values():
        totals.update(counts)
    return [county for county, _count in totals.most_common(top_n)]


def summarize_counties(all_years: dict[int, dict[str, int]]) -> dict[str, object]:
    """回傳澎湖比例、第二大來源縣市等分析資料。"""
    totals: Counter[str] = Counter()
    for counts in all_years.values():
        totals.update(counts)

    total_students = sum(totals.values())
    penghu = totals.get("澎湖縣", 0)
    ratio = penghu / total_students if total_students else 0
    ranking = totals.most_common()
    second = ranking[1] if len(ranking) > 1 else ("無", 0)

    return {
        "total_students": total_students,
        "penghu": penghu,
        "penghu_ratio": ratio,
        "second_county": second[0],
        "second_count": second[1],
        "ranking": ranking,
    }


def plot_heatmap(years: tuple[int, ...] = YEARS, data_dir: Path = DATA_DIR) -> Path:
    """產生 Task 2 縣市 × 年份熱力圖，輸出 output/task2.png。"""
    setup_chinese_font()
    data_dir = resolve_data_dir(data_dir)
    all_years = {year: load_county_counts(year, data_dir) for year in years}
    counties = get_top_counties(all_years, top_n=10)
    matrix = [[all_years[year].get(county, 0) for year in years] for county in counties]

    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "task2.png"

    fig, ax = plt.subplots(figsize=(10, max(6, len(counties) * 0.55)))
    image = ax.imshow(matrix, aspect="auto", cmap="YlOrRd")
    colorbar = fig.colorbar(image, ax=ax)
    colorbar.set_label("人數")

    ax.set_xticks(range(len(years)))
    ax.set_xticklabels([str(year) for year in years])
    ax.set_yticks(range(len(counties)))
    ax.set_yticklabels(counties)
    ax.set_xlabel("學年度")
    ax.set_ylabel("縣市")
    ax.set_title("109～114 學年度新生來源縣市熱力圖")

    max_value = max((max(row) for row in matrix if row), default=0)
    threshold = max_value * 0.55
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            text_color = "white" if value >= threshold and max_value > 0 else "black"
            ax.text(j, i, str(value), ha="center", va="center", fontsize=8, color=text_color)

    fig.tight_layout()
    fig.savefig(output_path, dpi=160)
    plt.close(fig)
    return output_path


if __name__ == "__main__":
    actual_data_dir = resolve_data_dir(DATA_DIR)
    all_data = {year: load_county_counts(year, actual_data_dir) for year in YEARS}
    path = plot_heatmap(YEARS, actual_data_dir)
    summary = summarize_counties(all_data)
    print(f"Task 2 圖表已輸出：{path}")
    print(
        "澎湖縣學生："
        f"{summary['penghu']} / {summary['total_students']} "
        f"({summary['penghu_ratio']:.1%})；"
        f"第二大來源：{summary['second_county']}（{summary['second_count']} 人）"
    )
