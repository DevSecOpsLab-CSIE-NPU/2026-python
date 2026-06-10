# 6/10 Starter — 數字根

## 使用方式

```bash
cp -r weeks/week-16/in_class/0610-starter weeks/week-16/solutions/<學號>/0610
cd weeks/week-16/solutions/<學號>/0610
```

## 檔案說明

- `test_digit_root.py`：測試骨架，**請先補 ≥3 個 test case**（含 edge case 與例外案例）
- `digit_root.py`：實作檔（尚未建立）。測試紅燈 commit 之後再建立，內容見下方規格。
- 完成後追加 `AI_LOG.md`（範本見 [`week-15/in_class/ai-log-template.md`](../../../week-15/in_class/ai-log-template.md)）

## `digit_root.py` 要寫什麼

這個檔案只需要一個函式，規格如下：

```python
def digit_root(n: int) -> int:
    ...
```

- **行為**：反覆把 `n` 的各位數字相加，直到結果只剩一位數，回傳那個一位數。
  例：`199 → 1+9+9=19 → 1+9=10 → 1+0=1`，所以 `digit_root(199)` 回傳 `1`。
- **輸入範圍**：正整數 `n`（1 ≤ n ≤ 2,000,000,000）。一位數直接回傳自己。
- **例外**：`n < 1` 時必須 `raise ValueError("n must be >= 1")`——訊息文字要一字不差，測試會比對。
- **不需要** `input()` / `print()`：這題只考核心函式，測試會直接 import 來呼叫。
  檔名、函式名都不能改，否則 `test_digit_root.py` 的 import 會失敗。

**完成的定義**：`python -m unittest` 從全紅變全綠，然後 commit（`feat:` 開頭）。
怎麼寫、要不要用迴圈、問 AI 什麼——都是你的事，但 AI 給的程式碼你要能解釋，
並把過程記進 `AI_LOG.md`。

更多範例值見 [`../0610-timed-drill.md`](../0610-timed-drill.md) 的題目表格。

## 本日規則

- [ ] 只准看[精簡版檢查表](../../../week-15/in_class/exam-sop-checklist-lite.md)，完整版請闔上
- [ ] AI 提示詞自己打，逐字記入 `AI_LOG.md`
- [ ] 60 分鐘內開出 PR

詳細見 [`../0610-timed-drill.md`](../0610-timed-drill.md)。
