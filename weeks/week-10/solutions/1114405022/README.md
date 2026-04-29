# UVA 10226 - Hardwood Species 完整解決方案

**學號**: 1114405022  
**週次**: Week 10  
**題號**: 10226  
**題名**: Hardwood Species  
**難度**: ⭐ (Easy)  

---

## 📋 題目概述

### 題目敘述
統計森林調查數據中各樹種出現的百分比。輸入為多筆測資，每筆以空行分隔，每行為一個樹種名稱。
要求依字典序輸出每個樹種及其百分比（四位小數）。

### 輸入格式
```
T                    # 測資筆數
<空行>
樹種1
樹種2
...
<空行>
樹種n
...
```

### 輸出格式
```
樹種 百分比
樹種 百分比
...
<空行>  # 測資間空一行
```

---

## 💡 解題思路

### 核心概念
1. **測資分隔**: 以空行(`\n\n`)分隔每筆測資
2. **統計方法**: 使用 Counter 或 defaultdict 計算出現次數
3. **排序輸出**: 字典序(alphabetical order)
4. **格式化**: 百分比固定四位小數點

### Easy 版本（考場快速版）
```
優點：
✓ 流程簡潔，易於回想
✓ 使用 split("\n\n") 直接切分
✓ 適合考場時間壓力下快速編寫

缺點：
✗ 對格式變異的容錯率較低
```

### 一般版本（穩健版）
```
優點：
✓ 逐行掃描，狀態控制精確
✓ 能應對各種格式變異
✓ 邊界情況處理完整

缺點：
✗ 代碼行數較多，需多花時間
```

---

## 📁 文件結構

```
1114405022/
├── README.md                 # 本文件（完整整理文檔）
├── QUESTION-10226.md         # 題目說明與優化紀錄
├── 10226_easy.py            # AI 教你的簡單版本（有中文註解）
├── 10226.py                 # 你手打的程式（逐行掃描版）
├── test_10226.py            # 測試程式（包含 3 個測試用例）
├── manual-test-log.txt      # 測試執行紀錄與結果
├── QUESTION-10235.md        # 其他題目說明
├── QUESTION-10242.md        # 其他題目說明
├── QUESTION-10252.md        # 其他題目說明
└── QUESTION-10268.md        # 其他題目說明
```

---

## 💻 程式代碼

### 1. Easy 版本 (10226_easy.py) - 考場快速版

```python
"""UVA 10226 - Hardwood Species

好記版（-easy）：
1. 先把整份輸入切成「每一筆測資一塊」
2. 每塊直接做次數統計
3. 排序後輸出百分比

這個版本的重點是流程非常固定，方便考場快速回想。
"""

from collections import Counter
import sys


def solve(data: str) -> str:
    # 把 Windows 的換行 \r\n 統一成 \n，避免分割時出現平台差異。
    text = data.replace("\r\n", "\n")

    # 去掉開頭/結尾多餘空白，避免 split 後多出空區塊。
    text = text.strip()
    if not text:
        return ""

    # 第一行是測資數量，先切出第一個換行位置。
    first_newline = text.find("\n")
    if first_newline == -1:
        return ""

    t = int(text[:first_newline].strip())

    # 剩下內容通常是「空行 + 測資內容」，先去掉前面空白再處理。
    rest = text[first_newline + 1 :].lstrip("\n")

    # UVA 10226 每筆測資之間以空行分隔。
    # 因此可直接用 "\n\n" 分割成每一筆。
    blocks = rest.split("\n\n") if rest else []

    # 保險做法：只取前 t 筆，避免尾端異常空白造成多餘區塊。
    blocks = blocks[:t]

    answers = []

    for block in blocks:
        # 每一行就是一個樹種名稱（名稱可能有空白，所以不能再 split 空白）。
        trees = [line for line in block.split("\n") if line != ""]

        # Counter 一次完成次數統計。
        freq = Counter(trees)
        total = len(trees)

        # 題目要求字典序輸出。
        lines = []
        for tree in sorted(freq.keys()):
            percent = freq[tree] * 100.0 / total
            lines.append(f"{tree} {percent:.4f}")

        answers.append("\n".join(lines))

    # 不同測資之間要空一行。
    return "\n\n".join(answers)


def main() -> None:
    # 一次讀完整個標準輸入，最適合這題空行分隔格式。
    data = sys.stdin.read()
    output = solve(data)
    if output:
        print(output)


if __name__ == "__main__":
    main()
```

