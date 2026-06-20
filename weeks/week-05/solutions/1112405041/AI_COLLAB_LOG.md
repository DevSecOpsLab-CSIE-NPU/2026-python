# AI 協作紀錄 - Big Two

## 我下的指令

1. 讀 week05 game design folder，用開發訪談模式做 P1~P6
2. 模仿之前 07、10、13、15、16、17 週的做法
3. 加快速度，30 分鐘搞定，直接 RED→GREEN commit

## AI 問我的概念題

| 問題 | 我回答 |
|------|--------|
| Card rank 怎麼訂？ | 3~15，A=14，2=15，照 p1-dev.md |
| 同花順跟四條哪個大？ | 同花順 |
| 順子 A-2-3-4-5 rank 組合？ | 14,15,3,4,5 |

## TDD 進度

P1~P6 全部 RED→GREEN 完成，總共 71 tests PASS。

## 目錄結構

最後扁平化，所有 .py 直接放在 solutions/1112405041/ 下。

## 執行

```
pip install pygame
python main.py
python -m unittest discover -v
```
