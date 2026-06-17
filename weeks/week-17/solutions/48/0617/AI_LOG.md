# AI_LOG — 0617 timeit + 搜尋效能評估

## 我問 AI 什麼

「請幫我完成 0617 任務一（timing.py timeit 裝飾器）與任務二（search.py linear_search / binary_search）的 TDD 流程。」

## AI 反問我什麼 / 我怎麼回答

| AI 反問 | 我怎麼回答 |
|---------|-----------|
| timeit 的函式簽名是什麼？接受什麼參數？回傳什麼？ | def timeit(func, repeat=3)，回傳包裝後的 wrapper 函式 |
| repeat 的有效範圍？repeat=1 行為正確嗎？ | repeat >= 1；repeat=1 應正常運作，平均值即該次耗時 |
| repeat < 1 的例外行為？ | repeat=0 和 -5 都應 raise ValueError |
| 還有哪些邊緣案例？ | 被裝飾函式拋例外應向外傳播、回傳 None、metadata 保留 |
| 驗收標準是什麼？ | 先 stub 跑出 AssertionError 才算紅燈（非 ImportError） |
| search.py 簽名與邊界？ | linear_search(data, target)/binary_search(data, target)，找不到回 -1 |
| data is None 怎麼處理？ | raise ValueError |

## AI 給了什麼

- 任務一：timeit 裝飾器（支援 repeat 參數、records/last_elapsed、functools.wraps、例外傳播、repeat < 1 raise ValueError）
- 任務二：linear_search（O(n) 逐一比對）與 binary_search（O(log n) 已排序資料）
- 效能評估腳本與數據

## 我改了什麼

確認了檢查表所有項目並決定 edge case 行為（None 輸入 raise ValueError、例外需向外傳播）。
