from pathlib import Path

magic = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])
Path("fake.png").write_bytes(magic)

with open("fake.png", "rb") as f:
    head = f.read(8)
print(head)
print(head == magic)

for b in head[:4]:
    print(b, hex(b))

s = "你好"
b = s.encode("utf-8")
print(s, type(s))
print(b, type(b))
print(b.decode("utf-8"))

Path("zh.txt").write_text("中文測試\n", encoding="utf-8")

print(Path("zh.txt").read_text(encoding="utf-8"))

try:
    print(Path("zh.txt").read_text(encoding="big5"))
except UnicodeDecodeError as e:
    print("解碼錯誤:", e)