# Week 04 課堂範例：字串、數字與日期時間

本目錄涵蓋：
- [Python3 Cookbook 第二章：字符串和文本](https://python3-cookbook.readthedocs.io/zh-cn/latest/chapters/p02_strings_and_text.html)
- [Python3 Cookbook 第三章：数字日期和时间](https://python3-cookbook.readthedocs.io/zh-cn/latest/chapters/p03_numbers_dates_times.html)

---

## 章節對照表

### 第二章：字串與文字處理

| 節次 | 主題 | 核心技術 | 範例 |
|------|------|----------|------|
| 2.1–2.3 | 分割、前後綴匹配、通配符 | `re.split` / `startswith` / `fnmatch` | [R01](./R01-strings-split-match.py) |
| 2.4–2.8 | 正則搜尋、替換、旗標 | `re.compile` / `sub` / `IGNORECASE` / `DOTALL` | [R02](./R02-strings-regex.py) |
| 2.11–2.16 | 清理、對齊、拼接、格式化 | `strip` / `format` / `join` / `textwrap` | [R03](./R03-strings-format.py) |
| 2.20 | 位元組字串操作 | `bytes` / `bytearray` | [R04](./R04-strings-bytes.py) |

### 第三章：數字與日期時間

| 節次 | 主題 | 核心技術 | 範例 |
|------|------|----------|------|
| 3.1–3.4 | 四捨五入、精確計算、格式化、進制 | `round` / `Decimal` / `format` / `bin` | [R05](./R05-numbers-basic.py) |
| 3.7–3.11 | 無窮大、NaN、分數、隨機 | `float('inf')` / `Fraction` / `random` | [R06](./R06-numbers-special.py) |
| 3.12–3.13 | 日期加減、指定星期計算 | `timedelta` / `weekday()` | [R07](./R07-datetime-basics.py) |
| 3.14–3.15 | 月份範圍、字串轉日期 | `calendar.monthrange` / `strptime` | [R08](./R08-datetime-calendar.py) |
| 3.16 | 時區操作 | `zoneinfo` | [R09](./R09-datetime-timezone.py) |

---

## 範例清單

### 記憶層（R — Remember）：直接複製可執行的基礎用法

| 檔案 | 涵蓋節次 | 主題 |
|------|----------|------|
| [R01-strings-split-match.py](./R01-strings-split-match.py) | 2.1–2.3 | re.split / startswith / fnmatch |
| [R02-strings-regex.py](./R02-strings-regex.py) | 2.4–2.8 | 正則搜尋、替換、非貪婪、多行 |
| [R03-strings-format.py](./R03-strings-format.py) | 2.11–2.16 | 清理、對齊、join、format、textwrap |
| [R04-strings-bytes.py](./R04-strings-bytes.py) | 2.20 | bytes / bytearray 操作 |
| [R05-numbers-basic.py](./R05-numbers-basic.py) | 3.1–3.4 | round / Decimal / format / 進制轉換 |
| [R06-numbers-special.py](./R06-numbers-special.py) | 3.7–3.11 | inf / NaN / Fraction / random |
| [R07-datetime-basics.py](./R07-datetime-basics.py) | 3.12–3.13 | timedelta 加減 / 指定星期日期 |
| [R08-datetime-calendar.py](./R08-datetime-calendar.py) | 3.14–3.15 | 月份範圍 / strptime / strftime |
| [R09-datetime-timezone.py](./R09-datetime-timezone.py) | 3.16 | zoneinfo 時區轉換 |

### 理解層（U — Understand）：為什麼這樣做？陷阱與進階技巧

| 檔案 | 主題 | 關鍵概念 |
|------|------|----------|
| [U01-strings-split-gotchas.py](./U01-strings-split-gotchas.py) | 分割與匹配的陷阱 | 捕獲分組保留分隔符 / startswith 只接受 tuple / strip 不處理中間空白 |
| [U02-regex-advanced.py](./U02-regex-advanced.py) | 正則進階技巧 | 預編譯效能比較 / sub 回呼函數 / 大小寫一致替換 |
| [U03-strings-format-perf.py](./U03-strings-format-perf.py) | 格式化效能與陷阱 | join vs + 效能 / format_map 缺失鍵 / bytes 索引回傳整數 |
| [U04-numbers-precision.py](./U04-numbers-precision.py) | 數字精度陷阱 | 銀行家捨入 / NaN 無法用 == / float vs Decimal 選擇 |
| [U05-datetime-gotchas.py](./U05-datetime-gotchas.py) | 日期時間陷阱 | timedelta 不支援月份 / strptime 效能問題 |
| [U06-datetime-timezone.py](./U06-datetime-timezone.py) | 時區最佳實踐 | UTC 優先 / 夏令時邊界處理 |
| [U07-random-advanced.py](./U07-random-advanced.py) | 隨機進階 | 種子可重現性 / secrets 密碼學安全亂數 |
