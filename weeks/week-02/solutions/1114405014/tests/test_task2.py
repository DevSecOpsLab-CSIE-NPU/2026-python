print("請輸入學生數量、顯示名次:")
n, k = int(input()), int(input())
students_list = []
print("請輸入學生姓名、分數、年齡:(以空格作為分隔符)")
for i in range(n):
    name, score, age = input().split()
    students_list.append((name, int(score), int(age)))

students=sorted(students_list, key=lambda x: (-x[1], x[2], x[0]))
print("學生排序結果:")
for student in students[:k]:
    print(student[0], student[1], student[2])