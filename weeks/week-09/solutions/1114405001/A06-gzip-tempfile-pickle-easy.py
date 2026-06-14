# A06-easy. 壓縮檔、臨時資料夾、物件序列化 - 簡化版
# 三個進階檔案操作技巧

import gzip
import pickle
import tempfile
from pathlib import Path

print("=== 1. gzip：壓縮檔案（API 和 open() 一樣） ===")
# 寫入壓縮檔
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")
print("✅ 寫入 notes.txt.gz")

# 讀回壓縮檔（用法一樣！）
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print(f"  讀到：{line.rstrip()}")

# 檔案大小
size = Path("notes.txt.gz").stat().st_size
print(f"壓縮檔大小：{size} bytes")

print("\n=== 2. tempfile：臨時資料夾（自動清理） ===")
# with 結束時自動刪除，不留垃圾
with tempfile.TemporaryDirectory() as tmp_dir:
    tmp = Path(tmp_dir)
    print(f"暫存資料夾：{tmp}")
    print(f"存在？{tmp.exists()}")
    
    # 在裡面建立檔案
    (tmp / "a.txt").write_text("文件A\n", encoding="utf-8")
    (tmp / "b.txt").write_text("文件B\n", encoding="utf-8")
    
    # 列出內容
    for file in tmp.iterdir():
        print(f"  {file.name}：{file.read_text(encoding='utf-8').strip()}")

# 離開 with 後自動刪除
print(f"離開後存在？{tmp.exists()}")

print("\n=== 3. tempfile：臨時檔案 ===")
# 建立臨時檔（可以指定副檔名）
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log", encoding="utf-8") as f:
    f.write("暫存 log 內容\n")
    log_path = f.name
    print(f"暫存檔：{log_path}")

# 用完後手動刪除
Path(log_path).unlink()
print(f"刪除後存在？{Path(log_path).exists()}")

print("\n=== 4. pickle：物件序列化（存 Python 物件） ===")
# 想存複雜物件？不用轉 JSON，直接 pickle
data = {
    "名字": "alice",
    "成績": [90, 85, 88],
    "標籤": ["優秀", "認真"]
}

# 序列化：物件 → 位元組
pickle_file = Path("data.pkl")
with open(pickle_file, "wb") as f:
    pickle.dump(data, f)
print(f"✅ 存入 {pickle_file}")

# 反序列化：位元組 → 物件
with open(pickle_file, "rb") as f:
    loaded = pickle.load(f)
print(f"讀回：{loaded}")

print("\n=== 記憶重點 ===")
print("""
三個技巧：
1. gzip.open() → API 和 open() 完全一樣
2. tempfile.TemporaryDirectory() → 自動清理，實驗用
3. pickle.dump/load() → 存複雜 Python 物件

何時用：
- gzip：需要壓縮空間時
- tempfile：測試、實驗、不留垃圾
- pickle：存 Python dict/list/object
""")