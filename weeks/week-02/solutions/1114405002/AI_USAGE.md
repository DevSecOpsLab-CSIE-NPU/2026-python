# AI Usage Reflection

## 問題
- 如何實作去重維持順序？
- sorted key 多條件排序語法？
- Counter most_common 用法？

## 採用建議
- 使用 list 與 set 去重。
- sorted key lambda 多條件。
- Counter.most_common(1)

## 拒絕建議
- 無，使用了所有建議。

## 誤導案例
AI 建議使用 set 去重，但忘了順序，修正為手動檢查。