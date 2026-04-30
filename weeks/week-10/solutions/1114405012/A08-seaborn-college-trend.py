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

# ── 中文字型設定：依執行平台自動選用適配的字體 ─────────────────────────
# matplotlib 預設的字體不支援中文，所以要手動指定系統內建的 CJK 字體。
# 依平台不同準備不同的字體清單，優先嘗試常見的幾個，都沒有就用通用的 sans-serif。
# Darwin = macOS、Windows = Windows、Linux = Linux
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])


def _apply_cjk_font():
    """每次 sns.set_theme 都會重設 rcParams，所以需要獨立成函數，在必要時重新套用中文字體。

    設定三項重點：
    1. font.sans-serif：把我們選好的 CJK 字體清單放在最前面
    2. font.family：告訴 matplotlib 使用 sans-serif 這族字體
    3. axes.unicode_minus：關閉負號 - 被誤認成連字符的問題，改用真正的負號
    """
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False


_apply_cjk_font()

# ── 系所 → 學院 對照表（NPU 三大學院） ─────────────────
# 這個字典用來把各個系所名稱對應到其所屬學院。
# 資料來源的 CSV 內只有系所名稱，沒有學院資訊，所以用這張表手動對應。
# 若有系所在表中找不到，會默認分類成「其他」。
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

# ── 5.11 定位資料檔 ─────────────────────────────────────
# HERE 是這支程式所在的資料夾，接著往上 3 層到專案根目錄，再進 assets 找 zip 檔。
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
# 若資料檔不存在就立刻停止，避免後面出現難以追蹤的錯誤。
assert ZIP_PATH.exists(), f"找不到：{ZIP_PATH}"


# ── 5.7 + 5.6 + 5.1 從 zip 內逐一讀 CSV，轉成長格式 DataFrame ─
def load_long_frame(zip_path: Path) -> pd.DataFrame:
    """把壓縮檔中所有 CSV 讀取並整合成單一 DataFrame，每一列代表一個學生。

    流程：
    1. 枚舉 zip 內的 CSV 檔
    2. 用 DictReader（而非 reader）讓每列自動對應到欄位名
    3. 抽取年度、系所，並透過 DEPT_TO_COLLEGE 映射到學院
    4. 累積所有學生記錄再轉成 DataFrame
    """
    records = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            # 只處理 CSV，忽略其他可能的檔案
            if not info.filename.endswith(".csv"):
                continue
            # 檔名前 3 碼是學年度
            year = info.filename[:3]                     # '109'..'114'
            # 讀 bytes 後解碼為字串，utf-8-sig 會自動去掉 Excel 的 BOM
            text = z.read(info).decode("utf-8-sig")      # 去 BOM
            # DictReader 讓每列自動跟欄位名配對，比手動 index 更清楚
            reader = csv.DictReader(io.StringIO(text))   # 當檔讀
            for row in reader:
                # 取出系所名稱，並清除前後空白
                dept = row.get("系所名稱", "").strip()
                # 若欄位空白則略過這一列
                if not dept:
                    continue
                # 組成「一個學生」的記錄，包含年度、所屬學院（透過映射表查詢）、原始系所名稱
                records.append({
                    "學年": int(year),
                    "學院": DEPT_TO_COLLEGE.get(dept, "其他"),
                    "系所": dept,
                })
    # 把所有記錄轉成 DataFrame，每列一個學生
    return pd.DataFrame.from_records(records)


# 載入所有學生資料
df = load_long_frame(ZIP_PATH)
print("總筆數:", len(df))
print(df.head())

# ── 樞紐轉換：把「學生記錄」轉成「各學年×各學院的人數統計」 ───
# groupby(["學年", "學院"]) 會依這兩個欄位分組
# .size() 計算每個分組的列數（即該組有多少學生）
# .reset_index() 把分組結果轉回一般 DataFrame
# name="人數" 把計數結果取名為「人數」這個新欄位
pivot = (df.groupby(["學年", "學院"])
           .size()
           .reset_index(name="人數"))
print("\n各學年各學院:")
# 再做一次 pivot，把「學院」轉成欄（便於橫向比較每年各院的人數）
print(pivot.pivot(index="學年", columns="學院", values="人數"))


# ── seaborn 繪圖設定 ──────────────────────────────────────
# set_theme 統一設定視覺風格
#  - style="whitegrid"：背景有淺灰格線
#  - context="talk"：字體與線條粗細適合簡報展示
#  - palette="Set2"：選用柔和的配色方案
sns.set_theme(style="whitegrid", context="talk", palette="Set2")
# set_theme 會重設 rcParams，所以要再次套用中文字體
_apply_cjk_font()  # 蓋回中文字型

