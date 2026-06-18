# AI_LOG - 0618 搜尋效能實驗室

## 各階段提示詞記錄

### Stage 1：timeit 裝飾器
- 請幫我用最低難度解釋什麼是裝飾器和 timeit
- 請幫我寫 test_timing.py 測試程式，規格每條都要覆蓋

### Stage 2：三種搜尋 + 量測
- 請幫我解釋 linear/binary/set 搜尋的概念與差異
- 請幫我寫 test_search.py 三種共用 subTest
- 請幫我寫 search.py 實作

### Stage 3：加速實驗 + 交叉點
- 請幫我把 bisect 和 fast_set 加入 benchmark
- 請幫我找出交叉點 n

### Stage 4：雷達圖
- 請幫我畫 radar chart，6 個維度

### Stage 5：安全自掃
- 請幫我掃 OpenSSF 3 條規則

## AI 反問我什麼 / 我怎麼回答

### Stage 1
| AI 問 | 我答 |
|-------|------|
| timeit 簽名？兩種用法？ | @timeit 和 @timeit(repeat=N) 都支援 |
| repeat 邊界？ | <1 就 raise，≥1 交給 Python |
| 為什麼不用 assert？ | python -O 會吃掉 assert |
| 被裝飾函式拋例外？ | timeit 不攔，讓它往上拋 |
| 什麼算紅燈？ | 全部 Fail（ImportError） |

### Stage 2
| AI 問 | 我答 |
|-------|------|
| 三種共用測試，共同判準？ | 轉成 ≥0 (int) / True (bool) |
| 空 list 回什麼？ | -1 / False |
| binary 未排序？ | 回 -1，docstring 說明 |
| data=None 要檢查嗎？ | 不用，讓 Python 自己炸 |
| 重複值測試？ | 有找到就好，不強求 index |

### Stage 3
| AI 問 | 我答 |
|-------|------|
| 加速方案用什麼？ | bisect + fast_set（預建 set） |
| 預測交叉點？ | n > 100，實測約 10~50 |

### Stage 4
| AI 問 | 我答 |
|-------|------|
| 雷達圖維度？ | Speed/Index/No Sort/Simplicity/Memory/Multi-Query |

## 我改了什麼

（請你自己填寫：例如檢查了 AI 給的測試齊不齊、修改了 benchmark 的 sorting bug、調整了雷達圖分數等等）