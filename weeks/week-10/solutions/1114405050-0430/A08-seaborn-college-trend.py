# A08. 用 seaborn 畫 109~114 學年各學院生源分析圖
# Bloom: Apply — 把 A07 的統計成果交給視覺化套件
#
# 需要：pip install seaborn matplotlib pandas
#
# 用到的 I/O 技巧延續 A07：
#   5.7  zipfile 不解壓讀 CSV
#   5.1  utf-8-sig 去 BOM
#   5.6  io.StringIO → csv
#   5.11 pathlib
#   5.5  open('x') 不覆蓋輸出檔

import csv
import io
import platform
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ── 設定中文字型：根據不同作業系統自動挑選支援的字型 ─────────────────────────
# 說明：matplotlib 預設的字型不包含中文，直接繪圖會出現方塊（俗稱豆腐字）。
# 這裡我們針對不同作業系統（macOS, Windows, Linux）提供對應的中文字型清單。
# macOS 預設抓不到 PingFang TC，因此改用系統內建的 Heiti TC 或 Arial Unicode MS。
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])


def _apply_cjk_font():
    """
    將挑選好的中文字型套用到 matplotlib 的全域設定 (rcParams) 中。
    注意：seaborn 的 sns.set_theme() 會重設 rcParams，所以如果在設定 theme 之後，
    必須重新呼叫此函式再套用一次中文字型。
    """
    # 將選定的中文字型加到預設的無襯線字型 (sans-serif) 列表的最前面
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    plt.rcParams["font.family"] = "sans-serif"
    # 解決中文字型設定下，負號 (-) 無法正常顯示的問題
    plt.rcParams["axes.unicode_minus"] = False


_apply_cjk_font()

# ── 建立系所對應學院的查找表（字典） ─────────────────
# 由於原始資料只有「系所名稱」，為了做學院級別的統計，我們定義這個 mapping 字典。
DEPT_TO_COLLEGE = {
    # 人文暨管理學院
    "應用外語系":       "人文暨管理學院",
    "航運管理系":       "人文暨管理學院",
    "行銷與物流管理系": "人文暨管理學院",
    "觀光休閒系":       "人文暨管理學院",
    "資訊管理系":       "人文暨管理學院",
    "餐旅管理系":       "人文暨管理學院",
    # 海洋資源暨工程學院
    "水產養殖系":       "海洋資源暨工程學院",
    "海洋遊憩系":       "海洋資源暨工程學院",
    "食品科學系":       "海洋資源暨工程學院",
    # 電資工程學院
    "資訊工程系":       "電資工程學院",
    "電信工程系":       "電資工程學院",
    "電機工程系":       "電資工程學院",
}

# ── 5.11 定位資料檔路徑 ─────────────────────────────────────
# 利用 pathlib 取得目前執行檔案的絕對路徑，再往上層目錄尋找目標 ZIP 檔案。
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
# 確保檔案存在，否則拋出 AssertionError
assert ZIP_PATH.exists(), f"找不到：{ZIP_PATH}"


# ── 5.7 + 5.6 + 5.1 讀取壓縮檔內所有 CSV，並整合成 pandas DataFrame ─
def load_long_frame(zip_path: Path) -> pd.DataFrame:
    """
    不解壓縮，直接讀取 ZIP 檔案內的所有 CSV，轉換為適合分析的長表格 (long-form) DataFrame。
    """
    records = []
    with zipfile.ZipFile(zip_path) as z:
        # 遍歷壓縮檔內的每個檔案資訊
        for info in z.infolist():
            # 只處理附檔名為 .csv 的檔案
            if not info.filename.endswith(".csv"):
                continue
            
            # 從檔名切出前 3 個字元作為學年度 (例如 '109')
            year = info.filename[:3]                     
            # 讀取檔案內容 (bytes)，並使用 utf-8-sig 解碼以去除 Windows 常見的 BOM 字元
            text = z.read(info).decode("utf-8-sig")      
            # 將字串內容包裝成 StringIO (file-like 物件)，交給 csv.DictReader 解析
            reader = csv.DictReader(io.StringIO(text))   
            
            # 逐列讀取資料並轉換成字典格式
            for row in reader:
                dept = row.get("系所名稱", "").strip()
                if not dept:
                    continue # 忽略沒有系所名稱的空資料
                records.append({
                    "學年": int(year),
                    "學院": DEPT_TO_COLLEGE.get(dept, "其他"), # 查表，若找不到則歸類為"其他"
                    "系所": dept,
                })
    # 將 list of dicts 轉換為 pandas DataFrame
    return pd.DataFrame.from_records(records)


df = load_long_frame(ZIP_PATH)
print("總筆數:", len(df))
print(df.head())

