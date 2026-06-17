# Robot Lost Game (pygame MVP)

這是依據 UVA 118 概念做的 pygame MVP：
- 指令 `L/R/F`
- 越界會 `LOST`
- 在掉落點留下 `scent`
- 後續機器人可忽略同格同方向的危險 `F`

## 檔案

- `robot_game_mvp.py`：pygame 互動版本
- `robot_core.py`：核心邏輯（可測試）
- `test_robot_core.py`：核心邏輯單元測試

## 安裝與執行

```bash
python3 -m pip install pygame
python3 robot_game_mvp.py
```

## 控制

- `L`：左轉
- `R`：右轉
- `F`：前進
- `N`：部署新機器人（重置到 `(0,0,N)`，保留 scent）
- `C`：清除 scent
- `ESC`：離開

## 測試

```bash
python3 -m unittest test_robot_core.py -v
```
