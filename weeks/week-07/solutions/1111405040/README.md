# Week 07 作業說明

## 作業主題
- 三國武將 PK 版 - 赤壁戰役遊戲引擎

## 完成內容
- `chibi_battle.py`
  - 手寫版核心引擎
- `chibi_battle_easy.py`
  - 簡單版執行入口
- `generals.txt`
  - 9 位武將資料，使用 EOF 結尾
- `battles.txt`
  - 戰役設定資料
- `tests/test_chibi.py`
  - 依照 Stage 1、Stage 2、Stage 3 設計的單元測試
- `TEST_CASES.md`
  - 測試案例說明
- `TEST_LOG.md`
  - TDD 開發與測試紀錄
- `AI_USAGE.md`
  - AI 協助範圍說明

## 執行方式

### 方法 1：執行全部測試
```powershell
cd weeks/week-07/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

### 方法 2：執行主程式
```powershell
cd weeks/week-07/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe chibi_battle.py
```

### 方法 3：執行簡單版
```powershell
cd weeks/week-07/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe chibi_battle_easy.py
```

## 設計重點
- 使用 `namedtuple` 定義武將與戰役資料結構
- 使用 `sorted(key=...)` 依速度安排出手順序
- 使用 `Counter` 統計每位武將的總傷害
- 使用 `defaultdict(int)` 統計每位武將的總損失
- 使用檔案 I/O 讀取 `generals.txt` 與 `battles.txt`
- 以 `EOF` 作為輸入結束標記
- 產生 ASCII 版戰役開始畫面與傷害統計報告

## 依賴套件
- 無
- 使用 Python 3.10+ 內建模組即可

## 補充說明
- 本次實作與資料檔都放在 `weeks/week-07/solutions/1111405040/`
- 依照作業需求採用 TDD 流程，先寫測試，再補實作，最後整理報告輸出
- 共撰寫 17 個測試案例，全部通過
