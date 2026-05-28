from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Noto Sans CJK TC", "SimHei", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False


DATA_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent / "assets" / "stu-data"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
TARGET_YEARS = (109, 110, 111, 112, 113, 114)

ZIPCODE_TO_COUNTY = {
    "880": "澎湖縣", "881": "澎湖縣", "882": "澎湖縣", "884": "澎湖縣",
    "100": "台北市", "103": "台北市", "104": "台北市", "106": "台北市",
    "110": "台北市", "111": "台北市", "114": "台北市", "115": "台北市",
    "116": "台北市",
    "200": "基隆市", "201": "基隆市", "202": "基隆市", "203": "基隆市",
    "220": "新北市", "221": "新北市", "231": "新北市", "234": "新北市",
    "235": "新北市", "236": "新北市", "238": "新北市", "239": "新北市",
    "241": "新北市", "242": "新北市", "243": "新北市", "244": "新北市",
    "247": "新北市", "248": "新北市", "251": "新北市", "252": "新北市",
    "253": "新北市",
    "260": "宜蘭縣", "261": "宜蘭縣", "263": "宜蘭縣", "265": "宜蘭縣",
    "300": "新竹市", "302": "新竹縣", "303": "新竹縣", "304": "新竹縣",
    "305": "新竹縣", "306": "新竹縣", "307": "新竹縣", "308": "新竹縣",
    "310": "苗栗縣", "350": "苗栗縣", "351": "苗栗縣", "360": "苗栗縣",
    "400": "台中市", "401": "台中市", "402": "台中市", "403": "台中市",
    "404": "台中市", "406": "台中市", "407": "台中市", "408": "台中市",
    "411": "台中市", "412": "台中市", "413": "台中市", "420": "台中市",
    "421": "台中市", "422": "台中市", "423": "台中市", "424": "台中市",
    "426": "台中市", "427": "台中市", "428": "台中市", "429": "台中市",
    "430": "台中市", "431": "台中市", "432": "台中市", "433": "台中市",
    "434": "台中市", "435": "台中市", "436": "台中市", "437": "台中市",
    "438": "台中市", "439": "台中市",
    "500": "彰化縣", "502": "彰化縣", "503": "彰化縣", "504": "彰化縣",
    "505": "彰化縣", "506": "彰化縣", "507": "彰化縣", "508": "彰化縣",
    "509": "彰化縣", "510": "彰化縣", "511": "彰化縣", "512": "彰化縣",
    "513": "彰化縣", "514": "彰化縣", "515": "彰化縣", "516": "彰化縣",
    "520": "南投縣", "521": "南投縣", "522": "南投縣", "523": "南投縣",
    "545": "南投縣", "546": "南投縣",
    "600": "嘉義市", "602": "嘉義縣", "603": "嘉義縣", "604": "嘉義縣",
    "605": "嘉義縣",
    "630": "雲林縣", "631": "雲林縣", "632": "雲林縣", "633": "雲林縣",
    "640": "雲林縣", "641": "雲林縣",
    "700": "台南市", "701": "台南市", "702": "台南市", "703": "台南市",
    "704": "台南市", "708": "台南市", "709": "台南市", "710": "台南市",
    "711": "台南市", "712": "台南市", "713": "台南市", "714": "台南市",
    "715": "台南市", "716": "台南市", "717": "台南市", "718": "台南市",
    "719": "台南市", "720": "台南市", "721": "台南市", "722": "台南市",
    "723": "台南市", "724": "台南市", "725": "台南市", "726": "台南市",
    "730": "台南市", "731": "台南市", "732": "台南市", "733": "台南市",
    "734": "台南市", "735": "台南市", "736": "台南市",
    "800": "高雄市", "801": "高雄市", "802": "高雄市", "803": "高雄市",
    "804": "高雄市", "805": "高雄市", "806": "高雄市", "807": "高雄市",
    "811": "高雄市", "812": "高雄市", "813": "高雄市", "814": "高雄市",
    "815": "高雄市", "820": "高雄市", "821": "高雄市", "822": "高雄市",
    "823": "高雄市", "824": "高雄市", "825": "高雄市", "826": "高雄市",
    "827": "高雄市", "828": "高雄市", "829": "高雄市", "830": "高雄市",
    "831": "高雄市", "832": "高雄市", "833": "高雄市", "840": "高雄市",
    "842": "高雄市", "843": "高雄市", "844": "高雄市", "845": "高雄市",
    "846": "高雄市", "847": "高雄市",
    "900": "屏東縣", "901": "屏東縣", "902": "屏東縣", "903": "屏東縣",
    "904": "屏東縣", "905": "屏東縣", "906": "屏東縣", "907": "屏東縣",
    "908": "屏東縣", "909": "屏東縣", "911": "屏東縣", "912": "屏東縣",
    "913": "屏東縣", "920": "屏東縣", "921": "屏東縣", "922": "屏東縣",
    "923": "屏東縣", "924": "屏東縣", "925": "屏東縣", "926": "屏東縣",
    "927": "屏東縣", "928": "屏東縣", "929": "屏東縣", "931": "屏東縣",
    "932": "屏東縣", "940": "屏東縣", "941": "屏東縣", "942": "屏東縣",
    "943": "屏東縣", "944": "屏東縣", "945": "屏東縣", "946": "屏東縣",
    "947": "屏東縣", "950": "屏東縣", "951": "屏東縣", "952": "屏東縣",
    "953": "屏東縣", "954": "屏東縣", "955": "屏東縣", "956": "屏東縣",
    "957": "屏東縣", "958": "屏東縣", "966": "屏東縣",
    "950": "台東縣", "951": "台東縣", "952": "台東縣", "953": "台東縣",
    "970": "花蓮縣", "971": "花蓮縣", "972": "花蓮縣", "973": "花蓮縣",
    "974": "花蓮縣", "975": "花蓮縣", "976": "花蓮縣", "977": "花蓮縣",
    "978": "花蓮縣", "981": "花蓮縣", "983": "花蓮縣",
}


