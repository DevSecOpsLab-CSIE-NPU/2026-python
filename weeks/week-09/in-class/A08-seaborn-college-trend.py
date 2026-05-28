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

# ── 中文字型：依平台挑一個有的 ─────────────────────────
# matplotlib 在 macOS 預設抓不到 PingFang TC，用系統內建的 Heiti TC / Arial Unicode MS
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])


def _apply_cjk_font():
    """sns.set_theme 會重設 rcParams，需要在它之後再套一次。"""
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False


_apply_cjk_font()

# ── 系所 → 學院 對照表（NPU 三大學院） ─────────────────
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

# ── 5.11 定位資料 ─────────────────────────────────────
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到：{ZIP_PATH}"


# ── 5.7 + 5.6 + 5.1 讀 zip 內所有 CSV 成一張 long-form 表 ─
def load_long_frame(zip_path: Path) -> pd.DataFrame:
    records = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            if not info.filename.endswith(".csv"):
                continue
            year = info.filename[:3]                     # '109'..'114'
            text = z.read(info).decode("utf-8-sig")      # 去 BOM
            reader = csv.DictReader(io.StringIO(text))   # 當檔讀
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

# 樞紐：各學年 × 各學院 的人數
pivot = (df.groupby(["學年", "學院"])
           .size()
           .reset_index(name="人數"))
print("\n各學年各學院:")
print(pivot.pivot(index="學年", columns="學院", values="人數"))


# ── seaborn 繪圖 ──────────────────────────────────────
sns.set_theme(style="whitegrid", context="talk", palette="Set2")
_apply_cjk_font()  # 蓋回中文字型

fig, axes = plt.subplots(1, 2, figsize=(15, 6),
                         gridspec_kw={"width_ratios": [1.3, 1]})

# 圖 A：折線＋散點 —— 各學院逐年趨勢
sns.lineplot(data=pivot, x="學年", y="人數", hue="學院",
             marker="o", markersize=10, linewidth=2.5, ax=axes[0])
axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=16, pad=12)
axes[0].set_xticks(sorted(pivot["學年"].unique()))
axes[0].legend(title="學院", loc="upper right", frameon=True)

# 在每個點上標註人數
for _, r in pivot.iterrows():
    axes[0].annotate(int(r["人數"]),
                     (r["學年"], r["人數"]),
                     textcoords="offset points", xytext=(0, 8),
                     ha="center", fontsize=9, alpha=0.8)

# 圖 B：堆疊長條 —— 每年學院占比
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)
pivot_wide.plot(kind="bar", stacked=True,
                ax=axes[1], colormap="Set2", width=0.75, edgecolor="white")
axes[1].set_title("各學年學院結構（堆疊）", fontsize=16, pad=12)
axes[1].set_ylabel("人數")
axes[1].tick_params(axis="x", rotation=0)
axes[1].legend(title="學院", loc="upper right", fontsize=9)

fig.suptitle("國立澎湖科技大學  109–114 學年新生生源分析",
             fontsize=18, fontweight="bold", y=1.02)
fig.tight_layout()

# ── 5.5 'x' 模式輸出：檔已存在就保留舊的 ────────────────
OUT = HERE / "A08-college-trend.png"
try:
    with open(OUT, "xb") as f:
        fig.savefig(f, dpi=150, bbox_inches="tight")
    print(f"\n圖檔已寫入：{OUT.name}")
except FileExistsError:
    print(f"\n{OUT.name} 已存在，保留舊檔（要重畫請先刪除）")

plt.show()

# ── 延伸挑戰 ──────────────────────────────────────────
# 1) 改畫「各系所」熱力圖：sns.heatmap(pivot_by_dept, annot=True, fmt='d')
# 2) 加一張圓餅圖：114 學年學院占比
# 3) 把年度 x 軸改成 '109學年'~'114學年' 字串（需轉型 + set_xticklabels）
