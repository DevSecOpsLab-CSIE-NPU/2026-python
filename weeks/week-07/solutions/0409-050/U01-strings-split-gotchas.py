# U01. 字串分割與匹配的陷阱（2.1–2.11）
# 捕獲分組保留分隔符 / startswith 必須傳 tuple / strip 只處理頭尾

# 導入正則表達式模組，用於更複雜的字串匹配和分割操作。
import re

# ── 捕獲分組保留分隔符（2.1）─────────────────────────
# 說明：當使用 re.split() 且正則表達式中包含捕獲分組 (即括號 `()`) 時，
# 分隔符本身也會被包含在結果列表中。這與簡單的字串 split() 方法不同。
line = "asdf fjdk; afed, fjek,asdf, foo"
# 使用正則表達式分割字串。
# r"(;|,|\s)\s*"：
#   - (;|,|\s)：這是一個捕獲分組，匹配分號、逗號或任何空白字元。因為是捕獲分組，這些分隔符會被保留在結果中。
#   - \s*：匹配零個或多個空白字元。這會消耗掉分隔符後面的任何空白，確保分割結果更乾淨。
fields = re.split(r"(;|,|\s)\s*", line)
# 輸出 fields 的內容，可以看到原始值和分隔符交錯出現。
# 例如：['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

# 從 fields 列表中提取實際的數值部分。
# fields[::2] 表示從索引 0 開始，每隔一個元素取一個，即取得所有偶數索引的元素。
values = fields[::2]  # 偶數索引 = 實際值
# 輸出 values 的內容，例如：['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 從 fields 列表中提取分隔符部分。
# fields[1::2] 表示從索引 1 開始，每隔一個元素取一個，即取得所有奇數索引的元素。
# + [""] 是為了確保 delimiters 列表的長度與 values 列表匹配，因為最後一個值後面沒有分隔符。
delimiters = fields[1::2] + [""]
# 輸出 delimiters 的內容，例如：[' ', ';', ',', ',', ',', '']

# 將提取出的值和分隔符重新組合，以驗證分割和提取的正確性。
# zip(values, delimiters) 將兩個列表的對應元素配對。
# (v + d for v, d in zip(values, delimiters)) 是一個生成器表達式，用於將每個值和其後的分隔符拼接起來。
# "".join(...) 將所有拼接後的字串連接成一個單一字串。
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
# 輸出重建後的字串，例如：'asdf fjdk;afed,fjek,asdf,foo'
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'

# ── startswith 必須傳 tuple（2.2）────────────────────
# 說明：字串的 startswith() 和 endswith() 方法在檢查多個前綴或後綴時，
# 必須傳入一個元組 (tuple) 作為參數，而不是列表 (list)。
url = "http://www.python.org"
# 定義一個包含多個前綴的列表。
choices = ["http:", "ftp:"]
try:
    # 嘗試將列表直接傳給 startswith()，這會導致 TypeError。
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    # 捕獲並列印 TypeError 錯誤訊息。
    print(f"TypeError: {e}")  # 不能傳 list！
# 正確的做法是將列表轉換為元組後再傳入。
print(url.startswith(tuple(choices)))  # True（轉成 tuple 才行）

# ── strip 只處理頭尾，不處理中間（2.11）──────────────
# 說明：字串的 strip()、lstrip() 和 rstrip() 方法只會移除字串「開頭」和「結尾」的指定字元（預設為空白字元），
# 它們不會處理字串「中間」的空白或其他字元。
s = "  hello     world  "
# strip() 移除了字串兩端的空白，但中間的多餘空白仍然保留。
print(repr(s.strip()))  # 'hello     world'（中間多餘空白還在）
# replace(" ", "") 會移除字串中所有的空白，包括單詞之間必要的空白，這通常不是期望的結果。
print(repr(s.replace(" ", "")))  # 'helloworld'（過頭，連詞間空白也消）
# 正確且常見的做法是先用 strip() 移除兩端空白，然後再用正則表達式 re.sub() 將中間連續的多個空白替換為單一空白。
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'（正確）

# 生成器逐行清理（高效，不預載入記憶體）
# 說明：當處理大型檔案或多行輸入時，使用生成器表達式 (generator expression) 可以避免一次性將所有處理後的行載入記憶體，
# 這樣更高效且節省記憶體。
lines = ["  apple  \n", "  banana  \n"]
# (l.strip() for l in lines) 是一個生成器表達式，它會逐行處理並移除每行兩端的空白，
# 但並不會立即創建一個新的列表，而是在迭代時按需生成。
for line in (l.strip() for l in lines):
    print(line)
