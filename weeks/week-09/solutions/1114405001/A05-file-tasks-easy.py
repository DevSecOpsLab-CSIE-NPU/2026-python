# A05-easy. 綜合應用：檔案操作 - 簡化版
# 實戰例子：日記工具、代碼統計

from pathlib import Path
from datetime import date

print("=== 1. 日記工具：檔案不存在才建立 ===")
# 'x' 模式 = exclusive create（檔案存在就會錯誤）
today = date.today().isoformat()
diary = Path(f"diary-{today}.txt")

try:
    with open(diary, "x", encoding="utf-8") as f:
        f.write(f"# {today} 的日記\n")
        f.write("今天學了什麼？\n")
    print(f"✅ 建立新日記：{diary}")
except FileExistsError:
    print(f"⚠️ {diary} 已存在，不覆蓋")

print("\n=== 2. 統計資料夾中的 .py 檔 ===")
def count_py_files(folder: Path):
    """計算資料夾中所有 .py 檔的統計"""
    total = 0          # 總行數
    nonblank = 0       # 非空白行
    with_def = 0       # 有 def 的行

    # 走訪資料夾中所有 .py 檔
    for py_file in folder.glob("*.py"):
        with open(py_file, "rt", encoding="utf-8") as f:
            for line in f:
                total += 1
                stripped = line.strip()
                
                if stripped:  # 不是空行
                    nonblank += 1
                
                if stripped.startswith("def "):  # 是函數定義
                    with_def += 1
    
    return total, nonblank, with_def

# 測試
folder = Path(".")
total, nonblank, defs = count_py_files(folder)
print(f"\n{folder} 統計結果：")
print(f"  總行數：{total}")
print(f"  非空白行：{nonblank}")
print(f"  def 定義行：{defs}")

print("\n=== 3. 課堂延伸挑戰 ===")
print("""
✏️ 試著做做看：
1. 把日記改成 'a' 模式（附加），同一天可以多次追寫
2. count_py_files 再加一個統計：註解行（以 # 開頭）
3. 把統計結果寫到 stats.tsv（tab 分隔）

小提示：
- 'x' 模式只能用一次（之後會 FileExistsError）
- 'a' 模式可以多次附加
- 'w' 模式會覆蓋（危險！）
""")