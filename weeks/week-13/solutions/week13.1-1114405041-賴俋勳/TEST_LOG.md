# TEST_LOG (Red -> Green)

## Task 1
- Red：先寫 `test_get_top_depts_length`，初版未限制長度時失敗。
- Green：在 `get_top_depts` 最後加入 `[:top_n]`，測試通過。

## Task 2
- Red：先寫 `test_zip_to_county_unknown`，初版未處理短字串時失敗。
- Green：在 `zip_to_county` 加入空字串/長度判斷後通過。
- Red：新增 `test_zip_to_county_taitung` 與 `test_get_top_counties_excludes_other` 後，發現 950 系列映射與前十名邏輯不符合題意。
- Green：修正 950～958、966 為台東縣，並在 `get_top_counties` 排除「其他」，測試通過。

## 整體測試
- 指令：`python -m unittest discover -s tests -p "test_*.py" -v`
- 結果：全部通過（12 tests）。
