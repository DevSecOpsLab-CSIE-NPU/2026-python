# AI_LOG - 平方數計數 (count_squares)

## 我問 AI 什麼

「請幫我用 unittest 寫 count_squares(a, b) 的測試，需要計算 [a, b] 區間內完全平方數的個數。」

## AI 給了什麼

AI 提供了測試骨架，包含 3 個待實作的測試方法：
- `test_basic_range()` - 基本案例
- `test_edge_case()` - Edge case（未具體指定）
- `test_invalid_input_raises()` - 例外案例（但需要自己填入 assertRaises）

但 AI 沒有明確填寫預期答案，也沒有補充足夠的 edge case。

## 我改了什麼

1. **補充具體測試用例和預期值**：
   - `test_basic_range()`：count_squares(1, 10) == 3 (1, 4, 9)
   - `test_single_point_is_square()`：count_squares(1, 1) == 1
   - `test_no_squares_in_range()`：count_squares(5, 8) == 0
   - `test_single_large_perfect_square()`：count_squares(100, 100) == 1

2. **完成例外測試**：
   - `test_invalid_input_raises_value_error()`：使用 assertRaises 驗證 a > b 會丟 ValueError

3. **實作演算法**：
   - 用數學方法計算最小和最大的完全平方數根
   - 若 min_sqrt > max_sqrt，回傳 0（區間內無完全平方數）
   - 否則回傳 max_sqrt - min_sqrt + 1

4. **驗證 TDD 流程**：
   - 紅燈：3 個失敗，2 個通過（ValueError 檢查已自動通過）
   - 綠燈：全部 5 個測試通過

---

## 關鍵改進

AI 的骨架不夠明確，需要我主動補充：
- **測試邏輯**：不只是框架，要填入具體的期望值
- **邊界掩蓋**：5 個測試而非 3 個，更全面地覆蓋場景
- **數學最佳化**：用 sqrt 而非逐一檢查每個數字，提升效率
