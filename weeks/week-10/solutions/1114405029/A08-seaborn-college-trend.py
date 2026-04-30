# A08. 用 seaborn 畫 109~114 學年各學院生源分析圖
# Bloom: Apply — 把 A07 的統計成果交給視覺化套件
#
# 資料來源與 A07 相同，都是讀取 assets/npu-stu-109-114-anon.zip
# 這份程式的主要目標：
# 1. 從 zip 壓縮檔中讀取 109~114 學年的 CSV 新生資料
# 2. 根據「系所名稱」對應到「學院」
# 3. 整理成 pandas DataFrame
# 4. 統計各學年、各學院的新生人數
# 5. 使用 seaborn / matplotlib 畫出趨勢圖與堆疊長條圖
#
# 需要：pip install seaborn matplotlib pandas
#
# 用到的 I/O 技巧延續 A07：
#   5.7  zipfile 不解壓讀 CSV
#   5.1  utf-8-sig 去 BOM
#   5.6  io.StringIO → csv
#   5.11 pathlib
#   5.5  open('x') 不覆蓋輸出檔

# 匯入 csv 模組，用來讀取 CSV 格式的學生資料
import csv

# 匯入 io 模組，這裡會使用 io.StringIO
# StringIO 可以把字串包裝成「像檔案一樣」的物件，讓 csv 可以讀取
import io

# 匯入 platform 模組，用來判斷目前作業系統是 Windows、macOS 還是 Linux
# 後面會根據不同系統選擇適合的中文字型
import platform

# 匯入 zipfile 模組，用來直接讀取 zip 壓縮檔內的 CSV，不需要先手動解壓縮
import zipfile

# 從 pathlib 匯入 Path
# Path 可以用比較清楚的方式處理資料夾與檔案路徑
from pathlib import Path

# 匯入 matplotlib.pyplot，主要負責建立圖表、設定標題、座標軸、儲存圖片等
import matplotlib.pyplot as plt

# 匯入 pandas，主要用來建立 DataFrame、分組統計、樞紐表整理資料
import pandas as pd

# 匯入 seaborn，主要用來畫比較漂亮且方便的統計圖表
import seaborn as sns

# ── 中文字型：依平台挑一個有的 ─────────────────────────
# matplotlib 在 macOS 預設抓不到 PingFang TC，用系統內建的 Heiti TC / Arial Unicode MS
# 這個字典會依照不同作業系統，準備可能支援繁體中文的字型清單
# Darwin 代表 macOS
# Windows 代表 Windows 系統
# Linux 代表 Linux 系統
# 如果偵測不到系統，就使用 sans-serif 當作預設字型
_CJK_FONTS = {
    "Darwin":  ["Heiti TC", "Arial Unicode MS", "PingFang TC"],
    "Windows": ["Microsoft JhengHei", "Microsoft YaHei"],
    "Linux":   ["Noto Sans CJK TC", "WenQuanYi Zen Hei"],
}.get(platform.system(), ["sans-serif"])


# 定義套用中文字型的函式
# 因為 seaborn 的 sns.set_theme() 會重設 matplotlib 的 rcParams
# 所以設定 seaborn 主題之後，中文字型可能會被覆蓋掉
# 因此這個函式後面會呼叫兩次：
# 第一次先套用中文字型
# 第二次在 sns.set_theme() 之後再套用一次
def _apply_cjk_font():
    """sns.set_theme 會重設 rcParams，需要在它之後再套一次。"""

    # 設定 sans-serif 字型清單
    # 把前面依作業系統挑出的中文字型放在原本字型清單前面
    # 這樣 matplotlib 會優先使用可顯示中文的字型
    plt.rcParams["font.sans-serif"] = _CJK_FONTS + plt.rcParams["font.sans-serif"]

    # 指定整體字型家族使用 sans-serif
    plt.rcParams["font.family"] = "sans-serif"

    # 避免座標軸中的負號顯示成方框或亂碼
    plt.rcParams["axes.unicode_minus"] = False


