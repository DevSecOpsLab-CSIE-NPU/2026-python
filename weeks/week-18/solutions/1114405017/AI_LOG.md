# AI_LOG

## 日期
- 2026-06-22

## 學號
- 1114405017

## 內容
- 已完成 `week-18` 期末考四題程式實作。
- 四題程式已放置於以下資料夾：
  - `1/main.py`
  - `2/main.py`
  - `3/main.py`
  - `4/main.py`
- 每題已補上單元測試：
  - `1/test_main.py`
  - `2/test_main.py`
  - `3/test_main.py`
  - `4/test_main.py`
- 每題已補上說明文件：
  - `1/README.md`
  - `2/README.md`
  - `3/README.md`
  - `4/README.md`（已更新爲中文雷達圖說明與本地圖檔位置）

## 根據題目規則計算的學號參數
- Q1 整除數 D = u % 4 + 2 = 7 % 4 + 2 = 5
- Q2 SHIFT = u % 25 + 1 = 7 % 25 + 1 = 8
- Q3 進位基底 base = 11（學號末位 7 對應表格）
- Q4 搜尋目標 K = 100 + 末兩碼 = 100 + 17 = 117

## 測試紀錄
### 執行方式
- `python test_main.py` 於每題資料夾內執行

### 結果
- Question 1: OK
- Question 2: OK
- Question 3: OK
- Question 4: OK

### 綜合測試指令
在 `d:\2026-python` 目錄執行：
```bash
python -c "from pathlib import Path; import subprocess, sys; root=Path('weeks/week-18/solutions/1114405017');
for part in ['1','2','3','4']:
    proc=subprocess.run([sys.executable, str(root/part/'test_main.py')], capture_output=True, text=True)
    print('---', part)
    print('returncode:', proc.returncode)
    print(proc.stdout)
    print(proc.stderr)
```

### 測試狀態
- 所有四題測試皆通過
- 沒有出現例外或錯誤訊息

## 附註
- 程式已符合 `jpg/0-1.jpg` 的題目參數與規則。
- Q4 已額外生成中文雷達圖，存放於 `4/radar.png`。
- Q4 `README.md` 已更新為中文圖表解讀與本地圖檔路徑。