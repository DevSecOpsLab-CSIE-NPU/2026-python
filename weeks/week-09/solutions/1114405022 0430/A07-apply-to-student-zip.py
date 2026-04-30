# A07. 綜合應用：把 I/O 技巧套到真實學生資料
# Bloom: Apply — 複習並組合 R01~A06 的 API
#
# 資料來源：assets/npu-stu-109-114-anon.zip（6 屆新生資料庫，學號已匿名）
# 用到的小節對照：
#   5.11 pathlib 組路徑
#   5.12 exists 檢查
#   5.7  zipfile 讀壓縮檔（不解壓）
#   5.1  encoding='utf-8-sig' 處理 Excel 存的 BOM
#   5.6  io.StringIO 把 bytes 轉成 csv 可讀的 file-like
#   5.19 TemporaryDirectory 沙箱輸出
#   5.5  open(..., 'x') 只寫一次的報告檔
#   5.21 pickle 保存跨屆統計快照
#   5.2  print(file=) 寫 Markdown 週報

# ─────────────────────────────────────────────────────────────
# 必要的模組導入
# ─────────────────────────────────────────────────────────────
import csv                    # 用於讀寫 CSV 格式的資料
import io                     # 提供 StringIO 類別，將 bytes 轉換為 file-like 物件供 csv.reader 使用
import pickle                 # 序列化 Python 物件，用於保存複雜的資料結構（如 dict）
import tempfile               # 建立臨時檔案和目錄，用來沙箱化輸出（避免留下臨時檔案）
import zipfile                # 讀取壓縮檔（.zip），無須先解壓到磁碟
from collections import Counter  # 計數工具，統計元素出現次數
from pathlib import Path      # 跨平台的路徑操作（取代 os.path）

# ─────────────────────────────────────────────────────────────
# 5.11 / 5.12 節：用 pathlib 組路徑並檢查檔案是否存在
# ─────────────────────────────────────────────────────────────
HERE = Path(__file__).resolve().parent
# 組路徑：當前檔案位置 → 向上 4 層 → assets 資料夾 → zip 檔
# 層級：A07-apply-to-student-zip.py → 1114405022 0430 → solutions → week-09 → weeks → 2026 python
ZIP_PATH = HERE.parent.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
# assert：如果檔案不存在，程式停止並輸出錯誤訊息
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ─────────────────────────────────────────────────────────────
# 5.7 / 5.6 / 5.1 節：不解壓直接讀 zip 中的 CSV
# ─────────────────────────────────────────────────────────────
def iter_year_csv(zip_path: Path):
    """
    從 zip 檔逐年讀取 CSV，每次 yield 一年份的資料。
    
    參數：
        zip_path：zip 檔的路徑
    
    Yield：
        (年度字串, CSV 表頭列表, CSV 資料列表的列表)
        例：('109', ['學號', '姓名', '系所名稱', ...], [['學生1資料'], ['學生2資料'], ...])
    """
    # 用 with 陳述式自動管理 zip 檔的開關
    with zipfile.ZipFile(zip_path) as z:
        # z.infolist()：列出 zip 內所有檔案的資訊
        for info in z.infolist():
            # 舊版 zip 常用 cp437 編碼，導致中文檔名亂碼，此版本已是乾淨 utf-8
            name = info.filename
            
            # 只處理 .csv 檔案，跳過其他檔案
            if not name.endswith(".csv"):
                continue
            
            # 從檔名前 3 個字元提取年份（如 '109-abc.csv' → '109'）
            year = name[:3]  # 年份字串，例：'109'~'114'

            # 5.7 節：從 zip 內讀取檔案，回傳 bytes 型別的原始資料
            raw = z.read(info)                       
            
            # 5.1 節：decode('utf-8-sig') 將 bytes 轉為字串，並移除 BOM（Byte Order Mark）
            # BOM 是 Excel 存 utf-8 時常加的前綴，需要移除才能正確解析
            text = raw.decode("utf-8-sig")           
            
            # 5.6 節：io.StringIO 將字串「包裝」成檔案物件供 csv.reader 使用
            # csv.reader 只能讀檔案物件，不能直接讀字串，所以需要 StringIO
            reader = csv.reader(io.StringIO(text))   
            
            # 將所有列轉成 list（list of lists）：第一行是表頭，後續是資料行
            rows = list(reader)
            
            # yield：每次產出一年份的資料（年份, 表頭, 資料行）
            yield year, rows[0], rows[1:]


# ─────────────────────────────────────────────────────────────
# 主要分析：跨 6 屆統計新生數量、系所分布、入學方式分布
# ─────────────────────────────────────────────────────────────
# 資料結構設計：
#   summary = {
#       '109': {'total': 總人數, 'by_dept': Counter({系所名稱: 人數}), 'by_entry': Counter({入學方式: 人數})},
#       '110': {...},
#       ...
#   }
summary = {}        
all_depts = Counter()  # 跨全部 6 屆統計各系所累計人數