# 呼叫函式，先套用一次中文字型設定
_apply_cjk_font()

# ── 系所 → 學院 對照表（NPU 三大學院） ─────────────────
# 這個字典用來把每個「系所名稱」對應到所屬的「學院」
# 後面讀取每一筆學生資料時，會根據系所名稱查出該學生屬於哪個學院
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
# __file__ 代表目前這支 Python 程式檔案的位置
# resolve() 會轉成絕對路徑
# parent 代表取得目前程式所在的資料夾
HERE = Path(__file__).resolve().parent

# 組出學生資料 zip 檔的位置
# HERE.parent.parent.parent 代表從目前程式所在資料夾往上三層
# 再進入 assets 資料夾，找到 npu-stu-109-114-anon.zip
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"

# 檢查 zip 檔是否存在
# 如果檔案不存在，程式會停止，並顯示找不到檔案的錯誤訊息
assert ZIP_PATH.exists(), f"找不到：{ZIP_PATH}"


# ── 5.7 + 5.6 + 5.1 讀 zip 內所有 CSV 成一張 long-form 表 ─
# 定義函式 load_long_frame
# 功能：
# 1. 開啟 zip 檔
# 2. 逐一讀取 zip 裡面的 CSV 檔
# 3. 把每一位學生整理成一筆 record
# 4. 最後轉成 pandas DataFrame 回傳
def load_long_frame(zip_path: Path) -> pd.DataFrame:

    # records 用來暫存每一位學生的整理結果
    # 每一筆資料會是一個字典，例如：
    # {
    #   "學年": 109,
    #   "學院": "電資工程學院",
    #   "系所": "資訊工程系"
    # }
    records = []

    # 使用 zipfile.ZipFile 開啟 zip 壓縮檔
    # with 區塊結束後會自動關閉 zip 檔
    with zipfile.ZipFile(zip_path) as z:

        # z.infolist() 會列出 zip 檔裡所有檔案的資訊
        # info 代表 zip 裡面的其中一個檔案
        for info in z.infolist():

            # 如果檔名不是 .csv 結尾，就跳過
            # 這樣可以避免讀到非 CSV 檔案
            if not info.filename.endswith(".csv"):
                continue

            # 從檔名前三個字元取得學年
            # 例如 109.csv 會取得 "109"
            year = info.filename[:3]                     # '109'..'114'

            # 從 zip 中讀出 CSV 檔內容
            # z.read(info) 讀出來的是 bytes
            # decode("utf-8-sig") 會把 bytes 轉成文字，並處理可能存在的 BOM
            text = z.read(info).decode("utf-8-sig")      # 去 BOM

            # 使用 csv.DictReader 讀取 CSV
            # DictReader 會把每一列資料轉成字典
            # 欄位名稱會來自 CSV 第一列 header
            # io.StringIO(text) 則是把文字包裝成 file-like object
            reader = csv.DictReader(io.StringIO(text))   # 當檔讀

            # 逐列讀取學生資料
            # row 是一位學生的資料字典
            for row in reader:

                # 從該列資料取出「系所名稱」
                # 如果沒有這個欄位，就給空字串
                # strip() 用來去除前後空白，避免資料中多餘空白影響比對
                dept = row.get("系所名稱", "").strip()

                # 如果系所名稱是空的，代表這筆資料不完整
                # 直接跳過，不加入統計
                if not dept:
                    continue

                # 將整理好的資料加入 records
                # "學年" 轉成 int，方便後面排序與畫圖
                # "學院" 透過 DEPT_TO_COLLEGE 查詢
                # 如果系所不在對照表中，就分類成 "其他"
                # "系所" 保留原始系所名稱，方便後續延伸分析
                records.append({
                    "學年": int(year),
                    "學院": DEPT_TO_COLLEGE.get(dept, "其他"),
                    "系所": dept,
                })

    # 將 records 轉成 pandas DataFrame
    # DataFrame 是表格資料結構，方便後面 groupby、pivot、畫圖
    return pd.DataFrame.from_records(records)