# ── 資料聚合 (Aggregation) ──────────────────────────────────────
# 利用 groupby 將資料按「學年」與「學院」分組，計算各組人數，並將結果重設為平坦的 DataFrame。
pivot = (df.groupby(["學年", "學院"])
           .size()
           .reset_index(name="人數"))
print("\n各學年各學院:")
# 將長表格轉為寬表格 (pivot) 以便於在終端機預覽
print(pivot.pivot(index="學年", columns="學院", values="人數"))


# ── 視覺化 (seaborn / matplotlib 繪圖) ──────────────────────────────────────
# 設定 seaborn 的主題樣式：白色網格背景 (whitegrid)、適合演講的字體大小 (talk) 以及 Set2 配色
sns.set_theme(style="whitegrid", context="talk", palette="Set2")
# 因為 sns.set_theme 會覆蓋掉我們之前設定的字型，所以必須再次呼叫套用中文字型
_apply_cjk_font()  

# 建立一個包含 1 列 2 欄的圖表 (subplots)，總大小為 15x6 英吋。
# gridspec_kw 用來設定左右兩張圖的寬度比例為 1.3 : 1。
fig, axes = plt.subplots(1, 2, figsize=(15, 6),
                         gridspec_kw={"width_ratios": [1.3, 1]})

# ── 圖 A：折線＋散點 —— 各學院逐年趨勢 (左圖 ax=axes[0]) ──
# 使用 seaborn 的 lineplot 繪製折線圖，依照「學院」區分顏色 (hue)
sns.lineplot(data=pivot, x="學年", y="人數", hue="學院",
             marker="o", markersize=10, linewidth=2.5, ax=axes[0])
axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=16, pad=12)
# 強制設定 X 軸的刻度為所有出現過的學年度
axes[0].set_xticks(sorted(pivot["學年"].unique()))
axes[0].legend(title="學院", loc="upper right", frameon=True)

# 在折線圖的每個資料點上方標註具體的人數數值
for _, r in pivot.iterrows():
    axes[0].annotate(int(r["人數"]),
                     (r["學年"], r["人數"]),        # 標籤放置的基準點
                     textcoords="offset points", xytext=(0, 8), # 往上偏移 8 點
                     ha="center", fontsize=9, alpha=0.8)        # 水平置中、字體大小、透明度

# ── 圖 B：堆疊長條圖 —— 每年學院結構與占比 (右圖 ax=axes[1]) ──
# 先將資料轉換為寬表格，若有缺失值則填補為 0 (fillna)
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)
# 使用 pandas 內建的 plot 功能畫長條圖 (kind="bar")，並開啟堆疊效果 (stacked=True)
pivot_wide.plot(kind="bar", stacked=True,
                ax=axes[1], colormap="Set2", width=0.75, edgecolor="white")
axes[1].set_title("各學年學院結構（堆疊）", fontsize=16, pad=12)
axes[1].set_ylabel("人數")
# 設定 X 軸標籤不旋轉 (水平顯示)
axes[1].tick_params(axis="x", rotation=0)
axes[1].legend(title="學院", loc="upper right", fontsize=9)

# 為整張圖表加上一個大標題 (suptitle)
fig.suptitle("國立澎湖科技大學  109–114 學年新生生源分析",
             fontsize=18, fontweight="bold", y=1.02)
# 自動調整子圖之間的間距，避免圖形與文字重疊
fig.tight_layout()

# ── 5.5 檔案輸出：使用 'x' 模式避免覆蓋現有檔案 ────────────────
# 'x' 模式代表 exclusive creation (互斥建立)。如果檔案已存在，會拋出 FileExistsError。
OUT = HERE / "A08-college-trend.png"
try:
    # 開啟二進位寫入 ('xb') 模式來儲存圖片
    with open(OUT, "xb") as f:
        # 將 matplotlib 的圖表物件寫入到檔案中，設定解析度為 150 dpi，並裁切掉多餘的白邊
        fig.savefig(f, dpi=150, bbox_inches="tight")
    print(f"\n圖檔已寫入：{OUT.name}")
except FileExistsError:
    # 捕捉檔案已存在的例外，並提示使用者
    print(f"\n{OUT.name} 已存在，保留舊檔（要重畫請先刪除）")

# 在視窗中顯示圖表
plt.show()

# ── 延伸挑戰 ──────────────────────────────────────────
# 1) 改畫「各系所」熱力圖：sns.heatmap(pivot_by_dept, annot=True, fmt='d')
# 2) 加一張圓餅圖：114 學年學院占比
# 3) 把年度 x 軸改成 '109學年'~'114學年' 字串（需轉型 + set_xticklabels）
