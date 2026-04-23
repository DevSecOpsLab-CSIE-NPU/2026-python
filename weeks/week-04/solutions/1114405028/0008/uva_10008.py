import sys

input = sys.stdin.read
data = input().splitlines()
n = int(data[0])
text = ''.join(data[1:]).upper()
count = {}
for char in text:
    if char.isalpha():
        count[char] = count.get(char, 0) + 1
result = sorted(count.items(), key=lambda x: (-x[1], x[0]))
for char, cnt in result:
    print(char, cnt)