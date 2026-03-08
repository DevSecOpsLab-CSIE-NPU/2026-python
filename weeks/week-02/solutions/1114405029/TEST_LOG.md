# TEST_LOG.md - Week 02

## Red Stage

Initial test run before full implementation.

Command:

python -m unittest discover -s tests -p "test_*.py" -v

Result:

Total tests: 15  
Passed: 0  
Failed: 15  

Reason:

The tests failed because the main functions for Task1, Task2, and Task3 had not been fully implemented yet. The sorting logic, duplicate removal logic, and log summary logic were still incomplete.

---

## Green Stage

Test run after implementing and fixing the solutions.

Command:

python -m unittest discover -s tests -p "test_*.py" -v

Result:

Total tests: 15  
Passed: 15  
Failed: 0  

Changes made:

Implemented the required functions for Task1, Task2, and Task3, including duplicate removal, multi-condition student sorting, and log summary using defaultdict and Counter. Also fixed the working directory issue so the tests could import the correct modules.

---

**Status:** All tests passed successfully and Week 02 homework is complete.