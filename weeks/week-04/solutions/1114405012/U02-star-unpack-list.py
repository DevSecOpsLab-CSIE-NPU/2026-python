# U02. 星號解包的特性：可接不定長，且結果型別固定為 list（1.2）
# 觀念：*變數 會把「剩下全部元素」收進 list，不論來源是 tuple 或 list。


def section(title: str) -> None:
    print(f"\n=== {title} ===")


section("來源為 tuple")
record = ("Dave", "dave@example.com")
name, email, *phones = record
print("name:", name)
print("email:", email)
print("phones:", phones, "type:", type(phones).__name__)

section("有多個剩餘元素")
record2 = ("Tom", "tom@example.com", "0912-000-111", "02-1234-5678")
name2, email2, *phones2 = record2
print("name2:", name2)
print("email2:", email2)
print("phones2:", phones2, "type:", type(phones2).__name__)

section("星號可放中間")
first, *middle, last = [1, 2, 3, 4, 5]
print("first:", first)
print("middle:", middle)
print("last:", last)