# 逐年讀取資料並統計
for year, header, rows in iter_year_csv(ZIP_PATH):
    # 找出「系所名稱」和「入學方式」兩欄的位置
    # header.index() 傳回該欄位在列中的索引位置
    dept_idx  = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    # 逐行統計：提取對應欄位的值，用 Counter 計算出現次數
    # if len(r) > dept_idx：檢查該行是否有足夠的欄位（防止索引超界）
    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    # 為該年份建立統計摘要
    summary[year] = {
        "total":    len(rows),      # 該年份學生總人數
        "by_dept":  by_dept,        # 該年份各系所人數分布
        "by_entry": by_entry,       # 該年份各入學方式人數分布
    }
    
    # 更新跨屆系所統計（累加該年份的各系所人數到全體統計）
    all_depts.update(by_dept)

# ─────────────────────────────────────────────────────────────
# 終端輸出：統計摘要和主要發現
# ─────────────────────────────────────────────────────────────
print("\n=== 6 屆新生人數 ===")
for year in sorted(summary):  # sorted()：按年份從小到大排列
    # :>4 格式化：數字右對齐，佔用 4 個字符寬度
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")

print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")
# Counter.most_common(5)：回傳出現最頻繁的 5 個元素及其計數
for dept, n in all_depts.most_common(5):
    print(f"  {n:>4} 人  {dept}")

print("\n=== 114 學年入學方式分布 ===")
# 列出 114 年份中所有入學方式及其人數，按人數從多到少排列
for kind, n in summary["114"]["by_entry"].most_common():
    print(f"  {n:>4} 人  {kind}")


# ─────────────────────────────────────────────────────────────
# 5.19 / 5.5 / 5.2 / 5.21 節：沙箱輸出和序列化
# 使用臨時目錄產生報告和快照，避免在真實專案留下測試檔案
# ─────────────────────────────────────────────────────────────
# with tempfile.TemporaryDirectory()：建立臨時目錄，在 with 區塊結束時自動清除
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)  # 轉換為 Path 物件，方便路徑操作

    # ─ 5.21 節：pickle 序列化 ─
    # pickle：將複雜 Python 物件（如 dict）序列化成二進制格式存檔
    # 優點：完全保留資料型態，日後可用 pickle.load() 直接還原
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:  # "wb"：binary write 模式
        pickle.dump(summary, f)  # 把 summary dict 序列化並寫入檔案
    # stat().st_size：取得檔案大小（位元組）
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # ─ 5.5 / 5.2 節：產生 Markdown 報告 ─
    # 5.5 節：open() 的 'x' 模式 = exclusive creation
    # 作用：若檔案已存在會拋例外，防止意外覆蓋
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:      # "x"：exclusive 只寫一次
        # 5.2 節：print(file=f) 將輸出寫到檔案而非終端
        print("# 6 屆新生概況報告\n", file=f)           # 標題
        print("| 學年 | 人數 | 第一大系所 |", file=f)    # 表格標頭
        print("|------|------|------------|" , file=f)   # 表格分隔線
        
        # 逐年製作報告行
        for year in sorted(summary):
            # most_common(1)[0]：取最熱門的 1 個系所，[0] 取出 tuple 中的項目
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # ─ 5.1 節：讀取 Markdown 檔案並輸出預覽 ─
    # Path.read_text()：一次性讀整個檔案到字串
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # ─ 驗證 pickle 反序列化 ─
    # pickle.load()：從二進制檔案讀回並還原 Python 物件
    # 驗證型別和內容是否完全一致
    with open(snap, "rb") as f:  # "rb"：binary read 模式
        loaded = pickle.load(f)
    # 印出還原後的 dict key，驗證結構正確
    print("pickle 讀回 key:", sorted(loaded.keys()))

# ─ 臨時目錄自動清理 ─
# 離開 with tempfile.TemporaryDirectory() 區塊後，
# tmp 目錄及其所有內容自動刪除，不會在專案留下臨時檔案
print("\n(沙箱已自動清理)")


# ─────────────────────────────────────────────────────────────
# 課堂延伸挑戰（供學習者進階練習）
# ─────────────────────────────────────────────────────────────
# 1) 把報告改寫到 HERE / 'report.md'
#    挑戰：改用 'w' 模式會覆蓋舊檔，'x' 模式會報錯
#    需要檢查檔案是否存在，決定使用 'w' 或 'x'
#
# 2) 加一欄「女性比例」：找出性別欄位後用 Counter 統計
#    提示：先用 header.index("性別") 定位性別欄
#    然後統計男女人數，計算百分比
#
# 3) 把 summary 壓縮存成 summary.pkl.gz
#    提示：使用 gzip.open('wb') 代替 open('wb')
#    再用 pickle.dump(summary, f) 寫入
#
# 4) 跨屆找出「人數逐年下降最明顯」的系所
#    提示：把 by_dept 按年份排成時間序列（tuple list）
#    計算首尾人數差異，找最大負數差
#    可用 matplotlib 畫折線圖視覺化趨勢
