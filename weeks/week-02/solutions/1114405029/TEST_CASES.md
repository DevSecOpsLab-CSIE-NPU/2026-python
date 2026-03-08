# TEST_CASES.md - Week 02

## Case 1: Normal Input (Task1)

Input:

5 3 5 2 9 2 8 3 1

Expected Output:

dedupe: 5 3 2 9 8 1  
asc: 1 2 2 3 3 5 5 8 9  
desc: 9 8 5 5 3 3 2 2 1  
evens: 2 2 8  

Actual Output:

dedupe: 5 3 2 9 8 1  
asc: 1 2 2 3 3 5 5 8 9  
desc: 9 8 5 5 3 3 2 2 1  
evens: 2 2 8  

Result:

PASS

Related Test:

tests/test_task1.py::test_normal_case

Key Fix:

Ensured duplicate removal keeps the first occurrence order.

---

## Case 2: Edge Case – Empty Input (Task1)

Input:

(empty list)

Expected Output:

dedupe:  
asc:  
desc:  
evens:  

Actual Output:

dedupe:  
asc:  
desc:  
evens:  

Result:

PASS

Related Test:

tests/test_task1.py::test_empty_list_case

Key Fix:

Handled empty list input safely without errors.

---

## Case 3: Student Ranking with Score Tie (Task2)

Input:

bob 88 19  
ian 88 19  
zoe 92 21  

Expected Output:

zoe 92 21  
bob 88 19  
ian 88 19  

Actual Output:

zoe 92 21  
bob 88 19  
ian 88 19  

Result:

PASS

Related Test:

tests/test_task2.py::test_tie_break_by_name

Key Fix:

Implemented multi-key sorting: (-score, age, name).

---

## Case 4: Edge Case – Single Student (Task2)

Input:

alice 95 18

Expected Output:

alice 95 18

Actual Output:

alice 95 18

Result:

PASS

Related Test:

tests/test_task2.py::test_single_student

Key Fix:

Handled list with a single element.

---

## Case 5: Log Summary Normal Case (Task3)

Input:

alice login  
bob login  
alice logout  

Expected Output:

alice 2  
bob 1  
top_action: login 2  

Actual Output:

alice 2  
bob 1  
top_action: login 2  

Result:

PASS

Related Test:

tests/test_task3.py::test_normal_logs

Key Fix:

Used defaultdict for user counting and Counter for action frequency.

---

## Case 6: Edge Case – Empty Logs (Task3)

Input:

(no records)

Expected Output:

(no user output)  
top_action: None 0  

Actual Output:

(no user output)  
top_action: None 0  

Result:

PASS

Related Test:

tests/test_task3.py::test_empty_input

Key Fix:

Added handling for empty action_counter to avoid errors.