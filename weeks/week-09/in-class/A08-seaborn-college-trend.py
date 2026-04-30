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
#
# 新技巧：pandas dataframe / seaborn 繪圖 / matplotlib 中文字型

# ╔════════════════════════════════════════════════════╗
# ║ 【導入模組】I/O + 資料處理 + 視覺化                ║
# ╚════════════════════════════════════════════════════╝

import csv             # CSV 讀寫
import io              # StringIO：字串當檔案
import platform        # 偵測作業系統（決定字型）
import zipfile         # 讀壓縮檔

import matplotlib.pyplot as plt  # matplotlib 繪圖核心（底層）
import pandas as pd             # pandas dataframe（高階表格操作）
import seaborn as sns           # seaborn 統計繪圖（基於 matplotlib）
from pathlib import Path        # 跨平台路徑

# ╔════════════════════════════════════════════════════╗
# ║ 【matplotlib 中文字型設定】跨平台支援              ║
# ║ 問題：matplotlib 預設字型不含中文字符            ║
# ║ 解法：按作業系統選用有中文的系統字型              ║
# ╚════════════════════════════════════════════════════╝

# 【字型字典】各平台內建的中文字型
# macOS（Darwin）：Heiti TC / Arial Unicode MS / PingFang TC
# Windows：Microsoft JhengHei（微軟正黑體）/ Microsoft YaHei（微軟雅黑）
# Linux：Noto Sans CJK TC / WenQuanYi Zen Hei
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])  # 預設值


def _apply_cjk_font():
    """【功能】套用中文字型到 matplotlib。
    
    【為什麼需要這個函數？】
      - sns.set_theme() 會重設所有 rcParams（包括字型）
      - 所以每次呼叫 set_theme 後都要重新套用中文字型
      - 獨立函數便於複用
    
    【rcParams 說明】
      - 'font.sans-serif'：無襯線字族（中文通常無襯線）
      - 'font.family'：指定為 'sans-serif' 使用上面的字體列表
      - 'axes.unicode_minus'：False = 不用 U+2212（防止負號亂碼）
    """
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.unicode_minus"] = False


_apply_cjk_font()  # 程式開始時先套用一次

# ╔════════════════════════════════════════════════════╗
# ║ 【系所→學院對照表】NPU 的組織結構                  ║
# ║ 用途：把細粒度的「系所」聚合成粗粒度的「學院」    ║
# ║ 好處：資料分群，視覺化時不會太繁雜               ║
# ╚════════════════════════════════════════════════════╝

DEPT_TO_COLLEGE = {
    # ╔═ 人文暨管理學院 ═╗
    "應用外語系":       "人文暨管理學院",
    "航運管理系":       "人文暨管理學院",
    "行銷與物流管理系": "人文暨管理學院",
    "觀光休閒系":       "人文暨管理學院",
    "資訊管理系":       "人文暨管理學院",
    "餐旅管理系":       "人文暨管理學院",
    
    # ╔═ 海洋資源暨工程學院 ═╗
    "水產養殖系":       "海洋資源暨工程學院",
    "海洋遊憩系":       "海洋資源暨工程學院",
    "食品科學系":       "海洋資源暨工程學院",
    
    # ╔═ 電資工程學院 ═╗
    "資訊工程系":       "電資工程學院",
    "電信工程系":       "電資工程學院",
    "電機工程系":       "電資工程學院",
}

# ╔════════════════════════════════════════════════════╗
# ║ 【5.11】路徑定位 + 資料檔案檢查                    ║
# ╚════════════════════════════════════════════════════╝

HERE = Path(__file__).resolve().parent  # 當前 .py 檔所在資料夾
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到：{ZIP_PATH}"


# ╔════════════════════════════════════════════════════╗
# ║ 【5.7+5.6+5.1】讀 zip 內所有 CSV 成 long-form     ║
# ║ long-form 表：一列一筆記錄，便於 pandas 和 seaborn ║
# ╚════════════════════════════════════════════════════╝

