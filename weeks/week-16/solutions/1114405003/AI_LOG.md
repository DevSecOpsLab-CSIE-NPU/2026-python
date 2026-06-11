# AI_LOG

## 我問 AI 什麼

> 請幫我分析 digit_root 的規格，拆出至少 3 個 test case（含 edge case 與例外案例），先討論再寫。

## AI 給了什麼

> 給了 3 個 test method：`test_basic`（199→1、38→2、7→7）、`test_edge_case`（1→1、2000000000→2、10→1）、`test_invalid_input_raises`（0、-5、-1 各 raise ValueError），共 9 個 assertion。

## 我改了什麼

> 確認 AI 提出的案例涵蓋正常邏輯、邊界值（最小正整數、大數）、例外輸入，且符合題目「≥3 個 test case、≥1 edge case、≥1 例外」的要求，直接採用。
