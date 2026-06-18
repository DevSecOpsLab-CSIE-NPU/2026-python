# A07. 把 I/O 技巧套到真實學生資料
# 這個版本將 Week 09 的 A07 範例搬到 week-10 的解題資料夾，並補上詳細繁體中文註解。

import csv
import io
import pickle
import tempfile
import zipfile
from collections import Counter
from pathlib import Path

# 先定位本檔案所在目錄，並組出 assets 資料檔的路徑
HERE = Path(__file__).resolve().parent
ZIP_PATH = HERE.parent.parent.parent / "assets" / "npu-stu-109-114-anon.zip"
assert ZIP_PATH.exists(), f"找不到資料：{ZIP_PATH}"
print("資料來源:", ZIP_PATH.name)


def iter_year_csv(zip_path: Path):
    """逐年從 zip 檔讀出 CSV 內容，回傳 (年度, header, rows)。"""
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            name = info.filename
            if not name.endswith(".csv"):
                continue
            year = name[:3]  # 例如 '109'
            raw = z.read(info)
            text = raw.decode("utf-8-sig")  # 處理 CSV 前的 BOM
            reader = csv.reader(io.StringIO(text))
            rows = list(reader)
            yield year, rows[0], rows[1:]


summary = {}       # {年度: 整年度統計資料}
all_depts = Counter()

for year, header, rows in iter_year_csv(ZIP_PATH):
    dept_idx = header.index("系所名稱")
    entry_idx = header.index("入學方式")

    by_dept = Counter(r[dept_idx] for r in rows if len(r) > dept_idx)
    by_entry = Counter(r[entry_idx] for r in rows if len(r) > entry_idx)

    summary[year] = {
        "total": len(rows),
        "by_dept": by_dept,
        "by_entry": by_entry,
    }
    all_depts.update(by_dept)

print("\n=== 6 屆新生人數 ===")
for year in sorted(summary):
    print(f"  {year} 學年：{summary[year]['total']:>4} 人")

print("\n=== 全體最熱門 5 個系所（累計 6 屆） ===")
for dept, n in all_depts.most_common(5):
    print(f"  {n:>4} 人  {dept}")

print("\n=== 114 學年入學方式分布 ===")
for kind, n in summary["114"]["by_entry"].most_common():
    print(f"  {n:>4} 人  {kind}")

with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)

    snap = tmp / "summary.pkl"
    with open(snap, "wb") as f:
        pickle.dump(summary, f)
    print(f"\n快照寫入 {snap.name}：{snap.stat().st_size} bytes")

    report = tmp / "report.md"
    with open(report, "x", encoding="utf-8") as f:
        print("# 6 屆新生概況報告\n", file=f)
        print("| 學年 | 人數 | 第一大系所 |", file=f)
        print("|------|------|------------|", file=f)
        for year in sorted(summary):
            top_dept, top_n = summary[year]["by_dept"].most_common(1)[0]
            print(
                f"| {year} | {summary[year]['total']} | {top_dept} ({top_n}) |",
                file=f,
            )

    print("\n=== Markdown 報告預覽 ===")
    print(report.read_text(encoding="utf-8"))

    with open(snap, "rb") as f:
        loaded = pickle.load(f)
    print("pickle 讀回 key:", sorted(loaded.keys()))

print("\n(沙箱已自動清理)")
