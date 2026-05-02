# A08. 用 seaborn 畫 109~114 學年各學院生源分析圖
# 這份版本保留原本繪圖流程，並補上較完整的繁體中文註解。
#
# Bloom: Apply — 把 A07 的統計成果交給視覺化套件
#
# 需要：pip install seaborn matplotlib pandas
#
# 用到的 I/O 技巧延續 A07：
# 5.7 zipfile 不解壓讀 CSV
# 5.1 utf-8-sig 去 BOM
# 5.6 io.StringIO → csv
# 5.11 pathlib
# 5.5 open('x') 不覆蓋輸出檔

import csv
import io
import platform
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# ── 中文字型：依平台挑一個有的 ─────────────────────────
# matplotlib 在不同作業系統上的預設中文字型支援不一樣，
# 所以這裡先列出常見可用字型，再在後面統一套用。
_CJK_FONTS = {
    "Darwin": ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux": ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])


def _apply_cjk_font():
    """sns.set_theme 會重設 rcParams，因此要在它之後再套一次中文字型。"""
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False


_apply_cjk_font()


# ── 系所 → 學院 對照表（NPU 三大學院） ─────────────────
DEPT_TO_COLLEGE = {
    # 人文暨管理學院
    "應用外語系": "人文暨管理學院",
    "航運管理系": "人文暨管理學院",
    "行銷與物流管理系": "人文暨管理學院",
    "觀光休閒系": "人文暨管理學院",
    "資訊管理系": "人文暨管理學院",
    "餐旅管理系": "人文暨管理學院",
    # 海洋資源暨工程學院
    "水產養殖系": "海洋資源暨工程學院",
    "海洋遊憩系": "海洋資源暨工程學院",
    "食品科學系": "海洋資源暨工程學院",
    # 電資工程學院
    "資訊工程系": "電資工程學院",
    "電信工程系": "電資工程學院",
    "電機工程系": "電資工程學院",
}


# ── 5.11 定位資料 ─────────────────────────────────────
HERE = Path(__file__).resolve().parent


def _find_zip_path() -> Path:
    """從目前檔案位置往上找，直到找到 assets 底下的資料壓縮檔。"""
    for base in [HERE, *HERE.parents]:
        candidate = base / "assets" / "npu-stu-109-114-anon.zip"
        if candidate.exists():
            return candidate
    raise FileNotFoundError("找不到 assets/npu-stu-109-114-anon.zip")


try:
    ZIP_PATH = _find_zip_path()
except FileNotFoundError:
    ZIP_PATH = None


# ── 5.7 + 5.6 + 5.1 讀 zip 內所有 CSV 成一張 long-form 表 ─
def load_long_frame(zip_path: Path) -> pd.DataFrame:
    """把 zip 內多個年度 CSV 合併成一張長表，方便做群組統計。"""
    records = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            if not info.filename.endswith(".csv"):
                continue
            # 檔名前 3 碼是學年，例如 109、110、111 ... 114
            year = info.filename[:3]
            # 先把 bytes 轉成文字，再交給 DictReader 依欄名讀值。
            text = z.read(info).decode("utf-8-sig")
            reader = csv.DictReader(io.StringIO(text))
            for row in reader:
                dept = row.get("系所名稱", "").strip()
                if not dept:
                    continue
                # 每一筆只保留分析需要的欄位：學年、學院、系所。
                records.append(
                    {
                        "學年": int(year),
                        "學院": DEPT_TO_COLLEGE.get(dept, "其他"),
                        "系所": dept,
                    }
                )
    return pd.DataFrame.from_records(records)


if ZIP_PATH is not None:
    df = load_long_frame(ZIP_PATH)
    print("總筆數:", len(df))
    print(df.head())
else:
    # fallback: generate synthetic example data when zip not available
    print("assets zip not found — using synthetic sample data for plotting")
    years = [109, 110, 111, 112, 113, 114]
    cols = [
        '人文暨管理學院',
        '海洋資源暨工程學院',
        '電資工程學院',
    ]
    vals = {
        '人文暨管理學院': [120, 130, 125, 140, 150, 160],
        '海洋資源暨工程學院': [80, 85, 90, 88, 92, 95],
        '電資工程學院': [100, 110, 115, 120, 130, 135],
    }
    records = []
    for i, y in enumerate(years):
        for c in cols:
            records.append({'學年': y, '學院': c, '人數': vals[c][i]})
    df = pd.DataFrame.from_records(records)

# 樞紐：各學年 × 各學院 的人數
if "人數" in df.columns:
    pivot = df.groupby(["學年", "學院"])['人數'].sum().reset_index(name="人數")
else:
    pivot = df.groupby(["學年", "學院"]).size().reset_index(name="人數")
print("\n各學年各學院:")
print(pivot.pivot(index="學年", columns="學院", values="人數"))


# ── seaborn 繪圖 ──────────────────────────────────────
# 設定主題後再補一次中文字型，避免 seaborn 重設 matplotlib rcParams。
sns.set_theme(style="whitegrid", context="notebook", palette="Set2")
_apply_cjk_font()

fig, axes = plt.subplots(
    1,
    2,
    figsize=(9.2, 3.8),
    gridspec_kw={"width_ratios": [1.3, 1]},
)

# 圖 A：折線＋散點 —— 各學院逐年趨勢
sns.lineplot(
    data=pivot.sort_values("學年"),
    x="學年",
    y="人數",
    hue="學院",
    style="學院",
    markers=True,
    dashes=False,
    marker="o",
    markersize=8,
    linewidth=2.2,
    ax=axes[0],
)
axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=12, pad=8)
axes[0].set_xticks(sorted(pivot["學年"].unique()))
axes[0].legend(title="學院", loc="upper right", frameon=True, fontsize=8, title_fontsize=9)

# 在每個點上標註人數，方便肉眼直接讀出數值。
for _, r in pivot.iterrows():
    axes[0].annotate(
        int(r["人數"]),
        (r["學年"], r["人數"]),
        textcoords="offset points",
        xytext=(0, 5),
        ha="center",
        fontsize=7,
        alpha=0.8,
    )

# 圖 B：堆疊長條 —— 每年學院占比
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)
pivot_wide.plot(
    kind="bar",
    stacked=True,
    ax=axes[1],
    colormap="Set2",
    width=0.75,
    edgecolor="white",
)
axes[1].set_title("各學年學院結構（堆疊）", fontsize=12, pad=8)
axes[1].set_ylabel("人數")
axes[1].tick_params(axis="x", rotation=0)
axes[1].legend(title="學院", loc="upper right", fontsize=8, title_fontsize=9)

fig.suptitle(
    "國立澎湖科技大學 109–114 學年新生生源分析",
    fontsize=11,
    fontweight="bold",
    y=0.98,
)
fig.tight_layout(rect=(0, 0, 1, 0.92))

# ── 5.5 輸出圖片：每次執行都直接產生新檔 ────────────────
OUT = HERE / "A08-college-trend.png"
# 直接覆寫輸出檔，這樣每次執行都一定會更新圖片內容。
fig.savefig(OUT, dpi=110, bbox_inches="tight", pad_inches=0.08)
print(f"\n圖檔已寫入：{OUT.name}")

plt.show()


# ── 延伸挑戰 ──────────────────────────────────────────
# 1) 改畫「各系所」熱力圖：sns.heatmap(pivot_by_dept, annot=True, fmt='d')
# 2) 加一張圓餅圖：114 學年學院占比
# 3) 把年度 x 軸改成 '109學年'~'114學年' 字串（需轉型 + set_xticklabels）