# 呼叫 load_long_frame，讀取 zip 內所有 CSV，並整理成一張長格式資料表
df = load_long_frame(ZIP_PATH)

# 印出總筆數，也就是所有年度加總後的學生資料筆數
print("總筆數:", len(df))

# 印出 DataFrame 前五筆資料，方便確認欄位與資料內容是否正確
print(df.head())

# 樞紐：各學年 × 各學院 的人數
# 這裡先使用 groupby(["學年", "學院"])
# 代表依照學年與學院分組
# size() 會計算每一組有幾筆資料，也就是人數
# reset_index(name="人數") 會把統計結果重新變回表格，並把數量欄命名為「人數」
pivot = (df.groupby(["學年", "學院"])
           .size()
           .reset_index(name="人數"))

# 印出提示文字，表示接下來要顯示各學年、各學院的人數表
print("\n各學年各學院:")

# 將 pivot 轉成寬表格式印出
# index="學年" 代表每一列是學年
# columns="學院" 代表每一欄是學院
# values="人數" 代表表格中的值是人數
print(pivot.pivot(index="學年", columns="學院", values="人數"))


# ── seaborn 繪圖 ──────────────────────────────────────
# 設定 seaborn 主題
# style="whitegrid" 代表使用白底網格
# context="talk" 會讓字體與圖表元素較大，適合展示
# palette="Set2" 代表使用 Set2 色盤
sns.set_theme(style="whitegrid", context="talk", palette="Set2")

# 因為 sns.set_theme() 可能會重設字型設定
# 所以這裡再呼叫一次 _apply_cjk_font()，確保中文字能正常顯示
_apply_cjk_font()  # 蓋回中文字型

# 建立一張圖 fig，並建立左右兩個子圖 axes
# 1, 2 表示一列兩欄
# figsize=(15, 6) 表示整張圖的寬度 15、高度 6
# gridspec_kw={"width_ratios": [1.3, 1]} 表示左圖寬度比右圖稍大
fig, axes = plt.subplots(1, 2, figsize=(15, 6),
                         gridspec_kw={"width_ratios": [1.3, 1]})

# 圖 A：折線＋散點 —— 各學院逐年趨勢
# 使用 seaborn 的 lineplot 畫折線圖
# data=pivot 指定資料來源
# x="學年" 表示 x 軸使用學年
# y="人數" 表示 y 軸使用人數
# hue="學院" 表示不同學院用不同顏色區分
# marker="o" 表示每個資料點用圓點標示
# markersize=10 設定圓點大小
# linewidth=2.5 設定線條粗細
# ax=axes[0] 表示畫在左邊第一張子圖
sns.lineplot(data=pivot, x="學年", y="人數", hue="學院",
             marker="o", markersize=10, linewidth=2.5, ax=axes[0])

# 設定左圖標題
# fontsize=16 設定字體大小
# pad=12 設定標題與圖表的距離
axes[0].set_title("109–114 各學院新生人數趨勢", fontsize=16, pad=12)

# 設定 x 軸刻度
# sorted(pivot["學年"].unique()) 會取得所有不重複學年，並排序
axes[0].set_xticks(sorted(pivot["學年"].unique()))

# 設定左圖圖例
# title="學院" 表示圖例標題
# loc="upper right" 表示圖例放在右上角
# frameon=True 表示圖例外框顯示
axes[0].legend(title="學院", loc="upper right", frameon=True)

# 在每個點上標註人數
# pivot.iterrows() 會逐列取出資料
# r 代表其中一列資料，包含學年、學院、人數
for _, r in pivot.iterrows():

    # annotate 用來在圖上加入文字標註
    # int(r["人數"]) 是要顯示的文字，也就是人數
    # (r["學年"], r["人數"]) 是文字標註對應的資料點位置
    # textcoords="offset points" 表示文字位置使用偏移點數
    # xytext=(0, 8) 表示文字往上偏移 8 點，避免蓋住圓點
    # ha="center" 表示文字水平置中
    # fontsize=9 設定標註字體大小
    # alpha=0.8 設定透明度
    axes[0].annotate(int(r["人數"]),
                     (r["學年"], r["人數"]),
                     textcoords="offset points", xytext=(0, 8),
                     ha="center", fontsize=9, alpha=0.8)

