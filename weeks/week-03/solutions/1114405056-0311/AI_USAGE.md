# AI 使用說明

**學號**：1114405056  
**姓名**：尤靖崵

---

## 使用工具

- **GitHub Copilot Chat** (VS Code)
- 模型：Claude Sonnet 4

---

## 使用方式說明

### easy 版本（`*-easy.py`）

以下檔案為 AI 輔助生成的教學版本，包含詳細的中文註解，適合學習理解演算法邏輯：

- `uva100-easy.py`
- `uva118-easy.py`
- `uva272-easy.py`
- `uva299-easy.py`
- `uva490-easy.py`

**AI 使用流程**：
1. 提供題目說明（QUESTION-xxx.md 內容）
2. 請 AI 生成含中文說明的解法
3. 閱讀並理解 AI 的解題思路
4. 測試確認正確性

### hand 版本（`*-hand.py`）

以下檔案為自行手打版本，模擬 CPE 考場情境，**不使用 AI 生成**：

- `uva100-hand.py`
- `uva118-hand.py`
- `uva272-hand.py`
- `uva299-hand.py`
- `uva490-hand.py`

**撰寫方式**：
1. 先理解 easy 版本的演算法邏輯
2. 不參考 easy 版本，自行從零撰寫
3. 盡量精簡，模擬考場在時限內完成

### 測試程式（`test_*.py`）

測試程式使用 AI 協助生成測試案例架構，並手動補充邊界測試案例。

---

## 心得

透過先讓 AI 示範詳細解法，再自行手打精簡版的方式，能更深入理解各題目的演算法核心。  
AI 生成的 easy 版本作為學習素材，hand 版本才是實際練習成果。
