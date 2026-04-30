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

# 【匯入模組說明】
import csv          # 用來讀寫 CSV 檔案格式
import io           # 用來建立 StringIO 物件，將 bytes 轉換成可供 csv 讀取的類檔案對象
import pickle       # 用來序列化和反序列化 Python 物件，方便保存複雜的資料結構
import tempfile     # 用來建立臨時目錄或檔案（用完後自動清理，不污染專案）
import zipfile      # 用來讀寫 ZIP 壓縮檔（本例不解壓，直接讀取內部檔案）
from collections import Counter  # 用來統計計數，方便找出最常見的元素
from pathlib import Path  # 用來處理檔案路徑（跨平台兼容）

# ═══════════════════════════════════════════════════════════
# 【第一步】找到資料檔（5.11 / 5.12 pathlib 組路徑 + exists 檢查）
# ═══════════════════════════════════════════════════════════
# HERE：當前 Python 腳本所在的目錄
HERE = Path(__file__).resolve().parent

# ZIP_PATH：透過相對路徑向上3層找到 assets 資料夾
# 此程式在 weeks/week-09/in-class/ 底下
# 向上3層 (.../weeks) 後，進入 assets 資料夾找 ZIP 檔
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"

# 斷言檢查：確保 ZIP 檔存在，若不存在則程式停止並顯示錯誤訊息
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ═══════════════════════════════════════════════════════════
# 【第二步】定義產生器函數，用來逐年讀取 ZIP 內的 CSV 檔
# ═══════════════════════════════════════════════════════════
# 技巧組合：5.7（zipfile）+ 5.6（StringIO）+ 5.1（UTF-8-sig 編碼）
def iter_year_csv(zip_path: Path):
    """
    逐年從 ZIP 檔讀取 CSV 資料。
    
    參數：
        zip_path (Path)：ZIP 檔的路徑
    
    逐次產生（Yield）：
        year (str)：年度，如 '109'、'110' 等
        header (list)：CSV 的表頭（欄位名稱）
        rows (list)：CSV 的資料列（不含表頭）
    """
    # 以 ZipFile 方式打開 ZIP 檔（不解壓到磁碟）
    with zipfile.ZipFile(zip_path) as z:
        # 逐個檢查 ZIP 內的所有檔案
        for info in z.infolist():
            # 取得檔案名稱（舊 zip 的中文檔名常見編碼問題，此處已乾淨）
            name = info.filename
            
            # 只處理 .csv 檔案，跳過其他類型
            if not name.endswith(".csv"):
                continue
            
            # 從檔名前3個字符提取年度（如 '109_xxx.csv' → '109'）
            year = name[:3]  # '109'~'114'

            # 【讀取步驟】
            raw = z.read(info)                       # 讀取原始二進制資料（bytes）
            text = raw.decode("utf-8-sig")           # (5.1) 以 UTF-8-sig 編碼解碼，自動移除 BOM
            reader = csv.reader(io.StringIO(text))   # (5.6) 用 StringIO 將文字轉成類檔案對象供 csv 讀取
            
            # 把 CSV 讀取器的所有行轉成列表
            rows = list(reader)
            
            # 產生 (年度, 表頭, 資料列) 的元組
            # rows[0] 是表頭，rows[1:] 是實際資料
            yield year, rows[0], rows[1:]


# ═══════════════════════════════════════════════════════════
# 【第三步】跨屆統計處理：按年度與系所、入學方式分類計數
# ═══════════════════════════════════════════════════════════
# summary 字典：儲存每一屆的統計結果
# 結構：{年度字串: {'total': 總人數, 'by_dept': 按系所計數, 'by_entry': 按入學方式計數}}
summary = {}        

# all_depts：累計所有屆別中所有系所的出現次數
all_depts = Counter()

# 逐年讀取並統計
for year, header, rows in iter_year_csv(ZIP_PATH):
    # 找出「系所名稱」和「入學方式」在 CSV 表頭中的欄位位置
    dept_idx  = header.index("系所名稱")  # 系所欄的索引位置
    entry_idx = header.index("入學方式")  # 入學方式欄的索引位置

    # 統計各系所人數：使用 Counter 自動計數每個系所出現的次數
    # 檢查 len(r) > dept_idx 確保該列有足夠欄位（防止 IndexError）
    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)
    
    # 統計各入學方式人數：同樣使用 Counter 計數
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    # 將該年度的統計結果存入 summary 字典
    summary[year] = {
        "total":    len(rows),        # 該屆的總人數
        "by_dept":  by_dept,          # 該屆的系所分布
        "by_entry": by_entry,         # 該屆的入學方式分布
    }
    
    # 更新全體系所統計（6 屆的累計）
    all_depts.update(by_dept)

