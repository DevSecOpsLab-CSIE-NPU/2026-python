#!/bin/bash
# run_all_tests.sh
# 執行所有單元測試並輸出至 test_log.txt

echo "Running all tests for Week 02..." > test_log.txt
echo "=================================" >> test_log.txt

echo "Running test_task1.py..." >> test_log.txt
python -m unittest test_task1.py -v >> test_log.txt 2>&1
echo "" >> test_log.txt

echo "Running test_task2.py..." >> test_log.txt
python -m unittest test_task2.py -v >> test_log.txt 2>&1
echo "" >> test_log.txt

echo "Running test_task3.py..." >> test_log.txt
python -m unittest test_task3.py -v >> test_log.txt 2>&1
echo "" >> test_log.txt

echo "All tests completed. Check test_log.txt for results."