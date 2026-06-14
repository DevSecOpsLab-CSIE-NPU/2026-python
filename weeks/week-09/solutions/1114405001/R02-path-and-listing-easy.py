# R02-easy. 路徑操作與目錄列舉 - 簡化版
# 最常用的路徑操作和檔案搜尋

from pathlib import Path

print("=== 1. 路徑組合最簡單 ===")
# 用 / 直接組合路徑
base = Path("weeks") / "week-09" / "solutions"
print(f"完整路徑：{base}")
print(f"最後的名字：{base.name}")          # week-09
print(f"上一層：{base.parent}")             # weeks/week-09

print("\n=== 2. 檔案名稱拆解 ===")
file = Path("hello.txt")
print(f"檔名：{file.stem}")                # hello
print(f"副檔名：{file.suffix}")            # .txt
print(f"完整名稱：{file.name}")            # hello.txt

print("\n=== 3. 檔案存在判定（最常用） ===")
if file.exists():
    print(f"{file} 存在")
else:
    print(f"{file} 不存在")

# 其他判定
print(f"是檔案？ {file.is_file()}")
print(f"是資料夾？ {file.is_dir()}")

print("\n=== 4. 搜尋檔案（當層） ===")
# 搜尋當層所有 .py 檔
here = Path(".")
py_files = list(here.glob("*.py"))
print(f"當層 .py 檔：{len(py_files)} 個")
for p in py_files[:3]:
    print(f"  - {p.name}")

print("\n=== 5. 搜尋所有子資料夾的檔案（遞迴） ===")
# 搜尋所有 .txt 檔，包含子資料夾
# txt_files = list(Path(".").rglob("*.txt"))
# print(f"所有 .txt：{len(txt_files)} 個")

print("\n=== 記憶重點 ===")
print("""
3個最常用操作：
1. Path(a) / b / c  → 組合路徑
2. path.exists()    → 檢查存在
3. path.glob("*.py") → 搜尋檔案

小技巧：
- .stem 取名字（不含副檔名）
- .suffix 取副檔名
- .parent 取上一層
- rglob("*.txt") 包含子資料夾搜尋
""")