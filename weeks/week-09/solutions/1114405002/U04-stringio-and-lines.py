# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# ============================================================================
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用
# 重要概念：
#   - 鴨子型別：只要有 read/write/seek 方法就算「像檔案」，可互換
#   - StringIO：記憶體中的虛擬檔案，用法和真檔一樣
#   - 大檔逐行讀：節省記憶體的必備技能
# ============================================================================

import io
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# StringIO 用途：
#   1. 單元測試：不用真的寫到硬碟，但效果一樣
#   2. 暫存：處理資料流時當作緩衝區
#   3. 協議轉換：某些 API（csv/json/logging）要求 file-like 物件
# 好處：既快又不佔硬碟，測試友善

buf = io.StringIO()  # 建立記憶體中的虛擬檔案（文字模式）

# 當檔案寫入：用 print(..., file=buf)
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# 取出整段字串
text = buf.getvalue()  # getvalue() = 提取虛擬檔案的全部內容
print("---StringIO 內容---")
print(text)  # 全部內容一次性取出

# 也能當讀檔用：seek 回開頭再逐行讀
buf.seek(0)  # seek(0) = 檔案指針回到開頭
for i, line in enumerate(buf, 1):  # enumerate 加上行號（從 1 開始）
    print(i, line.rstrip())  # 逐行迭代

# StringIO 應用：任何收 file-like 的 API 都能無縫使用
# 例如 csv 模組、json 模組、logging - 全都支援 StringIO
# 好處：測試時不用真的寫檔，加快速度

import csv

mem = io.StringIO()  # 虛擬檔案當 CSV 的輸出目標
writer = csv.writer(mem)  # CSV writer 把資料寫到記憶體
writer.writerow(["name", "score"])  # 寫標頭
writer.writerow(["alice", 90])       # 寫資料列

print("---CSV in memory---")
print(mem.getvalue())  # 取出 CSV 內容（純文字，不是真檔案）
# 輸出：
# name,score
# alice,90

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 逐行讀檔的優點：
#   - 記憶體節省：一次只讀一行，不管檔多大
#   - 適合流處理：邊讀邊處理（如日誌分析）
# 應用場景：處理 GB 級大檔、即時日誌監控

# 先造一個多行示範檔
src = Path("poem.txt")
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：
#   1. 過濾空行（skip 空白行）
#   2. 加上行號
#   3. 寫到新檔
# 此流程適合大檔處理，一次性讀全檔會爆記憶體

dst = Path("poem_numbered.txt")
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    """
    同時開啟兩個檔：
    - fin：原始檔（讀）
    - fout：目標檔（寫）
    """
    n = 0  # 非空行計數器
    for line in fin:               # for 迴圈逐行迭代（一次只讀一行）
        line = line.rstrip()       # 移除行尾空白（包括 \n）
        if not line:
            continue               # 跳過空行（不寫、不計數）
        n += 1
        print(f"{n:02d}. {line}", file=fout)  # 寫到輸出檔

print("---加行號後---")
print(dst.read_text(encoding="utf-8"))
# 輸出：
# 01. 床前明月光
# 02. 疑是地上霜
# 03. 舉頭望明月
# 04. 低頭思故鄉
