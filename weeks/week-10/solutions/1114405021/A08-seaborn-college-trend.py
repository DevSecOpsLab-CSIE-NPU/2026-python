# A08. 用 seaborn 畫 109~114 學年各學院生源分析圖
# Bloom: Apply — 這支程式承接 A07 的資料處理結果，
# 把原始 CSV 轉成可視化圖表，讓跨年度趨勢更容易看懂。
#
# 需要：pip install seaborn matplotlib pandas
#
# 用到的 I/O 技巧延續 A07：
#   5.7  zipfile：直接從壓縮檔讀 CSV，不先解壓到磁碟
#   5.1  utf-8-sig：處理 CSV 常見的 BOM 問題
#   5.6  io.StringIO：把字串包成檔案物件，方便 csv 模組讀取
#   5.11 pathlib：用物件化方式組路徑
#   5.5  open('x')：避免覆蓋已存在的輸出圖檔

import csv
import io
import platform
import zipfile
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ── 中文字型：依平台挑一個有的 ─────────────────────────
# matplotlib 預設字型通常不完整，若直接畫中文，標題與座標軸很容易變成方塊。
# 這裡依作業系統挑選常見的中文黑體或通用中文字型，盡量提高相容性。
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])


def _apply_cjk_font():
    """設定中文顯示所需的字型與負號樣式。

    seaborn 的 set_theme 可能會重設 matplotlib 的 rcParams，
    所以這個函式會在需要的地方重複呼叫，確保中文字型真的生效。
    """
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False


_apply_cjk_font()

# ── 系所 → 學院 對照表（NPU 三大學院） ─────────────────
# 原始 CSV 只提供系所名稱，若要分析學院層級趨勢，
# 就必須先把每個系所歸類到對應學院。
# 這個對照表就是資料清洗與重新分群的核心。
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
# 先抓出目前檔案所在位置，再一路回到專案根目錄，
# 最後拼出 assets 內的資料檔路徑。
# 檔案位置：d:\21\weeks\week-10\solutions\1114405021\A08-seaborn-college-trend.py
# 專案根目錄：d:\21
# 所以需要往上走 4 層：solutions -> week-10 -> weeks -> 21（根目錄）
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到：{ZIP_PATH}"


# ── 5.7 + 5.6 + 5.1 讀 zip 內所有 CSV 成一張 long-form 表 ─
# 這個函式是整支程式的資料入口。
# 它會逐一打開 zip 裡的 CSV，讀出每列資料，再轉成適合 pandas 分析的資料表。
def load_long_frame(zip_path: Path) -> pd.DataFrame:
    # records 先用 list 累積所有資料列，最後一次轉成 DataFrame。
    # 這種寫法比每讀到一列就直接拼 DataFrame 更直覺，也比較適合教學展示。
    records = []
    with zipfile.ZipFile(zip_path) as z:
        # z.infolist() 會列出 zip 裡所有檔案，包含資料檔、可能的資料夾項目等。
        # 所以這裡先過濾副檔名，只保留真正要分析的 CSV。
        for info in z.infolist():
            if not info.filename.endswith(".csv"):
                continue

            # 檔名像 109.csv、110.csv ...，前 3 碼就是學年代號。
            # 這裡是用檔名來辨識學年，避免額外再查其他欄位。
            year = info.filename[:3]

            # 先把 bytes 解碼成文字，再交給 DictReader。
            # DictReader 會把第一列欄名轉成字典 key，因此程式不用手算欄位位置，
            # 只要欄名固定，之後欄位順序改變也不會壞掉。
            text = z.read(info).decode("utf-8-sig")
            reader = csv.DictReader(io.StringIO(text))
            for row in reader:
                # 只保留系所名稱有值的資料列，避免空白列或異常列影響分析。
                # strip() 會順手去掉左右空白，減少像 " 資訊工程系" 這種格式問題。
                dept = row.get("系所名稱", "").strip()
                if not dept:
                    continue

                # 將原始資料整理成長表（long-form）：
                # 每一筆只保留「學年 / 學院 / 系所」三個分析欄位。
                # 這樣做的好處是後面可以很自然地用 groupby、pivot、seaborn 繪圖。
                records.append({
                    "學年": int(year),
                    "學院": DEPT_TO_COLLEGE.get(dept, "其他"),
                    "系所": dept,
                })
    # pandas 可以直接把 list of dicts 轉成 DataFrame，方便後續 groupby 與繪圖。
    # 回傳 DataFrame 後，就可以把原始字串資料當成結構化資料來做統計分析。
    return pd.DataFrame.from_records(records)


df = load_long_frame(ZIP_PATH)
# 先印出總筆數與前幾列，方便確認資料是否成功載入、欄位是否正確。
print("總筆數:", len(df))
print(df.head())

# 樞紐：各學年 × 各學院 的人數
# groupby + size() 會把同一學年、同一學院的資料筆數統計出來，
# 再 reset_index 變回普通資料表，方便後續拿去畫圖。
pivot = (df.groupby(["學年", "學院"])
           .size()
           .reset_index(name="人數"))
