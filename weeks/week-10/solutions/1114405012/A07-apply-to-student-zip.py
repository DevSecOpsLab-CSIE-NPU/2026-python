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

# ── 先定位資料來源，並確認壓縮檔真的存在 ─────────────────────────────
# 這個練習的核心是「直接從壓縮檔讀資料」，所以第一步先找出 zip 檔位置。
# HERE 代表目前這支程式所在的資料夾，接著一路往專案根目錄與 assets 找檔案。
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
# 如果資料檔不存在，就在一開始直接失敗，避免後面才出現難以理解的錯誤。
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
# 印出檔名，方便執行時快速確認目前讀到的是哪個資料來源。
print("資料來源:", ZIP_PATH.name)


# ── 從 zip 內逐一讀出每份 CSV，不需要先解壓縮到磁碟 ──────────────
def iter_year_csv(zip_path: Path):
    """逐年 yield (年度, header, rows)。

    這個 generator 的設計重點是把「檔案枚舉」、「bytes 轉文字」、
    「CSV 解析」三件事集中在一起，讓後面的統計邏輯只需要處理資料表內容。
    """
    # zipfile.ZipFile 可以直接讀壓縮檔內容，不必先手動解壓。
    with zipfile.ZipFile(zip_path) as z:
        # infolist() 會列出壓縮檔中的每個項目，包含檔名、大小、時間等資訊。
        for info in z.infolist():
            # 這裡只處理 CSV 檔，其他可能的雜項檔案一律略過。
            name = info.filename
            if not name.endswith(".csv"):
                continue
            # 檔名開頭是學年度，例如 109.csv、110.csv，用前 3 個字元就能取出年度。
            year = name[:3]  # '109'~'114'

            # z.read() 讀到的是位元組資料，先轉成文字再交給 csv.reader。
            raw = z.read(info)                       # bytes
            # utf-8-sig 會自動把 Excel 常見的 BOM 去掉，避免第一欄標題出問題。
            text = raw.decode("utf-8-sig")           # 5.1 去 BOM
            # StringIO 讓字串看起來像一個檔案物件，csv.reader 才能直接逐列讀取。
            reader = csv.reader(io.StringIO(text))   # 5.6 StringIO 當檔
            # 先把整份 CSV 讀進記憶體，方便後面分出表頭與資料列。
            rows = list(reader)
            # rows[0] 是欄位名稱，rows[1:] 才是學生資料。
            yield year, rows[0], rows[1:]


# ── 跨屆統計：把每個年度的總人數、系所分布、入學方式分布整理起來 ───────────────────────────────────────────
# summary 會保存每一屆的統計結果，all_depts 則用來累積 6 屆合併後的系所總計。
summary = {}        # {年度: {'total': n, 'by_dept': Counter, 'by_entry': Counter}}
all_depts = Counter()

# 逐年讀取 CSV，依欄位名稱找出需要的欄位位置，再做 Counter 統計。
for year, header, rows in iter_year_csv(ZIP_PATH):
    # 透過欄名定位欄位，比直接寫死 index 更穩健；如果欄位順序改變也不怕。
    dept_idx  = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    # 只要該列長度夠長，就把對應欄位拿出來累加次數。
    # Counter 很適合做這類「分類統計」，可以自動累計每個值出現幾次。
    by_dept  = Counter(r[dept_idx]  for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    # 每一屆的統計結果都放進 summary，後面輸出報表會直接讀這個結構。
    summary[year] = {
        "total":    len(rows),
        "by_dept":  by_dept,
        "by_entry": by_entry,
    }
    # 另外把系所總數累積起來，方便找出跨 6 屆最熱門的系所。
    all_depts.update(by_dept)

# ── 終端輸出：先印出最重要的總覽資訊 ─────────────────────────────────────
# 這一段是讓使用者不用打開報表，就能先在終端機快速看見摘要。
print("\n=== 6 屆新生人數 ===")
# sorted(summary) 會依年度字串由小到大排序，也就是 109 → 114。
for year in sorted(summary):
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")

print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")
# most_common(5) 直接取出出現次數最高的前 5 名。
for dept, n in all_depts.most_common(5):
    print(f"  {n:>4} 人  {dept}")

print("\n=== 114 學年入學方式分布 ===")
# 這裡專門看最新一屆，方便觀察當年度入學來源的組成。
for kind, n in summary["114"]["by_entry"].most_common():
    print(f"  {n:>4} 人  {kind}")


# ── 在暫存沙箱中產生報告與快照，避免污染專案目錄 ─────────
# TemporaryDirectory 會在區塊結束時自動清掉，適合做練習或中間產物。
with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    # 把整個 summary 序列化成 pickle，之後可以直接 load 回來做後續分析。
    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    # stat().st_size 可確認檔案真的有寫入，而且大小合理。
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    # 用 'x' 開啟檔案，代表「只在檔案不存在時建立」，可避免誤覆蓋既有報告。
    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:      # 5.5
        # print(..., file=f) 可以直接把格式化後的文字輸出到檔案。
        print("# 6 屆新生概況報告\n", file=f)           # 5.2
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        # 把每一屆的總人數與第一大系所整理成 Markdown 表格。
        for year in sorted(summary):
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(f"| {year} | {summary[year]['total']} | "
                  f"{top_dept} ({top_n}) |", file=f)

    # 直接把 Markdown 內容讀回並印到終端，方便快速預覽成果。
    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    # 再把 pickle 讀回來，驗證序列化與反序列化都正常。
    with open(snap, "rb") as f:
        loaded = pickle.load(f)
    # 這裡只檢查 key，確認每一屆的統計資料都有完整保存。
    print("pickle 讀回 key:", sorted(loaded.keys()))

# 離開 with 之後，TemporaryDirectory 會自動刪除暫存資料夾，不會在專案中留下檔案。
print("\n(沙箱已自動清理)")


# ── 課堂延伸挑戰：可以試著再往下練習的方向 ───────────────────────────────────────
# 這些題目不是主流程的一部分，而是提供你練習延伸分析的方向。
# 1) 把報告改寫到 HERE / 'report.md'（改用 'w' 模式會覆蓋，'x' 會報錯）。
# 2) 加一欄「女性比例」：找出性別欄位後用 Counter 統計。
# 3) 把 summary 壓縮存成 summary.pkl.gz（gzip.open('wb') + pickle.dump）。
# 4) 跨屆找出「人數逐年下降最明顯」的系所（需要把 by_dept 按年排成折線）。
