# 6/11 Starter — 進位計數

## 使用方式

```bash
cp -r weeks/week-16/in_class/0611-starter weeks/week-16/solutions/<學號>/0611
cd weeks/week-16/solutions/<學號>/0611
```

## 檔案說明

- `test_carry_counter.py`：測試骨架，**請先補 ≥3 個 test case**（含 edge case 與例外案例）
- `carry_counter.py`：實作檔（尚未建立）。測試紅燈 commit 之後再建立，內容見下方規格。
- 完成後追加 `AI_LOG.md`（範本見 [`week-15/in_class/ai-log-template.md`](../../../week-15/in_class/ai-log-template.md)）

## `carry_counter.py` 要寫什麼

這個檔案只需要一個函式，規格如下：

```python
def count_carries(a: int, b: int) -> int:
    ...
```

- **行為**：回傳直式計算 `a + b` 時發生進位的次數。
  例：`555 + 555`，個位 `5+5=10` 進位、十位 `5+5+1=11` 進位、百位 `5+5+1=11` 進位，
  所以 `count_carries(555, 555)` 回傳 `3`。注意前一位的進位會影響下一位（`999 + 1` 是 3 次）。
- **輸入範圍**：非負整數 `a`, `b`（0 ≤ a, b < 10,000,000,000）。
- **例外**：`a` 或 `b` 為負數時必須 `raise ValueError("operands must be non-negative")`——訊息文字要一字不差，測試會比對。
- **不需要** `input()` / `print()`：這題只考核心函式，測試會直接 import 來呼叫。
  檔名、函式名都不能改，否則 `test_carry_counter.py` 的 import 會失敗。

**完成的定義**：`python -m unittest` 從全紅變全綠，然後 commit（`feat:` 開頭）。
AI 給的程式碼你要能解釋，並把過程記進 `AI_LOG.md`。

更多範例值見 [`../0611-solo-drill.md`](../0611-solo-drill.md) 的題目表格。

## 本日規則

- [ ] **不看任何檢查表**，八個步驟憑記憶
- [ ] AI 提示詞自己打，逐字記入 `AI_LOG.md`
- [ ] 60 分鐘內開出 PR
- [ ] 課末完成五題自我檢測，補強清單寫進 PR 描述

詳細見 [`../0611-solo-drill.md`](../0611-solo-drill.md)。