# 建立一個 1×2 的子圖配置，左邊較寬（1.3 倍）用來放線圖，右邊放長條圖
fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.2),
                         gridspec_kw={"width_ratios": [1.25, 1]})

# ── 圖 A（左）：折線圖 —— 各學院逐年人數趨勢 ────────────────────
# lineplot 會自動依 hue="學院" 繪製多條線（一個學院一條）
# marker="o" 在每個資料點標出圓形標記，便於識別確切年份
sns.lineplot(data=pivot, x="學年", y="人數", hue="學院",
             marker="o", markersize=10, linewidth=2.5, ax=axes[0])
# 設定標題、x 軸標籤（只顯示整數年份）、圖例位置
axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=16, pad=12)
axes[0].set_xticks(sorted(pivot["學年"].unique()))
axes[0].legend(title="學院", loc="upper right", frameon=True,
               fontsize=8, title_fontsize=10, markerscale=0.8,
               labelspacing=0.4, borderpad=0.5, handlelength=2.0)

# ── 在線圖上標註人數（方便直接看到數值）────────────────
# 逐列遍歷統計表 pivot，在每個資料點上加上人數標籤
for _, r in pivot.iterrows():
    # annotate 的參數：
    # - 第 1 個 int(r["人數"]) 是標籤文字
    # - (r["學年"], r["人數"]) 是標籤要貼在圖上的座標
    # - textcoords="offset points", xytext=(0, 8) 代表標籤位置相對於點向上偏移 8 個點
    # - ha="center" 文字水平置中
    axes[0].annotate(int(r["人數"]),
                     (r["學年"], r["人數"]),
                     textcoords="offset points", xytext=(0, 8),
                     ha="center", fontsize=9, alpha=0.8)

# ── 圖 B（右）：堆疊長條圖 —— 各年度學院結構比例 ────────────────────
# pivot_wide 的資料格式為 (學年 × 各學院)，每一列是某年度各學院的人數
# fillna(0) 若有缺失值（某年某院沒招生）則填 0
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)
# kind="bar" 繪製長條圖，stacked=True 讓多個學院的長條疊在一起
# 這樣可以看出每年度各學院占整體的比例，以及逐年結構變化
pivot_wide.plot(kind="bar", stacked=True,
                ax=axes[1], colormap="Set2", width=0.75, edgecolor="white")
axes[1].set_title("各學年學院結構（堆疊）", fontsize=16, pad=12)
axes[1].set_ylabel("人數")
# rotation=0 使 x 軸年份標籤保持水平，易於閱讀
axes[1].tick_params(axis="x", rotation=0)
axes[1].legend(title="學院", loc="upper right", fontsize=8,
               title_fontsize=10, labelspacing=0.4, borderpad=0.5,
               handlelength=1.5)

# 加上整張圖的總標題，y 放低一點，避免被上緣裁切
fig.suptitle("國立澎湖科技大學  109–114 學年新生生源分析",
             fontsize=16, fontweight="bold", y=0.98)
# tight_layout 只排版子圖，但保留上方給總標題的空間
fig.tight_layout(rect=[0, 0, 1, 0.93])

# ── 5.5 以 'xb' 模式輸出：避免誤覆蓋既有檔案 ────────────────
# 'xb' 代表「binary exclusive write」，只在檔案不存在時才建立並寫入
# 如果檔案已存在就會拋出 FileExistsError，讓使用者明確決定是否刪除舊檔再重新繪製
OUT = HERE / "A08-college-trend.png"
try:
    with open(OUT, "xb") as f:
        # dpi=150 輸出高解析度，bbox_inches="tight" 去掉周邊白邊
        fig.savefig(f, dpi=150, bbox_inches="tight")
    print(f"\n圖檔已寫入：{OUT.name}")
except FileExistsError:
    # 檔案已存在時，保留舊檔而不覆蓋
    print(f"\n{OUT.name} 已存在，保留舊檔（要重畫請先刪除）")

# 在 Jupyter 或互動式環境中顯示圖表
plt.show()

# ── 延伸挑戰：可以繼續練習的方向 ──────────────────────────────────────────
# 這些題目提供進一步延伸分析與視覺化的想法。
# 1) 改畫「各系所」熱力圖：先 groupby(["學年", "系所"]).size()，再 pivot 成 2D 表
#    然後用 sns.heatmap(pivot_by_dept, annot=True, fmt='d', cmap='YlOrRd')
# 2) 加一張圓餅圖：計算 114 學年各學院總人數，用 axes[2].pie() 或 plt.figure 畫圓餅
# 3) 把年度 x 軸改成 '109學年'~'114學年' 字串
#    做法：在 pivot 中新增欄位 year_str = pivot["學年"].apply(lambda x: f"{x}學年")
#    再用 set_xticklabels 替換軸標籤
