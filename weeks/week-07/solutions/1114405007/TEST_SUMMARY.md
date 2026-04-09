# Week 04 - 單元測試報告

## 測試執行時間
- **日期**：2026-04-09
- **環境**：Python 3.13.9, Windows
- **測試框架**：unittest

## 測試結果

### 整體統計
- **總測試數**：41
- **通過**：41 ✅
- **失敗**：0
- **執行時間**：5ms

### 各個測試模組

#### U01 - 字串分割與匹配的陷阱 (test_U01_strings_split_gotchas.py)
| 測試名稱 | 狀態 | 測試內容 |
|---------|------|--------|
| test_capturing_group_preserves_delimiters | ✅ | 捕獲分組保留分隔符 |
| test_startswith_requires_tuple_not_list | ✅ | startswith 必須傳 tuple，不能傳 list |
| test_strip_only_handles_edges_not_middle | ✅ | strip 只處理頭尾，不處理中間空白 |
| test_generator_cleanup_efficient | ✅ | 生成器逐行清理（高效） |

#### U02 - 正則表達式進階技巧 (test_U02_regex_advanced.py)
| 測試名稱 | 狀態 | 測試內容 |
|---------|------|--------|
| test_precompiled_regex_performance_matters | ✅ | 預編譯的正則表達式 |
| test_sub_with_callback_function | ✅ | sub 回呼函數進行動態替換 |
| test_case_preserving_substitution | ✅ | 保持大小寫一致的替換 |
| test_findall_with_groups | ✅ | findall 回傳捕獲分組 |

#### U03 - 字串格式化效能與陷阱 (test_U03_strings_format_perf.py)
| 測試名稱 | 狀態 | 測試內容 |
|---------|------|--------|
| test_join_faster_than_concatenation | ✅ | join 效能優於 + |
| test_format_map_with_missing_keys | ✅ | format_map 處理缺失鍵 |
| test_bytes_indexing_returns_int | ✅ | bytes 索引回傳整數 |
| test_bytes_formatting | ✅ | bytes 無法直接 format，需先格式化再 encode |
| test_safe_sub_with_vars | ✅ | SafeSub 搭配 vars() 處理本地變數 |

#### U04 - 數字精度的陷阱與選擇 (test_U04_numbers_precision.py)
| 測試名稱 | 狀態 | 測試內容 |
|---------|------|--------|
| test_banker_rounding_python_round | ✅ | Python 的 round() 使用銀行家捨入 |
| test_traditional_rounding_with_decimal | ✅ | 傳統四捨五入（用 Decimal + ROUND_HALF_UP） |
| test_nan_comparison_fails | ✅ | NaN 無法用 == 比較 |
| test_nan_detection_with_isnan | ✅ | 檢測 NaN 必須用 math.isnan() |
| test_filter_nan_from_list | ✅ | 從列表中過濾 NaN |
| test_float_precision_issue | ✅ | float 的精度問題 |
| test_decimal_precision_exact | ✅ | Decimal 的精確計算 |
| test_float_vs_decimal_choice | ✅ | float vs Decimal 的選擇 |

#### U05 - 日期時間的陷阱 (test_U05_datetime_gotchas.py)
| 測試名稱 | 狀態 | 測試內容 |
|---------|------|--------|
| test_timedelta_does_not_support_months | ✅ | timedelta 不支援 months 參數 |
| test_add_one_month_correct_implementation | ✅ | 正確的月份加法實現 |
| test_add_months_year_boundary | ✅ | 跨年份的月份加法 |
| test_timedelta_supports_days_seconds_microseconds | ✅ | timedelta 支援的參數 |
| test_strptime_parsing | ✅ | strptime 日期解析 |
| test_manual_date_parsing_faster | ✅ | 手動解析比 strptime 更快 |

#### U06 - 時區操作最佳實踐 (test_U06_datetime_timezone.py)
| 測試名稱 | 狀態 | 測試內容 |
|---------|------|--------|
| test_naive_datetime_addition_dst_problem | ✅ | 直接在本地時間加減日期在夏令時邊界會出錯 |
| test_correct_timezone_addition_via_utc | ✅ | 正確做法 - 先轉 UTC 再計算 |
| test_user_input_to_utc_storage | ✅ | 最佳實踐 - 輸入→UTC→計算→輸出時轉本地 |
| test_timezone_aware_comparison | ✅ | 具有時區的日期時間比較 |
| test_naive_vs_aware_datetime | ✅ | naive datetime vs aware datetime |

#### U07 - 隨機種子與安全亂數 (test_U07_random_advanced.py)
| 測試名稱 | 狀態 | 測試內容 |
|---------|------|--------|
| test_same_seed_produces_same_sequence | ✅ | 相同種子產生相同序列 |
| test_different_seeds_produce_different_sequences | ✅ | 不同種子產生不同序列 |
| test_separate_random_instances_independent | ✅ | 不同 Random 實例各自獨立 |
| test_same_seed_different_instances_same_sequence | ✅ | 相同種子的不同實例產生相同序列 |
| test_secrets_randbelow_produces_value_in_range | ✅ | secrets.randbelow 產生指定範圍內的密碼學安全整數 |
| test_secrets_token_hex_length | ✅ | secrets.token_hex 產生指定字節數的十六進位字串 |
| test_secrets_token_bytes_length | ✅ | secrets.token_bytes 產生指定字節數的安全 bytes |
| test_random_vs_secrets_for_different_purposes | ✅ | random vs secrets 的用途差異 |
| test_secrets_choices_secure_random | ✅ | secrets.choice 選擇密碼學安全隨機選項 |

## 主要測試涵蓋內容

### 字串處理（U01-U03）
- ✅ 正則表達式的捕獲分組和分隔符
- ✅ startswith/strip 的常見陷阱
- ✅ 正則預編譯優化
- ✅ 字串拼接效能（join vs +）
- ✅ bytes 與 str 的索引差異

### 數字精度（U04）
- ✅ Python 銀行家捨入 vs 傳統四捨五入
- ✅ NaN 的比較和檢測
- ✅ float vs Decimal 的精度差異
- ✅ 金融/科學計算中的選擇

### 日期時間（U05-U06）
- ✅ timedelta 的限制和月份加法實現
- ✅ 時區操作和 UTC 最佳實踐
- ✅ 夏令時邊界問題
- ✅ strptime 性能問題

### 隨機數（U07）
- ✅ random 種子的可重現性
- ✅ secrets 密碼學安全亂數
- ✅ random vs secrets 的應用場景

## 文件位置
```
d:\1114405007\2026-python\weeks\week-04\in-class\
├── test_U01_strings_split_gotchas.py
├── test_U02_regex_advanced.py
├── test_U03_strings_format_perf.py
├── test_U04_numbers_precision.py
├── test_U05_datetime_gotchas.py
├── test_U06_datetime_timezone.py
├── test_U07_random_advanced.py
├── test_results.log         (詳細測試日誌)
└── TEST_SUMMARY.md          (本報告)
```

## 結論
✅ **所有 41 個單元測試全部通過**，驗證了 U01-U07 所有進階概念的正確實現！
