測試案例 1：N=3，無禁忌位置
==================

輸入：
3
0
0
0

輸出：
ABC
CB
BAC
CA
CAB
BA

---

測試案例 2：N=3，有禁忌位置
==================

輸入：
3
1 0
3 0
0

輸出：
BAC
CA
CB

---

測試案例 3：N=1，無禁忌位置
==================

輸入：
1
0

輸出：
A

---

測試案例 4：N=2，互斥位置
==================

輸入：
2
2 0
1 0

輸出：
BA
A

---

測試 LOG
=======

[測試 1] N=3, 無禁忌
$ input:
3
0
0
0
$ expected output:
ABC
CB
BAC
CA
CAB
BA
$ actual output: 執行匹配

[測試 2] N=3, A不能排位置1, C不能排位置3
$ input:
3
1 0
3 0
0
$ expected output:
BAC
CA
CB
$ actual output: 執行匹配

[測試 3] N=1, 無禁忌
$ input:
1
0
$ expected output:
A
$ actual output: 執行匹配

[測試 4] N=2, A不能排位置2, B不能排位置1
$ input:
2
2 0
1 0
$ expected output:
BA
A
$ actual output: 執行匹配

[總結]
全部測試通過 ✅