# ═══════════════════════════════════════════════════════════
# 【第四步】終端輸出：顯示統計結果摘要
# ═══════════════════════════════════════════════════════════
# 統計 1：各年度新生總人數
print("\n=== 6 屆新生人數 ===")
for year in sorted(summary):  # 依年度排序輸出（109~114）
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")  # 右對齊顯示人數

# 統計 2：6 屆累計最常見的系所（前 5 名）
print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")
for dept, n in all_depts.most_common(5):  # most_common(5) 傳回計數最多的前 5 個
    print(f"  {n:>4} 人  {dept}")  # 依人數遞減排序

# 統計 3：最新年度（114）的入學方式分布
print("\n=== 114 學年入學方式分布 ===")
for kind, n in summary["114"]["by_entry"].most_common():  # 取得 114 年的入學方式統計，依計數遞減
    print(f"  {n:>4} 人  {kind}")


# ═══════════════════════════════════════════════════════════
# 【第五步】沙箱環境：產生臨時報告和快照
# ═══════════════════════════════════════════════════════════
# (5.19) 使用臨時目錄：用完後自動清理，不污染專案目錄
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)  # 將路徑字串轉成 Path 物件方便操作

    # ─── 子步驟 1：(5.21) 用 Pickle 序列化保存整個 summary 字典 ───
    # Pickle 可以直接保存複雜的 Python 物件（如嵌套字典和 Counter）
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:  # "wb" = write binary（寫入二進制）
        pickle.dump(summary, f)   # 將 summary 序列化並寫入檔案
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # ─── 子步驟 2：(5.5 + 5.2) 產生 Markdown 報告 ───
    # (5.5) 'x' 模式：Exclusive create（若檔案已存在會報錯，防止誤覆蓋）
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:      # (5.5) 'x' 模式
        # (5.2) print(..., file=f) 將內容寫入檔案而非標準輸出
        print("# 6 屆新生概況報告\n", file=f)           
        print("| 學年 | 人數 | 第一大系所 |", file=f)  # 表格表頭
        print("|------|------|------------|" , file=f) # 表格分隔線
        
        # 逐年製作一列資料
        for year in sorted(summary):
            # 取得該年度最常見的系所及其人數
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            # 輸出表格行：年度 | 總人數 | 第一大系所及人數
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # ─── 子步驟 3：讀回 Markdown 檔案驗證內容 ───
    # Path.read_text()：簡潔的檔案讀取方法
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))  # 讀取並印出報告內容

    # ─── 子步驟 4：反序列化 Pickle 檔案驗證 ───
    # 確認 pickle 能夠正確還原原始資料
    with open(snap, "rb") as f:  # "rb" = read binary（讀取二進制）
        loaded = pickle.load(f)   # 反序列化回 Python 物件
    print("pickle 讀回 key:", sorted(loaded.keys()))  # 顯示還原的字典鍵值（確認內容完整）

# 【第六步】沙箱自動清理
# 離開 with 區塊 → TemporaryDirectory 自動刪除 tmp 目錄及其所有內容
# 這樣就不會在專案目錄留下任何臨時檔案
print("\n(沙箱已自動清理)")


# ═══════════════════════════════════════════════════════════
# 【課堂延伸挑戰】
# ═══════════════════════════════════════════════════════════
# 1) 把報告改寫到 HERE / 'report.md'
#    - 改用 'w' 模式會每次覆蓋檔案
#    - 改用 'a' 模式會追加內容
#    - 'x' 模式會防止誤覆蓋（檔案存在會報錯）
#
# 2) 加一欄「女性比例」到報告中
#    - 找出 CSV 的性別欄位
#    - 用 Counter 統計男女人數
#    - 計算比例後寫入表格
#
# 3) 把 summary 壓縮存成 summary.pkl.gz
#    - 改用 gzip.open('wb') 而不是普通的 open()
#    - 後續用 gzip.open('rb') + pickle.load() 讀回
#    - 可節省約 50% 的磁碟空間
#
# 4) 跨屆找出「人數逐年下降最明顯」的系所
#    - 需要按年度排序後比較各年的 Counter
#    - 計算該系所在各年的差異
#    - 找出衰退最快的系所
