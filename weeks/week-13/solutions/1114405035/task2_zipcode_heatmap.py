# -*- coding: utf-8 -*-
import os
import csv
from pathlib import Path
import matplotlib
matplotlib.use('Agg')  # 設為無 GUI 模式以防 headless 環境崩潰
import matplotlib.pyplot as plt
import numpy as np

# 郵遞區號對照表
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
    """
    郵遞區號前 3 碼 → 縣市名稱，找不到回傳 '其他'
    """
    if not zipcode or len(zipcode) < 3:
        return "其他"
    return ZIPCODE_TO_COUNTY.get(zipcode[:3], "其他")

def load_county_counts(year: int, data_dir: Path) -> dict[str, int]:
    """
    讀取單一年份，回傳 {縣市: 人數} 的 dict
    """
    file_path = data_dir / f"{year}年新生資料庫.csv"
    if not file_path.exists():
        raise FileNotFoundError(f"找不到檔案: {file_path}")
        
    counts = {}
    with open(file_path, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            zipcode = row.get("郵遞區號", "").strip()
            county = zip_to_county(zipcode)
            counts[county] = counts.get(county, 0) + 1
    return counts

def get_top_counties(all_years: dict[int, dict], top_n: int = 10) -> list[str]:
    """
    6 年合計，回傳人數前 top_n 的縣市清單
    """
    total_counts = {}
    for year, counts in all_years.items():
        for county, cnt in counts.items():
            total_counts[county] = total_counts.get(county, 0) + cnt
            
    # 依人數降序排序，人數相同時依縣市名稱升序排序
    sorted_counties = sorted(total_counts.items(), key=lambda x: (-x[1], x[0]))
    return [county for county, _ in sorted_counties[:top_n]]

def main():
    # 尋找資料目錄
    curr = Path(__file__).resolve()
    data_dir = None
    while curr.parent != curr:
        temp_dir = curr / "assets" / "stu-data"
        if temp_dir.exists():
            data_dir = temp_dir
            break
        curr = curr.parent

    if data_dir is None:
        data_dir = Path(__file__).parent.parent.parent.parent.parent / "assets" / "stu-data"
        
    # 讀取 109 ~ 114 六年的資料
    years = [109, 110, 111, 112, 113, 114]
    all_years_data = {}
    for y in years:
        all_years_data[y] = load_county_counts(y, data_dir)
        
    # 取得 6 年合計人數前 10 名的縣市
    top_counties = get_top_counties(all_years_data, top_n=10)
    
    # 準備繪製熱力圖的 2D 矩陣 (10 縣市 x 6 年)
    heatmap_matrix = np.zeros((len(top_counties), len(years)))
    for i, county in enumerate(top_counties):
        for j, year in enumerate(years):
            heatmap_matrix[i, j] = all_years_data[year].get(county, 0)
            
    # 設定字型以支援中文顯示
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'DFKai-SB', 'SimHei', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 繪製圖表
    fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
    
    # 使用 YlGnBu 色系 (黃-綠-藍)
    im = ax.imshow(heatmap_matrix, cmap='YlGnBu', aspect='auto')
    
    # 設定 x, y 軸刻度與標籤
    ax.set_xticks(np.arange(len(years)))
    ax.set_xticklabels([f"{y}學年度" for y in years], fontsize=10, fontweight='bold')
    
    ax.set_yticks(np.arange(len(top_counties)))
    ax.set_yticklabels(top_counties, fontsize=10, fontweight='bold')
    
    # 在儲存格內標記數值
    # 為了閱讀體驗，我們根據數值深淺自動決定字體顏色（深背景用白字，淺背景用黑字）
    max_val = np.max(heatmap_matrix)
    threshold = max_val / 2.0
    for i in range(len(top_counties)):
        for j in range(len(years)):
            val = int(heatmap_matrix[i, j])
            color = "white" if val > threshold else "black"
            ax.text(j, i, f"{val}", ha="center", va="center", color=color, fontsize=10, fontweight='bold')
            
    # 加上色條
    cbar = ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.ax.set_ylabel("新生入學人數 (人)", rotation=-90, va="bottom", fontsize=10, fontweight='bold')
    cbar.ax.tick_params(labelsize=9)
    
    # 圖表標題與排版美化
    ax.set_title('109-114 學年度新生來源縣市分佈熱力圖\n(僅顯示六年合計人數前 10 名縣市)', fontsize=14, fontweight='bold', pad=15)
    
    # 隱藏外邊框，使熱力圖感覺更精緻
    for edge in ['top', 'bottom', 'left', 'right']:
        ax.spines[edge].set_visible(False)
        
    plt.tight_layout()
    
    # 建立輸出目錄並儲存
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    output_path = output_dir / "task2.png"
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()
    print(f"成功產生熱力圖並儲存至: {output_path}")

if __name__ == "__main__":
    main()
