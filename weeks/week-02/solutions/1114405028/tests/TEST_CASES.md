# Test Cases Documentation

## Task 1: Sequence Clean

### Normal Case
- Input: [5, 3, 5, 2, 9, 2, 8, 3, 1]
- Expected:
  - dedupe: [5, 3, 2, 9, 8, 1]
  - asc: [1, 2, 2, 3, 3, 5, 5, 8, 9]
  - desc: [9, 8, 5, 5, 3, 3, 2, 2, 1]
  - evens: [2, 2, 8]

### Edge Case: Empty List
- Input: []
- Expected: All outputs empty

### Edge Case: All Same Numbers
- Input: [2, 2, 2, 2]
- Expected: dedupe [2], others [2,2,2,2] or filtered

### Edge Case: No Duplicates
- Input: [1, 3, 5, 7]
- Expected: dedupe same as input, sorted versions, no evens

### Edge Case: Mixed Positive/Negative
- Input: [-1, 2, -3, 4, -1, 2]
- Expected: Proper dedupe, sorting, even filtering

## Task 2: Student Ranking

### Normal Case
- Input: Students with various scores, ages, names; k=3
- Expected: Sorted by score desc, age asc, name asc, top 3

### Edge Case: k > n
- Input: 2 students, k=5
- Expected: All 2 students

### Edge Case: Same score and age, different names
- Input: 3 students with same score/age
- Expected: Sorted by name asc

### Edge Case: Empty list
- Input: [], k=3
- Expected: []

### Edge Case: k=0
- Input: Students, k=0
- Expected: []

## Task 3: Log Summary

### Normal Case
- Input: 8 logs with alice, bob, chris
- Expected: bob 4, alice 3, chris 1; top_action login 3

### Edge Case: Single user
- Input: Multiple actions by one user
- Expected: User with total count, most frequent action

### Edge Case: Tie in actions
- Input: Two actions with same count
- Expected: One of them as top (implementation dependent)

### Edge Case: Empty logs
- Input: []
- Expected: [], None

### Edge Case: One log
- Input: [('user', 'act')]
- Expected: [('user', 1)], ('act', 1)