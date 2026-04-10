# AI 使用說明 (AI_USAGE.md)

## 使用工具
- GitHub Copilot (Claude Sonnet 4.6)

## AI 協助內容

### 1. 程式架構設計
- 提示詞: 「依照 HOMEWORK.md 的 TDD 三階段設計整合 Week02 與 Week07 技能」
- AI 產出: `chibi_battle.py` 整體架構 (namedtuple + Counter + defaultdict + 檔案I/O)

### 2. 測試案例生成
- 提示詞: 「依照作業說明自動建立符合各 Stage 測試邏輯的 unittest 案例」
- AI 產出: `test_chibi.py` 17 個 unittest 測試

### 3. 除錯修正
- AI 協助發現 `simulate_wave` 雙向攻擊導致魏傷害 > 蜀吳的邏輯問題
- 修正方向: 改為蜀軍單向攻擊魏軍，符合作業原設計意圖

### 4. 簡化版產出
- `chibi_battle_easy.py`: 以函式取代 class，降低初學者閱讀門檻

## 人工完成部分
- 確認 `generals.txt` 資料與標準值吻合 (攻/防/速屬性)
- 測試邊界條件驗證 (EOF 解析、速度排序方向)
- 閱讀作業需求並決定最終 TDD 三階段切分

## 結論
AI 加速了樣板程式碼與測試的撰寫速度，但邏輯判斷
（單向 vs 雙向攻擊）仍需人工確認，確保符合作業預期。
