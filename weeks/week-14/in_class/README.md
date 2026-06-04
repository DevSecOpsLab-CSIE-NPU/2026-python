# Week 14 課堂範例：測試、除錯與例外

本目錄涵蓋：[Python3 Cookbook 第 14 章：測試、調試和異常](https://python3-cookbook.readthedocs.io/zh-cn/latest/chapters/p14_test_debug_and_exceptions.html)

依 **Bloom's Taxonomy** 分為兩層，整理成 5 個範例：

- **R（Remember 記憶層）**：直接可複製、可執行的基礎用法
- **U（Understand 理解層）**：為什麼這樣做？陷阱、抉擇與背後原理

---

## 章節對照表

### 記憶層（R）

| 範例 | 涵蓋節次 | 主題 | 核心 API |
|------|----------|------|----------|
| [R01](./R01-unittest-basics.py) | 14.1–14.3 | unittest 基礎 | `redirect_stdout` / `mock.patch` / `assertRaises` |
| [R02](./R02-exceptions-basic.py) | 14.6–14.8 | 例外處理基本 | 多例外 tuple / `except Exception` / 自定義例外類別 |
| [R03](./R03-profile-basic.py) | 14.13 | 效能測量 | `timed` 裝飾器 / `timeit` / `cProfile` |

### 理解層（U）

| 範例 | 涵蓋節次 | 主題 | 關鍵概念 |
|------|----------|------|----------|
| [U01](./U01-test-warnings-why.py) | 14.4, 14.5, 14.11 | 測試控制與警告的「為什麼」 | `skipIf` vs `if return` / `expectedFailure` 的價值 / `stacklevel=2` / Warning 種類選擇 |
| [U02](./U02-debug-speedup-why.py) | 14.9, 14.10, 14.12, 14.14 | 例外、除錯與加速的「為什麼」 | `raise from` vs `raise X` vs bare `raise` vs `raise e` / `print_exc` vs `print(e)` / `LOAD_FAST` vs `LOAD_GLOBAL` |

---

## 執行方式

```bash
cd weeks/week-14/in_class

# 記憶層
python R01-unittest-basics.py
python R02-exceptions-basic.py
python R03-profile-basic.py

# 理解層
python U01-test-warnings-why.py
python U01-test-warnings-why.py --log    # 把測試結果寫到 test_result.log
python U02-debug-speedup-why.py
```

---

## 學習重點（一句話帶走）

- **R01**：mock 掉外部相依、用 `assertRaises` 驗證例外、用 `redirect_stdout` 驗證輸出。
- **R02**：多例外用 tuple；`except Exception` 不要寫成 bare `except:`；自定義例外繼承 `Exception`。
- **R03**：粗測用 `time.perf_counter`，微測用 `timeit`，找瓶頸用 `cProfile`。
- **U01**：`skipIf` 讓報表能看出「為什麼沒測」；`warnings.warn` 必加 `stacklevel=2` 指向呼叫端。
- **U02**：包裝底層錯誤用 `raise X from e`；中途記 log 再拋用 bare `raise`；**不要寫 `raise e`**，那會丟失 traceback。
