# 赤壁戰役 - 測試執行日誌

- 測試時間：由 run_tests.py 自動產生
- 總測試數量：18
- 失敗數量：0
- 錯誤數量：0

```text
test_eof_parsing (test_chibi.TestStage1DataLoading.test_eof_parsing) ... ok
test_faction_distribution (test_chibi.TestStage1DataLoading.test_faction_distribution) ... ok
test_load_generals_from_file (test_chibi.TestStage1DataLoading.test_load_generals_from_file) ... ok
test_parse_general_attributes (test_chibi.TestStage1DataLoading.test_parse_general_attributes) ... ok
test_battle_order_by_speed (test_chibi.TestStage2BattleLogic.test_battle_order_by_speed) ... ok
test_calculate_damage (test_chibi.TestStage2BattleLogic.test_calculate_damage) ... ok
test_damage_counter_accumulation (test_chibi.TestStage2BattleLogic.test_damage_counter_accumulation) ... ok
test_damage_ranking_most_common (test_chibi.TestStage2BattleLogic.test_damage_ranking_most_common) ... ok
test_defeated_generals (test_chibi.TestStage2BattleLogic.test_defeated_generals) ... ok
test_faction_damage_stats (test_chibi.TestStage2BattleLogic.test_faction_damage_stats) ... ok
test_simulate_one_wave (test_chibi.TestStage2BattleLogic.test_simulate_one_wave) ... ok
test_simulate_three_waves (test_chibi.TestStage2BattleLogic.test_simulate_three_waves) ... ok
test_troop_loss_tracking (test_chibi.TestStage2BattleLogic.test_troop_loss_tracking) ... ok
test_auto_battle_output_contains_report (test_chibi.TestStage3InteractiveAndRefactor.test_auto_battle_output_contains_report) ... ok
test_easy_auto_output (test_chibi.TestStage3InteractiveAndRefactor.test_easy_auto_output) ... ok
test_easy_version_can_finish_battle (test_chibi.TestStage3InteractiveAndRefactor.test_easy_version_can_finish_battle) ... ok
test_stats_unchanged_after_report_generation (test_chibi.TestStage3InteractiveAndRefactor.test_stats_unchanged_after_report_generation) ... ok
test_status_command (test_chibi.TestStage3InteractiveAndRefactor.test_status_command) ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.273s

OK
```

整體結果：PASS
