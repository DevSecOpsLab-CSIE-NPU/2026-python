# 題2 AI_LOG（A區：凱撒密碼）

## AI 反問我什麼 / 我怎麼回答

| AI 問 | 我答 |
|-------|------|
| 函式簽名？ | `encrypt_line(text, shift)` -> `str`；`solve(input_text, shift)` -> `str` |
| 輸入邊界？ | 多行至 EOF，每行 `<= 1000` 字元 |
| 例外處理？ | 空行原樣保留；非字母不處理 |
| Edge case？ | `Z/z` 循環回 `A/a`；整行無字母不變 |
| 驗收標準？ | `SHIFT = 8`（公式 `u%25+1`, `u=7`） |

## 我問了 AI 什麼（本題）
1. 幫我實作凱撒密碼，使用學號對應位移。
2. 拆出至少 3 組測資，含 edge case，先 Red 再 Green。

## AI 建議採用 / 修正
- 採用字元區間判斷分開處理大小寫。
- 以 `%26` 進行循環位移避免越界。
- 後續修正為與文件一致的公式 `u%25+1`。

## Git PR SOP（本題）
- [x] 分支：`0622-1114405007`
- [x] 先紅後綠：
	- Red commit：`bc55096`（test: add failing tests for caesar）
	- Green commit：`bf09bf6`（feat: implement caesar）
- [x] PR base:compare：`DevSecOpsLab-CSIE-NPU/2026-python:main <- GuZhe-Yu/2026-python:0622-1114405007`
- [x] PR 描述三要件：
	- 題目摘要：已描述題2凱撒密碼與 `SHIFT=8`
	- 測試結果：已提供測試通過紀錄（見 `TEST_LOG.md`）
	- 我跟 AI 改了什麼：已在本檔完整記錄