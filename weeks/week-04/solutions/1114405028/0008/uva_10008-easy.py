# Easy version
n = int(input())
text = ""
for _ in range(n):
    text += input().upper()
count = {}
for char in text:
    if char.isalpha():
        count[char] = count.get(char, 0) + 1
result = sorted(count.items(), key=lambda x: (-x[1], x[0]))
for char, cnt in result:
    print(char, cnt)