def zip_to_county(zipcode: str) -> str:
    """郵遞區號前 3 碼 → 縣市名稱，找不到回傳 '其他'"""

    return ZIPCODE_TO_COUNTY.get(zipcode[:3], "其他")


def load_county_counts(year: int, data_dir: Path) -> dict[str, int]:
    """讀取單一年份，回傳 {縣市: 人數} 的 dict"""

    path = data_dir / f"{year}年新生資料庫.csv"
    counts: Counter[str] = Counter()
    with path.open(encoding="utf-8-sig", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            zipcode = (row.get("郵遞區號") or "").strip()
            counts[zip_to_county(zipcode)] += 1
    return dict(counts)


def get_top_counties(all_years: dict[int, dict[str, int]], top_n: int = 10) -> list[str]:
    """6 年合計，回傳人數前 top_n 的縣市清單"""

    totals: Counter[str] = Counter()
    for counts in all_years.values():
        totals.update(counts)
    return [county for county, _ in totals.most_common(top_n)]


def build_heatmap(all_years: dict[int, dict[str, int]], output_path: Path) -> None:
    years = sorted(all_years)
    counties = get_top_counties(all_years, top_n=10)
    matrix = [[all_years[year].get(county, 0) for year in years] for county in counties]
    max_value = max((value for row in matrix for value in row), default=0)

    fig, ax = plt.subplots(figsize=(11, max(6, len(counties) * 0.55)))
    image = ax.imshow(matrix, cmap="YlGnBu", aspect="auto")

    ax.set_xticks(range(len(years)))
    ax.set_xticklabels([f"{year}學年度" for year in years])
    ax.set_yticks(range(len(counties)))
    ax.set_yticklabels(counties)
    ax.set_xlabel("學年度")
    ax.set_ylabel("縣市")
    ax.set_title("109～114學年度來源縣市招生熱力圖", fontsize=15, pad=14)

    for row_index, county in enumerate(counties):
        for col_index, year in enumerate(years):
            value = all_years[year].get(county, 0)
            if value:
                text_color = "white" if value >= max_value * 0.55 else "black"
                ax.text(col_index, row_index, str(value), ha="center", va="center", color=text_color, fontsize=9)

    fig.colorbar(image, ax=ax, shrink=0.88, label="人數")
    fig.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    all_years = {year: load_county_counts(year, DATA_DIR) for year in TARGET_YEARS}
    build_heatmap(all_years, OUTPUT_DIR / "task2.png")


if __name__ == "__main__":
    main()