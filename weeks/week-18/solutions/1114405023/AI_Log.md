# AI_LOG.md

## CPE 模擬實戰 AI 協作紀錄

## 基本資料

* 學號後兩碼：`23`
* 個位數：`3`
* 十位數：`2`

## 依學號決定的參數

| 題目          | 參數      |  數值 |
| ----------- | ------- | --: |
| 第一題：資料清理    | `D`     |   5 |
| 第二題：凱撒密碼    | `SHIFT` |   4 |
| 第三題：任意進位數字根 | `base`  |   3 |
| 第四題：二分搜尋效能  | `K`     | 123 |

---

# 使用 AI 的目的

本次使用 AI 協助完成 CPE 模擬實戰四題，包含：

1. 讀懂題目需求
2. 依照學號後兩碼推算參數
3. 依照 TDD 流程先寫測試，再實作程式
4. 建立紅燈與綠燈測試紀錄
5. 討論 edge case
6. 討論二分搜尋效能比較方式
7. 產生 `README.md`
8. 產生 `TEST_LOG.md`
9. 整理 `AI_LOG.md`

---

# AI 反問我什麼 / 我怎麼回答

---

## 第一題：資料清理 Data Cleaning

| AI 反問內容                                    | 我的回答                                                        |
| ------------------------------------------ | ----------------------------------------------------------- |
| `clean_numbers(numbers, divisor=5)` 要回傳什麼？ | 回傳處理後的整數 list，也就是 `list[int]`                               |
| `numbers` 可以是空 list 嗎？                     | 可以                                                          |
| `numbers` 可以有負數嗎？                          | 可以處理負數                                                      |
| `numbers` 可以有重複值嗎？                         | 可以有重複值                                                      |
| 如果沒有符合 divisor 的數字，要怎麼處理？                  | 函式回傳空 list，主程式輸出 `NONE`                                     |
| edge case 要測什麼？                            | 重複值、負數、沒有符合條件、原資料不能被修改                                      |
| 什麼情況算第一題綠燈成功？                              | `test_p1_data_cleaning.py` 全部通過，且輸入 `3 / 1 3 5 / 0` 時輸出 `5` |

---

## 第二題：凱撒密碼 Caesar Cipher

| AI 反問內容                               | 我的回答                                            |
| ------------------------------------- | ----------------------------------------------- |
| `caesar_cipher(text, shift=4)` 要回傳什麼？ | 回傳加密後的字串，型別是 `str`                              |
| 輸入可以有空白嗎？                             | 可以                                              |
| 輸入可以有數字與標點符號嗎？                        | 可以                                              |
| 輸入可以有多行文字嗎？                           | 可以                                              |
| 非英文字母要怎麼處理？                           | 非英文字母保持原樣，不做位移，也不丟出錯誤                           |
| edge case 要測什麼？                       | 大寫、小寫、`Z/z` 循環位移、非字母保留、多行 EOF                   |
| 什麼情況算第二題綠燈成功？                         | `test_p2_caesar_cipher.py` 全部通過，且輸入 `z` 時輸出 `d` |

---

## 第三題：任意進位的數字根

| AI 反問內容                            | 我的回答                                       |
| ---------------------------------- | ------------------------------------------ |
| `digit_root(value, base=3)` 要回傳什麼？ | 回傳最後的數字根，型別是 `int`                         |
| `value = 0` 可以嗎？                   | 可以，輸出 `0`                                  |
| `value` 可以是負數嗎？                    | 不接受負數                                      |
| 輸入有空行時怎麼辦？                         | 空行略過                                       |
| 如果 `value < 0` 要怎麼處理？              | `raise ValueError`                         |
| edge case 要測什麼？                    | `0`、小於 base 的數、需要多次相加的數、`-5`               |
| 什麼情況算第三題綠燈成功？                      | `test_p3_digit_root_base.py` 全部通過，沒有 error |

---

## 第四題：二分搜尋效能 Binary Search Performance