def load_long_frame(zip_path: Path) -> pd.DataFrame:
    """【功能】從 zip 讀取所有 CSV，轉成 pandas long-form 表。
    
    【long-form 格式說明】
      行（row）：每一列代表一個新生
      列（column）：學年、學院、系所
    
    【為什麼用 long-form？】
      - 便於 groupby / pivot / seaborn 統計
      - 每行一筆記錄，規範化設計
      - vs. wide-form（每欄一個分類），wide-form 難以統計
    
    【csv.DictReader vs csv.reader】
      - DictReader：用第一列做 key，回傳字典列表（推薦）
      - reader：回傳列表列表，需手動管理欄位名稱
    """
    records = []
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            # 【篩選】只處理 CSV 檔
            if not info.filename.endswith(".csv"):
                continue
            
            # 【提取年度】檔名前 3 字元 = '109'..'114'
            year = info.filename[:3]
            
            # ╔════════════════════════════════╗
            # ║ 【三步驟】bytes → 文字 → 表格   ║
            # ╚════════════════════════════════╝
            
            # 第1步：讀成 bytes
            # 第2步：decode("utf-8-sig") = 解碼 + 去 BOM
            raw_text = z.read(info).decode("utf-8-sig")
            
            # 第3步：StringIO 當檔案用，DictReader 讀成字典列表
            reader = csv.DictReader(io.StringIO(raw_text))
            
            # 【逐列處理】每一列是一個新生記錄
            for row in reader:
                # 【提取系所】row 是字典 {"系所名稱": "...", "入學方式": "...", ...}
                dept = row.get("系所名稱", "").strip()
                
                # 【防守】若系所欄空白，跳過
                if not dept:
                    continue
                
                # 【追加記錄】轉成統一格式，包括學院名稱
                records.append({
                    "學年": int(year),  # 型別轉換：'109' → 109
                    "學院": DEPT_TO_COLLEGE.get(dept, "其他"),  # 查表、預設值
                    "系所": dept,
                })
    
    # 【DataFrame 建構】從記錄列表建 dataframe
    # from_records：快速把 dict 列表轉 dataframe
    return pd.DataFrame.from_records(records)


# ╔════════════════════════════════════════════════════╗
# ║ 【資料加載】讀取 zip 轉成 dataframe                ║
# ╚════════════════════════════════════════════════════╝

df = load_long_frame(ZIP_PATH)  # 讀全部 CSV → long-form dataframe

# 【驗證資料】
print("總筆數:", len(df))  # 應該是 6 屆新生的總人數
print(df.head())  # 顯示前 5 列（檢查欄位和資料正確性）

# ╔════════════════════════════════════════════════════╗
# ║ 【樞紐表（Pivot）】按學年 × 學院統計人數          ║
# ║ 用途：從 long-form 轉成適合繪圖的形式            ║
# ╚════════════════════════════════════════════════════╝

# 【groupby】按 (學年, 學院) 分組
# 【size()】每組計數（人數）
# 【reset_index】把索引轉成欄位
# 【name="人數"】重命名計數欄位為「人數」
pivot = (df.groupby(["學年", "學院"])
           .size()
           .reset_index(name="人數"))

print("\n各學年各學院統計：")
# 【pivot()】轉成寬表：索引=學年，欄位=學院，值=人數
print(pivot.pivot(index="學年", columns="學院", values="人數"))


# ╔════════════════════════════════════════════════════╗
# ║ 【seaborn 繪圖】視覺化呈現                          ║
# ║ sns.set_theme：全域樣式設定                        ║
# ║   - style="whitegrid"：白背景 + 網格線            ║
# ║   - context="talk"：中等字體（演講用）            ║
# ║   - palette="Set2"：配色方案                      ║
# ╚════════════════════════════════════════════════════╝

sns.set_theme(style="whitegrid", context="talk", palette="Set2")
_apply_cjk_font()  # 【重要】set_theme 會重設字型，須重新套用中文

# ╔════════════════════════════════════════════════════╗
# ║ 【建立圖表】2 個子圖並排                            ║
# ║ figsize=(15, 6)：寬 15、高 6 英吋                 ║
# ║ width_ratios=[1.3, 1]：左圖寬度 1.3，右圖 1       ║
# ╚════════════════════════════════════════════════════╝

fig, axes = plt.subplots(1, 2, figsize=(15, 6),
                         gridspec_kw={"width_ratios": [1.3, 1]})

# ╔════════════════════════════════════════════════════╗
# ║ 【圖 A】折線 + 散點圖：各學院逐年趨勢             ║
# ║ x=學年，y=人數，hue=學院（用顏色區分）           ║
# ╚════════════════════════════════════════════════════╝

sns.lineplot(data=pivot, x="學年", y="人數", hue="學院",
             marker="o",        # 圓形標記
             markersize=10,     # 標記大小
             linewidth=2.5,     # 線寬
             ax=axes[0])        # 畫在 axes[0]

axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=16, pad=12)
axes[0].set_xticks(sorted(pivot["學年"].unique()))  # x 軸標籤 = 所有年度
axes[0].legend(title="學院", loc="upper right", frameon=True)

# ╔════════════════════════════════════════════════════╗
# ║ 【資料標籤】在每個點上標註確切人數                ║
# ║ iterrows()：逐列迭代（效率次優，但程式簡潔）     ║
# ║ annotate()：在座標 (x, y) 加文字標籤              ║
# ║ xytext=(0, 8)：標籤向上偏移 8 點                 ║
# ╚════════════════════════════════════════════════════╝

for _, r in pivot.iterrows():
    axes[0].annotate(int(r["人數"]),
                     (r["學年"], r["人數"]),  # 標籤位置
                     textcoords="offset points",
                     xytext=(0, 8),           # 相對於點的偏移
                     ha="center",             # 水平置中
                     fontsize=9,
                     alpha=0.8)               # 透明度

