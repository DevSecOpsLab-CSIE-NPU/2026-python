# Week 03 - 1114405056

## 完成題目
- UVA 100 - The 3n + 1 problem
- UVA 118 - Mutant Flatworld Explorers
- UVA 272 - TEX Quotes
- UVA 299 - Train Swapping
- UVA 490 - Rotating Sentences

## 檔案結構
- `uvaXXX-easy.py`: AI 協助後整理的易讀版本
- `uvaXXX-hand.py`: 手打版本
- `test_uvaXXX.py`: 對應題目的測試程式

## 執行方式
在目前資料夾執行：

```bash
python -m unittest test_uva100.py
python -m unittest test_uva118.py
python -m unittest test_uva272.py
python -m unittest test_uva299.py
python -m unittest test_uva490.py
```

或一次執行全部：

```bash
python -m unittest discover -p "test_uva*.py"
```

## 資料結構與解法重點
- UVA 100：使用 `dict` 記憶化 cycle length，降低重複計算成本
- UVA 118：使用 `set` 儲存 scent（座標 + 方向）避免重複掉落
- UVA 272：使用布林旗標交替替換 `"` 為 ```` 與 `''`
- UVA 299：以雙迴圈計算 inversion 數量（即最少相鄰交換次數）
- UVA 490：以補空白矩陣概念做 90 度旋轉並移除行尾空白

## 主要修正紀錄
- 修正 UVA 118 越界後 scent 判斷流程，避免第二台機器人重複 LOST
- 修正 UVA 490 在不等長列時的補空白處理
- 強化 UVA 100 測試，加入反向區間與隨機小範圍案例
