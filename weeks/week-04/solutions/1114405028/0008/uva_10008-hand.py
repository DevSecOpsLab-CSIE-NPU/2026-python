# Hand version
# Manual input
n = 3
lines = ["This is a test", "Hello World", "Python Programming"]
text = ''.join(lines).upper()
count = {}
for char in text:
    if char.isalpha():
        count[char] = count.get(char, 0) + 1
result = sorted(count.items(), key=lambda x: (-x[1], x[0]))
for char, cnt in result:
    print(char, cnt)