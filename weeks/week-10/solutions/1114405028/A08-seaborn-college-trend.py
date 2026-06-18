# A08. 用 seaborn 畫 109~114 學年各學院生源分析圖
# 這個檔案是把週九的 A08 範例搬到 week-10 的解題資料夾，並加上詳細繁體中文註解。
# 範例重點：從 zip 壓縮檔中讀取 CSV 資料、轉成 DataFrame、畫折線圖與堆疊長條圖，最後將圖檔輸出。

import csv
import io
import platform
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 針對不同作業系統設定中文字型，避免 matplotlib 顯示中文亂碼
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])


def _apply_cjk_font():
    """為 matplotlib 設定中文字型與負號顯示。"""
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False


# 先套一次字型，讓後續繪圖能正確顯示中文
_apply_cjk_font()

# 將系所對應到三大學院，方便後續做學院級別統計
DEPT_TO_COLLEGE = {
    "應用外語系":       "人文暨管理學院",
    "航運管理系":       "人文暨管理學院",
    "行銷與物流管理系": "人文暨管理學院",
    "觀光休閒系":       "人文暨管理學院",
    "資訊管理系":       "人文暨管理學院",
    "餐旅管理系":       "人文暨管理學院",
    "水產養殖系":       "海洋資源暨工程學院",
    "海洋遊憩系":       "海洋資源暨工程學院",
    "食品科學系":       "海洋資源暨工程學院",
    "資訊工程系":       "電資工程學院",
    "電信工程系":       "電資工程學院",
    "電機工程系":       "電資工程學院",
}

# 檔案路徑：從本檔案位置往上走三層，再到 assets 目錄下讀取 ZIP
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到資料檔：{ZIP_PATH}"


def load_long_frame(zip_path: Path) -> pd.DataFrame:
    """讀取 ZIP 內所有 CSV 檔案，並回傳長格式的 DataFrame。"""
    records = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            if not info.filename.endswith(".csv"):
                continue
            year = info.filename[:3]  # 取檔名開頭的年度，例如 '109'
            text = z.read(info).decode("utf-8-sig")
            reader = csv.DictReader(io.StringIO(text))
            for row in reader:
                dept = row.get("系所名稱", "").strip()
                if not dept:
                    continue
                records.append({
                    "學年": int(year),
                    "學院": DEPT_TO_COLLEGE.get(dept, "其他"),
                    "系所": dept,
                })
    return pd.DataFrame.from_records(records)


df = load_long_frame(ZIP_PATH)
print("總筆數:", len(df))
print(df.head())

# 依學年與學院群組計算人數
pivot = (
    df.groupby(["學年", "學院"])
      .size()
      .reset_index(name="人數")
)
print("\n各學年各學院:")
print(pivot.pivot(index="學年", columns="學院", values="人數"))

# seaborn 主題設定，並在設定後重設中文字型
sns.set_theme(style="whitegrid", context="talk", palette="Set2")
_apply_cjk_font()

fig, axes = plt.subplots(1, 2, figsize=(15, 6), gridspec_kw={"width_ratios": [1.3, 1]})

# 圖A：折線圖顯示各學院逐年趨勢
sns.lineplot(
    data=pivot,
    x="學年",
    y="人數",
    hue="學院",
    marker="o",
    markersize=10,
    linewidth=2.5,
    ax=axes[0],
)
axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=16, pad=12)
axes[0].set_xticks(sorted(pivot["學年"].unique()))
axes[0].legend(title="學院", loc="upper right", frameon=True)

# 在每個資料點上加上人數標籤
for _, r in pivot.iterrows():
    axes[0].annotate(
        int(r["人數"]),
        (r["學年"], r["人數"]),
        textcoords="offset points",
        xytext=(0, 8),
        ha="center",
        fontsize=9,
        alpha=0.8,
    )

# 圖B：堆疊長條圖顯示各學年學院人數結構
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)
pivot_wide.plot(kind="bar", stacked=True, ax=axes[1], colormap="Set2", width=0.75, edgecolor="white")
axes[1].set_title("各學年學院結構（堆疊）", fontsize=16, pad=12)
axes[1].set_ylabel("人數")
axes[1].tick_params(axis="x", rotation=0)
axes[1].legend(title="學院", loc="upper right", fontsize=9)

fig.suptitle(
    "國立澎湖科技大學  109–114 學年新生生源分析",
    fontsize=18,
    fontweight="bold",
    y=1.02,
)
fig.tight_layout()

# 輸出圖檔，如果檔案已存在就保留舊檔
OUT = HERE / "A08-college-trend.png"
try:
    with open(OUT, "xb") as f:
        fig.savefig(f, dpi=150, bbox_inches="tight")
    print(f"\n圖檔已寫入：{OUT.name}")
except FileExistsError:
    print(f"\n{OUT.name} 已存在，保留舊檔（要重畫請先刪除）")

plt.show()
