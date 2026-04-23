# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# ============================================================================
# Bloom: Apply — 把前面學到的 API 組起來解小任務
# 本檔展示實務中常見的兩個應用：
# 1. 使用 'x' 模式寫檔（排除重複覆蓋的風險）
# 2. 遞迴統計提錄內所有 .py 檔案的各種指標
# ============================================================================

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 規則：每天只能建一次；同一天重複執行要提示「已存在」。
# 'x' 模式（exclusive create）相比 'w' 模式的優點：
#   - 'w' 會無條件覆蓋已存在的檔案（危險！）
#   - 'x' 若檔案已存在則拋出 FileExistsError（安全防護）
# 應用場景：避免誤覆蓋重要檔案、實現檔案鎖定等

today = date.today().isoformat()          # 取得今天日期，格式：YYYY-MM-DD（如 2026-04-23）
diary = Path(f"diary-{today}.txt")        # 建立路徑物件，檔名包含日期

try:
    with open(diary, "x", encoding="utf-8") as f:   # 'x' = exclusive create（獨佔建立）
        f.write(f"# {today} 日記\n")                 # 寫入日期標題
        f.write("今天學了檔案 I/O。\n")               # 寫入日記內容
    print(f"已建立 {diary}")                         # 成功訊息
except FileExistsError:
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")  # 若檔案已存在，提示不覆蓋

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 需求：
#   - 遞迴走訪目錄（包含子資料夾）
#   - 逐檔逐行讀取所有 .py 檔
#   - 統計共 3 個數字：總行數、非空白行數、def 起頭行數
# 日常應用：程式碼複雜度分析、程式碼量統計、檢查程式碼品質

def count_py(folder: Path):
    """
    統計資料夾內所有 Python 檔案的各項指標。
    
    參數:
        folder (Path): 要統計的資料夾路徑
    
    返回:
        tuple: (總行數, 非空白行數, def起頭行數)
    
    邏輯流程：
        1. 遞迴列舉所有 .py 檔案（rglob）
        2. 對每個檔案逐行讀取（file-like iteration）
        3. 累計統計三項計數
    """
    total, nonblank, defs = 0, 0, 0  # 初始化三個計數器
    
    for p in folder.rglob("*.py"):  # rglob = recursive glob，遞迴搜尋所有 .py 檔
        with open(p, "rt", encoding="utf-8", errors="replace") as f:  # 逐檔打開
            for line in f:  # 逐行迭代（大檔友善：一次只讀一行到記憶體）
                total += 1  # 計數：總行數
                s = line.strip()  # 移除行首尾空白
                if s:  # 非空白行
                    nonblank += 1
                if s.startswith("def "):  # 以 "def " 開頭的行（函數定義）
                    defs += 1
    
    return total, nonblank, defs


# 使用範例：統計 week-04/in-class 下的所有 Python 檔案
target = Path("..") / ".." / "week-04" / "in-class"  # 相對路徑組合
if target.exists():
    total, nonblank, defs = count_py(target)  # 呼叫統計函數
    print(f"{target}")
    print(f"  總行數       : {total}")  # 檔案中的所有行（包含空白行）
    print(f"  非空白行     : {nonblank}")  # 去除空白行和註解的實際程式碼行
    print(f"  def 起頭行數 : {defs}")  # 函數定義行數
else:
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 難度遞進的練習題，幫助鞏固檔案 I/O 相關技能：
#
# 1) 把日記工具改成「附加」模式 'a'：
#    - 同一天可多次追寫一行時間戳
#    - 好處：保留每次編輯時間的軌跡
#    - 方法：改用 open(diary, 'a', ...) 替代 'x'
#
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字：
#    - 提示：s.startswith("#")
#    - 可進一步分析程式碼品質（註解比例）
#
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv：
#    - 產生 Tab-Separated Values 格式
#    - 便於 Excel 或其他工具開啟
#    - 方法：新開  Path("stats.tsv") 的檔案，用 print 寫入
