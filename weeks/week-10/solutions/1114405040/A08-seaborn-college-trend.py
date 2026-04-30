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

# ── 中文字型設定：依作業系統挑一個可用的字型 ─────────────
# matplotlib 在不同平台可用的中文字型不同，所以先準備一份候選清單。
# 如果前面呼叫 sns.set_theme()，它可能會重設 rcParams，因此字型要再補一次。
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])


def _apply_cjk_font():
    """套用中文字型設定，避免圖表中文變成方塊。"""
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False


_apply_cjk_font()

# ── 系所對應學院的轉換表（國立澎湖科大三大學院） ─────────
# 這份對照表的用途，是把原始資料中的「系所名稱」轉成「學院」。
# 之後就能用學院為單位做統計與視覺化。
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

# ── 定位資料檔案位置 ──────────────────────────────────
# 以目前腳本所在位置為基準，往上找到專案根目錄，再連到 assets。
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到：{ZIP_PATH}"


# ── 讀取 zip 內所有 CSV，整理成長表格式資料 ─────────────
# 每一筆 record 代表「某學年、某系所」的一筆資料，方便後續 groupby。
def load_long_frame(zip_path: Path) -> pd.DataFrame:
    records = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            if not info.filename.endswith(".csv"):
                continue
            year = info.filename[:3]                     # 檔名開頭通常是 '109'..'114'
            text = z.read(info).decode("utf-8-sig")      # 去掉 Excel 常見的 BOM
            reader = csv.DictReader(io.StringIO(text))    # 讓字串可以像檔案一樣被 csv 讀取
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


# 讀入資料並先看一眼內容，確認有成功抓到資料。
df = load_long_frame(ZIP_PATH)
print("總筆數:", len(df))
print(df.head())

# 用 groupby 做出「學年 × 學院」的人數統計表。
pivot = (df.groupby(["學年", "學院"])
           .size()
           .reset_index(name="人數"))
print("\n各學年各學院:")
print(pivot.pivot(index="學年", columns="學院", values="人數"))


# ── 使用 seaborn / matplotlib 繪圖 ─────────────────────
# 先設定主題與風格，再畫兩張圖：趨勢折線圖與堆疊長條圖。
sns.set_theme(style="whitegrid", context="talk", palette="Set2")
_apply_cjk_font()  # 蓋回中文字型

fig, axes = plt.subplots(1, 2, figsize=(15, 6),
                         gridspec_kw={"width_ratios": [1.3, 1]})

# 圖 A：折線加散點，顯示各學院逐年變化趨勢。
sns.lineplot(data=pivot, x="學年", y="人數", hue="學院",
             marker="o", markersize=10, linewidth=2.5, ax=axes[0])
axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=16, pad=12)
axes[0].set_xticks(sorted(pivot["學年"].unique()))
axes[0].legend(title="學院", loc="upper right", frameon=True,
               fontsize=8, title_fontsize=9)

# 每個資料點都標上實際人數，讓圖表更容易直接閱讀。
for _, r in pivot.iterrows():
    axes[0].annotate(int(r["人數"]),
                     (r["學年"], r["人數"]),
                     textcoords="offset points", xytext=(0, 8),
                     ha="center", fontsize=9, alpha=0.8)

# 圖 B：堆疊長條圖，呈現每個學年各學院的結構分布。
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)
pivot_wide.plot(kind="bar", stacked=True,
                ax=axes[1], colormap="Set2", width=0.75, edgecolor="white")
axes[1].set_title("各學年學院結構（堆疊）", fontsize=16, pad=12)
axes[1].set_ylabel("人數")
axes[1].tick_params(axis="x", rotation=0)
axes[1].legend(title="學院", loc="upper right", fontsize=8, title_fontsize=9)

# 整體標題與版面微調，避免文字擠在一起。
fig.suptitle("國立澎湖科技大學  109–114 學年新生生源分析",
             fontsize=18, fontweight="bold", y=1.02)
fig.tight_layout()

# ── 只輸出一次圖檔：如果檔案已存在就不覆蓋 ─────────────
OUT = HERE / "A08-college-trend.png"
try:
    with open(OUT, "xb") as f:
        fig.savefig(f, dpi=150, bbox_inches="tight")
    print(f"\n圖檔已寫入：{OUT.name}")
except FileExistsError:
    print(f"\n{OUT.name} 已存在，保留舊檔（要重畫請先刪除）")

# 顯示圖表，方便在 Jupyter 或互動式環境直接查看。
plt.show()

# ── 延伸挑戰：可自行嘗試擴充功能 ───────────────────────
# 1) 改畫「各系所」熱力圖：sns.heatmap(pivot_by_dept, annot=True, fmt='d')
# 2) 加一張圓餅圖：114 學年學院占比
# 3) 把年度 x 軸改成 '109學年'~'114學年' 字串（需轉型 + set_xticklabels）
