from collections import Counter

n = int(input())
text = ""
for _ in range(n):
    text += input().upper()

char_count = Counter(text)
sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

for char, count in sorted_chars:
    if char.isalpha():
        print(f"{char} {count}")
