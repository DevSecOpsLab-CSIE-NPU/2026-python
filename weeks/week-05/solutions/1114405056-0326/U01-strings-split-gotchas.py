import re

# ── 用 re.split 保留分隔符號 ─────────────────────────────
# 當 pattern 含有捕捉群組 (capturing group) 時，
# re.split 會把分隔符號本身也放進回傳列表
line = "asdf fjdk; afed, fjek,asdf, foo"
# fields 的奇偶索引：偶數=值、奇數=分隔符號
fields = re.split(r"(;|,|\s)\s*", line)
values = fields[::2]            # 取出所有「值」
delimiters = fields[1::2] + [""]  # 取出所有「分隔符號」，尾端補空字串
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 還原原始字串（大致相同）

# ── startswith / endswith 的常見陷阱 ─────────────────────
# startswith 的第一個參數必須是 str 或 tuple[str]，不能直接傳 list
url = "http://www.python.org"
choices = ["http:", "ftp:"]
try:
    url.startswith(choices)  # type: ignore[arg-type]  → 會拋 TypeError
except TypeError as e:
    print(f"TypeError: {e}")
# 正確做法：先用 tuple() 轉換
print(url.startswith(tuple(choices)))  # True

# ── 空白字元處理三種方式 ──────────────────────────────────
s = " hello world "
print(repr(s.strip()))               # 去除首尾空白
print(repr(s.replace(" ", "")))      # 移除所有空格（包含中間）
print(repr(re.sub(r"\s+", " ", s.strip())))  # 將連續空白壓縮成單一空格

# ── 批次去除每行的前後空白 ───────────────────────────────
lines = [" apple \n", " banana \n"]
# 使用生成器運算式惰性處理，不建立中間列表
for line in (l.strip() for l in lines):
    print(line)