# 圖 B：堆疊長條 —— 每年學院占比
# 將 pivot 轉成寬表格式
# 每一列是一個學年
# 每一欄是一個學院
# 表格中的值是人數
# fillna(0) 代表如果某學年某學院沒有資料，就補 0
pivot_wide = pivot.pivot(index="學年", columns="學院", values="人數").fillna(0)

# 使用 pandas 內建的 plot 畫堆疊長條圖
# kind="bar" 表示長條圖
# stacked=True 表示堆疊長條
# ax=axes[1] 表示畫在右邊第二張子圖
# colormap="Set2" 指定色盤
# width=0.75 設定每個長條寬度
# edgecolor="white" 設定每個堆疊區塊邊線為白色，讓區塊更清楚
pivot_wide.plot(kind="bar", stacked=True,
                ax=axes[1], colormap="Set2", width=0.75, edgecolor="white")

# 設定右圖標題
axes[1].set_title("各學年學院結構（堆疊）", fontsize=16, pad=12)

# 設定右圖 y 軸標籤
axes[1].set_ylabel("人數")

# 設定右圖 x 軸刻度文字不旋轉
# rotation=0 表示水平顯示
axes[1].tick_params(axis="x", rotation=0)

# 設定右圖圖例
# fontsize=9 讓圖例字體稍微小一點，避免佔太多空間
axes[1].legend(title="學院", loc="upper right", fontsize=9)

# 設定整張圖的大標題
# fontsize=18 設定字體大小
# fontweight="bold" 設定粗體
# y=1.02 表示標題稍微往上，避免和子圖標題擠在一起
fig.suptitle("國立澎湖科技大學  109–114 學年新生生源分析",
             fontsize=18, fontweight="bold", y=1.02)

# 自動調整圖表間距，避免標題、座標軸、圖例互相重疊
fig.tight_layout()

# ── 5.5 'x' 模式輸出：檔已存在就保留舊的 ────────────────
# 設定輸出圖片檔案的位置
# 圖片會輸出到目前程式所在資料夾
# 檔名為 A08-college-trend.png
OUT = HERE / "A08-college-trend.png"

# 使用 try / except 處理檔案已存在的情況
try:

    # 使用 "xb" 模式開啟檔案
    # x 表示 exclusive creation，也就是只允許建立新檔案
    # b 表示 binary，因為圖片檔是二進位檔案
    # 如果檔案已存在，會直接丟出 FileExistsError
    with open(OUT, "xb") as f:

        # 將 fig 圖表存成圖片
        # dpi=150 設定解析度
        # bbox_inches="tight" 會盡量裁掉多餘空白，讓圖片邊界更剛好
        fig.savefig(f, dpi=150, bbox_inches="tight")

    # 如果成功寫入圖片，就印出成功訊息
    print(f"\n圖檔已寫入：{OUT.name}")

# 如果圖片檔已經存在，就進入這裡
except FileExistsError:

    # 印出提醒訊息
    # 因為使用 x 模式，所以不會覆蓋原本舊圖檔
    print(f"\n{OUT.name} 已存在，保留舊檔（要重畫請先刪除）")

# 顯示圖表視窗
# 在 Jupyter 或部分 IDE 中，會直接顯示圖表
plt.show()

# ── 延伸挑戰 ──────────────────────────────────────────
# 1) 改畫「各系所」熱力圖：sns.heatmap(pivot_by_dept, annot=True, fmt='d')
# 2) 加一張圓餅圖：114 學年學院占比
# 3) 把年度 x 軸改成 '109學年'~'114學年' 字串（需轉型 + set_xticklabels）