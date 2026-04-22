# U01. 解包失敗的原因：變數數量必須和元素數量一致（1.1）
# 觀念：序列解包時，左邊要接收的變數個數，通常要和右邊元素個數一致。
# 例外：有使用星號變數（*rest）時，才可吸收多餘元素。


def section(title: str) -> None:
    print(f"\n=== {title} ===")


section("一般解包成功")
p = (4, 5)
x, y = p
print("p:", p)
print("x, y:", x, y)

section("變數太多會失敗")
try:
    x, y, z = p
except ValueError as e:
    print("ValueError:", e)

section("用星號解包處理不定長")
a, *rest = [10, 20, 30, 40]
print("a:", a)
print("rest:", rest)