| AI 反問內容                                             | 我的回答                                                                                                       |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `linear_search_with_count(data, target=123)` 要回傳什麼？ | 回傳 index 與比較次數                                                                                             |
| `binary_search_with_count(data, target=123)` 要回傳什麼？ | 回傳 index 與比較次數                                                                                             |
| 效能比較要記錄什麼？                                          | 記錄兩種搜尋法的搜尋時間，以及比較次數                                                                                        |
| `data` 可以是空 list 嗎？                                 | 可以                                                                                                         |
| 找不到 target 時要怎麼處理？                                  | 回傳未找到該筆資料，也就是 index 為 `-1`                                                                                 |
| 如果 `data` 沒排序時要怎麼處理？                                | 視為無法正確搜尋，回傳 `-1`                                                                                           |
| edge case 要測什麼？                                     | 找到、找不到、空 list、未排序資料、有兩個相同整數、不修改原資料                                                                         |
| 陣列大小至少要多少？                                          | 至少 `10^5`，所以使用 `DATA_SIZE = 100000`                                                                        |
| 題目要求的陣列排序方式是什麼？                                     | 升冪陣列                                                                                                       |
| 為了比較 best / middle / worst，要怎麼設計資料？                 | 固定 `K = 123`，產生不同升冪陣列，讓 `K` 分別位在 index `0`、`50000`、`99999`                                                 |
| not_found case 要怎麼設計？                               | 建立長度 `100000` 的升冪陣列，但不包含 `K = 123`                                                                         |
| 搜尋計時要包含資料建立、輸入、輸出嗎？                                 | 不包含，benchmark 只量搜尋函式本身                                                                                     |
| 兩種搜尋法共同的提速方式是什麼？                                    | 資料先建立好、找到就立刻 return、不把 input / print / 建資料算進時間、使用相同資料與 repeat 次數                                           |
| 雷達圖要比較哪些項目？                                         | `BestCmp`、`MiddleCmp`、`WorstCmp`、`NotFoundCmp`、`BestTime`、`MiddleTime`、`WorstTime`、`NotFoundTime`          |
| 雷達圖正規化方式是什麼？                                        | 比較次數與時間都是越小越好，所以用「越小越好」的正規化方式                                                                              |
| 什麼情況算第四題綠燈成功？                                       | `test_p4_binary_search_perf.py` 全部通過，能輸出 best / middle / worst / not_found 的比較次數與時間，並產生 `assets/radar.png` |

---


## 第四題後續討論與修改紀錄

| 討論項目 | 決定 / 修改內容 |
| --- | --- |
| 是否要使用 `timeit`？ | 原本使用一般計時方式，後續改成 Python 標準庫 `timeit.repeat()`，讓第四題更符合題目要求的「用 timeit 比較」。 |
| `timeit` 要量哪些東西？ | 只量搜尋函式本身，不把資料建立、輸入、輸出、雷達圖產生時間算進搜尋時間。 |
| 是否要加入 found / not_found 彙整？ | 加入 found / not_found summary。found 使用 best、middle、worst 三種找到目標的 case 取平均；not_found 使用找不到目標的 case。 |
| `cmp` 是什麼？ | `cmp` 代表 comparisons，也就是搜尋過程中的比較次數。 |
| 是否要輸出較快者？ | 新增 `fastest` 欄位，比較 linear search 與 binary search 的 `timeit` 平均時間，輸出 `linear`、`binary` 或 `tie`。 |
| best case 誰較快？ | best case 中 linear search 較快，因為目標 `K=123` 位於 index `0`，只需要比較 1 次。 |
| middle / worst / not_found 誰較快？ | middle、worst、not_found 三種情況皆為 binary search 較快，因為 binary search 每次將搜尋範圍縮小一半。 |
| 是否要更新 README？ | 需要在 README 補上 found / not_found summary、`cmp` 說明、`timeit` 說明與較快者欄位。 |
| 是否要更新 TEST_LOG？ | 需要更新第四題輸出結果，包含 `fastest=linear` 或 `fastest=binary`。 |
| 是否要更新測試檔？ | 建議在 `test_p4_binary_search_perf.py` 中補 `fastest_search()` 測試，確認 linear、binary、tie 三種結果都正確。 |

---

## 第四題 found / not_found 效能彙整

根據第四題最新執行結果：

| Case | Linear cmp | Binary cmp | Linear timeit | Binary timeit | 較快者 |
| --- | ---: | ---: | ---: | ---: | --- |
| found 平均 | 50000.67 | 16.33 | 0.0072284400 | 0.0000058667 | binary |
| not_found | 100000 | 16 | 0.0135415800 | 0.0000065400 | binary |

### found 平均計算方式

found 平均是由 best、middle、worst 三個有找到目標的 case 計算平均值。

```text
linear_cmp_avg = (1 + 50001 + 100000) / 3 = 50000.67
binary_cmp_avg = (16 + 16 + 17) / 3 = 16.33
```

```text
linear_timeit_avg = (0.0000046200 + 0.0076549000 + 0.0140258000) / 3
                  = 0.0072284400

binary_timeit_avg = (0.0000071000 + 0.0000052400 + 0.0000052600) / 3
                  = 0.0000058667
```

### not_found 結果

not_found case 中，陣列長度為 `100000`，且不包含 `K = 123`。

```text
linear_cmp = 100000
binary_cmp = 16
linear_timeit = 0.0135415800
binary_timeit = 0.0000065400
fastest = binary
```
