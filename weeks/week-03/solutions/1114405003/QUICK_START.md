# 🎮 快速啟動指南

## 方法 1：使用推薦的啟動腳本（最簡單）

```bash
python run.py
```

然後按照提示：
1. 看到 `輸入地圖大小 (直接按 Enter 使用 5 5):` 提示
2. **選項 A**: 直接按 `Enter` 使用預設的 5×5 地圖
3. **選項 B**: 輸入寬度和高度，例如 `10 10`，然後按 `Enter`
4. 遊戲窗口會立即出現！

### 範例：
```
輸入地圖大小 (直接按 Enter 使用 5 5): 
→ 按 Enter (使用 5×5)
或
輸入地圖大小 (直接按 Enter 使用 5 5): 8 8
→ 按 Enter (使用 8×8)
```

---

## 方法 2：直接運行主程式

```bash
python robot_game.py
```

說明同上。

---

## 方法 3：在 VS Code 中運行

### 步驟：
1. 打開 VS Code 終端（Ctrl + `）
2. 輸入：`python run.py`
3. 在終端中看到提示時，輸入地圖大小或直接按 Enter
4. **Pygame 遊戲窗口會彈出**

### 如果看不到窗口：
- 檢查是否有彈出窗口在屏幕邊緣（有時會出現在其他屏幕或被最小化）
- 按 Alt+Tab 查看所有打開的窗口
- 確保 pygame 已安裝（見下方檢查依賴）

---

## 檢查依賴

### 驗證 pygame 已安裝：
```bash
python -c "import pygame; print(f'pygame {pygame.version.ver} installed!')"
```

如果看到版本信息，說明已正確安裝。

### 如果 pygame 未安裝：
```bash
pip install pygame
```

---

## 遊戲操作說明

遊戲窗口出現後，使用以下按鍵：

| 按鍵 | 功能 |
|------|------|
| **L** | 左轉 |
| **R** | 右轉 |
| **F** | 前進 |
| **N** | 新機器人（輸入座標和方向） |
| **SPACE** | 切換機器人 |
| **C** | 清除 Scent |
| **ESC** | 結束遊戲 |

---

## 常見問題排查

### ❌ 問題：看不到任何窗口
**解決方案：**
- 檢查終端是否停留在 `輸入地圖大小 (直接按 Enter 使用 5 5):` 
- 按 Enter（如果有提示未回應）
- 稍等 2-3 秒讓 Pygame 初始化

### ❌ 問題：pygame 安裝失敗
**解決方案：**
```bash
pip install pygame --upgrade
```

### ❌ 問題：遊戲窗口黑屏
**解決方案：**
- 這是正常的初始化，稍等片刻
- 如果持續黑屏超過 5 秒，按 ESC 退出重試

---

## 推薦步驟

1. ✅ 打開 PowerShell 或 VS Code 終端
2. ✅ 進入項目目錄：
   ```bash
   cd "d:\1114405003李玉蓉\2026-python\weeks\week-03\solutions\1114405003"
   ```
3. ✅ 運行遊戲：
   ```bash
   python run.py
   ```
4. ✅ 按提示輸入地圖大小（或直接按 Enter）
5. ✅ **遊戲窗口應該會立即出現！** 🎮

---

**如果仍有問題，請檢查：**
- [ ] pygame 已安裝（`pip list | grep pygame`）
- [ ] Python 版本 3.8+ （`python --version`）
- [ ] 項目目錄正確（包含 robot_game.py 和 run.py）

---

**祝遊戲愉快！** 🚀
