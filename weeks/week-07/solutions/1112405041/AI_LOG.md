# AI_LOG — 三國武將赤壁戰役



## Stage 1

### 我問 AI 什麼
> 幫我寫 Week 7 三國武將 PK 版，照 TDD 三階段，從 Stage 1 開始。

### AI 反問我什麼 / 我怎麼回答
> AI 問：`General` namedtuple 有哪些欄位？
> 我答：faction, name, hp, atk, def_, spd, is_leader
>
> AI 問：檔案不存在會拋什麼？
> 我答：FileNotFoundError，可以不攔
>
> AI 問：4 個測試在測什麼？
> 我答：①讀取 9 位 ②關羽屬性 ③三國各 3 人 ④EOF 沒多讀

### AI 給了什麼
> 給了我 test_chibi.py（4 個 Stage 1 測試）和 chibi_battle.py（load_generals 實作）
給我 程式碼 補齊


### 我改了什麼
> 測試期望值依實際資料微調（諸葛亮 spd=60 而非 68）
根據 有出甚麼 bug 請 opencode 幫我弄 

## Stage 2

### 我問 AI 什麼
> 繼續 Stage 2，幫我補戰鬥模擬的測試和實作。

### AI 反問我什麼 / 我怎麼回答
> AI 問：sorted(reverse=True) 拿掉誰先攻？
> 我答：速度慢的先攻
>
> AI 問：max(1, atk-def_) 為什麼不能直接減？
> 我答：防>攻變負數
>
> AI 問：Counter 和 defaultdict 差在哪？
> 我答：Counter 有 most_common()

### AI 給了什麼
> 給了 simulate_wave、simulate_battle、calculate_damage 等完整實作

### 我改了什麼
> simulate_wave 原本只攻 1 個魏將，改成蜀吳聯軍全員攻擊、魏軍反擊

## Stage 3

### 我問 AI 什麼
> 補 Stage 3 ASCII 視覺化。

### AI 反問我什麼 / 我怎麼回答
> AI 問：偷改 stats 哪個測試會抓到？
> 我答：test_stats_unchanged_after_refactor

### AI 給了什麼
> print_damage_report、run_full_battle 實作

### 我改了什麼
> 新增檔案 coderun 過程紀錄等等 on 直播
對話紀錄 錄影