# ╔════════════════════════════════════════════════════╗
# ║ 【圖 B】堆疊長條圖：每年學院占比結構               ║
# ║ 寬表：行=學年，列=學院，值=人數                   ║
# ║ stacked=True：堆疊各學院的長條                   ║
# ╚════════════════════════════════════════════════════╝

# 【轉換】pivot 是 long-form → 轉成寬表
# fillna(0)：缺失值填 0（避免計算錯誤）
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)

# 【堆疊長條圖】
# kind="bar"：長條圖
# stacked=True：堆疊模式
# edgecolor="white"：長條邊框為白色（便於視覺區隔）
pivot_wide.plot(kind="bar", stacked=True,
                ax=axes[1], colormap="Set2", width=0.75, edgecolor="white")

axes[1].set_title("各學年學院結構（堆疊）", fontsize=16, pad=12)
axes[1].set_ylabel("人數")
axes[1].tick_params(axis="x", rotation=0)  # x 軸標籤不旋轉
axes[1].legend(title="學院", loc="upper right", fontsize=9)

# ╔════════════════════════════════════════════════════╗
# ║ 【總標題】整張圖表標題 + 調整佈局                  ║
# ╚════════════════════════════════════════════════════╝

fig.suptitle("國立澎湖科技大學  109–114 學年新生生源分析",
             fontsize=18, fontweight="bold", y=1.02)
fig.tight_layout()  # 自動調整子圖間距，避免重疊

# ╔════════════════════════════════════════════════════╗
# ║ 【5.5】排他性寫檔：檔案已存在就保留舊的            ║
# ║ open(..., "xb")：exclusive binary write            ║
# ║   存在 → FileExistsError                           ║
# ║   不存在 → 建立新檔並寫入                          ║
# ║ 用途：防止誤覆蓋手工調整後的圖檔                  ║
# ╚════════════════════════════════════════════════════╝

OUT = HERE / "A08-college-trend.png"  # 輸出路徑

try:
    # 【"xb" 模式】exclusive binary：存在就報錯，不存在才寫
    with open(OUT, "xb") as f:
        # 【fig.savefig(f, ...)】把圖表存成 PNG
        # dpi=150：圖片解析度（150 dpi = 高品質）
        # bbox_inches="tight"：去除圖表周圍空白
        fig.savefig(f, dpi=150, bbox_inches="tight")
    print(f"\n✓ 圖檔已寫入：{OUT.name}")
except FileExistsError:
    print(f"\n⚠ {OUT.name} 已存在，保留舊檔")
    print(f"   （要重畫請先刪除舊檔或改檔名）")

plt.show()  # 在螢幕顯示圖表


# ╔════════════════════════════════════════════════════╗
# ║ 【課堂延伸挑戰】進階視覺化練習                    ║
# ╚════════════════════════════════════════════════════╝

# 1️⃣  【目標】改畫「各系所」熱力圖
#    【步驟】
#      1. 建立 pivot：index=系所、columns=學年、values=人數
#      2. 用 sns.heatmap(pivot_by_dept, annot=True, fmt='d')
#      3. 熱力圖會自動用顏色深淺表現人數多寡
#    【技巧】
#      - annot=True：在格子裡顯示數字
#      - fmt='d'：數字格式（整數）
#      - cmap='YlOrRd'：顏色方案（黃→橙→紅）
#      - cbar_kws={'label': '人數'}：色列標籤
#
# 2️⃣  【目標】加一張圓餅圖：114 學年學院占比
#    【步驟】
#      1. 過濾 114 年資料：data_114 = pivot[pivot['學年']==114]
#      2. plt.figure(figsize=(8, 8))
#      3. plt.pie(data_114['人數'], labels=data_114['學院'], autopct='%1.1f%%')
#    【技巧】
#      - autopct='%1.1f%%'：自動標註百分比
#      - startangle=90：圓餅起始角度
#      - colors=sns.color_palette('Set2')：用 seaborn 配色
#
# 3️⃣  【目標】把年度 x 軸改成字串：'109學年'~'114學年'
#    【步驟】
#      1. 建立新欄位：pivot['年度標籤'] = pivot['學年'].apply(lambda y: f'{y}學年')
#      2. lineplot 改用 x='年度標籤'（字串而非整數）
#      3. set_xticklabels(sorted(...), rotation=45)：旋轉標籤便於閱讀
#    【技巧】
#      - apply() + lambda：批量轉換欄位
#      - 字串 x 軸需要 set_xticklabels()
#
# 4️⃣  【進階】做交互式圖表（plotly）
#    【工具】import plotly.express as px
#    【優勢】
#      - 互動式滑鼠懸停顯示資訊
#      - 可縮放 / 移動 / 輸出
#      - 比靜態圖表更吸引人
#    【程式】px.line(pivot, x='學年', y='人數', color='學院', markers=True)

