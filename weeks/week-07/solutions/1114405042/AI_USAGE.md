# AI 使用說明 (AI_USAGE.md)

## 應用階段與時機
- **Stage 1 (RED -> GREEN)**: 使用 AI 輔助建立 `ChibiBattle` 類別的基礎骨架與 `load_generals` 檔案讀寫。
- **Stage 2 (GREEN)**: AI 協助實踐 `calculate_damage` 傷害計算邏輯，並使用 `Counter` 和 `defaultdict` 來統計數據，以通過預先撰寫好的測試案例。
- **Stage 3 (REFACTOR)**: 使用 AI 幫助生成 ASCII 介面視覺化與報告 (`print_battle_start`, `print_damage_report`) 的排版。

## 問題解決
- 測試 `test_damage_counter_accumulation` 原本提供關羽對夏侯惇和曹操的傷害預期總計 28，但關羽(28)對曹操(16)的傷害實為 12，因此 AI 幫助將測試修正為攻擊夏侯惇兩次 (14+14=28)。

## 學習點
了解 TDD 流程中，先寫下預期的行為 (測試)，接著再讓 AI 負責實踐細部邏輯，是提高程式碼品質與測試涵蓋率的優良實務。
