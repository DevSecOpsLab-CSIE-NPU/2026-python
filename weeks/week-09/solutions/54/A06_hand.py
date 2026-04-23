import gzip
import pickle
import tempfile
from pathlib import Path

with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        print("gz:", line.rstrip())

with gzip.open("blob.bin.gz", "wb") as f:
    f.write(b"\x00\x01\x02\x03")

print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

print("離開後還存在嗎？", tmp.exists())

with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                             encoding="utf-8") as f:
    f.write("暫存 log\n")
    log_path = f.name
print("暫存檔位置:", log_path)
Path(log_path).unlink()

scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

with open("scores.pkl", "wb") as f:
    pickle.dump(scores, f)

with open("scores.pkl", "rb") as f:
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)
print("內容相等?", loaded == scores)
print("alice 平均:", sum(loaded["alice"]) / 3)