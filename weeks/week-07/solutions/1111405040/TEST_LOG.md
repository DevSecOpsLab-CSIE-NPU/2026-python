# 赤壁戰役 - 測試執行日誌

## Stage 1：資料讀取
- 先設計資料讀取測試：
  - 武將數量
  - 屬性解析
  - 勢力分布
  - EOF 停止
  - 戰役設定解析
- 完成 `load_generals()` 與 `load_battle_config()` 後，Stage 1 測試通過

## Stage 2：戰鬥模擬
- 先設計戰鬥順序、傷害計算、累加統計與戰敗判定測試
- 依序補上：
  - `get_battle_order()`
  - `calculate_damage()`
  - `simulate_wave()`
  - `simulate_battle()`
  - `get_damage_ranking()`
  - `get_faction_stats()`
  - `get_defeated_generals()`
- Stage 2 測試通過後，再進入報告輸出整理

## Stage 3：ASCII 報告
- 新增 `generate_battle_start()` 與 `generate_damage_report()`
- 驗證報告輸出不會改動統計資料
- 驗證完整報告包含必要區塊

## 最終測試指令
```powershell
cd weeks/week-07/solutions/1111405040
C:\Users\a4528\AppData\Local\Programs\Python\Python310\python.exe -m unittest discover -s tests -p "test_*.py" -v
```

## 最終測試結果
```text
Ran 17 tests in 0.033s

OK
```

## 結論
- 17 個測試案例全部通過
- 三階段需求皆完成
- 主程式與簡單版都可以直接執行
