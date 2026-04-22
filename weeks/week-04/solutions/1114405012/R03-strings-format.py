# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# strip / ljust / join / format / format_map / textwrap

import textwrap


def section(title: str) -> None:
    print(f"\n=== {title} ===")

# ── 2.11 清理字元 ─────────────────────────────────────
s = "  hello world \n"
section("2.11 清理字元")
print("原始字串 repr:", repr(s))
print("strip 後:", repr(s.strip()))
print("lstrip 後:", repr(s.lstrip()))
print("自訂移除字元 strip('-='):", "-----hello=====".strip("-="))

# ── 2.13 字串對齊 ─────────────────────────────────────
text = "Hello World"
section("2.13 字串對齊")
print("ljust(20):", repr(text.ljust(20)))
print("rjust(20):", repr(text.rjust(20)))
print("center(20, '*'):", repr(text.center(20, "*")))
print("format ^20:", repr(format(text, "^20")))
print("數字對齊 + 小數位:", repr(format(1.2345, ">10.2f")))

# ── 2.14 合併拼接 ─────────────────────────────────────
parts = ["Is", "Chicago", "Not", "Chicago?"]
section("2.14 合併拼接")
print("空白 join:", " ".join(parts))
print("逗號 join:", ",".join(parts))

data = ["ACME", 50, 91.1]
print("混合型別 join:", ",".join(str(d) for d in data))

# ── 2.15 插入變量 ─────────────────────────────────────
name, n = "Guido", 37
s = "{name} has {n} messages."
section("2.15 插入變量")
print("format:", s.format(name=name, n=n))
print("format_map(vars()):", s.format_map(vars()))
print("f-string:", f"{name} has {n} messages.")

# ── 2.16 指定列寬 ─────────────────────────────────────
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
section("2.16 指定列寬")
print(textwrap.fill(long_s, 40))
print(textwrap.fill(long_s, 40, initial_indent="    "))