---

### 2. 手打版本 (10226.py) - 穩健版

```python
"""UVA 10226 - Hardwood Species

一般版：使用逐行掃描的方式解析輸入，
可正確處理多筆測資、空行分隔、以及名稱含空白的樹種。
"""

from collections import defaultdict
import sys


def solve(data: str) -> str:
    # 先把輸入切成行，保留空字串（空行）以便辨識測資分隔。
    lines = data.splitlines()
    if not lines:
        return ""

    # 第一行是測資數量，前後空白要去除再轉整數。
    t = int(lines[0].strip())
    i = 1

    # 讀完測資數量後，常見格式會有一個空行，先略過。
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    outputs = []

    for case_idx in range(t):
        counter = defaultdict(int)
        total = 0

        # 讀取本筆測資直到遇到空行（或檔尾）。
        while i < len(lines) and lines[i].strip() != "":
            tree = lines[i]
            counter[tree] += 1
            total += 1
            i += 1

        # 依字典序輸出樹種，百分比固定四位小數。
        case_lines = []
        for tree in sorted(counter):
            percent = (counter[tree] * 100.0) / total
            case_lines.append(f"{tree} {percent:.4f}")

        outputs.append("\n".join(case_lines))

        # 移到下一筆測資（跳過測資間空行）。
        while i < len(lines) and lines[i].strip() == "":
            i += 1

    # 測資間要空一行。
    return "\n\n".join(outputs)


def main() -> None:
    data = sys.stdin.read()
    result = solve(data)
    if result:
        print(result)


if __name__ == "__main__":
    main()
```

---

### 3. 測試程式 (test_10226.py)

```python
"""QUESTION-10226 測試程式

用途：
- 自動測試一般版 10226.py
- 自動測試簡單版 10226_easy.py
- 顯示每組測試是否通過
"""

import subprocess
import sys
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TARGETS = [
    BASE_DIR / "10226.py",
    BASE_DIR / "10226_easy.py",
]


def run_program(path: Path, input_data: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(path)],
        input=input_data,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"程式 {path.name} 執行失敗，return code={completed.returncode}\n"
            f"stderr:\n{completed.stderr}"
        )
    return completed.stdout.rstrip("\n")


def main() -> None:
    # Case 1：一般多樹種統計
    case1_input = (
        "1\n"
        "\n"
        "Oak\n"
        "Pine\n"
        "Oak\n"
        "Maple\n"
        "Pine\n"
        "Oak\n"
    )
    case1_expected = "\n".join(
        [
            "Maple 16.6667",
            "Oak 50.0000",
            "Pine 33.3333",
        ]
    )

    # Case 2：單一樹種 100%
    case2_input = (
        "1\n"
        "\n"
        "Red Maple\n"
        "Red Maple\n"
        "Red Maple\n"
    )
    case2_expected = "Red Maple 100.0000"

    # Case 3：多測資 + 大小寫視為不同字串
    case3_input = (
        "2\n"
        "\n"
        "oak\n"
        "Oak\n"
        "oak\n"
        "\n"
        "Beech\n"
        "Ash\n"
        "Beech\n"
    )
    case3_expected = "\n\n".join(
        [
            "\n".join(
                [
                    "Oak 33.3333",
                    "oak 66.6667",
                ]
            ),
            "\n".join(
                [
                    "Ash 33.3333",
                    "Beech 66.6667",
                ]
            ),
        ]
    )

    tests = [
        ("case1", case1_input, case1_expected),
        ("case2", case2_input, case2_expected),
        ("case3", case3_input, case3_expected),
    ]

    all_passed = True

    for target in TARGETS:
        print(f"=== 測試 {target.name} ===")
        for name, inp, expected in tests:
            actual = run_program(target, inp)
            ok = actual == expected
            print(f"[{name}] {'PASS' if ok else 'FAIL'}")
            if not ok:
                all_passed = False
                print("--- 預期輸出 ---")
                print(expected)
                print("--- 實際輸出 ---")
                print(actual)
        print()

    if all_passed:
        print("全部測試通過")
    else:
        print("有測試失敗")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

---

## ✅ 測試結果

### 測試執行日期
2026-04-29

### 測試命令
```bash
python test_10226.py
```

### 測試輸出
```
=== 測試 10226.py ===
[case1] PASS
[case2] PASS
[case3] PASS

