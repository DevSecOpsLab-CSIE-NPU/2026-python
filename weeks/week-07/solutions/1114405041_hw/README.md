# 1114405041 Week 07 Homework

這份作業是依照 week-07 HOMEWORK.md 製作的赤壁戰役遊戲引擎。

## 檔案說明

- chibi_battle.py：手寫版核心引擎，支援互動模式與自動模擬。
- chibi_battle_easy.py：較好記的簡化版。
- test_chibi.py：共 18 個 unittest 測試。
- run_tests.py：執行測試並產生 TEST_LOG.md。
- generals.txt：武將資料。
- battles.txt：戰役設定。
- AI_USAGE.md：AI 使用說明。

## 執行方式

```bash
python chibi_battle.py
python chibi_battle.py --auto
python chibi_battle_easy.py --auto
python run_tests.py
```

## 遊玩方式

- 直接執行 chibi_battle.py 會進入互動選單。
- 可以先看武將狀態，再逐波進行戰鬥。
- 也可以用 --auto 直接看完整戰報。