# Robot Lost 遊戲（pygame MVP）

本版本依據 UVA 118 規則完成 pygame MVP，重點如下：
- 支援指令 `L/R/F`
- 越界會變成 `LOST`
- 在掉落前位置 + 方向留下 `scent`
- 後續機器人遇到同格同方向危險前進時會忽略 `F`

## 檔案說明

- `robot_game.py`：pygame 互動版本
- `robot_core.py`：核心規則邏輯（可單元測試）
- `tests/test_robot_core.py`：核心邏輯測試
- `tests/test_robot_scent.py`：scent 規則測試

## 安裝與執行

```bash
python -m pip install pygame
python robot_game.py
```

## 操作方式

- `L`：左轉
- `R`：右轉
- `F`：前進
- `N`：生成新機器人（重置到 `(0,0,N)`，保留 scent）
- `C`：清除 scent
- `P`：播放回放
- `ESC`：離開

## 測試

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```
