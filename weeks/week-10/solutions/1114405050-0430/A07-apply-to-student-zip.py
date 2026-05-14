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

import csv
import io
import pickle
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

# ── 5.11 / 5.12 找到資料檔 ─────────────────────────────
# 取得目前程式檔案所在的絕對路徑，並往上層資料夾尋找 ZIP 壓縮檔
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
# 確保 ZIP 檔案存在，如果不存在就會拋出 AssertionError 並終止程式
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


# ── 5.7 + 5.6 + 5.1 不解壓讀 zip 裡的 CSV ──────────────
def iter_year_csv(zip_path: Path):
    """逐年 yield (年度, header, rows)。
    這是一個生成器 (Generator)，可以逐一吐出各年度的 CSV 資料，避免一次把所有檔案塞進記憶體。
    """
    # 開啟 ZIP 壓縮檔（不需要解壓縮到硬碟）
    with zipfile.ZipFile(zip_path) as z:
        # 遍歷壓縮檔內的每一個檔案資訊
        for info in z.infolist():
            # 舊 zip 的中文檔名常見 cp437 錯碼，這裡已經是乾淨的 utf-8 檔名
            name = info.filename
            # 只處理附檔名為 .csv 的檔案
            if not name.endswith(".csv"):
                continue
            # 從檔名（例如 "109-xxx.csv"）切出前 3 個字元作為學年度
            year = name[:3]

            # 讀取檔案內容，會得到 bytes 格式的二進位資料
            raw = z.read(info)
            # 5.1 使用 utf-8-sig 解碼，這可以自動去掉 Windows Excel 產生的 BOM (Byte Order Mark) 標記
            text = raw.decode("utf-8-sig")
            # 5.6 利用 io.StringIO 將字串包裝成類似檔案的物件，讓 csv.reader 可以順利讀取
            reader = csv.reader(io.StringIO(text))
            # 將 CSV 內容轉為二維列表
            rows = list(reader)
            # yield 回傳：學年度、標題列 (第 0 列)、資料列 (第 1 列開始到最後)
            yield year, rows[0], rows[1:]


# ── 跨屆統計 ───────────────────────────────────────────
# 準備用來存放統計結果的字典結構與計數器
summary = {}          # 格式：{年度: {'total': 總人數, 'by_dept': 各系所人數, 'by_entry': 各入學方式人數}}
all_depts = Counter() # 計算所有年度累計的各系所總人數

# 呼叫上面的生成器，逐年處理 CSV 資料
for year, header, rows in iter_year_csv(ZIP_PATH):
    # 動態找出「系所名稱」與「入學方式」在 CSV 標題列中的索引位置 (欄位順序)
    dept_idx  = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    # 使用 Counter 快速統計，並加上防呆機制 (len(r) > idx) 避免因資料缺漏造成 IndexError
    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    # 將今年的統計結果存入 summary 字典
    summary[year] = {
        "total":    len(rows), # 該年度總人數
        "by_dept":  by_dept,   # 該年度各系所人數
        "by_entry": by_entry,  # 該年度各入學管道人數
    }
    # 將今年的系所人數加總到跨屆累計計數器中
    all_depts.update(by_dept)

# ── 終端輸出：總覽 ─────────────────────────────────────
print("\n=== 6 屆新生人數 ===")
# sorted(summary) 會自動將年份由小到大排序 (109, 110, ...)
for year in sorted(summary):
    # :>4 代表靠右對齊並佔 4 個字元寬度
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")

print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")
# most_common(5) 會回傳數量最多的前 5 名
for dept, n in all_depts.most_common(5):
    print(f"  {n:>4} 人  {dept}")

print("\n=== 114 學年入學方式分布 ===")
# most_common() 不帶參數會依數量多寡列出所有項目
for kind, n in summary["114"]["by_entry"].most_common():
    print(f"  {n:>4} 人  {kind}")


# ── 5.19 + 5.5 + 5.2 沙箱產生報告、5.21 存快照 ─────────
# 使用 TemporaryDirectory 建立一個暫存資料夾，離開 with 區塊後會自動刪除，不會弄髒專案目錄
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    # 5.21 pickle 保存整個 summary，日後可直接 load
    # 日後只需 pickle.load() 就能讀回完整的 dict，不用重新算一次
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f: # 注意：pickle 必須用 'wb' (寫入位元組) 模式
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 5.5 'x' 模式 (Exclusive Creation) 確保檔案不存在時才建立，若已存在則拋出例外防覆寫
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:      
        # 5.2 利用 print(..., file=f) 將輸出重新導向到檔案中，代替 f.write()
        print("# 6 屆新生概況報告\n", file=f)           
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        # 逐年產生 Markdown 表格的資料列
        for year in sorted(summary):
            # 取出該年度人數最多的第 1 個系所與人數
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # 把剛剛寫入的 Markdown 報告檔讀出來並印在終端機上（5.1 文字讀檔）
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 驗證 pickle 是否能成功讀回（型別、內容與原本一致）
    with open(snap, "rb") as f: # 必須用 'rb' (讀取位元組) 模式
        loaded = pickle.load(f)
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 with 區塊後，tmp 目錄及裡面的 report.md, summary.pkl 都已被系統自動刪除
print("\n(沙箱已自動清理)")


# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把報告改寫到 HERE / 'report.md'（改用 'w' 模式會覆蓋，'x' 會報錯）。
# 2) 加一欄「女性比例」：找出性別欄位後用 Counter 統計。
# 3) 把 summary 壓縮存成 summary.pkl.gz（gzip.open('wb') + pickle.dump）。
# 4) 跨屆找出「人數逐年下降最明顯」的系所（需要把 by_dept 按年排成折線）。