=== 測試 10226_easy.py ===
[case1] PASS
[case2] PASS
[case3] PASS

全部測試通過
```

### 測試用例覆蓋

#### Case 1: 一般多樹種統計
- **輸入**: 6 個樹種（Oak×3, Pine×2, Maple×1）
- **輸出**: 依字典序排序，顯示百分比
- **驗證**: 多樹種統計和排序邏輯

#### Case 2: 單一樹種 100%
- **輸入**: 3 個相同樹種（Red Maple）
- **輸出**: 100.0000% 百分比
- **驗證**: 邊界情況（百分比=100）

#### Case 3: 多測資 + 大小寫敏感
- **輸入**: 2 筆測資，驗證大小寫區分
- **輸出**: Oak vs oak 視為不同樹種
- **驗證**: 多筆測資分隔、大小寫敏感

---

## 🚀 使用說明

### 方式 1: 執行單個程式
```bash
# Easy 版本
python 10226_easy.py < input.txt

# 一般版本
python 10226.py < input.txt
```

### 方式 2: 執行完整測試
```bash
python test_10226.py
```

### 方式 3: 手動測試
```bash
# 創建輸入文件
cat > input.txt << EOF
1

Oak
Pine
Oak
Maple
Pine
Oak
EOF

# 執行程式
python 10226_easy.py < input.txt
```

---

## 📊 效能對比

| 特性 | Easy 版 | 一般版 |
|-----|--------|------|
| 代碼行數 | 79 | 57 |
| 可讀性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 考場速度 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| 穩健性 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 格式容錯 | 低 | 高 |

---

## 🔑 關鍵技巧

### 1. 字典序排序
```python
# Python 內建的 sorted() 預設為字典序
for tree in sorted(counter):
    # 此時 tree 已依字典序排列
```

### 2. 空行分隔
```python
# Easy 版本用 split("\n\n")
blocks = rest.split("\n\n")

# 一般版本用逐行掃描
while i < len(lines) and lines[i].strip() != "":
    # 讀取一行
```

### 3. 百分比計算
```python
# 確保浮點數除法
percent = (count * 100.0) / total
# 格式化為四位小數
f"{percent:.4f}"
```

### 4. 跨平台換行處理
```python
# 統一 Windows \r\n 和 Unix \n
text = data.replace("\r\n", "\n")
```

---

## 🎯 優化紀錄

### 版本 1 (初版)
- 基礎實現，功能完整
- 測試用例不完善

### 版本 2 (0422 分支復原)
- 加強中文註解
- 擴展測試用例至 3 個
- 完善邊界情況處理

### 版本 3 (當前版本)
- 整理成完整文檔
- 詳細說明解題思路
- 優化易讀性和可維護性

---

## 📝 提交說明

本解決方案包含：
- ✅ AI 教你的簡單版本，有中文註解
- ✅ 你手打的程式
- ✅ 測試程式
- ✅ 你手打程式的測試 LOG 記錄

**提交方式**: 按 GITHUB_WORKFLOW.md 流程提交

---

## 🔗 相關連結

- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a219)
- [Yui Huang 題解](https://yuihuang.com/zj-a219/)
- [Week 10 主頁](../README.md)

---

## 📞 備註

- 所有程式均已通過測試
- 支援多平台（Windows、Linux、macOS）
- 代碼使用 UTF-8 編碼
- Python 版本: 3.6+

**最後更新**: 2026-04-29
