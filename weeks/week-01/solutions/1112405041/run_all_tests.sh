#!/bin/bash

# Week 01 測試執行腳本
# 執行所有 12 個主題的單元測試，並將結果輸出到 test_log.txt

echo "開始執行 Week 01 測試..." | tee test_log.txt
echo "========================================" >> test_log.txt
echo "執行時間: $(date)" >> test_log.txt
echo "========================================" >> test_log.txt

# 測試計數
PASSED=0
FAILED=0
TOTAL=0

# 執行每個測試
for i in {01..12}; do
    TEST_FILE="test_${i}.py"
    if [ -f "$TEST_FILE" ]; then
        TOTAL=$((TOTAL + 1))
        echo "" >> test_log.txt
        echo "執行 $TEST_FILE..." >> test_log.txt
        echo "----------------------------------------" >> test_log.txt
        
        if python "$TEST_FILE" >> test_log.txt 2>&1; then
            echo "✓ $TEST_FILE 通過" >> test_log.txt
            PASSED=$((PASSED + 1))
        else
            echo "✗ $TEST_FILE 失敗" >> test_log.txt
            FAILED=$((FAILED + 1))
        fi
    fi
done

# 測試總結
echo "" >> test_log.txt
echo "========================================" >> test_log.txt
echo "測試總結" >> test_log.txt
echo "========================================" >> test_log.txt
echo "總測試數: $TOTAL" >> test_log.txt
echo "通過: $PASSED" >> test_log.txt
echo "失敗: $FAILED" >> test_log.txt
echo "成功率: $(echo "scale=2; $PASSED * 100 / $TOTAL" | bc)%" >> test_log.txt
echo "完成時間: $(date)" >> test_log.txt

# 同時輸出到控制臺
echo ""
echo "測試完成！結果已保存到 test_log.txt"
echo "總測試數: $TOTAL"
echo "通過: $PASSED"
echo "失敗: $FAILED"