# 這裡先做出「長格式統計表」，每列代表某一個學年 + 某一個學院的總人數。
# .size() 會回傳每個群組有幾筆資料，reset_index 後就會變成可直接檢視的表格。
# 之所以先印出來，是為了在畫圖前先確認分類結果沒有跑掉。
print("\n各學年各學院:")
print(pivot.pivot(index="學年", columns="學院", values="人數"))


# ── seaborn 繪圖 ──────────────────────────────────────
# 先設定 seaborn 主題，再補回中文字型設定，避免 theme 覆蓋掉前面的 rcParams。
sns.set_theme(style="whitegrid", context="talk", palette="Set2")
_apply_cjk_font()  # 蓋回中文字型

# 兩張圖並排：左邊看趨勢，右邊看結構。
fig, axes = plt.subplots(1, 2, figsize=(15, 6),
                         gridspec_kw={"width_ratios": [1.3, 1]})

# 圖 A：折線＋散點 —— 各學院逐年趨勢
# 折線圖適合看時間序列的變化；marker 則讓每個年度的資料點更明確。
# hue="學院" 會讓每個學院畫成不同顏色，方便比較誰成長、誰下降。
sns.lineplot(data=pivot, x="學年", y="人數", hue="學院",
             marker="o", markersize=10, linewidth=2.5, ax=axes[0])
axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=16, pad=12)
# 這裡手動指定 x 軸刻度，避免 seaborn 自動挑選時漏掉年度或排序混亂。
axes[0].set_xticks(sorted(pivot["學年"].unique()))
# 把圖例字體改小（fontsize=8），避免壓到折線圖。
axes[0].legend(title="學院", loc="upper right", frameon=True, fontsize=8)

# 在每個點上標註人數，讓讀圖者不必另外估算數值。
for _, r in pivot.iterrows():
    axes[0].annotate(int(r["人數"]),
                     (r["學年"], r["人數"]),
                     textcoords="offset points", xytext=(0, 8),
                     ha="center", fontsize=9, alpha=0.8)

# 圖 B：堆疊長條 —— 每年學院占比
# 先把長表 pivot 成寬表，讓每個學年是一列、每個學院是一欄。
# fillna(0) 代表若某學年沒有某學院資料，就補 0，避免畫圖時出現空值。
# 再用 stacked bar 直接觀察各學年的組成結構，也就是「總量」與「比例」同時看。
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)
pivot_wide.plot(kind="bar", stacked=True,
                ax=axes[1], colormap="Set2", width=0.75, edgecolor="white")
axes[1].set_title("各學年學院結構（堆疊）", fontsize=16, pad=12)
# y 軸標示人數，讓讀者知道這是數量圖，不是比例圖。
axes[1].set_ylabel("人數")
axes[1].tick_params(axis="x", rotation=0)
# 圖例說明每一種顏色對應哪個學院，方便快速辨識堆疊區塊。
axes[1].legend(title="學院", loc="upper right", fontsize=9)

# suptitle 是整張圖的總標題，用來交代分析主題與年度範圍。
fig.suptitle("國立澎湖科技大學  109–114 學年新生生源分析",
             fontsize=18, fontweight="bold", y=1.02)
# tight_layout 會自動調整邊界，避免標題、圖例、座標軸互相重疊。
fig.tight_layout()

# ── 5.5 'x' 模式輸出：檔已存在就保留舊的 ────────────────
# 圖檔輸出放在程式同一層目錄，方便同學直接找到生成結果。
OUT = HERE / "A08-college-trend.png"
try:
    # 使用 xb 代表二進位建立模式；若檔案已存在，會直接丟出 FileExistsError。
    # 這比先判斷 exists 再開檔更安全，因為檢查與建立之間不會被其他流程插隊覆蓋。
    with open(OUT, "xb") as f:
        # 將圖直接寫入已開啟的檔案物件，避免路徑重複處理。
        fig.savefig(f, dpi=150, bbox_inches="tight")
    print(f"\n圖檔已寫入：{OUT.name}")
except FileExistsError:
    # 如果舊圖還在，就不覆蓋，避免不小心把前一次輸出的成果洗掉。
    print(f"\n{OUT.name} 已存在，保留舊檔（要重畫請先刪除）")

# 顯示圖形視窗，讓執行時可以立即檢視成果。
# 如果是在沒有圖形介面的環境執行，這行可能只會停在後端繪圖，不一定跳出視窗。
plt.show()

# ── 延伸挑戰 ──────────────────────────────────────────
# 這些延伸題目可用來練習把同一份資料換不同角度分析：
# 1) 改畫「各系所」熱力圖：sns.heatmap(pivot_by_dept, annot=True, fmt='d')
# 2) 加一張圓餅圖：114 學年學院占比
# 3) 把年度 x 軸改成 '109學年'~'114學年' 字串（需轉型 + set_xticklabels）
