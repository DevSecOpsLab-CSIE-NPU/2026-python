"""
Task 2: 來源縣市熱力圖 (縣市 × 年份招生人數)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import matplotlib
import numpy as np

# 設定中文字體
matplotlib.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 郵遞區號 → 縣市對照表
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
    "970": "花蓮縣", "971": "花蓮縣", "972": "花蓮縣", "973": "花蓮縣",
    "974": "花蓮縣", "975": "花蓮縣", "976": "花蓮縣", "977": "花蓮縣",
    "978": "花蓮縣", "981": "花蓮縣", "983": "花蓮縣",
}


def zip_to_county(zipcode: str) -> str:
    """
    郵遞區號前 3 碼 → 縣市名稱，找不到回傳 '其他'
    
    Args:
        zipcode: 郵遞區號 (字串)
        
    Returns:
        縣市名稱
    """
    if pd.isna(zipcode):
        return "其他"
    
    zipcode_str = str(zipcode).strip()
    return ZIPCODE_TO_COUNTY.get(zipcode_str[:3], "其他")


def load_county_counts(year: int, data_dir: Path) -> dict[str, int]:
    """
    讀取單一年份，回傳 {縣市: 人數} 的 dict
    
    Args:
        year: 學年度 (109, 110, 111, 112, 113, 114)
        data_dir: 資料目錄路徑
        
    Returns:
        {縣市: 人數} 的字典
    """
    # CSV 檔案名格式
    filename = f"{year}年新生資料庫.csv"
    filepath = data_dir / filename
    
    # 讀取 CSV 檔案
    df = pd.read_csv(filepath, encoding='utf-8-sig')
    
    # 將郵遞區號轉換為縣市
    df['縣市'] = df['郵遞區號'].apply(zip_to_county)
    
    # 計算每個縣市的人數
    county_counts = df['縣市'].value_counts().to_dict()
    
    return county_counts


def get_top_counties(all_years: dict[int, dict], top_n: int = 10) -> list[str]:
    """
    6 年合計，回傳人數前 top_n 的縣市清單
    
    Args:
        all_years: {年份: {縣市: 人數}} 的嵌套字典
        top_n: 前幾名
        
    Returns:
        符合條件的縣市清單
    """
    # 計算每個縣市在所有年份的總人數
    county_total = {}
    
    for year, county_dict in all_years.items():
        for county, count in county_dict.items():
            if county not in county_total:
                county_total[county] = 0
            county_total[county] += count
    
    # 排除「其他」，確保前 10 名都是具體縣市，避免「其他」佔用排名
    county_total.pop("其他", None)
    
    # 按總人數排序，取前 top_n
    sorted_counties = sorted(county_total.items(), key=lambda x: x[1], reverse=True)
    top_counties = [county for county, _ in sorted_counties[:top_n]]
    
    return sorted(top_counties)


def plot_heatmap(all_years: dict[int, dict], output_path: Path) -> None:
    """
    繪製縣市 × 年份熱力圖
    
    Args:
        all_years: {年份: {縣市: 人數}} 的嵌套字典
        output_path: 輸出圖片路徑
    """
    # 取得前 10 名縣市
    top_counties = get_top_counties(all_years, top_n=10)
    
    # 準備資料矩陣
    years = sorted(all_years.keys())
    data_matrix = []
    
    for county in top_counties:
        row = [all_years[year].get(county, 0) for year in years]
        data_matrix.append(row)
    
    # 建立 DataFrame
    heatmap_data = pd.DataFrame(
        data_matrix,
        index=top_counties,
        columns=years
    )
    
    # 建立圖表
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 繪製熱力圖
    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt='d',
        cmap='YlOrRd',
        cbar_kws={'label': '人數'},
        ax=ax,
        linewidths=0.5,
        linecolor='gray'
    )
    
    # 設定標籤和標題
    ax.set_title('招生人數熱力圖：來源縣市 × 入學年份 (109-114年)', fontsize=14, fontweight='bold')
    ax.set_xlabel('入學年份', fontsize=12, fontweight='bold')
    ax.set_ylabel('來源縣市', fontsize=12, fontweight='bold')
    
    # 調整布局
    plt.tight_layout()
    
    # 儲存圖表
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"熱力圖已保存至: {output_path}")
    plt.close()


def main():
    """主程式"""
    # 取得資料路徑 - 從 solution 目錄向上 6 層到 2026-python
    current_file = Path(__file__).resolve()
    # week-13/solutions/1114405017/task2_zipcode_heatmap.py
    # 往上數：task2一層，1114405017兩層，solutions三層，week-13四層，weeks五層，2026-python六層
    data_dir = current_file.parent.parent.parent.parent.parent / "assets" / "stu-data"
    
    # 讀取 109～114 年份的資料
    years = [109, 110, 111, 112, 113, 114]
    all_years = {}
    
    for year in years:
        all_years[year] = load_county_counts(year, data_dir)
        print(f"已讀取 {year} 年度資料，共 {len(all_years[year])} 個縣市")
    
    # 繪製並保存熱力圖
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "task2.png"
    
    plot_heatmap(all_years, output_path)
    
    # 打印摘要
    print("\n=== 前十名縣市分析 ===")
    top_counties = get_top_counties(all_years, top_n=10)
    for county in top_counties:
        total = sum(all_years[year].get(county, 0) for year in years)
        print(f"{county}: {total} 人 ("
              f"109={all_years[109].get(county, 0)}, "
              f"110={all_years[110].get(county, 0)}, "
              f"111={all_years[111].get(county, 0)}, "
              f"112={all_years[112].get(county, 0)}, "
              f"113={all_years[113].get(county, 0)}, "
              f"114={all_years[114].get(county, 0)})")


if __name__ == "__main__":
    main()
